# Prompts — Screening & Thematic Research

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## SCR-01 · Bloomberg / FactSet Healthcare Idea Screen Builder
Tags: `#screen #cross-sector #bloomberg #factset #senior-judgment`
**When to use.** When designing a screen with analytically grounded filters.
**Inputs.** Thesis or theme; syntax preferences.
**Output.** Screen design with triage process.

PROMPT:
> Design a Bloomberg EQS or FactSet screen for [thesis]. (1) Universe; (2) 4–7 filter criteria with thresholds and reasoning; (3) field codes; (4) expected hit count and triage; (5) the one filter to loosen for long-tail ideas; (6) post-screen workflow.

## SCR-03 · Hidden Compounder Screen
Tags: `#screen #cross-sector #bloomberg #senior-judgment #pm-level`
**When to use.** When generic quality screens are too crowded.
**Inputs.** Universe; screening subscription.
**Output.** Ranked candidate list.

PROMPT:
> Design screen for 'hidden compounders'. (1) 5-year organic CC growth >8%; (2) stable/expanding gross margin; (3) ROIC > WACC 4 of 5 years; (4) GPA > 0.20 to filter speculative pre-revenue; (5) exclude >40% M&A-driven growth; (6) capex/sales >4%; (7) insider >5%; (8) sell-side <10 analysts. Surface 8–12 names with one-line rationale.

## SCR-04 · Thematic Beneficiary Screen
Tags: `#screen #thematic #cross-sector #senior-judgment`
**When to use.** When mapping a theme to listed-equity beneficiaries.
**Inputs.** Theme; transcripts; sector knowledge.
**Output.** Supply chain map, ranked basket, substantiation.

PROMPT:
> Theme: [X]. Map supply chain. Per node: (1) value chain role; (2) listed exposure; (3) mechanism (volume, price, mix, share, optionality); (4) cost-bearer flag; (5) earnings call substantiation. Rank by pass-through quality. Candidate basket of 8–12 names.

## SCR-05 · Activist Investor Target Screen
Tags: `#screen #cross-sector #sec-filings #senior-judgment`
**When to use.** When screening for potential activist targets in healthcare.
**Inputs.** Screening data; 13D filings; proxy statements.
**Output.** Ranked list with playbook and uplift per name.

PROMPT:
> Screen for activist targets. Criteria: (1) market cap >$1B; (2) operating margin declining 3 years; (3) cash/investments >30% of EV; (4) R&D productivity below peer median; (5) exec comp disconnected from TSR; (6) board tenure >10 years or <3 independent with sector expertise; (7) recent 13D filings. Per hit: likely playbook and uplift estimate.

## THM-01 · Theme Validation Framework
Tags: `#thematic #cross-sector #senior-judgment #pm-level`
**When to use.** Before investing 3 weeks in a thematic deep-dive.
**Inputs.** Theme; universe; recent literature.
**Output.** Validation memo, 800–1,200 words, with verdict.

PROMPT:
> Theme: [paste]. (1) Is it real — empirical evidence? (2) Is it durable — 3 sustaining forces? (3) Differentiated from consensus? (4) Investable — listed pure-plays? (5) Time horizon vs fund? (6) Verdict: full work / basket / pass.

## THM-02 · TAM Bottoms-Up Build
Tags: `#thematic #cross-sector #senior-judgment`
**When to use.** When a theme depends on a TAM claim.
**Inputs.** TAM claim; epidemiology/market data.
**Output.** TAM table, gap analysis, basket implication.

PROMPT:
> TAM claim: [$XB by YYYY]. (1) Bottoms-up population→use case→addressable→price→penetration; (2) compare to claim; (3) gap driver; (4) historical analogues; (5) verdict; (6) basket implication.

## THM-03 · Thematic Basket Construction
Tags: `#thematic #portfolio #cross-sector #pm-level`
**When to use.** When theme is validated and you need an investable expression.
**Inputs.** Validated theme; candidate names; portfolio constraints.
**Output.** Basket proposal with weights, factor map, rebalance and kill rules.

PROMPT:
> 6–10 name basket for theme [X]. (1) Purity map; (2) quality map; (3) weights with 1–2 pair shorts; (4) factor exposure; (5) rebalance trigger; (6) kill switch.

## SUB-PHA-02 · GLP-1 Class Dynamics Map
Tags: `#pharma #thematic #senior-judgment`
**When to use.** For any name with GLP-1 exposure.
**Inputs.** NN/LLY commentary, payor data, KOL views.
**Output.** GLP-1 memo, 2,000 words, with adjacent-name map.

PROMPT:
> GLP-1 dynamics for 36 months. (1) On-market players; (2) late-stage challengers; (3) indication expansion; (4) pricing trajectory; (5) compounded grey market; (6) adjacent-name impact; (7) regime shift signals.

## SUB-TLS-01 · Bioprocessing Cycle Tracker
Tags: `#tools-dx #thematic #senior-judgment`
**When to use.** Quarterly bioprocessing demand assessment.
**Inputs.** Bioprocessing transcripts, biotech funding, China policy.
**Output.** Cycle tracker with positioning calls.

PROMPT:
> Track bioprocessing cycle for [companies]. (1) Backlog and book-to-bill; (2) customer commentary; (3) inventory normalisation credibility; (4) gene/cell therapy optionality; (5) China dynamics; (6) cycle stage; (7) cohort positioning.

## TECH-03 · FactSet Universal Screening for Healthcare
Tags: `#data-extraction #cross-sector #factset #fql #senior-judgment`
**When to use.** When building a quant screen in FactSet with healthcare-specific criteria.
**Inputs.** Screen criteria; output format preference.
**Output.** FactSet screening formula and API payload.

PROMPT:
> Build a FactSet Universal Screening formula for [screen description]. (1) Assign correct data library prefixes — FF_ for FactSet Fundamentals, FG_ for Global Constituents. (2) Apply relative date parameters: (0) for most recent, (-1) for prior year. (3) Map to the correct API endpoint if programmatic extraction is needed — /metrics for income statement items, OFDB for non-portfolio databases. (4) For healthcare-specific criteria, include: therapeutic area classification, pipeline stage filters, patent expiry windows, and clinical trial event flags. (5) Output the screen as both a FactSet workstation formula and a JSON payload for the FactSet Fundamentals API. My screen: [describe criteria].

## TECH-04 · FactSet Document Search for Transcript Mining
Tags: `#data-extraction #cross-sector #factset #fql #senior-judgment`
**When to use.** When mining earnings transcripts for specific themes across the coverage universe.
**Inputs.** Topic; universe; quarter.
**Output.** Transcript mining results with source links and cross-read.

PROMPT:
> Command the FactSet Document Search (GenAI-powered) to extract specific commentary from healthcare earnings transcripts. (1) Construct the query to search for [topic — e.g. 'GLP-1 cost impact', 'supply chain bottlenecks', 'pricing pressure', 'biosimilar competition'] across the most recent quarter's transcripts for [universe]. (2) Filter by section (prepared remarks vs Q&A) if the topic is more likely to surface in one or the other. (3) Request source-linked results so each excerpt maps back to a specific transcript, speaker, and timestamp. (4) Summarise the results as: company, relevant quote, sentiment (positive/negative/neutral), and cross-read implication for my coverage.
