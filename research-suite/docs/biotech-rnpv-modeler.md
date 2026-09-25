# Biotech rNPV Modeler

Use to construct or audit biotech risk-adjusted NPV, trial-outcome scenarios, development costs, commercial cash flows and equity-value bridges. Require explicit assumptions and probability timing; never present model inputs as calibrated forecasts or personalized trading instructions.

## Try it

- Build bear/base/bull rNPV scenarios with an auditable cash-flow bridge.
- Audit this model for double-counting probability or corporate overhead.
- How does delayed launch change value under these assumptions?

## Run the reproducible utility

```bash
hh-research rnpv examples/valuation.json --out outputs/biotech-rnpv-modeler.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Define asset, indication, geography, valuation date, currency and cash-flow units. Build bear, base and bull cases for decision-facing analysis.
2. Separate sourced observations from commercial, cost, timing and probability assumptions. Map each clinical scenario to an explicit model change.
3. Build signed end-of-year cash flows. Assign each row its unconditional probability of being incurred or received. Current committed costs usually have probability one; later costs depend on reaching the stage, not ultimate commercial success.
4. Use unlevered after-tax cash flows for enterprise/asset valuation. Document tax, working capital, capex, royalties, partnering and exclusivity assumptions. Set any terminal/residual cash flow explicitly.
5. Add cash, subtract debt and unallocated overhead only once. Use diluted shares in matching units and include financing scenarios where material.
6. Run `hh-research rnpv valuation.json --out valuation.md --json-out valuation-results.json`. Read the cash-flow audit and recompute a representative row.
7. Stress probability, launch timing, peak sales, margins and discount rate through explicit alternative input scenarios. Do not multiply the output by PoS a second time.
8. Deliver scenario values, drivers, sourced inputs, assumption uncertainty, disconfirming evidence and financing risks. No default investment recommendation.

## Existing platform handoff

[Healthcare Equity Research Platform](../../README.md)

[Skill instructions](../skills/biotech-rnpv-modeler/SKILL.md) · [Agent workflow](../agents/biotech-rnpv-modeler.md) · [Input contracts](input-contracts.md)
