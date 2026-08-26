# Prompts — Initiation of Coverage

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## INIT-01 · 30-Minute Name Scoping Memo
Tags: `#initiation #cross-sector #sec-filings #bloomberg #junior-task`
**When to use.** When a name is flagged for potential coverage and you need a fast read on whether it is worth deeper work.
**Reasoning.** scope → inventory → hypothesise → prioritise
**Inputs.** Most recent 10-K, latest 10-Q, latest investor presentation; optionally a sell-side initiation note for context.
**Output.** One-page memo, ~500 words, prose with light structure.

PROMPT:
> You are a senior buy-side healthcare analyst doing initial triage. I will provide a company's most recent 10-K, 10-Q, and latest investor presentation. Produce a one-page scoping memo with: (1) business model in three sentences (what they sell, to whom, on what economics); (2) revenue mix by segment, geography, and customer concentration with the top three risks each implies; (3) sub-sector classification and the two closest listed peers, with a one-line statement on why this name is differentiated or commoditised vs them; (4) capital structure snapshot (net debt/EBITDA, cash runway if pre-profit, refinancing wall); (5) the three things I would need to believe for the bull case and the three for the bear case, ranked by how testable they are; (6) a 'do I keep going?' verdict with two sentences of reasoning. Be ruthless about omitting boilerplate.

## INIT-02 · Full Initiation Memo Skeleton
Tags: `#initiation #cross-sector #sec-filings #sell-side #senior-judgment`
**When to use.** When you have decided to initiate coverage and need a structured first draft to populate over 1–2 weeks.
**Reasoning.** structure → populate → benchmark → synthesise
**Inputs.** Ticker, sub-sector context, any sell-side initiation notes.
**Output.** Long-form structured memo skeleton with TBD checklist.

PROMPT:
> Build the skeleton of a full buy-side initiation memo for [TICKER]. Use the following structure: (i) Investment summary — thesis in 150 words, rating, 12-month price target with method, position size recommendation, expected IRR; (ii) Why this, why now — what the market is missing, why the inefficiency exists, why it persists, what closes it; (iii) Business deep dive — segments, unit economics, moat sources mapped to Hamilton Helmer's 7 Powers; (iv) Industry context — TAM with bottoms-up build, growth drivers, competitive structure, regulatory regime; (v) Management and capital allocation — track record on R&D ROI, M&A, buybacks, insider alignment; (vi) Financial model summary — 5-year P&L, FCF bridge, balance sheet, key KPIs; (vii) Valuation — primary method with cross-checks; (viii) Catalysts — next 6, 12, 24 months with probabilities; (ix) Risks — ranked, with monitoring metrics; (x) Engagement plan — questions for management, expert network priorities, KOL diligence list. Leave numbered placeholders [TBD-1, TBD-2…] for primary research.

## INIT-04 · Industry Primer in 90 Minutes
Tags: `#initiation #thematic #cross-sector #reasoning-only #junior-task`
**When to use.** When entering an unfamiliar sub-segment and you need a working model of the industry.
**Reasoning.** map industry → catalogue players → benchmark → identify levers
**Inputs.** Segment name; optionally a recent industry conference deck.
**Output.** Long-form primer, 1,500–2,500 words, written as prose.

PROMPT:
> Write a primer on the [sub-segment, e.g. CDMO, CGM, PBM, ADC bioconjugation, NGS instruments] industry as if briefing a new buy-side analyst with healthcare fluency but no segment-specific background. Cover: (1) what the industry does and where it sits in the value chain; (2) unit economics of a typical participant — gross margins, capital intensity, cash conversion, working capital quirks; (3) two or three structural growth drivers and what could break them; (4) competitive structure and how it has evolved; (5) regulatory and reimbursement regime and the most plausible policy shocks; (6) listed pure-plays, diversified players with material exposure, and key private competitors; (7) the three pieces of jargon that signal someone actually understands the space.

## INIT-05 · Bull / Base / Bear Decomposition with Probability Weights
Tags: `#initiation #modeling #thesis #cross-sector #senior-judgment`
**When to use.** When constructing the formal scenario set for a price target, avoiding mechanical interpolation.
**Reasoning.** frame scenarios → quantify paths → weight probabilities → decide
**Inputs.** Current operating model, base assumptions, consensus PT range.
**Output.** Structured scenario matrix with probability-weighted PT and sensitivity note.

PROMPT:
> For [TICKER], construct three scenarios — bull, base, bear — that are qualitatively distinct rather than linear interpolations. Each must be driven by a different dominant causal mechanism. For each: (1) dominant mechanism in one sentence; (2) three to five operational assumptions; (3) 5-year P&L sketch; (4) appropriate valuation method and equity value per share; (5) subjective probability with reasoning, ensuring the residual 'unknown unknown' bucket is not zero; (6) leading indicator that would shift probability weighting. End with a probability-weighted PT and a flag if the modal scenario differs materially from the weighted average.

## INIT-06 · Biotech-Specific Initiation Layer
Tags: `#initiation #biotech #ctgov #fda-ema #pubmed #senior-judgment`
**When to use.** When initiating on a clinical-stage biotech and the standard template needs the science layer.
**Reasoning.** map pipeline → risk-weight assets → bridge to valuation → recommend
**Inputs.** Pipeline page, investor deck, ClinicalTrials.gov entries, recent abstracts.
**Output.** Structured clinical layer, 1,500–2,500 words.
**Suite note.** Source sections (3)–(6) from the clinical-catalysts plugin (pipeline-landscape, readout-handicap, catalyst-calendar, device-diligence).

PROMPT:
> I am initiating on [TICKER], a clinical-stage biotech with a lead asset in [indication, mechanism]. Build the science and clinical layer: (1) mechanism of action at generalist PM level; (2) standard of care, unmet need quantified, realistic addressable population; (3) competitive landscape — every asset in development ranked by stage and probability; (4) lead asset's clinical package — trial design, endpoints, readouts, statistical robustness, criticisms a short would raise; (5) next two readouts with timing and quantitative success thresholds (note: ~70% of Phase II and ~50% of Phase III trials fail to meet primary endpoints — use indication-specific rates where available); (6) regulatory pathway — Breakthrough, Fast Track, Priority Review, AdCom likelihood, PDUFA; (7) probability of success using transparent decomposition (technical PoS × regulatory PoS × commercial PoS).

## INIT-07 · Medtech-Specific Initiation Layer
Tags: `#initiation #medtech #cms #ir-materials #senior-judgment`
**When to use.** When initiating on a medical device or capital equipment company.
**Reasoning.** decompose device → reimbursement-test → unit-economics → conclude
**Inputs.** Company filings, IR deck, reimbursement schedule, peer notes.
**Output.** Structured layer, 1,200–2,000 words.
**Suite note.** Source section (2) from cms-reimbursement, (4) from provider-adoption + procedure-exposure.

PROMPT:
> Build the procedure, reimbursement, and adoption layer for [TICKER] with primary exposure to [device category]. Cover: (1) procedure or use case — patient pathway, decision-maker, site of service, competing options; (2) US reimbursement — CPT codes, ICD-10, CMS payment rates (OPPS, ASC, physician fee schedule), prior auth, pending NCD/LCD changes; (3) ex-US reimbursement; (4) adoption curve — penetration, pace by site, bottleneck; (5) capital equipment dynamics if relevant — placement model, installed base, utilisation, consumables pull-through; (6) competitive set ranked by share and evidence; (7) three operational KPIs the company will be judged on quarterly.

## SS-02 · Initiation Note Decoder
Tags: `#sell-side-synth #initiation #cross-sector #sell-side #junior-task`
**When to use.** When a sell-side initiation drops and you want the analytical core without 80 pages.
**Reasoning.** triangulate broker vs filings → identify gaps → build variant → falsify
**Inputs.** Sell-side initiation PDF.
**Output.** One-page decoded summary.

PROMPT:
> Distil initiation note on [TICKER]. (1) Central thesis in two sentences; (2) PT method and weakest assumption; (3) three differentiated insights; (4) three weakest claims; (5) unique data sources; (6) analyst rigour read; (7) what I'd push back on in 10 minutes.
