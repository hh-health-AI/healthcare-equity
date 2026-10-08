# Intuitive Surgical: procedures, revenue and the price of growth

**Research question:** how much does a change in procedure growth or revenue per procedure change annual instruments and accessories revenue?

**Answer:** in this explicitly assumed platform allocation, one percentage point of da Vinci procedure growth changes annual I&A revenue by **$58.39m**. A 1% change in da Vinci revenue per procedure changes it by **$66.85m** at base-case volume. Hospital adoption matters, but placement counts alone do not establish procedure productivity or shareholder return.

This is a real-company worked research case with a reproducible revenue sensitivity, not a live stock recommendation. Information cutoff: **July 16, 2026**; sources checked **October 8, 2026**. No information published after the cutoff is incorporated. All monetary inputs use USD; output dollar precision is computational and does not imply forecast accuracy.

## Read and reproduce

```bash
python examples/research-cases/medtech-procedures-revenue/model.py
python examples/research-cases/medtech-procedures-revenue/model.py --check
```

No packages or credentials are required. [inputs.json](inputs.json) separates reported history, management guidance and analyst assumptions. [sources.json](sources.json) identifies the document, date, units and locator for every reported field. [results.json](results.json) contains the exact model output and sensitivity grids.

## What is observed, and what is inferred?

Q2 2026 growth was approximately **15% for da Vinci procedures**, **36% for Ion**, and **16% combined**. Quarter-end installed bases were **11,710 da Vinci** and **1,096 Ion** systems. I&A revenue was **$1,734.9m** versus **$1,474.1m** a year earlier. The revenue statement uses USD millions; installed bases are endpoint counts. [SEC release: Q2 Highlights and quarterly revenue table](https://www.sec.gov/Archives/edgar/data/1035267/000103526726000047/q226ex-991earningsrelease.htm).

Management's FY2026 da Vinci procedure-growth outlook was **13.5–15.5%**, with performance expected near the midpoint. This is guidance as of July 16, not a realized result or consensus estimate. [Issuer release: 2026 Financial Outlook](https://investor.intuitivesurgical.com/news-releases/news-release-details/intuitive-announces-second-quarter-earnings-6).

The annual model anchors to FY2025 platform-specific procedure counts and consolidated revenue, rather than annualizing one quarter. The [FY2025 10-K](https://isrg.intuitive.com/static-files/f684d492-5169-48b5-9723-8ebcaa05c098), printed pages **68** and **76**, supplies these inputs. The revenue rows reconcile to the total before forecasting. SP procedures remain within the da Vinci count; no third platform is added.

**Analytical hypothesis:** procedure growth plus revenue per procedure explains recurring consumable demand more directly than ending installed base. This is a model mapping, not causal proof. We do not calculate utilization growth: the combined procedure numerator must never be divided by only the da Vinci base, and even matching platform ending bases are not average active systems.

## Model bridge and assumptions

The filing does not provide platform-specific I&A revenue in the used table. We therefore assume **$1,250 per Ion procedure** for the FY2025 calibration and solve the residual da Vinci revenue per procedure at **$1,851.82**. Both are model constructs; neither is a reported platform ASP. The calibrated components sum to reported I&A revenue.

```text
Baseline da Vinci I&A = reported total I&A − Ion procedures × assumed Ion revenue/procedure
Forecast platform I&A = baseline platform procedures × (1 + procedure growth)
                       × calibrated/assumed revenue/procedure × (1 + price/mix change)
Total forecast revenue = da Vinci I&A + Ion I&A + systems + services
```

The base uses the guidance midpoint for da Vinci volumes, assumed Ion growth of 30%, unchanged platform revenue per procedure, systems revenue growth of 12%, and service growth of 15%. Only the da Vinci volume midpoint comes from management guidance. Systems revenue includes different recognition arrangements; the model therefore grows its reported revenue line directly, without multiplying placements by an invented system ASP. Service growth is assumed directly, without dividing by an endpoint installed base.

| Analyst scenario | da Vinci volume growth | Ion volume growth | da Vinci price/mix change | FY2026 I&A revenue | FY2026 total revenue |
|---|---:|---:|---:|---:|---:|
| Bear | 10.0% | 20.0% | −3.0% | $6.446bn | $10.773bn |
| Base | 14.5% | 30.0% | 0.0% | $6.920bn | $11.498bn |
| Bull | 18.0% | 40.0% | +2.0% | $7.280bn | $12.085bn |

Systems/service growth also varies by scenario: **5%/10% bear**, **12%/15% base**, **18%/20% bull**. These scenarios are sensitivities, not assigned probabilities.

For an illustrative earnings bridge, assume 60% of changed I&A revenue converts to incremental operating profit. The bear/bull I&A deviations from base then imply **−$284.06m / +$216.10m** of operating contribution. This excludes changes to fixed costs, tariffs, tax, share count and other segment margins; it is not a company EPS forecast. Price/mix means the effective revenue per procedure, not list-price increases alone. Shipment timing and stocking can also affect this calibration.

The allocation sensitivity varies assumed Ion revenue per procedure from **$750 to $1,750**, recalibrating da Vinci revenue each time to preserve the reported baseline total. The growth/mix grid varies da Vinci growth across the guidance bounds and price/mix from −3% to +3%. Do not treat procedure growth and mix as statistically independent; these grids explore conditional outcomes.

## Market expectations: a conditional inversion

**Status: NEEDS_MARKET_INPUTS.** No current price, dated enterprise value, sell-side consensus or observed market-implied growth has been inserted. To compare with a valuation, supply a dated enterprise value and an explicit assumed forward EV/sales multiple:

```bash
# Illustrative inputs only; these are not a market quote or a recommended multiple.
python examples/research-cases/medtech-procedures-revenue/model.py \
  --enterprise-value-usd 150000000000 --ev-sales-multiple 12
```

This hypothetical pair requires **$12.5bn** of revenue and **31.66%** da Vinci procedure growth if all other base assumptions hold. The result illustrates a conditional expectations hurdle, not the market's actual forecast. A chosen multiple can explain the same enterprise value with different growth; the inversion is not a unique valuation.

Before making a trade decision, refresh net cash/debt, share count, enterprise value and consensus for a single valuation date. Resolve whether the relevant multiple is justified by growth duration, margin quality and capital needs. A full intrinsic valuation would need cash flow, dilution and terminal assumptions beyond this revenue case.

## Falsifiers and update rules

1. **Volume:** replace the base thesis if a subsequent full-year da Vinci outcome is below the **13.5%** lower guidance bound. The case deliberately tests adoption through procedures, not shipment counts.
2. **Monetization:** challenge flat da Vinci revenue per procedure if disclosed pricing/mix or revenue reconciliations require a sustained reduction beyond the **−3%** sensitivity. The current platform split cannot prove that threshold has already been breached.
3. **Profit conversion:** replace the assumed 60% conversion if tariffs, servicing, product mix or operating expense change the incremental margin. Strong consumable revenue alone does not establish EPS upside.
4. **Capital equipment:** reopen the systems-growth assumption if revenue recognition, lease mix, trade-ins or capital spending change materially. Do not infer net installed-base additions directly from gross placements.
5. **Source scope:** reopen if a restatement changes a used number, platform revenue becomes available, or a new reporting period replaces the cutoff. Match platform, geography, period and denominator before adding utilization.

**Confidence:** 0.97 in transcription of the specified checked primary-source fields; 0.65 in the usefulness of the assumed platform allocation for predicting actual revenue. **Key caveats:** approximate procedure counts, assumed platform monetization, timing/mix effects, no live market inputs, and no cash-flow valuation. Executable reproduction checks arithmetic; it does not independently certify source truth.
