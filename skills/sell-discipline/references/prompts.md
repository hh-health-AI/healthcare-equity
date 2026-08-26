# Prompts — Sell Discipline & Risk Monitoring

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## SELL-01 · Sell Discipline Scorecard
Tags: `#sell-discipline #risk #cross-sector #pm-level`
**When to use.** Quarterly review of every name against a consistent exit framework.
**Inputs.** Thesis, recent prints, peer comparison, entry memo.
**Output.** Six-line scorecard with verdict.

PROMPT:
> Scorecard for [TICKER]. Score 0–3: (1) thesis intact; (2) execution; (3) competitive trend; (4) valuation vs entry; (5) better alternatives; (6) conviction calibration — am I in love with the story? Sum: 14–18 hold/add, 9–13 trim, <9 exit-by-default.

## SELL-02 · Thesis-Breaking Signal Watchlist
Tags: `#sell-discipline #risk #cross-sector #senior-judgment`
**When to use.** After establishing a position, to lock in disconfirming signals before drift.
**Inputs.** Thesis, KPIs, competitive set, regulatory calendar.
**Output.** Categorised watchlist with pre-committed actions.

PROMPT:
> Watchlist for [TICKER]. 8–10 signals by category: (1) fundamental KPI thresholds; (2) competitive events; (3) regulatory decisions; (4) management behavioural signals; (5) market structure. For each: threshold, source, frequency, pre-committed action.

## SELL-03 · Position Sizing Sanity Check
Tags: `#portfolio #risk #cross-sector #pm-level`
**When to use.** Before adding or doubling down.
**Inputs.** Sizing, portfolio context, scenarios, factor exposures.
**Output.** Sizing recommendation with reasoning.

PROMPT:
> Test sizing for [TICKER]. (1) Expected 12-month return and implied Sharpe; (2) marginal correlation to top 5; (3) drawdown at bear case; (4) information vs mood driver; (5) 90-day justification forward. Clear recommendation.

## SELL-04 · Single-Name Thesis Post-Mortem
Tags: `#sell-discipline #post-mortem #cross-sector #senior-judgment #pm-level`
**When to use.** After exiting a position at a loss, holding a winner past the thesis horizon, or any outcome that materially differed from the original thesis. Run within two weeks of exit while details are fresh.
**Inputs.** Original initiation or entry memo; complete holding-period timeline including earnings prints and catalysts; exit rationale if documented; original KPI tracker; sell discipline scorecard updates during the holding period.
**Output.** Structured post-mortem with error classification, transferable lesson, and sell discipline framework update.

PROMPT:
> Conduct a thesis post-mortem on [TICKER], exited on [date] at [price] after [entry price, holding period]. The goal is not to assign blame but to extract transferable lessons. (1) Original thesis reconstruction — pull the initiation memo or entry rationale verbatim. Do not rewrite with hindsight. State the thesis pillars, the variant perception, the catalysts relied upon, the risks I acknowledged, and the position size and rationale. (2) What actually happened — a factual timeline of operational events (earnings prints, catalysts, management changes, competitive developments) and share-price reaction during the holding period. Separate price action from fundamentals. (3) Pillar-by-pillar verdict — for each original thesis pillar, mark as confirmed, intact but irrelevant (true but did not drive the stock), weakened, broken, or untested. The 'intact but irrelevant' category is the most important diagnostic — it identifies the thesis claim that was correct in substance but wrong in thesis relevance. (4) Error classification — place the outcome into one of five categories: (a) thesis was wrong in substance (my analysis of the business was incorrect); (b) thesis was correct but the market cared about different things (variant perception was right but immaterial); (c) thesis was correct but timing was wrong (horizon mismatch); (d) sizing was wrong for the conviction level (risk-reward was mispriced relative to my own expressed view); (e) process error (I did not follow my own sell discipline signals). Each category implies a different lesson. (5) Signal forensics — identify the one operational or market signal that, if I had noticed it in real time, would have forced a different decision. Where was it disclosed? Was it in my KPI tracker? Did I see it and dismiss it? (6) Transferable lesson — state in one sentence the rule I will apply to similar situations in the future. The rule must be operational ('when MLR exceeds X, I will re-underwrite') rather than aspirational ('I will be more disciplined'). (7) Update the sell discipline scorecard template — if the lesson implies a new signal to monitor or a new threshold to respect, encode it into SELL-02 for the rest of the book. End with confidence score and an honest note on whether the lesson generalises or is specific to this situation.

## SELL-05 · Book-Wide Annual Post-Mortem and Process Audit
Tags: `#sell-discipline #post-mortem #portfolio #pm-level`
**When to use.** Annually, ideally in January after the calendar year closes, to audit the year's decisions across the entire book rather than name-by-name.
**Inputs.** Full year's initiation memos, post-print notes, sell discipline scorecards, single-name post-mortems, and portfolio performance attribution.
**Output.** Year-end audit report with error pattern analysis, base rate updates, process discipline scorecard, and committed framework updates for the year ahead.

PROMPT:
> Conduct an annual post-mortem on my healthcare sleeve for [year]. The scope is the full book of positions, not any single name. (1) Performance attribution by decision type — decompose total return into: conviction positions held through volatility (top 5 names), opportunistic trades (positions held less than 90 days), hedges, shorts, and cash drag. Identify which decision categories added or subtracted value. (2) Error pattern recognition — review the single-name post-mortems from SELL-04 conducted during the year and cluster them. Are the errors concentrated in a particular decision category (e.g. I am consistently late to exit clinical-stage biotech after failed readouts), a particular sub-sector (e.g. my tools and diagnostics work is weaker than my biotech work), a particular market regime (e.g. I underperformed during risk-off periods), or a particular process failure (e.g. I override my own sell discipline scorecard too often)? (3) Base rate calibration — did the base rates I assumed (Phase III success at approximately 50 per cent, biosimilar uptake curves, MA bid cycle outcomes) hold in the actual year? Where they did not, update the base rates I apply going forward. (4) Process discipline scorecard — how often did I complete the full earnings workflow (EARN-01 through EARN-04) on my positions versus skipping steps? How often did I run the full sell discipline scorecard at quarter-end versus deferring? Process discipline is an input to performance; measure it directly. (5) Sizing audit — were my largest positions my highest-conviction positions in retrospect, or did sizing drift toward positions I had grown comfortable with rather than positions where the risk-reward was best? (6) External-to-me lessons — what happened in the year that I did not anticipate and could not reasonably have anticipated, versus what I should have anticipated but did not? The honest distinction between these two matters for confidence calibration. (7) Framework updates — for v[N+1] of my own process, what specifically changes in my watchlist thresholds, my sizing rules, my base rates, or my KPI tracker? Commit to the changes in writing. End with confidence score.
