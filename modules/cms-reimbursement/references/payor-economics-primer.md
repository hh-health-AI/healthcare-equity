# Payor Economics Primer — how the machine makes and loses money

Working model for analysis; `project_search` the project KB textbooks for depth.

## The core equation

Underwriting profit = member-months × premium PMPM × (1 − MCR − admin ratio). Everything in payor analysis is a decomposition of one of those four factors. Premium is largely set 6–18 months ahead (bids, rate filings); cost trend is discovered in real time — so the recurring failure mode is **pricing lag**: utilization accelerates, this year's premiums can't respond, margins compress for 12–24 months until repricing catches up. Read every payor print by asking "is current-period trend running above or below what was priced in?" — normalized for reserve development first.

## Reserve mechanics (why reported MLR lies)

Claims lag service. Payors book IBNR estimates; revisions surface later as prior-period development. Favorable PPD in a quarter means *last* period was better than booked — it says nothing about the current run-rate, and can mask current deterioration. Discipline: strip PPD to get current-service MCR (the scenario discriminator), and watch days-claims-payable for reserve drawdown funding earnings.

## Government books

**MA:** revenue = benchmark-driven bids × risk scores × Star bonuses. Three exogenous dials CMS turns annually — benchmark growth (Rate Notice), risk model (V28 compresses RAF revenue), Stars (quality bonus two years forward). Cohort effect: new members run higher benefit ratios than retained members until "seasoned" — fast MA growth mechanically pressures margin before it accretes. **Medicaid:** state rates renegotiated on acuity; redetermination churn shifts both membership and mix. **Exchange/commercial:** annual repricing, faster correction cycle.

## Where the profit pools sit

Underwriting margins are thin (low single digits) and politically capped (minimum MLR rebates). Diversified payors therefore push profit into owned services — PBM, specialty pharmacy, provider/VBC, health services — where intercompany pricing shifts margin out of the regulated insurance entity. Analytical consequence: segment MLRs of vertically integrated payors are not comparable to pure insurers without repricing intercompany flows at market (see SUB-SVC-03 in healthcare-equity).

## Provider-side mirror

For hospitals and risk-bearing providers the same flows invert: payor mix (Medicare/Medicaid/commercial) sets realized rate; acuity and site of service set revenue per case; labor and supplies set cost per case. Contribution per adjusted case — not revenue per case — is the scenario discriminator.

## What moves stocks

MLR surprise vs pricing assumption (±100 bps bands), Rate Notice benchmark growth, Stars distribution shifts, V28/RADV developments, redetermination and enrollment swings, utilization inflections (e.g., outpatient surgical recovery, behavioral, GLP-1 spillover), and policy shocks (PBM reform, MFP expansion, site-neutral payment). Each maps to a dated release — feed them to the rule-cycle calendar.
