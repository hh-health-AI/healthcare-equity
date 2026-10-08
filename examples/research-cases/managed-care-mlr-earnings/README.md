# UnitedHealth: medical costs → quarterly earnings

**A 100 bp increase in the medical care ratio reduces modeled quarterly pretax earnings by $869.56 million and diluted EPS by about $0.78, with premiums, other costs, shares and the assumed marginal tax rate held constant.** The same scale makes reserve development worth examining before extrapolating an underwriting recovery.

This is a real-company research case using the primary issuer release dated **July 16, 2026**, for the **three months ended June 30, 2026**. Analysis prepared October 8, 2026. It is a reproducible sensitivity exercise rather than a current recommendation, consensus estimate or issuer forecast. The company calls this metric **MCR**; “medical loss ratio” describes the broader industry concept.

## Evidence and scope

The [primary earnings release](https://www.unitedhealthgroup.com/content/dam/UHG/PDF/investors/2026/unh-reports-second-quarter-2026-results.pdf) reports consolidated quarterly premiums of **$86,956 million**, medical costs of **$75,358 million**, MCR of **86.7%**, and **$860 million of net favorable medical reserve development**. Most of that development concerns **2026 dates of service**, so it cannot all be described as a release of prior-year reserves. The statement of operations reports pretax earnings of **$6,968 million**, taxes of **$1,298 million**, net earnings of **$5,670 million**, noncontrolling earnings of **$186 million**, common earnings of **$5,484 million**, diluted shares of **906 million**, and diluted EPS of **$6.04**. Its dated full-year adjusted EPS guidance is **$19.50–$20.00**.

Locators: physical PDF **page 1**, MCR performance bullet; **page 3**, medical reserve development discussion; **page 10**, consolidated statement, Q2 2026 column and EPS footnote (a); **page 6**, July 16 outlook column. [sources.json](sources.json) records each checked statement, unit, locator and retrieval date. Verification covers these selected facts; it is not independent assurance of the accounts.

## Reconcile the denominator before changing the ratio

`75,358 / 86,956 = 86.662220%`, which rounds to the issuer's 86.7%. These are matching **consolidated medical costs and premium revenue**. Applying the ratio to total corporate revenue, segment revenue or all people served would introduce a different denominator.

The earnings bridge also reconciles: `6,968 − 1,298 = 5,670`; `5,670 − 186 = 5,484` (USD millions). The model uses the observed **18.628014% effective tax rate as an assumed marginal tax rate**. That assumption does not establish the actual tax effect of an incremental medical claim.

Published rounded earnings and shares give `5,484 / 906 = $6.052980`, rather than reported EPS of $6.04. The release identifies a diluted EPS numerator reduction for forward share repurchase contracts, while the table rounds earnings and shares. The exact numerator is unavailable here. Therefore the model **anchors EPS to the reported $6.04 and adds only incremental aftertax earnings / 906 million shares**. It does not invent a balancing item or claim exact EPS reconstruction.

## Quarterly scenarios

Change is relative to the **unrounded computed ratio**; positive basis points mean higher medical costs. Assumptions: premiums, nonmedical expenses, interest, other items, noncontrolling earnings and diluted shares stay fixed; all aftertax cost changes affect common earnings. No scenario is annualized.

| MCR change | Computed MCR | Pretax earnings change ($m) | Aftertax common earnings change ($m) | EPS change | EPS from reported anchor |
|---:|---:|---:|---:|---:|---:|
| −100 bp | 85.6622% | +869.56 | +707.58 | +$0.7810 | $6.8210 |
| −50 bp | 86.1622% | +434.78 | +353.79 | +$0.3905 | $6.4305 |
| 0 bp | 86.6622% | 0.00 | 0.00 | $0.0000 | $6.0400 |
| +50 bp | 87.1622% | −434.78 | −353.79 | −$0.3905 | $5.6495 |
| +100 bp | 87.6622% | −869.56 | −707.58 | −$0.7810 | $5.2590 |

Formulas: `incremental medical costs = premium revenue × ΔMCR`; `Δpretax earnings = −incremental medical costs`; `Δcommon earnings = Δpretax × (1 − assumed marginal tax rate)`; `ΔEPS = Δcommon earnings / diluted shares`. One basis point equals `0.0001` of the ratio, not `0.01`.

Adding all $860 million of favorable development back to medical costs produces a mechanical **87.651226% no-development proxy** and reduces anchored EPS by about **$0.7724 to $5.2676**. This proxy includes changes in estimates for other 2026 service dates and is **not a pure current-quarter service-cost ratio**. It also is not the issuer's non-GAAP adjusted EPS. The addback is a separate illustration, not an additional deduction in the scenario table.

## What the market would need to believe

No market price or consensus estimate was verified for this packet. Use the following conditional hurdle rather than claiming an observed valuation gap. The **18× annual adjusted EPS multiple** and share prices are analyst-selected examples; the **$19.75 midpoint** is derived from guidance dated July 16, not confirmed as the latest outlook.

| Illustrative share price | Selected P/E | Annual adjusted EPS required (`price / P/E`) | Required EPS less dated $19.75 guidance midpoint |
|---:|---:|---:|---:|
| $300 | 18× | $16.67 | −$3.08 |
| $350 | 18× | $19.44 | −$0.31 |
| $400 | 18× | $22.22 | +$2.47 |

This answers a conditional underwriting question: at the selected multiple, which annual earnings level would support the selected price? It does **not** convert quarterly MCR directly into annual EPS. A live valuation requires a dated price, matched forward consensus period, annual premium forecast, seasonality, taxes, repurchases, and a separate Optum earnings build.

## Investment hypothesis, catalysts and falsifiers

**Analyst hypothesis:** an underwriting recovery has greater persistence if medical costs on matching service periods improve after isolating reserve development, while pricing and benefit design remain adequate. The reported headline alone does not demonstrate that persistence. The quarterly sensitivity shows the earnings scale at risk, but not the probability of a change.

| Evidence to monitor | Catalyst or decision | What would weaken the hypothesis |
|---|---|---|
| Subsequent quarterly cost ratios and reserve-development disclosures | Recalculate the matched-period bridge on the next issuer release; no event date asserted here | Apparent improvement disappears when favorable development is removed, or later adverse development offsets it |
| Premium yields, membership and product mix by business | Assess whether repricing protects earnings after enrollment responses | Membership/mix losses or benefit changes consume the pricing gain |
| Utilization, acuity and claims completion | Distinguish actual service-cost trend from estimation changes | Utilization or unit costs repeatedly exceed pricing assumptions |
| Optum earnings and intercompany exposure | Reconcile the consolidated result with separate business economics | An insurance improvement is offset by care-delivery/PBM weakness or inconsistent consolidation |
| Government payment, Stars and risk-adjustment disclosures | Revisit earned premium and margin assumptions when official policy changes | Payment or risk-adjustment changes lower earned premium without matching cost relief |

These are analytical reopening criteria, not claims that any specific future outcome or announced catalyst date has been verified. A variant view should identify the cost trend and reserve assumption that differs from a **dated, separately sourced consensus** before proposing a trade.

## Reproduce and review

From the repository root:

```bash
python examples/research-cases/managed-care-mlr-earnings/model.py
python examples/research-cases/managed-care-mlr-earnings/model.py --check
```

The first command regenerates [results.json](results.json); the second checks it without writing. [inputs.json](inputs.json) separates observed values from assumptions. [model.py](model.py) uses standard-library decimal arithmetic and validates the rounded MCR and earnings bridge before producing results.

**Confidence: 0.93 for the selected source facts and static arithmetic; no probability assigned to a future earnings recovery.** Main caveats: one-quarter static model; rounded EPS denominator; marginal-tax assumption; reserve proxy does not isolate current-quarter service; dated guidance and illustrative market hurdles. No independent human accuracy review has been completed.
