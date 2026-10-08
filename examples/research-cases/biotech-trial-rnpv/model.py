#!/usr/bin/env python3
"""Reproduce the HELIOS-B research case with standard-library arithmetic.

The clinical evidence is real. All commercial inputs are explicitly illustrative.
An approval probability is applied once to future conditional operating FCF.
No company price target, calibrated clinical probability or treatment advice is produced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent


def number(value, label, minimum=None, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a finite number")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{label} must be finite")
    if minimum is not None and value < minimum:
        raise ValueError(f"{label} must be >= {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{label} must be <= {maximum}")
    return value


def validate(packet):
    if packet.get("schema_version") != 1:
        raise ValueError("Unsupported input schema")
    valuation_date = date.fromisoformat(packet["valuation_date"])
    if packet.get("currency") != "USD" or packet.get("output_units") != "millions":
        raise ValueError("This case requires USD and output units millions")
    gate = packet["approval_gate"]
    for stage in ("before", "after"):
        number(gate[stage], f"approval_gate.{stage}", 0, 1)
    price = number(packet["annual_net_revenue_per_paid_patient_usd"], "annual net price", 0)
    if price == 0:
        raise ValueError("annual net price must be positive")
    schedule = packet["commercial_schedule"]
    if not schedule:
        raise ValueError("Cash-flow schedule cannot be empty")
    dates = []
    for row in schedule:
        period_end = date.fromisoformat(row["period_end"])
        if period_end <= valuation_date:
            raise ValueError("Commercial period ends must follow the valuation date")
        dates.append(period_end)
        number(row["paid_patient_years"], "paid_patient_years", 0)
    if dates != sorted(set(dates)):
        raise ValueError("Period ends must be unique and chronological")
    scenarios = packet["scenarios"]
    if not scenarios or len({s["name"] for s in scenarios}) != len(scenarios):
        raise ValueError("Scenario names must be unique and the list nonempty")
    weights = []
    for scenario in scenarios:
        weights.append(number(scenario["weight_conditional_on_approval"], "scenario weight", 0, 1))
        for field in ("patient_year_multiplier", "net_price_multiplier", "upfront_launch_investment_m", "discount_rate"):
            number(scenario[field], f"{scenario['name']}.{field}", 0)
        number(scenario["after_tax_fcf_conversion"], "FCF conversion", 0, 1)
    if not math.isclose(sum(weights), 1.0, abs_tol=1e-10):
        raise ValueError("Conditional commercial scenario weights must sum to 1")
    for p in packet["sensitivity"]["approval_gate"]:
        number(p, "sensitivity approval gate", 0, 1)
    for r in packet["sensitivity"]["discount_rate"]:
        number(r, "sensitivity discount rate", 0)
    return valuation_date


def scenario_rows(packet, scenario, discount_rate=None):
    valuation_date = date.fromisoformat(packet["valuation_date"])
    rate = scenario["discount_rate"] if discount_rate is None else discount_rate
    rows = []
    for period in packet["commercial_schedule"]:
        years = (date.fromisoformat(period["period_end"]) - valuation_date).days / 365.25
        patient_years = period["paid_patient_years"] * scenario["patient_year_multiplier"]
        net_price = packet["annual_net_revenue_per_paid_patient_usd"] * scenario["net_price_multiplier"]
        revenue_m = patient_years * net_price / 1_000_000
        conditional_fcf_m = revenue_m * scenario["after_tax_fcf_conversion"]
        pv_m = conditional_fcf_m / (1 + rate) ** years
        rows.append({
            "period_end": period["period_end"],
            "years_from_valuation": years,
            "paid_patient_years": patient_years,
            "annual_net_revenue_per_patient_usd": net_price,
            "revenue_m": revenue_m,
            "conditional_after_tax_unlevered_fcf_m": conditional_fcf_m,
            "conditional_operating_pv_m": pv_m,
        })
    return rows


def gated_asset_value(operating_pv_m, approval_gate, upfront_m):
    return approval_gate * operating_pv_m - upfront_m


def clean(value):
    if isinstance(value, float):
        return round(value, 6)
    if isinstance(value, list):
        return [clean(item) for item in value]
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    return value


def calculate(packet, target_asset_ev_m=None):
    validate(packet)
    if target_asset_ev_m is not None:
        target_asset_ev_m = number(target_asset_ev_m, "target asset EV", 0)
    stages = packet["approval_gate"]
    output = []
    weighted_before = weighted_after = 0.0
    for scenario in packet["scenarios"]:
        rows = scenario_rows(packet, scenario)
        operating_pv = sum(row["conditional_operating_pv_m"] for row in rows)
        upfront = scenario["upfront_launch_investment_m"]
        before = gated_asset_value(operating_pv, stages["before"], upfront)
        after = gated_asset_value(operating_pv, stages["after"], upfront)
        weighted_before += scenario["weight_conditional_on_approval"] * before
        weighted_after += scenario["weight_conditional_on_approval"] * after
        for row in rows:
            row["before_probability_weighted_operating_pv_m"] = stages["before"] * row["conditional_operating_pv_m"]
            row["after_probability_weighted_operating_pv_m"] = stages["after"] * row["conditional_operating_pv_m"]
        output.append({
            "scenario": scenario["name"],
            "commercial_weight_conditional_on_approval": scenario["weight_conditional_on_approval"],
            "discount_rate": scenario["discount_rate"],
            "upfront_launch_investment_m": upfront,
            "conditional_operating_pv_m": operating_pv,
            "before_asset_rnpv_m": before,
            "after_asset_rnpv_m": after,
            "approval_gate_change_m": after - before,
            "cashflow_audit": rows,
        })
    base = next(s for s in packet["scenarios"] if s["name"] == "base")
    sensitivity = []
    for rate in packet["sensitivity"]["discount_rate"]:
        operating_pv = sum(row["conditional_operating_pv_m"] for row in scenario_rows(packet, base, rate))
        for gate in packet["sensitivity"]["approval_gate"]:
            sensitivity.append({
                "discount_rate": rate,
                "approval_gate": gate,
                "asset_rnpv_m": gated_asset_value(operating_pv, gate, base["upfront_launch_investment_m"]),
            })
    base_operating_pv = next(s["conditional_operating_pv_m"] for s in output if s["scenario"] == "base")
    implied = None
    if target_asset_ev_m is not None:
        if base_operating_pv <= 0:
            raise ValueError("A market-implied gate needs positive conditional operating PV")
        implied_gate = (target_asset_ev_m + base["upfront_launch_investment_m"]) / base_operating_pv
        implied = {
            "hypothetical_residual_asset_ev_m": target_asset_ev_m,
            "base_implied_approval_gate": implied_gate,
            "within_zero_one": 0 <= implied_gate <= 1,
            "interpretation": (
                "Conditional on the illustrative base economics. Above 1 indicates the "
                "economic assumptions do not explain the target EV; after approval, use "
                "this framework to test commercial assumptions rather than infer approval risk."
            ),
        }
    return clean({
        "case_id": packet["case_id"],
        "valuation_date": packet["valuation_date"],
        "currency": "USD",
        "value_units": "millions",
        "evidence_status": "REAL_CLINICAL_AND_APPROVAL_OBSERVATIONS",
        "economic_input_status": "ILLUSTRATIVE_NOT_COMPANY_FORECASTS",
        "clinical_readout_only_implication": "UNCERTAINTY_ONLY: no mechanically calibrated gate change from hazard ratios",
        "realized_approval_implication": "CHANGE: illustrative predecision gate to realized US approval gate 1.00",
        "approval_gate_before": stages["before"],
        "approval_gate_after": stages["after"],
        "scenarios": output,
        "conditional_commercial_weighted_before_asset_rnpv_m": weighted_before,
        "conditional_commercial_weighted_after_asset_rnpv_m": weighted_after,
        "weighted_approval_gate_change_m": weighted_after - weighted_before,
        "base_sensitivity": sensitivity,
        "market_implied_result": implied,
        "equity_value_and_per_share": None,
        "equity_bridge_status": "NEEDS_DATA: company net cash, other assets, overhead, dilution and verified market price missing",
        "formula": "asset rNPV = approval_gate * sum(conditional_after_tax_unlevered_FCF / (1+r)^t) - upfront_launch_investment",
        "limits": [
            "No clinical hazard ratio, p-value or confidence interval is converted into a success probability.",
            "Approval risk is applied once; commercial scenario weights describe a separate conditional uncertainty.",
            "Same valuation date and operating inputs isolate the approval gate; this is not historical P&L.",
            "No terminal value, other indications, financing, future US label risk or company balance sheet.",
        ],
    })


def self_check():
    # Independent one-period arithmetic: -10 + 0.5 * 110 / 1.1 = 40.
    if not math.isclose(gated_asset_value(110 / 1.1, 0.5, 10), 40, abs_tol=1e-12):
        raise AssertionError("Hand-calculated one-period rNPV check failed")
    packet = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    result = calculate(packet)
    for scenario in result["scenarios"]:
        expected_change = (packet["approval_gate"]["after"] - packet["approval_gate"]["before"]) * scenario["conditional_operating_pv_m"]
        if not math.isclose(scenario["approval_gate_change_m"], expected_change, abs_tol=1e-6):
            raise AssertionError("Approval gate bridge failed")
    for bad in (float("nan"), float("inf"), True):
        try:
            number(bad, "bad input")
        except ValueError:
            pass
        else:
            raise AssertionError("Nonfinite/boolean input was accepted")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=HERE / "inputs.json")
    parser.add_argument("--out", type=Path, default=HERE / "results.json")
    parser.add_argument("--target-asset-ev-m", type=float, help="Hypothetical residual asset EV in USD millions, not observed ALNY market value")
    parser.add_argument("--check", action="store_true", help="Check arithmetic and compare the saved results without writing")
    args = parser.parse_args()
    try:
        if args.check:
            self_check()
        raw_input = args.input.read_bytes()
        packet = json.loads(raw_input)
        result = calculate(packet, args.target_asset_ev_m)
        result["input_sha256"] = hashlib.sha256(raw_input).hexdigest()
        source_path = HERE / "sources.json"
        result["source_ledger_sha256"] = hashlib.sha256(source_path.read_bytes()).hexdigest()
        if args.check:
            if not args.out.exists():
                raise ValueError("Saved results are missing; generate without --check first")
            saved = json.loads(args.out.read_text(encoding="utf-8"))
            if saved != result:
                raise ValueError("Saved results differ from current inputs, source ledger or calculation")
        else:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        print(json.dumps({
            "out": str(args.out),
            "weighted_before_m": result["conditional_commercial_weighted_before_asset_rnpv_m"],
            "weighted_after_m": result["conditional_commercial_weighted_after_asset_rnpv_m"],
            "weighted_change_m": result["weighted_approval_gate_change_m"],
            "market_implied": result["market_implied_result"],
            "self_checks": "passed; saved results match; no files written" if args.check else "not requested",
        }, indent=2))
    except (ValueError, KeyError, StopIteration, OSError) as exc:
        parser.exit(2, f"Research case error: {exc}\n")


if __name__ == "__main__":
    main()

