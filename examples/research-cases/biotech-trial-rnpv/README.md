# HELIOS-B: trial evidence, a realized approval gate and rNPV sensitivity

**Real clinical and regulatory observations; illustrative economic assumptions.** This is a retrospective, reproducible research case for Alnylam's vutrisiran in US ATTR cardiomyopathy, linked to teaching case **C03**. It is not a completed ALNY company valuation or a current price target.

Sources accessed **8 October 2026**. The counterfactual model holds its valuation date at **20 March 2025** to isolate an approval decision. It does not reconstruct a contemporaneous forecast or historical investment return.

## Research question and answer

Does strong Phase 3 evidence justify treating approval, patient conversion and valuation as one uncertainty?

No. The publication supports a clinical effect against placebo. The later realized US approval resolves that historical regulatory decision. Paid demand, realized net price and cash generation still require separate evidence. This case therefore keeps commercial assumptions visible and changes the approval gate only when the approval itself is observed.

## Reproduce the model

Python 3.10+; standard library only; no network, credentials or LLM needed:

~~~sh
python3 examples/research-cases/biotech-trial-rnpv/model.py
python3 examples/research-cases/biotech-trial-rnpv/model.py --check
~~~

The first command regenerates [results.json](results.json); the second compares the saved results and checks arithmetic without writing files. Each annual cash flow is inspectable, and hashes identify the exact [inputs.json](inputs.json) and [sources.json](sources.json) used. Input validation rejects missing fields, nonfinite numbers, probability/weight errors and invalid periods. The checks include an independent one-period hand calculation and the approval-gate bridge.

To test a **hypothetical residual asset EV** of USD 500m:

~~~sh
python3 examples/research-cases/biotech-trial-rnpv/model.py \
  --target-asset-ev-m 500 --out /tmp/helios-b-implied.json
~~~

The 500 is a user-selected example, not observed ALNY market value.

## Evidence ledger

| Source | Vintage / locator | Observation checked |
|---|---|---|
| [S1: ClinicalTrials.gov NCT04153149](https://clinicaltrials.gov/study/NCT04153149) | Current record update 12 January 2026; enrollment, design and first two primary outcomes | Phase 3 placebo-controlled study; 655 participants; overall and monotherapy composite endpoints |
| [S2: Fontana et al., PMID 39213194](https://pubmed.ncbi.nlm.nih.gov/39213194/) | NEJM 392:33–44, issue dated 2 January 2025; abstract Methods and Results | Overall composite HR 0.72 (95% CI 0.56–0.93); separate mortality endpoint through 42 months, HR 0.65 (0.46–0.90) |
| [S3: FDA approval record](https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=637618) | Marketing approved, entry 2 | US adult wild-type/hereditary ATTR-CM approval on 20 March 2025 |
| [S4: Alnylam SEC 8-K](https://www.sec.gov/Archives/edgar/data/1178670/000117867025000038/alny-20250320.htm) | Item 8.01, first paragraph; event 20 March, signature 21 March 2025 | Independent document cross-check of the issuer's approval announcement |

The registry is sponsor-submitted and later updated; it is not an archived predecision snapshot. The publication's abstract was retrieved through PubMed. Full paper, protocol/SAP, FDA clinical review and detailed label restrictions were not reviewed. Coverage limits and exact field locators remain in the source ledger.

**Endpoint discipline:** a 28% relative reduction in the composite hazard is not a mortality-only claim. The published mortality HR of 0.65 describes a 35% relative hazard reduction, not an absolute risk reduction. Any 36% figure would need its own analysis, population and time point; this case does not verify that broader statement. Neither comparison establishes superiority to tafamidis.

## Facts → inference → assumption

| Item | Type | Treatment in the model |
|---|---|---|
| Published Phase 3 treatment effect and uncertainty | Observed clinical evidence | Supports clinical appraisal; does not mechanically calibrate approval probability or sales |
| Prior approval gate of 0.60 | Illustrative assumption | Sensitivity anchor only; not a historical analyst estimate |
| Realized US ATTR-CM approval | Observed regulatory decision | Approval gate becomes 1.00 for this already realized decision |
| Treated and paid patient-years, net price, FCF conversion, discount rates | Illustrative commercial/financial assumptions | Explicit scenario inputs; need company, payer and competitive evidence before investment use |
| Actual market price, company cash/debt, dilution and other assets | Missing | Equity/per-share output remains null and marked NEEDS_DATA |

For the clinical publication alone, the defensible implication here is **UNCERTAINTY_ONLY**: retain the illustrative central gate, inspect its 0.40–0.80 sensitivity, and obtain a full regulatory/clinical review before proposing a calibrated change. The interval is a chosen modeling range, not an empirical confidence interval.

The realized approval implies **CHANGE: 0.60 → 1.00** for that historical regulatory gate. The hazard ratio is not used again to raise share, price or commercial probability.

## Commercial assumptions and cash-flow bridge

Every figure in this section is illustrative.

Base paid patient-years for 2026–2032 are 1,000; 2,500; 5,000; 8,000; 10,000; 12,000; 12,000. These are annual treated-and-paid exposure units, not incident patients, prescriptions, eligible prevalence or published company counts.

Annual net revenue per patient-year is USD 100,000. Base after-tax unlevered FCF is 35% of revenue. That conversion includes recurring costs, reinvestment and working capital; deducting those again would double-count expense. A separate USD 25m upfront committed launch investment is paid regardless of the approval gate. Historical R&D is sunk and excluded.

| Conditional commercial scenario | Patient-year multiplier | Net-price multiplier | After-tax FCF/revenue | Discount rate | Upfront USDm | Illustrative weight |
|---|---:|---:|---:|---:|---:|---:|
| Bear | 0.50× | 0.80× | 25% | 14% | 35 | 25% |
| Base | 1.00× | 1.00× | 35% | 12% | 25 | 50% |
| Bull | 1.50× | 1.10× | 45% | 10% | 20 | 25% |

These weights describe commercial uncertainty **conditional on approval** and sum to one. They do not replace the separate approval gate. They are not estimated outcome probabilities.

For each annual period:

- Revenue = paid patient-years × annual net revenue per patient ÷ 1,000,000.
- Conditional operating FCF = revenue × after-tax FCF conversion.
- Asset rNPV = approval gate × Σ[conditional FCF / (1 + r)^t] − upfront investment.
- t = days from 20 March 2025 to the period end ÷ 365.25.

Approval risk is applied once. No extra global PoS multiplier is applied to already gated cash flows. There is no terminal value, no cash flow beyond 2032 and no claim that 2032 is the actual patent/LOE cliff.

## Before/after approval sensitivity

USD millions; rounded here to one decimal. The exact results and annual audit rows are in [results.json](results.json).

| Scenario | Before: gate 0.60 | After: realized gate 1.00 | Change from gate only |
|---|---:|---:|---:|
| Bear | 107.8 | 203.0 | 95.2 |
| Base | 526.8 | 894.6 | 367.8 |
| Bull | 1,275.7 | 2,139.5 | 863.8 |
| Weighted across conditional commercial scenarios | 609.2 | 1,032.9 | 423.7 |

Economic inputs and discount date are held fixed. These changes isolate a hypothetical prior gate against a realized decision; they are not attributed stock-price moves or calibrated estimates of actual franchise value.

| Base discount rate | Gate 0.40 | Gate 0.60 | Gate 0.80 | Gate 1.00 |
|---|---:|---:|---:|---:|
| 10% | 382.2 | 585.8 | 789.4 | 992.9 |
| 12% | 342.8 | 526.8 | 710.7 | 894.6 |
| 14% | 308.2 | 474.8 | 641.4 | 807.9 |

Once the decision has occurred, gate values below one are counterfactual sensitivities. Forward underwriting should focus on commercial conversion and future risks, rather than pretending the completed approval remains pending.

## Conditional market-implied framework

A genuine variant view needs a verified market value and allocation to this indication. Those inputs are missing.

If an analyst supplies a residual asset EV after reconciling company net cash, other programs and unallocated costs:

**Implied gate = (residual asset EV + upfront investment) / conditional operating PV.**

The optional command calculates that expression for the base case. An implied value above one means the chosen economics cannot explain the supplied residual EV. After approval, the useful reverse-engineering question becomes which paid patient-years, net price or FCF conversion explain the residual EV at gate one.

No observed market price, consensus gap or equity/share value is claimed. The template view is conditional: “If verified residual asset EV implies weaker commercial conversion than independently verified access and paid-patient evidence support, and the resulting valuation gap survives downside scenarios, investigate a variant thesis.”

## Catalyst, falsifier and next diligence

The historical resolving catalyst was the **20 March 2025 US approval**. The next commercial checkpoint in this normalized exercise is the year ending **31 December 2026**; its actual results-release date and relevant disclosure granularity remain NEEDS_DATA.

A predefined economic falsifier is paid patient-years or realized net revenue more than 20% below the illustrative 2026–2027 path in two successive full-year checkpoints, without an offsetting price or margin improvement. That threshold is an analyst choice. Apply it only after matching geography, indication, exposure period and net-price definitions; group revenue alone may not isolate this indication. Missing disclosure gives NEEDS_DATA rather than a fabricated pass/fail.

The fastest way to break the commercial hypothesis is to find payer barriers, weak persistent paid starts, competitive displacement or lower incremental FCF that make the illustrative conversion path unattainable. The placebo-controlled result does not settle any of these questions.

Next diligence: review full trial/SAP and FDA documents; obtain indication-specific access, paid patient-year and net-price evidence; replace normalized assumptions with sourced forecasts; complete the company valuation bridge before comparing with market price.

**Confidence: 0.95 on the narrowly stated primary-source observations and reproduced arithmetic; 0.40 on economic applicability until commercial inputs are verified.** Scope is limited to this evidence-to-assumption exercise. No efficacy prediction, investment performance claim or buy/sell recommendation is supplied.

