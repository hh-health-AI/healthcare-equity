---
name: biotech-rnpv-modeler
description: Use to construct or audit biotech risk-adjusted NPV, development-cost
  timing, commercial cash flows, outcome scenarios and equity-value bridges. Require
  explicit probability and unit assumptions; avoid double weighting and do not present
  scenarios as validated forecasts or personal trading instructions.
---

# Biotech rNPV Modeler

## Workflow

1. Specify asset, indication, geography, valuation date, currency, cash-flow units and the economic ownership being valued. Separate assets and partnered economics. Use bear, base and bull for decision-facing work, stating which assumptions distinguish them.
2. Separate sourced observations from commercial, cost, launch, exclusivity, tax, probability and discount-rate assumptions. Trace clinical evidence to a specific changed, unchanged, uncertain or missing input. Do not invent a prior model when none was supplied.
3. Build signed, end-of-year cash-flow rows. Assign each row its **unconditional probability of being incurred or received**. Current committed costs normally have probability one; later development costs depend on reaching the stage, not on ultimate approval. Distinguish conditional stage success probabilities from their cumulative product.
4. Use unlevered after-tax cash flows for asset/enterprise valuation. Explicitly address royalties, partner shares, capex, working capital, taxes, maintenance/development costs and post-exclusivity erosion. Include terminal or residual cash flow only as an explicit, justified input; do not hide it inside a growth assumption.
5. Calculate each row as `PV = signed_cash_flow * unconditional_probability / (1 + discount_rate) ** years_from_valuation`. State timing convention. Sum rows for asset value. Add cash and nonoperating assets, subtract debt and separately valued unallocated overhead **once**, and reconcile to equity. Divide by matching-unit diluted shares. Show financing/dilution scenarios when cash runway matters.
6. Keep mutually exclusive scenario probabilities separate from within-scenario row probabilities. Explain what uncertainty each layer represents so the same approval risk is not discounted twice. Do not multiply a probability-weighted rNPV output by PoS again.
7. Use an actual calculation tool and independently recompute at least one cost row, one revenue row and the equity bridge. Show formulas and input lineage. The upstream hh-research calculator is optional external software, not a tool installed by this plugin.
8. Stress probability, launch delay, peak sales, market penetration, margins, exclusivity, financing and discount rate with explicit inputs. Where an input is absent, supply a clearly labeled illustrative scenario or mark valuation incomplete rather than presenting a fabricated fair value.

## Output

Scope and units; sourced inputs versus assumptions; scenario assumptions; cash-flow audit; asset-to-equity bridge; sensitivities; dominant drivers; disconfirming evidence; financing risks; confidence. Use the host's spreadsheet capability for a requested workbook and verify actual formulas and output. Calculated precision does not validate clinical or commercial assumptions.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
