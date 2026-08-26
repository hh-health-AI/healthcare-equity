---
name: sell-discipline
description: >
  This skill should be used when the user says "run the quarterly scorecards", "sell
  discipline check on [TICKER]", "refresh the thesis-breaking watchlist", "sanity-check
  my sizing", "post-mortem this exit", "annual book review", or any exit-discipline
  and process-audit task.
metadata:
  version: "0.1.0"
---

# Sell Discipline & Risk Monitoring

Knowing when to exit, when to add, and what would break the thesis — plus the learning loop. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/sell-discipline/references/prompts.md`.

## Route by cadence

| Cadence | Prompt |
|---|---|
| Quarterly, every name | SELL-01 scorecard (0–3 × six dimensions; 14–18 hold/add, 9–13 trim, <9 exit-by-default) |
| At position establishment, then refreshed | SELL-02 thesis-breaking signal watchlist |
| Before adding / doubling down | SELL-03 position sizing sanity check |
| Within two weeks of a material exit | SELL-04 single-name post-mortem |
| Annually (January) | SELL-05 book-wide post-mortem & process audit |

## Execution rules

1. **Pre-commitment is the mechanism:** watchlist signals carry thresholds, sources, frequencies, and pre-committed actions *before* drift sets in; scorecards use the fixed bands, and overriding them gets documented as an override (SELL-05 measures process discipline directly — how often the full workflow ran vs was skipped).
2. Wire the watchlist (SELL-02) to the suite's monitoring surfaces: regulatory decisions → cms-reimbursement rule-watcher and clinical-catalysts readout-watcher; competitive events → pipeline-landscape refreshes; fundamental KPI thresholds → the earnings skill's KPI tracker; market-structure signals → portfolio (TECH-05 EDGAR monitoring). Each signal names its watcher.
3. Post-mortems (SELL-04) follow the five-way error classification — wrong in substance / right but market cared about other things ("intact but irrelevant" is the key diagnostic) / right but timing / sizing mispriced vs conviction / process error — and must land on an *operational* transferable rule ("when MLR exceeds X, re-underwrite"), which is then encoded back into the SELL-02 template. That's the learning loop; don't skip the encoding step.
4. SELL-05 annually clusters the year's post-mortems for error patterns, recalibrates base rates actually used (phase-transition, biosimilar curves, MA bid outcomes — update clinical-catalysts' base-rates reference when they shift), audits sizing vs conviction, and commits written framework updates for the year ahead.
5. Chain: SELL-01 → SELL-02 refresh → thesis pre-mortem/steel-man (thesis skill) → portfolio sleeve review → annual chain (SELL-04s → SELL-05 → COMM-02 letter section via comms-compliance).
