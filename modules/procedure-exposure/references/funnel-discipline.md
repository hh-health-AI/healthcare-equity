# Funnel Discipline & Volume Metrics (from the project frameworks)

Slices of `Healthcare_Evidence_to_Valuation_Framework.xlsx` and `Healthcare_and_Life_Sciences_Commercial_Metrics.xlsx` for volume/exposure evidence. Master copies: healthcare-equity plugin.

## The funnel rule (evidence-translation usage row)

| Evidence | Model variables | Modeling instruction | NOT automatic | Observable follow-up |
|---|---|---|---|---|
| Prescriptions, orders or usage | Observed stage of the commercial funnel | **Bridge ordered → completed → paid → persistent → cash** | Revenue, gross profit or durable retention | Paid conversion; collections; cohort retention |

Every volume observation must name its funnel stage. Corollaries from the case library: covered lives and scripts are not paid courses (Vertex C04); reported tests are not paid tests, and accrual true-ups are not recurring price/mix (Natera C08); ordered/eligible is a ceiling, not demand (Guardant C09: contribution = eligible × offer × completion × reportability × paid rate × (cash ASP − COGS/test)).

## Scenario discriminators for volume-driven sectors (Scenario Matrix)

| Industry | Primary discriminator | Boundary discipline |
|---|---|---|
| Medical technology | Utilization per active installed system | Set thresholds before the operating update; placements without utilization = bear trap |
| Diagnostics | Paid tests × cash contribution/test (bear ≤80%, base 80–120%, bull >120% of base contribution) | Use cash contribution, not reported revenue/test |
| Providers/services | Contribution per adjusted case | Revenue/case alone is insufficient — acuity and cost must be in the read |
| Pharmaceuticals | Approval/launch gate, then three-year patient-years (75–125% bands) | Gate failure/delay first; then non-overlapping patient-year bands |

## Volume metric ladder (Commercial Metrics workbook)

Pharma: NRx (flow) / TRx (stock) / NBRx (true organic capture) / refill rate (adherence). MedTech: procedure volume (stock-equivalent), account reorder rate (flow/retention), system placements (capital flow), ASP (pricing power). Tools & Dx: placements → installed base → pull-through ($/instrument/yr) → attachment rate. Use the right ladder for the sub-sector and never mix flow with stock in a growth claim.

## Valuation-map anchors for this plugin's outputs

- Medtech economic unit: active system/treated patient — Recurring GP = active installed base × utilization × pull-through × contribution margin.
- Diagnostics economic unit: paid, reportable test — Contribution = paid tests × (cash ASP − COGS/test).
- Providers economic unit: adjusted case — EBITDA = cases × (reimbursement/case − care cost/case) − fixed cost.
- Common errors (verbatim from the map): valuing placements without utilization; using ordered tests or accounting ASP as cash economics; using revenue/case without acuity and cost.
