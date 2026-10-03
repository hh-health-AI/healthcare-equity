"""Explicit per-cash-flow probability weighting; no implied clinical prediction."""
from .common import number, require, report_header, table


def calculate(packet):
    require(bool(packet.get("currency")) and bool(packet.get("units")), "currency and units are required")
    require(bool(packet.get("as_of")), "Valuation as_of date is required")
    scenarios = packet.get("scenarios", [])
    require(len(scenarios) >= 1, "At least one scenario is required")
    seen, results = set(), []
    for s in scenarios:
        name = s.get("name")
        require(name and name not in seen, "Scenario names must be unique")
        seen.add(name)
        rate = number(s.get("discount_rate"), "discount_rate", 0, 1)
        flows = s.get("cashflows", [])
        require(bool(flows), "Each scenario requires cashflows")
        detail = []
        for f in flows:
            t = number(f.get("year"), "year", 0)
            cf = number(f.get("cashflow"), "cashflow")
            prob = number(f.get("probability"), "probability", 0, 1)
            require(f.get("kind") in {"development", "commercial", "other"}, "cashflow kind is required")
            require(f.get("assumption"), "Every cash flow needs an assumption/source note")
            weighted = cf * prob
            detail.append({**f, "expected_cashflow": weighted, "present_value": weighted / (1 + rate) ** t})
        asset = sum(r["present_value"] for r in detail)
        bridge_fields = ("cash", "debt", "unallocated_overhead_pv")
        missing_bridge = [k for k in bridge_fields if s.get(k) is None]
        bridge = {k: number(s[k], k, 0) for k in bridge_fields if s.get(k) is not None}
        equity = None if missing_bridge else asset + bridge["cash"] - bridge["debt"] - bridge["unallocated_overhead_pv"]
        shares = s.get("diluted_shares")
        if shares is not None:
            shares = number(shares, "diluted_shares", 0)
            require(shares > 0, "diluted_shares must be positive")
        results.append({"name": name, "discount_rate": rate, "asset_rnpv": asset, "equity_value": equity, "value_per_share": equity / shares if shares and equity is not None else None, "bridge": bridge, "missing_bridge_fields": missing_bridge, "cashflows": detail})
    return {"currency": packet["currency"], "units": packet["units"], "as_of": packet["as_of"], "scenarios": results, "convention": "End-of-year cash flows at t years from as_of; probability is unconditional payment/receipt probability for each row. No additional global PoS multiplier. No terminal value unless explicitly entered as a cash flow."}


def render(packet):
    r = calculate(packet)
    out = report_header("Biotech rNPV scenarios", packet) + f"Currency: {r['currency']} · Cash-flow units: {r['units']} · As of: {r['as_of']}\n\n"
    out += table(["Scenario", "Discount rate", "Asset rNPV", "Equity value", "Value/share"], [[s["name"], f"{s['discount_rate']:.1%}", round(s["asset_rnpv"], 4), round(s["equity_value"], 4) if s["equity_value"] is not None else "Not calculated: incomplete bridge", round(s["value_per_share"], 4) if s["value_per_share"] is not None else "Not calculated"] for s in r["scenarios"]]) + "\n\n"
    for s in r["scenarios"]:
        out += f"## {s['name']} equity bridge\n\n" + table(["Component", "Value"], [(k, s["bridge"].get(k)) for k in ("cash", "debt", "unallocated_overhead_pv")]) + "\n\n"
        out += f"## {s['name']} cash-flow audit\n\n" + table(["t (years)", "Kind", "Cash flow", "Probability", "Expected", "PV", "Assumption"], [[f["year"], f["kind"], f["cashflow"], f["probability"], round(f["expected_cashflow"], 4), round(f["present_value"], 4), f["assumption"]] for f in s["cashflows"]]) + "\n\n"
    return out + r["convention"] + "\n\nUse matching units for cash, debt and shares (e.g. USD millions and millions of shares). Supply unlevered after-tax cash flows for an enterprise-value interpretation. Subtract corporate overhead only if not already included. These user-defined probabilities are assumptions, not calibrated trial-success predictions. Correlated assets and financing dilution need separate scenarios.\n"
