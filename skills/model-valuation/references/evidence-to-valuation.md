# Healthcare Evidence-to-Valuation Framework (master distillation)

Distilled from `Healthcare_Evidence_to_Valuation_Framework.xlsx` (project file; 11 industries, 24 cases, as of 2026-08-25). The xlsx in the Healthcare Plugin project remains the working template.

## Universal lens

**Value = Σ scenario probability × PV[(eligible units × adoption × net price × duration × contribution margin) − required capital] − net debt − dilution.**
Evidence has entered valuation only when it changes probability, timing, units, realized economics, duration/retention, margin, or capital.

**Workflow:** 1) Start with the economic unit (patient-year, active system, paid test, case, member-month, claim, ARR customer) → 2) Translate evidence — move an explicit variable; record what the evidence does not prove → 3) Build scenarios — mutually exclusive terminal leaves, probabilities sum to 100% → 4) Reverse-engineer price — solve for implied PoA, units, margin, MCR, NRR, or utilization → 5) Define catalyst and falsifier — pre-commit to the observation that confirms or breaks the thesis.

**Scenario tree:** Clinical/technical evidence → CORE GATE CLEARS? — No/major delay → **BEAR** (failure, delay, dilution) · Yes → COMMERCIAL CONVERSION? — weak/uneconomic → BEAR · normal → **BASE** · superior & profitable → **BULL**. Each terminal leaf mutually exclusive; probabilities sum to 100%.

## Evidence Translation Rules (all 8)

*Every adjective must move an explicit probability, timing, unit, price, duration, margin or capital assumption.*

| Evidence | Model variables | Modeling instruction | NOT automatic | Observable follow-up |
|---|---|---|---|---|
| Better efficacy vs placebo | Approval probability; minimum clinical utility | Move PoA and/or regulatory timing | Peak share, premium price or superior line of therapy | Regulatory feedback; filing acceptance; label wording |
| Better efficacy vs active comparator | Line of therapy; peak share; adoption speed; persistence | Map endpoint advantage to segment-specific prescribing behavior | Manufacturing probability or automatic payer preference | New-to-brand share; guideline placement; switching |
| Better safety or tolerability | Eligible population; discontinuation; monitoring burden; persistence | Translate adverse events into label, discontinuation and care burden | Diagnosis rate or biological efficacy | Dose intensity; monitoring; real-world persistence |
| Easier administration | Initiation; site of care; throughput; persistence | Model format conversion, chair capacity, home use and service cost | Biological efficacy or incremental TAM | Format mix; starts; refill persistence; site economics |
| Broader regulatory label | Eligible population; launch date; commercial claims | Rebuild the funnel using exact label restrictions | Coverage, physician adoption or paid demand | Coverage policies; prior authorization; paid starts |
| Better reimbursement or coverage | Authorization; abandonment; paid conversion; net price | Separate covered lives from usable access and cash collections | Clinical adoption automatically | Approval-to-paid lag; cash ASP; abandonment |
| Manufacturing or CMC progress | Launch probability; timing; yield; capacity; capital | Model validation, batch success, ramp cost and capacity capex | Patient demand or market share | Inspection; yield; batch release; utilization |
| Prescriptions, orders or usage | Observed stage of the commercial funnel | Bridge ordered → completed → paid → persistent → cash | Revenue, gross profit or durable retention | Paid conversion; collections; cohort retention |

## Scenario Matrix (all 11 industries)

| Industry | Primary discriminator | Bear | Base | Bull | Key falsifier | Boundary discipline |
|---|---|---|---|---|---|---|
| Pharmaceuticals | Approval/launch then 3-year patient-years | Failure, >12-mo delay or ≤75% of base patient-years | Gate clears; 75–125% | Gate clears; >125% via label, share or persistence | Submission, label, persistence, net price | Gate failure/delay first; then non-overlapping patient-year bands |
| Biotechnology | Probability-adjusted treated patients | Clinical/CMC failure, financing or weak paid conversion | Approvable label, normal access | Differentiated label + superior paid starts/persistence | Endpoint/CMC; authorization; patient starts | Once approved, stop varying current approval probability |
| Medical technology | Utilization per active installed system | Flat/down utilization despite placements | Modest positive utilization, normal pull-through | Utilization and recurring revenue/system materially exceed plan | Procedures/system; revenue/procedure; lease returns | Set thresholds before the operating update |
| Diagnostics | Paid tests × cash contribution/test | Coverage/collections fail; ≤80% of base contribution | 80–120% | >120% via paid utilization and COGS leverage | Paid rate; cash ASP; COGS/test; collections | Use cash contribution, not reported revenue/test |
| Life-science tools | Order conversion and consumables pull-through | Cancellations or destocking persist | Normal conversion and utilization | Broad recovery + pull-through above installed-base growth | Backlog aging; consumables; utilization | Separate order growth from shipment timing |
| CRO / CDMO | Book-to-bill or capacity utilization | CRO B2B <1x; CDMO below return threshold | CRO 1.0–1.15x; normal CDMO ramp | CRO >1.15x or CDMO utilization → excess ROIC | Cancellations; conversion; yield; capex | LTM CRO bookings; project-level CDMO economics |
| Providers / services | Contribution per adjusted case | Payer/service mix and costs overwhelm volume | Normal reimbursement and productivity | Higher-acuity mix + labor/productivity leverage | Gross profit or EBITDA/adjusted case | Revenue/case alone is insufficient |
| Managed care | Reserve-normalized current-year MCR | >100 bps worse than pricing assumption | Within ~±100 bps | >100 bps favorable, excl. reserve releases | Current-service MCR; cohort experience | Normalize prior-period development first |
| Distribution / PBM | Normalized profit per unit or claim | Declines >5% | ~−5% to +5% | Grows >5% via specialty/services or procurement | GP/unit; profit/claim; client retention | Never use revenue growth as discriminator |
| Health technology | NRR and paid attach | NRR <105% or usage stays unpaid | NRR 105–110%; selective paid attach | NRR >110%; material paid attach + FCF leverage | NRR; RPO; paid attach; gross margin | Adjust thresholds for the software model |
| Consumer / animal health | Volume/share-led contribution growth | Share loss or negative contribution growth | Stable share, low/mid-single-digit profit growth | Volume, share, innovation → >5% profit growth | Volume/mix; share; recurring pull-through | Separate category, price, volume and share |

## Valuation Map (all 11 industries)

| Industry | Economic unit | Dominant formula | Preferred framework | Price-implied variable | Common error |
|---|---|---|---|---|---|
| Pharmaceuticals | Treated patient-year | Revenue = eligible × diagnosed × treated × share × persistence × net price | Franchise DCF / SOTP | Peak share, duration, LOE erosion | One corporate multiple without product/LOE replacement |
| Biotechnology | Probability-adjusted treated patient | rNPV = cash + Σ probability × NPV(product cash flows) − debt − dilution | Product/indication rNPV | PoA, peak patients, financing need | Double-counting trial evidence across PoA, share and price |
| Medical technology | Active system or treated patient | Recurring GP = active installed base × utilization × pull-through × contribution margin | DCF / EV-EBITDA | Procedures/system; recurring GP/system | Valuing placements without utilization |
| Diagnostics | Paid, reportable test | Contribution = paid tests × (cash ASP − COGS/test) | Probability-adjusted DCF | Paid rate, cash ASP, COGS/test | Ordered tests or accounting ASP as cash economics |
| Life-science tools | Active instrument or converted order | Revenue = orders × conversion; recurring GP = instruments × utilization × pull-through | DCF / EV-EBITDA | Normalized growth and pull-through | Treating placements/orders as revenue |
| CRO / CDMO | Converted backlog or productive capacity | CRO revenue = backlog × conversion; CDMO EBITDA = capacity × utilization × yield × price × margin | EV-EBITDA / DCF / project NPV | Book-to-bill, utilization, ROIC−WACC | Ignoring cancellations, validation timing, capex |
| Providers / services | Adjusted case or infusion | EBITDA = cases × (reimbursement/case − care cost/case) − fixed cost | EV-EBITDA / DCF | Normalized reimbursement less care cost/case | Revenue/case without acuity and cost |
| Managed care | Member-month | Profit = member-months × premium PMPM × (1 − MCR − admin ratio) | Normalized P/E / DCF / SOTP | Current-service MCR; cohort margin | Capitalizing reserve releases or member growth |
| Distribution / PBM | Drug unit or claim | Profit = units/claims × net profit/unit + specialty/services − opex | Normalized P/E / FCF yield / SOTP | Post-concession profit/unit; retention | Valuing pass-through drug revenue |
| Health technology | Recurring-revenue customer | Ending ARR = beginning ARR × NRR + new ARR; FCF = ARR × mature margin | EV-ARR / EV-revenue + FCF cross-check | Paid AI attach, NRR, terminal margin | Treating usage or launches as paid ARR |
| Consumer / animal health | Repeat purchase, visit or active instrument | Growth = category/visits + share + price/mix; recurring revenue = base × utilization × pull-through | DCF / P-E / EV-EBITDA | Volume, share, visits, pull-through | Capitalizing price or outbreak/timing effects |

## Investable View Builder (the six layers)

| Layer | Question | Required model output | Minimum evidence standard |
|---|---|---|---|
| Clinical | How differentiated is the product, and against which comparator? | PoA; eligible population; share; persistence | Endpoint hierarchy, effect size, multiplicity, safety, external validity |
| Regulatory | What exact label, restrictions and timing are probable? | Launch date; accessible population; monitoring burden | Agency feedback, filing status, CMC and label precedent |
| Commercial | How does eligibility become paid recurring demand? | Funnel conversion; net price; utilization; retention | Diagnosed → referred → authorized → started → paid → persistent |
| Competitive | Why should share and economics persist? | Share curve; price erosion; switching; terminal growth | Active-comparator profile, pipeline timing, contracting, workflow |
| Financial | What cash remains after delivery and reinvestment? | Contribution margin; capex; working capital; dilution | Unit economics, capacity, cash burn, leverage, runway |
| Valuation | What does the current price already assume? | Implied PoA; units; MCR; NRR; utilization or margin | Reverse DCF/rNPV and consensus bridge |

**Variant-perception test (score each):** disagreement is an explicit market-implied variable · evidence directly changes that variable · the difference matters after probability weighting · a catalyst can resolve the disagreement · the thesis has an observable falsifier.

**Template sentence:** *"At the current price, the market appears to imply [X]. Evidence [E] changes model variable [Y] from [A] to [B]. That produces [Δ revenue/margin/FCF/rNPV] under the base case. Catalyst [C] should resolve the disagreement within [time horizon]. Observation [F] would falsify the thesis."*
