---
name: model-valuation
description: >
  This skill should be used when the user says "stress-test my DCF", "build the rNPV",
  "SOTP for [TICKER]", "LOE bridge", "razor-blade model", "MA Stars model", "GTN
  analysis", "biosimilar erosion curve", "unit economics stress test", "working capital
  forensics", "construct scenarios", or any healthcare model-building or valuation task.
metadata:
  version: "0.1.0"
---

# Modeling & Valuation

Healthcare-specific model building, stress-testing, and valuation. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/model-valuation/references/prompts.md`; the methodology backbone is the Evidence-to-Valuation framework in `references/evidence-to-valuation.md` (+ `case-library.md`, `commercial-metrics.md`, and `loe-mechanics.md` for generic/biosimilar entry timing, 351(k) odds, CGT tail liabilities, and post-approval change tiers).

## Route by model

| Need | Prompt |
|---|---|
| DCF sanity + market-implied reverse-engineer | MOD-01 |
| Diversified pharma/medtech SOTP | MOD-02 |
| Biotech asset rNPV | MOD-03 |
| Large-cap pharma LOE bridge | MOD-04 (+ SUB-PHA-01 replenishment audit, SUB-PHA-05 biosimilar erosion, `references/loe-mechanics.md` for Orange Book × tentative-docket entry forecasting) |
| Capital + consumables (razor-blade) | MOD-05 |
| Tools/dx end-market capex cycle | MOD-06 (+ SUB-TLS-02 NGS mix, SUB-TLS-04 IVD pull-through) |
| MA operator Stars/bid model | MOD-07 (+ SUB-SVC-03 vertical integration, SUB-SVC-04 VBC capitation) |
| Digital health unit economics | MOD-08 |
| Earnings-quality / cash forensics | MOD-09 |
| Pricing/net-price work | SUB-PHA-04 GTN, SUB-MED-05 ASP deflation |
| Scenario construction as a discipline | MOD-10 |

## Execution rules — the framework is law

1. **Start with the economic unit** (valuation map, evidence-to-valuation.md): patient-year, probability-adjusted treated patient, active system, paid test, converted order/backlog, adjusted case, member-month, claim/unit, ARR customer. The unit selects the dominant formula, preferred valuation framework, and price-implied variable — quote the row.
2. **Translate evidence, don't vibe it:** every input change cites which variable moved and why, per the eight evidence-translation rules; respect the "not automatic" column (and never reward the same evidence twice — the post-approval PoA rule).
3. **Scenarios per MOD-10:** mechanism-distinct bear/base/bull on the sub-sector's primary discriminator (scenario matrix), probabilities sum to 1.00 with ≥5% unknown-unknown residual, early signal per scenario, thresholds set *before* the print.
4. **Reverse-engineer price:** always close with what the current price implies (implied PoA, patient-years, MCR, NRR, utilization, margin) — the variant-perception raw material. Live market/consensus figures come from the user's terminal; request, never fabricate.
5. **Avoid the mapped errors** (valuation map, verbatim per industry): one corporate multiple without LOE replacement; double-counting trial evidence across PoA/share/price; valuing placements without utilization; ordered tests or accounting ASP as cash economics; capitalizing reserve releases; pass-through revenue as distributor value; usage as paid ARR.
6. **Inputs from the engines:** PoS and readout scenarios → clinical-catalysts; coverage/rates/IRA → cms-reimbursement; funnels and volumes → procedure-exposure; adoption/capacity → provider-adoption. Cite their EVIDENCE BRIEFs as the inputs' provenance.
7. **Excel handoff:** workbook construction goes to the model-builder / financial-analysis plugins (their dcf/comps/3-statement/audit skills); this skill owns the healthcare methodology and assumptions. Analogous case patterns: check `references/case-library.md` (24 worked cases) for the matching evidence-type before building.
