"""Reproduce a sourced quarterly UNH medical-cost sensitivity; no dependencies."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parent


def decimal(value: object) -> Decimal:
    return Decimal(str(value))


def number(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP))


def build_results(inputs: dict) -> dict:
    obs = inputs["observations"]
    assumptions = inputs["assumptions"]
    constant_flags = (
        "premium_revenue_held_constant",
        "nonmedical_costs_interest_and_other_items_held_constant",
        "noncontrolling_earnings_held_constant",
        "diluted_shares_held_constant",
        "all_incremental_medical_cost_change_attributed_to_common_shareholders_after_tax",
    )
    if not all(assumptions[key] is True for key in constant_flags):
        raise ValueError("This static model requires its constant-base assumptions")
    if assumptions["marginal_tax_rate_method"] != (
        "reported_quarter_tax_provision_divided_by_reported_quarter_pretax_earnings"
    ):
        raise ValueError("Unsupported marginal tax rate method")
    if assumptions["eps_anchor_method"] != (
        "reported_diluted_eps_plus_modeled_incremental_aftertax_earnings_divided_by_rounded_reported_diluted_shares"
    ):
        raise ValueError("Unsupported EPS anchor method")
    if assumptions["reserve_addback_method"] != (
        "add_all_net_favorable_development_back_to_quarterly_medical_costs"
    ):
        raise ValueError("Unsupported reserve addback method")

    def observed(key: str) -> Decimal:
        return decimal(obs[key]["value"])

    premiums = observed("premium_revenue_usd_million")
    costs = observed("medical_costs_usd_million")
    pretax = observed("earnings_before_income_taxes_usd_million")
    taxes = observed("income_tax_provision_usd_million")
    net = observed("net_earnings_usd_million")
    nci = observed("noncontrolling_earnings_usd_million")
    common = observed("common_shareholder_earnings_usd_million")
    shares = observed("diluted_weighted_average_shares_million")
    eps_anchor = observed("reported_diluted_eps_usd")
    reported_mcr = observed("reported_mcr_percent")
    favorable_development = observed("net_favorable_medical_development_usd_million")
    if premiums <= 0 or shares <= 0 or pretax <= 0:
        raise ValueError("Positive premium, share and pretax denominators required")
    if pretax - taxes != net or net - nci != common:
        raise ValueError("Published earnings bridge does not reconcile")
    tax_rate = taxes / pretax
    if not Decimal(0) <= tax_rate < Decimal(1):
        raise ValueError("Invalid assumed marginal tax rate")
    ratio = costs / premiums
    if (ratio * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP) != reported_mcr:
        raise ValueError("Costs and premiums do not reproduce rounded reported MCR")

    scenarios = []
    for change_bps in assumptions["scenario_mcr_change_basis_points"]:
        ratio_change = decimal(change_bps) / 10000
        cost_change = premiums * ratio_change
        pretax_change = -cost_change
        tax_change = pretax_change * tax_rate
        aftertax_change = pretax_change - tax_change
        scenarios.append({
            "mcr_change_basis_points": change_bps,
            "mcr_percent": number((ratio + ratio_change) * 100),
            "medical_costs_usd_million": number(costs + cost_change),
            "pretax_earnings_change_usd_million": number(pretax_change),
            "aftertax_common_earnings_change_usd_million": number(aftertax_change),
            "incremental_diluted_eps_usd": number(aftertax_change / shares),
            "pretax_earnings_usd_million": number(pretax + pretax_change),
            "income_tax_provision_usd_million": number(taxes + tax_change),
            "net_earnings_usd_million": number(net + aftertax_change),
            "common_shareholder_earnings_usd_million": number(common + aftertax_change),
            "diluted_eps_from_reported_anchor_usd": number(eps_anchor + aftertax_change / shares),
        })

    guidance_midpoint = (
        observed("fy2026_adjusted_eps_guidance_low_usd")
        + observed("fy2026_adjusted_eps_guidance_high_usd")
    ) / 2
    multiple = decimal(assumptions["illustrative_forward_adjusted_pe_multiple"])
    if multiple <= 0:
        raise ValueError("Positive illustrative P/E required")
    hurdles = []
    for price in assumptions["illustrative_share_prices_usd"]:
        required_eps = decimal(price) / multiple
        hurdles.append({
            "illustrative_price_usd": price,
            "illustrative_adjusted_pe_multiple": number(multiple),
            "required_annual_adjusted_eps_usd": number(required_eps),
            "required_eps_minus_dated_guidance_midpoint_usd": number(required_eps - guidance_midpoint),
        })

    return {
        "case_id": inputs["case_id"],
        "analysis_date": inputs["analysis_date"],
        "model_type": "Illustrative static quarterly sensitivity",
        "reporting_period": inputs["reporting_period"],
        "units": "USD million and shares million, except ratios, basis points and USD per share",
        "reconciliation": {
            "computed_reported_mcr_percent": number(ratio * 100),
            "reported_rounded_mcr_percent": number(reported_mcr),
            "assumed_marginal_tax_rate_percent": number(tax_rate * 100),
            "pretax_to_net_earnings_reconciles": True,
            "net_to_common_earnings_reconciles": True,
            "rounded_earnings_divided_by_rounded_shares_eps_usd": number(common / shares),
            "reported_diluted_eps_anchor_usd": number(eps_anchor),
            "rounded_table_implied_numerator_minus_reported_eps_times_shares_usd_million": number(common - eps_anchor * shares),
            "exact_eps_numerator_reconciled": False,
        },
        "scenarios": scenarios,
        "no_favorable_development_proxy": {
            "added_medical_costs_usd_million": number(favorable_development),
            "mcr_percent": number((costs + favorable_development) / premiums * 100),
            "mcr_change_basis_points": number(favorable_development / premiums * 10000),
            "pretax_earnings_change_usd_million": number(-favorable_development),
            "aftertax_common_earnings_change_usd_million": number(-favorable_development * (1 - tax_rate)),
            "incremental_diluted_eps_usd": number(-favorable_development * (1 - tax_rate) / shares),
            "diluted_eps_from_reported_anchor_usd": number(eps_anchor - favorable_development * (1 - tax_rate) / shares),
            "interpretation": "Mechanical addback only; not a pure current-quarter cost ratio or issuer adjusted EPS",
        },
        "conditional_market_hurdles": {
            "market_price_verified": False,
            "consensus_verified": False,
            "guidance_date": inputs["source_release_date"],
            "dated_fy2026_adjusted_eps_guidance_midpoint_usd": number(guidance_midpoint),
            "rows": hurdles,
            "interpretation": "Illustrative price divided by selected multiple; no current valuation conclusion and no mapping from quarterly MCR to annual EPS",
        },
        "limitations": inputs["limitations"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check committed results without rewriting")
    args = parser.parse_args()
    inputs = json.loads((CASE_DIR / "inputs.json").read_text())
    results = build_results(inputs)
    destination = CASE_DIR / "results.json"
    if args.check:
        if json.loads(destination.read_text()) != results:
            raise SystemExit("Results differ: run model.py to regenerate")
        print("PASS: quarterly ratios, earnings bridge and committed results reproduce")
    else:
        destination.write_text(json.dumps(results, indent=2) + "\n")
        print(f"Wrote {destination.name}")


if __name__ == "__main__":
    main()
