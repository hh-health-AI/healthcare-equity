---
name: investable-view
description: Use to build a falsifiable healthcare investment view from clinical,
  regulatory, commercial, competitive and financial evidence; assemble an underwriting
  thesis with explicit model implications, scenarios and market-implied expectations.
---

# Investable View

## Workflow

1. **Frame the economic unit.** Resolve the company and one to three material revenue units from filings. State subsector, valuation date, currency, units, dominant revenue/cash-flow formula and the variable most likely to separate scenarios.
2. **Assemble five evidence layers.** Gather clinical, regulatory, commercial, competitive and financial briefs. Reuse dated evidence already available; retrieve missing material evidence through actual tools. The twelve evidence modules provide specialized inputs. Declare skipped, immaterial, thin or unavailable layers. Do not count a sponsor release, registry entry and paper from the same trial as three independent successes.
3. **Test the evidence boundary.** For each material finding, verify the primary source and whether it supports the precise population, endpoint, geography, period or economic claim. Seek failed precedents and disconfirming data. Record limitations instead of concealing them in a point estimate.
4. **Translate each finding.** Use CHANGE, NO_CHANGE, UNCERTAINTY_ONLY or NEEDS_DATA for every affected assumption. Record prior -> proposed value, or unavailable, reason, source/locator, evidence already reflected and next observable. Do not force a forecast change.
5. **Build mechanism-distinct scenarios.** Show bear, base and bull with early signals, swing assumptions and value per share where sufficient data exist. Preserve the source framework's explicit unknown-unknown residual of at least 5%; all mutually exclusive leaf probabilities, including that residual, must sum to 1.00. Explain the residual rather than hiding it in another case. These are analyst assumptions, not calibrated success forecasts. Use a scenario range or mark valuation incomplete when inputs are missing.
6. **Reverse-engineer the actual price.** Obtain a timestamped current price through an available tool or dated user input. Reconcile shares and enterprise-to-equity bridge. Solve for an interpretable implied variable such as approval probability, treated patient-years, utilization, medical-cost ratio, retention or margin, explaining the equation and other fixed assumptions. Consensus is a separate sourced input; do not invent it. Without price or necessary model inputs, deliver a conditional view and mark this step unavailable.
7. **Apply the five-leg test.** A differentiated thesis needs an explicit market-implied variable, evidence that challenges it, a difference surviving probability weighting, a catalyst that can resolve it and an observable falsifier. Report missing legs. A narrative without these is not a fully underwritten thesis.
8. **State the view.** Use: “At the observed price, the market appears to imply [X]. Evidence [E] gives [implication status] for [Y]: [prior] -> [proposed], because [reason]. This implies [valuation effect] under [case]. [Catalyst] may resolve the disagreement by [dated window]. [Observable] would falsify the view.” Only fill values supported by the analysis. Distinguish confirmed dates from estimates.

Deliver the conclusion, evidence/inference/model bridge, scenario matrix, market-implied analysis, strongest countercase, falsifiers and confidence, with the five layer briefs as an appendix. Hand off a watchlist or IC draft only when requested; no automatic monitoring or distribution.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
