# Payor Metrics & Evidence Translation (from the project frameworks)

Slices of `Healthcare_and_Life_Sciences_Commercial_Metrics.xlsx` and `Healthcare_Evidence_to_Valuation_Framework.xlsx` relevant to this plugin. Master copies live in the healthcare-equity plugin and the project.

## Managed care metrics (Commercial Metrics workbook)

| Metric | Full name | Role | Definition & strategic meaning |
|---|---|---|---|
| Lives / Covered Lives | Total Membership / Enrollees | Volume base ("TRx equivalent") | Total active subscribers across Commercial, MA, and Medicaid plans — the master volume base. |
| MLR / MBR | Medical Loss / Benefit Ratio | Margin / underwriting | Claims ÷ premium revenue; primary gauge of plan profitability (target ~80–85%). |
| PMPM | Per Member Per Month | Normalized financial unit | Standard unit for revenue and medical cost per enrollee per month. |
| Net Organic Additions | Net Membership Growth | Flow ("NRx dynamics") | New enrollees minus disenrollments in open/special enrollment periods. |

## Evidence translation — the coverage row (Evidence-to-Valuation workbook)

| Evidence | Model variables | Modeling instruction | NOT automatic | Observable follow-up |
|---|---|---|---|---|
| Better reimbursement or coverage | Authorization; abandonment; paid conversion; net price | Separate covered lives from usable access and cash collections | Clinical adoption | Approval-to-paid lag; cash ASP; abandonment |

Corollary for this plugin's briefs: coverage wins expand the **accessible** population and paid conversion; they never, by themselves, move prescribing, utilization, or clinical adoption — those are provider-adoption and procedure-exposure evidence.

## Managed care scenario row (Evidence-to-Valuation workbook)

- **Primary discriminator:** reserve-normalized current-year MCR.
- **Bear:** >100 bps worse than the pricing assumption. **Base:** within ~±100 bps. **Bull:** >100 bps favorable, excluding reserve releases.
- **Key falsifier:** current-service MCR and cohort experience. **Boundary discipline:** normalize prior-period development first.

## Managed care valuation row

- **Economic unit:** member-month. **Dominant formula:** Profit = member-months × premium PMPM × (1 − MCR − admin ratio).
- **Preferred framework:** normalized P/E · DCF · SOTP. **Price-implied variable:** current-service MCR and cohort margin.
- **Common error:** capitalizing reserve releases or membership growth as run-rate margin.

## Providers/services rows (for rule-impact work on hospitals & sites)

- Scenario discriminator: **contribution per adjusted case** (payer/service mix and cost vs volume); revenue/case alone is insufficient.
- Valuation: EBITDA = cases × (net reimbursement/case − care cost/case) − fixed cost; price-implied variable is normalized reimbursement less care cost per case.
