# Prompts — Modeling & Valuation

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## MOD-01 · DCF Stress Test and Reverse-Engineer
Tags: `#modeling #cross-sector #senior-judgment`
**When to use.** When you have a working DCF and need to know what the market prices.
**Inputs.** DCF assumptions.

PROMPT:
> I will paste my DCF assumptions for [TICKER]. (1) Stress-test: three most sensitive assumptions, aggressive vs mid-point positioning, terminal value share sanity check. (2) Reverse-engineer current price: what terminal margin and growth is the market pricing, is it internally consistent? End with the single assumption to pressure-test.

## MOD-02 · Sum-of-the-Parts for Diversified Pharma or Medtech
Tags: `#modeling #pharma #medtech #senior-judgment`
**When to use.** For diversified large-caps where consolidated multiples obscure segment value.
**Inputs.** Segment disclosure, peer multiples, balance sheet.

PROMPT:
> Build SOTP for [TICKER]. (1) Natural segments with proposed analytical split; (2) 5-year forecast per segment with peer-derived multiples; (3) balance sheet adjustments; (4) per-share value and conglomerate discount; (5) divestiture optionality; (6) sensitivity.

## MOD-03 · Risk-Adjusted NPV (rNPV) Model for a Biotech Asset
Tags: `#modeling #biotech #ctgov #fda-ema #pubmed #senior-judgment`
**When to use.** When valuing a single drug asset or building a clinical-stage biotech sum-of-pipelines.
**Inputs.** Asset details, epidemiology, comparable launches.

PROMPT:
> Build rNPV for [asset] in [indication]. (1) Patient funnel; (2) pricing by geography; (3) peak sales and time to peak; (4) COGS, R&D, SG&A, royalties; (5) LOE timing and decay; (6) PoS decomposition (phase transition × regulatory × commercial) with BIO/PhRMA base rates; (7) discount rate; (8) rNPV per share with PoS and peak share sensitivity.

## MOD-04 · Patent Cliff and LOE Bridge for Large-Cap Pharma
Tags: `#modeling #pharma #sec-filings #senior-judgment`
**When to use.** For mature pharma where LOE vs pipeline replenishment drives the next decade.
**Inputs.** 10-K product disclosures, pipeline page, sell-side LOE notes.

PROMPT:
> LOE bridge for [TICKER] 2025–2032. (1) Each franchise >5% revenue: molecule, revenue, LOE date, post-LOE trajectory (SM: 80–90% loss in 18 months; biologics: 30–50% over 3–5 years); (2) at-risk revenue by year; (3) pipeline contribution bridge; (4) organic revenue trajectory; (5) gap-to-consensus; (6) M&A burden.

## MOD-05 · Medtech Razor-Blade Model
Tags: `#modeling #medtech #sec-filings #senior-judgment`
**When to use.** For capital equipment + consumables companies.
**Inputs.** Installed base history, placement guidance, consumables disclosure, peer benchmarks.

PROMPT:
> Razor-blade model for [TICKER]. Benchmark: mature razor/blade models target 65–70% gross margin vs 50–60% for capital-equipment-only. (1) Installed base build; (2) utilisation trend; (3) placement forecast; (4) consumables forecast; (5) mix shift and margin trajectory; (6) sensitivity to placement slowdown vs utilisation drop; (7) cross-check vs management target.

## MOD-06 · Tools and Diagnostics Capex-Cycle Model
Tags: `#modeling #tools-dx #sec-filings #senior-judgment`
**When to use.** For life sciences tools where end-market capex cycles drive instrument revenue.
**Inputs.** End-market disclosure, NIH outlook, biotech funding, peer commentary.

PROMPT:
> End-market capex cycle model for [TICKER]. (1) Revenue by end-market; (2) cycle drivers and indicators per end-market; (3) forecast with indicator linkage; (4) instrument/consumables/services split; (5) margin mix consequence; (6) peak-to-trough sensitivity.

## MOD-07 · MA Star Ratings and Bid Cycle Model
Tags: `#modeling #services-payors #cms #senior-judgment`
**When to use.** For Medicare Advantage operators. (Cycle tracking lives in cms-reimbursement ma-bid-cycle; this is the financial model.)
**Inputs.** CMS Stars, rate notice, segment detail, bid commentary.

PROMPT:
> MA Star/bid cycle model for [TICKER]. (1) Membership by contract with Stars; (2) quality bonus exposure; (3) bid cycle dynamics (V28, IRA Part D, benchmark); (4) member growth scenarios; (5) revenue and MLR for next two plan years; (6) Stars and utilisation stress tests; (7) peer comparison.

## MOD-08 · Digital Health Unit Economics Stress Test
Tags: `#modeling #digital-health #sec-filings #senior-judgment`
**When to use.** For digital health names where unit economics at scale are questioned.
**Inputs.** Cohort disclosures, S-1, investor day decks, peer benchmarks.

PROMPT:
> Stress-test unit economics for [TICKER]. (1) Per-unit P&L; (2) CAC by channel with payback; (3) LTV with retention and expansion; (4) LTV/CAC by cohort — flag below the 3:1 sustainability threshold; (5) path to FCF; (6) reality check vs SaaS/consumer health comps; (7) smart short's first attack.

## MOD-09 · Working Capital and Cash Conversion Forensics
Tags: `#modeling #cross-sector #sec-filings #senior-judgment`
**When to use.** When FCF conversion is deteriorating or quality issues are suspected.
**Inputs.** 12 quarters of 10-Qs and 10-Ks, cash flow statements, footnotes.

PROMPT:
> Working capital forensics on [TICKER] for 12 quarters. (1) DSO, DIO, DPO, cash conversion cycle; (2) FCF/NI vs 5-year average with divergence flags; (3) plausible explanations for divergences; (4) MD&A and footnote cross-check; (5) earnings quality verdict.

## MOD-10 · Scenario Construction as a Discipline
Tags: `#modeling #thesis #cross-sector #senior-judgment #pm-level`
**When to use.** When building scenarios for a decision (valuation, hedge construction, position sizing) and avoiding linear interpolation and missed-scenario bias.
**Inputs.** Decision to be made; current consensus and market-implied positioning; relevant operational, competitive, regulatory and macro context.

PROMPT:
> Teach me to construct scenarios for [TICKER / decision] as a discipline, not just an output. (1) Decision frame — state the decision the scenarios must serve (set a price target; size a position; construct a hedge; assess portfolio fit). The number of scenarios should match the decision: two for binary (hedge or no hedge), three or four for sizing, more only if decision resolution requires it. (2) Mechanism-distinct generation — for each scenario, state the single dominant causal mechanism in one sentence. Two scenarios with the same mechanism operating at different magnitudes are not two scenarios; they are one scenario with a sensitivity band. (3) Missing-scenario audit — before accepting the scenario set, explicitly ask: what scenario would a smart short describe that I have not included? What scenario would a long-duration holder describe? What scenario does the options market appear to be pricing that I have not articulated? Any scenario identified here and absent from my set is evidence of a blind spot. (4) Probability discipline — assign probabilities that sum to 1.00 with a residual 'unknown unknown' bucket of at least 5 per cent. If the residual is zero, the scenario set is overconfident. Use round numbers (e.g. 40 / 30 / 20 / 10) rather than false-precision decimals. (5) Early-signal identification — for each scenario, the single operational or market signal that, if observed, would cause me to shift probability mass toward it. This is what makes scenarios actionable rather than academic. (6) Decision rule — state in advance how the probability-weighted output maps to the decision, so the decision is made by the analysis rather than re-made after the fact. (7) Premortem — if the scenario I am weighting least turns out to be correct, what failure in my generator allowed me to underweight it? End with the scenario set, probabilities, early signals, decision, and confidence score.

## SUB-PHA-01 · Pipeline Replenishment Audit
Tags: `#pharma #thesis #sec-filings #ir-materials #senior-judgment`
**When to use.** Annual pharma pipeline assessment.
**Inputs.** Pipeline, BD history, balance sheet, sell-side LOE notes.

PROMPT:
> Audit [TICKER]'s replenishment over 7 years. (1) LOE revenue at risk; (2) Phase 3/filed PoS-adjusted pipeline; (3) BD gap; (4) capital capacity; (5) M&A track record; (6) self-funder vs transformative deal verdict.

## SUB-PHA-04 · Gross-to-Net (GTN) Margin Erosion Analysis
Tags: `#pharma #modeling #senior-judgment`
**When to use.** When net revenue growth lags volume growth.
**Inputs.** Filings, IQVIA, IRA timelines, PBM commentary.

PROMPT:
> GTN analysis for [TICKER]. (1) Implied net price per unit over 8 quarters; (2) GTN discount trajectory; (3) driver decomposition; (4) peer comparison; (5) forward net revenue CAGR; (6) model adjustment.

## SUB-PHA-05 · Biosimilar Erosion Curve Modeller
Tags: `#pharma #modeling #senior-judgment`
**When to use.** When a biologic faces biosimilar entry.
**Inputs.** Patent data, biosimilar tracker, historical curves, defensive commentary.

PROMPT:
> Biosimilar erosion for [TICKER]'s [franchise]. (1) Entry timing; (2) biologic-specific decay (50–70% retained for 3–5 years vs 80–90% SM loss); (3) contracting/rebating dynamics; (4) geographic phasing; (5) year-by-year revenue bridge; (6) sensitivity to uptake speed.

## SUB-MED-05 · Average Selling Price (ASP) Deflation Analysis
Tags: `#medtech #modeling #senior-judgment`
**When to use.** When the thesis depends on pricing stability.
**Inputs.** Filings, hospital purchasing data, GPO data, peer pricing.

PROMPT:
> ASP analysis for [TICKER]. (1) Historical ASP trend from revenue/units; (2) GPO/IDN contract dynamics; (3) competitive pricing pressure; (4) technology cycle premium vs commoditisation; (5) COGS offset; (6) forward model at current deflation rate.

## SUB-SVC-03 · Vertical Integration MLR Shifting
Tags: `#services-payors #modeling #senior-judgment`
**When to use.** For vertically integrated insurers (UNH, CVS, ELV, CI).
**Inputs.** Segment disclosures, elimination notes, peer MLR, regulatory commentary.

PROMPT:
> Analyse [TICKER]'s vertical integration profit shifting. (1) Segment map and intercompany flows; (2) transfer pricing vs third-party benchmarks; (3) MLR with vs without market-rate repricing; (4) regulatory risk; (5) disclosure transparency; (6) margin sustainability.

## SUB-SVC-04 · Value-Based Care Capitation Tracking
Tags: `#services-payors #modeling #senior-judgment`
**When to use.** When evaluating provider groups transitioning to risk-bearing contracts.
**Inputs.** Segment disclosures, VBC contract details, quality metrics.

PROMPT:
> Risk-bearing exposure for [TICKER]. (1) Revenue mix: capitated/full-risk/shared-savings vs fee-for-service over 8 quarters; (2) risk corridor and stop-loss; (3) medical cost ratio on risk contracts; (4) patient attribution stability; (5) quality incentive attainment; (6) VBC revenue growth vs FFS trajectory; (7) margin implication at current transition pace.

## SUB-TLS-02 · NGS Instrument vs Consumables Mix Forecast
Tags: `#tools-dx #modeling #senior-judgment`
**When to use.** For NGS names where instrument cycle and consumables flywheel diverge.
**Inputs.** Installed base data, transcripts, peer commentary.

PROMPT:
> NGS forecast for [TICKER], 8 quarters. (1) Installed base by platform; (2) utilisation trend; (3) end-market mix; (4) gross margin trajectory; (5) competitive impact; (6) cross-check vs management targets.

## SUB-TLS-04 · IVD Reagent Pull-Through Rate Calculator
Tags: `#tools-dx #modeling #senior-judgment`
**When to use.** For IVD instrument/consumables names where menu breadth utilisation is the margin driver.
**Inputs.** Company disclosures, assay menu data, peer benchmarks.

PROMPT:
> Reagent pull-through for [TICKER]. (1) Installed IVD instruments by platform; (2) assay menu breadth (number of approved tests per platform); (3) reagent revenue per instrument per year; (4) menu utilisation rate (tests actually run vs tests available); (5) menu expansion pipeline; (6) competitive pull-through benchmarks; (7) gross margin sensitivity to utilisation changes.
