#!/usr/bin/env python3
"""Source-backed ISRG revenue sensitivity; standard library only.

python model.py
python model.py --check
python model.py --enterprise-value-usd 150000000000 --ev-sales-multiple 12

The optional valuation numbers are USER ASSUMPTIONS, not a retrieved market quote.
"""
import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate(data):
    for key in ("reported_fy2025", "reported_q2_2026"):
        row = data[key]
        total = sum(row[field] for field in (
            "instruments_accessories_revenue_usd", "systems_revenue_usd", "service_revenue_usd"))
        if total != row["total_revenue_usd"]:
            raise ValueError(f"{key}: revenue does not reconcile")
    a = data["analyst_assumptions"]
    if not 0 <= a["incremental_operating_profit_conversion_of_ia_revenue"] <= 1:
        raise ValueError("Contribution conversion must be between zero and one")
    for scenario in a["scenarios"].values():
        if any(value <= -1 for value in scenario.values()):
            raise ValueError("Growth inputs must exceed -100%")
    if a["ion_revenue_per_procedure_2025_usd"] <= 0:
        raise ValueError("Ion assumed revenue/procedure must be positive")


def calibration(data, ion_rpp=None):
    b = data["reported_fy2025"]
    ion_rpp = (data["analyst_assumptions"]["ion_revenue_per_procedure_2025_usd"]
               if ion_rpp is None else ion_rpp)
    ion_revenue = b["ion_procedures_approximately"] * ion_rpp
    dv_revenue = b["instruments_accessories_revenue_usd"] - ion_revenue
    if dv_revenue <= 0 or ion_rpp <= 0:
        raise ValueError("Assumed platform allocation must yield positive revenue")
    return {"assumed_ion_revenue_per_procedure_usd": ion_rpp,
            "calibrated_da_vinci_revenue_per_procedure_usd": dv_revenue / b["da_vinci_procedures_approximately"],
            "assumed_ion_baseline_ia_revenue_usd": ion_revenue,
            "calibrated_da_vinci_baseline_ia_revenue_usd": dv_revenue,
            "reconciled_baseline_ia_revenue_usd": ion_revenue + dv_revenue}


def forecast(data, scenario, ion_rpp=None):
    b, a = data["reported_fy2025"], data["analyst_assumptions"]
    c = calibration(data, ion_rpp)
    dv_procedures = b["da_vinci_procedures_approximately"] * (1 + scenario["da_vinci_procedure_growth"])
    ion_procedures = b["ion_procedures_approximately"] * (1 + scenario["ion_procedure_growth"])
    dv_rpp = c["calibrated_da_vinci_revenue_per_procedure_usd"] * (1 + scenario["da_vinci_revenue_per_procedure_change"])
    ion_rpp_future = c["assumed_ion_revenue_per_procedure_usd"] * (1 + a["ion_revenue_per_procedure_2026_change"])
    ia = dv_procedures * dv_rpp + ion_procedures * ion_rpp_future
    systems = b["systems_revenue_usd"] * (1 + scenario["systems_revenue_growth"])
    service = b["service_revenue_usd"] * (1 + scenario["service_revenue_growth"])
    return {"forecast_da_vinci_procedures": dv_procedures,
            "forecast_ion_procedures": ion_procedures,
            "assumed_da_vinci_revenue_per_procedure_usd": dv_rpp,
            "assumed_ion_revenue_per_procedure_usd": ion_rpp_future,
            "instruments_accessories_revenue_usd": ia,
            "instruments_accessories_growth": ia / b["instruments_accessories_revenue_usd"] - 1,
            "systems_revenue_usd": systems,
            "service_revenue_usd": service,
            "total_revenue_usd": ia + systems + service,
            "total_revenue_growth": (ia + systems + service) / b["total_revenue_usd"] - 1}


def implied_growth(data, enterprise_value, multiple):
    if not (math.isfinite(enterprise_value) and math.isfinite(multiple)) or enterprise_value <= 0 or multiple <= 0:
        raise ValueError("Enterprise value and EV/sales multiple must be positive and finite")
    s = data["analyst_assumptions"]["scenarios"]["base"]
    f, c = forecast(data, s), calibration(data)
    required_total = enterprise_value / multiple
    dv_required = required_total - f["systems_revenue_usd"] - f["service_revenue_usd"] - f["forecast_ion_procedures"] * f["assumed_ion_revenue_per_procedure_usd"]
    if dv_required < 0:
        return {"status": "INFEASIBLE_WITH_OTHER_ASSUMPTIONS", "required_total_revenue_usd": required_total}
    dv_baseline_adjusted = c["calibrated_da_vinci_baseline_ia_revenue_usd"] * (1 + s["da_vinci_revenue_per_procedure_change"])
    return {"status": "CONDITIONAL_ON_USER_VALUATION_INPUTS",
            "user_enterprise_value_usd": enterprise_value,
            "assumed_forward_ev_sales_multiple": multiple,
            "required_total_revenue_usd": required_total,
            "required_da_vinci_procedure_growth": dv_required / dv_baseline_adjusted - 1,
            "limitation": "One-year sales-multiple inversion, not DCF, verified consensus or a current price target; all other assumptions held at base."}


def build_results(data, enterprise_value=None, multiple=None):
    validate(data)
    a, b = data["analyst_assumptions"], data["reported_fy2025"]
    c = calibration(data)
    scenarios = {name: forecast(data, values) for name, values in a["scenarios"].items()}
    base = scenarios["base"]
    for row in scenarios.values():
        row["ia_revenue_delta_vs_base_usd"] = row["instruments_accessories_revenue_usd"] - base["instruments_accessories_revenue_usd"]
        row["illustrative_operating_profit_delta_vs_base_usd"] = row["ia_revenue_delta_vs_base_usd"] * a["incremental_operating_profit_conversion_of_ia_revenue"]
    grid = []
    for growth in a["sensitivity"]["da_vinci_procedure_growth"]:
        for rpp_change in a["sensitivity"]["da_vinci_revenue_per_procedure_change"]:
            s = dict(a["scenarios"]["base"], da_vinci_procedure_growth=growth, da_vinci_revenue_per_procedure_change=rpp_change)
            f = forecast(data, s)
            grid.append({"da_vinci_procedure_growth": growth,
                         "da_vinci_revenue_per_procedure_change": rpp_change,
                         "ia_revenue_usd": f["instruments_accessories_revenue_usd"],
                         "total_revenue_usd": f["total_revenue_usd"]})
    allocation = []
    for ion_rpp in a["sensitivity"]["ion_revenue_per_procedure_2025_usd"]:
        f = forecast(data, a["scenarios"]["base"], ion_rpp)
        allocation.append({"assumed_ion_baseline_revenue_per_procedure_usd": ion_rpp,
                           "ia_revenue_usd": f["instruments_accessories_revenue_usd"],
                           "reconciled_baseline_ia_revenue_usd": calibration(data, ion_rpp)["reconciled_baseline_ia_revenue_usd"]})
    delta_1pp = c["calibrated_da_vinci_baseline_ia_revenue_usd"] * 0.01
    delta_1pct_rpp = c["calibrated_da_vinci_baseline_ia_revenue_usd"] * (1 + a["scenarios"]["base"]["da_vinci_procedure_growth"]) * 0.01
    market = {"status": "NEEDS_MARKET_INPUTS", "required": ["dated enterprise value", "explicit assumed forward EV/sales multiple"],
              "no_market_quote_or_consensus_used": True}
    if enterprise_value is not None or multiple is not None:
        if enterprise_value is None or multiple is None:
            raise ValueError("Supply both --enterprise-value-usd and --ev-sales-multiple")
        market = implied_growth(data, enterprise_value, multiple)
    return {"case_id": data["case_id"], "information_cutoff": data["information_cutoff"],
            "forecast_period": a["forecast_period"], "classification": "analyst_sensitivity_not_company_guidance_or_live_recommendation",
            "calibration": c,
            "reported_revenue_reconciliation": {"fy2025_sum_usd": b["total_revenue_usd"], "q2_2026_sum_usd": data["reported_q2_2026"]["total_revenue_usd"]},
            "scenarios": scenarios, "growth_and_mix_sensitivity": grid,
            "platform_allocation_sensitivity": allocation,
            "marginal_sensitivities": {"one_percentage_point_da_vinci_growth_ia_revenue_usd": delta_1pp,
                                        "one_percent_da_vinci_rpp_change_ia_revenue_usd_at_base_growth": delta_1pct_rpp,
                                        "one_percentage_point_da_vinci_growth_illustrative_operating_profit_usd": delta_1pp * a["incremental_operating_profit_conversion_of_ia_revenue"]},
            "market_expectations": market,
            "utilization_status": "NOT_CALCULATED: matching average active platform installed bases are not used in this model"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify committed results against a fresh calculation without rewriting")
    parser.add_argument("--enterprise-value-usd", type=float)
    parser.add_argument("--ev-sales-multiple", type=float)
    args = parser.parse_args()
    data = json.loads((ROOT / "inputs.json").read_text())
    results = build_results(data, args.enterprise_value_usd, args.ev_sales_multiple)
    if args.check:
        if args.enterprise_value_usd is not None or args.ev_sales_multiple is not None:
            parser.error("--check validates default inputs only")
        if json.loads((ROOT / "results.json").read_text()) != results:
            raise SystemExit("FAIL: results.json differs from freshly calculated results")
        print("PASS: source revenue totals reconcile and committed results reproduce")
    elif args.enterprise_value_usd is not None or args.ev_sales_multiple is not None:
        print(json.dumps(results["market_expectations"], indent=2))
    else:
        (ROOT / "results.json").write_text(json.dumps(results, indent=2) + "\n")
        print(json.dumps({name: round(row["total_revenue_usd"]) for name, row in results["scenarios"].items()}, indent=2))


if __name__ == "__main__":
    main()
