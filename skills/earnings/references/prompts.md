# Prompts — Earnings Workflows

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## EARN-01 · Earnings Preview Note (T-7)
Tags: `#earnings-preview #cross-sector #sell-side #transcripts #senior-judgment`
**When to use.** Seven days ahead of a print.
**Inputs.** Prior four transcripts, consensus, my model, sell-side notes, options data.
**Output.** Preview note, 1,000–1,500 words, with pre-commit action plan.

PROMPT:
> Build an earnings preview for [TICKER] for [Q quarter year]. Structure: (1) consensus snapshot — top-line, segments, margins, EPS, key KPIs; (2) my model vs consensus with deltas and drivers; (3) buy-side whisper from sell-side tone; (4) three questions the print must answer for thesis; (5) anticipated management tone based on prior four prints; (6) trade setup — historical reaction, IV vs realised, asymmetry; (7) action plan — add / trim / exit triggers.

## EARN-02 · Buy-Side KPI Tracker Build
Tags: `#earnings-preview #cross-sector #sec-filings #transcripts #junior-task`
**When to use.** When systematising operational metrics beyond headline P&L.
**Inputs.** Eight quarters of releases and transcripts; investor day decks.
**Output.** KPI table with 12-quarter rolling view and narrative on KPI selection.

PROMPT:
> Build a KPI tracker for [TICKER] covering last 8 quarters and forecasting next 4. Identify 8–12 operational KPIs that drive the thesis. For each: define precisely, source from disclosure, show trend, note disclosure changes, forecast with reasoning. Flag KPIs the company has stopped disclosing.

## EARN-03 · Live-Call Triage Sheet
Tags: `#earnings-post #cross-sector #transcripts #senior-judgment`
**When to use.** On the call itself, to structure live note-taking.
**Inputs.** My preview note; prior transcripts.
**Output.** One-page triage sheet.

PROMPT:
> Generate a live-call triage sheet for [TICKER]'s [Q] call. Four columns: thesis question (top 5), management answer (blank), tone read, thesis impact. Add 'red flag word list' (8–10 phrases). Q&A section: 3–4 sell-side analysts likely to ask well, what they'll ask, surprising answer.

## EARN-04 · Post-Print Thesis Update Memo
Tags: `#earnings-post #cross-sector #transcripts #sec-filings #senior-judgment`
**When to use.** Within 24 hours of a print.
**Inputs.** Release, transcript, preview note, KPI tracker, model.
**Output.** 1,500-word memo with clear action.

PROMPT:
> Post-print thesis update for [TICKER] following [Q]. (1) Result vs my expectation vs consensus; (2) earnings quality assessment; (3) management tone delta; (4) thesis verdict per pillar (confirmed/intact/weakened/broken); (5) model changes with new PT bridge; (6) action with justification; (7) lessons learned.

## EARN-05 · Guide Decomposition and Path-to-Number Test
Tags: `#earnings-post #modeling #cross-sector #transcripts #senior-judgment`
**When to use.** When management has issued or revised guidance.
**Inputs.** Guidance release, slides, transcript, prior guide history.
**Output.** Bridge tables with verdict and model recommendation.

PROMPT:
> Decompose [TICKER]'s [FY] guidance. (1) Top-line bridge by segment; (2) margin bridge; (3) capex and FCF; (4) historical guide-in vs deliver; (5) verdict — conservative/achievable/stretch; (6) model positioning.

## EARN-06 · Biotech Quarterly Cash and Catalyst Refresh
Tags: `#earnings-post #biotech #sec-filings #ctgov #senior-judgment`
**When to use.** Each quarter for clinical-stage names.
**Inputs.** Press release, 10-Q, MD&A, transcript, prior catalyst calendar.
**Output.** Cash bridge, catalyst table, financing scenarios.

PROMPT:
> Refresh cash and catalyst for [TICKER] following [Q]. (1) Cash position with runway to named catalyst. Distinguish gross burn (total operating cash spent) from net burn (after collaborative revenue). (2) Burn quality — R&D by programme, G&A, non-cash. (3) Catalyst calendar — next 18 months, flag slippage. (4) Financing risk — equity raise, royalty, partnership scenarios. (5) Pipeline prioritisation signal.

## EARN-07 · Managed Care MLR Bridge
Tags: `#earnings-post #services-payors #sec-filings #cms #senior-judgment`
**When to use.** Each quarter for payors where MLR is the central driver.
**Inputs.** Release, supplement, transcript, prior-year prints.
**Output.** MLR bridge, drivers, forward-look, peer cross-read.

PROMPT:
> MLR bridge for [TICKER] for [Q]. (1) MLR by segment vs prior year/consensus; (2) drivers — utilisation, unit cost, mix, prior period, one-offs; (3) risk adjustment dynamics (RADV, V28, Stars); (4) forward colour; (5) full-year guide implication; (6) peer cross-read.

## SS-03 · Conference Call Cross-Read
Tags: `#sell-side-synth #earnings-post #cross-sector #transcripts #senior-judgment`
**When to use.** After a peer's earnings call, to extract signal for your names.
**Inputs.** Peer transcript; my ticker's thesis.
**Output.** Cross-read note, 400–600 words.

PROMPT:
> [Peer] just reported. I cover [my ticker]. (1) Direct read-across; (2) indirect signals; (3) their view on my name; (4) one quote for my next update; (5) action recommendation.

## COMM-03 · Quick-Reaction Internal Note
Tags: `#client-comms #earnings-post #cross-sector #senior-judgment`
**When to use.** Within 60 minutes of a print or event.
**Inputs.** Press release, headlines, transcript if available.
**Output.** 200-word internal note.

PROMPT:
> Quick-reaction on [TICKER]'s [event]. (1) One-line headline; (2) three things that matter; (3) thesis verdict; (4) action; (5) one open question. Under 200 words.

## SUB-PHA-03 · TRx vs NRx Divergence Monitor
Tags: `#pharma #earnings-post #senior-judgment`
**When to use.** When assessing true commercial momentum.
**Inputs.** IQVIA, Bloomberg BI, company disclosures.
**Output.** Volume monitor with divergence flags.

PROMPT:
> Scan prescription data for [TICKER]'s key franchises. (1) TRx and NRx with trends; (2) divergence flags; (3) market share; (4) revenue run-rate implication; (5) model revision flags.

## SUB-SVC-01 · Hospital Operator Earnings Cross-Read
Tags: `#services-payors #medtech #earnings-post #transcripts #senior-judgment`
**When to use.** After hospital operator earnings.
**Inputs.** Hospital operator transcripts; coverage list.
**Output.** Cross-read, 800–1,000 words.

PROMPT:
> Cross-read [HCA/THC/UHS] for [Q]. (1) Procedure volumes by category; (2) acuity mix; (3) capex; (4) labour cost; (5) payor mix; (6) drug expense/340B; (7) synthesis — top 3 medtech, 2 pharma, 1 payor implication.
