---
name: initiate
description: >
  This skill should be used when the user says "initiate on [TICKER]", "scope this
  name", "build an initiation memo", "write an industry primer on [sub-segment]",
  "construct bull/base/bear scenarios for a new name", or is building coverage of a
  healthcare company from zero.
metadata:
  version: "0.1.0"
---

# Initiation of Coverage

Build a new name from zero — quick scoping through full institutional initiation. Prompts (verbatim, with inputs/outputs) in `${CLAUDE_PLUGIN_ROOT}/skills/initiate/references/prompts.md`.

## Route by stage

| Stage | Prompt | Output |
|---|---|---|
| Fast triage — "worth deeper work?" | INIT-01 (30-minute scoping memo) | One-page memo with keep-going verdict |
| Unfamiliar sub-segment | INIT-04 (industry primer) | 1,500–2,500-word primer |
| Committed — structure the work | INIT-02 (full memo skeleton) | Long-form skeleton with TBD checklist |
| Clinical-stage biotech | INIT-06 (science/clinical layer) | Pipeline, PoS, readouts, regulatory path |
| Device/capital-equipment name | INIT-07 (procedure/reimbursement/adoption layer) | Reimbursement, adoption curve, KPIs |
| Scenario set for the PT | INIT-05 (bull/base/bear decomposition) | Probability-weighted PT |
| A sell-side initiation just dropped | SS-02 (initiation note decoder) | One-page decode |

## Execution rules

1. Follow the standing instructions (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`): filings first, time-stamped numbers, facts/inference separation, confidence score.
2. **Delegate the data layers to the engines** rather than working from priors: INIT-06's pipeline/competition/readout sections → clinical-catalysts (pipeline-landscape, readout-handicap, catalyst-calendar); INIT-07's reimbursement section → cms-reimbursement (coverage-check, reimbursement-impact) and its adoption section → provider-adoption + procedure-exposure; epidemiology/TAM inputs → procedure-exposure epi-funnel-input. Collect their EVIDENCE BRIEF blocks and cite them in the memo.
3. For INIT-04 primers, ground unit-economics claims in the model-valuation references (valuation map by industry) and, when attached to the project, `project_search` the KB books for domain depth.
4. Scenario work (INIT-05) obeys MOD-10 discipline: mechanism-distinct scenarios, probabilities sum to 1.00 with ≥5% unknown-unknown residual, early signal per scenario.
5. Chain: INIT-01 → (INIT-04 if unfamiliar) → INIT-02 → INIT-06/07 → model-valuation (sub-sector model) → thesis (INIT-03 variant perception) → INIT-05 → esg-stewardship (materiality) → comms-compliance (COMM-01 IC memo). Offer the evidence-assembler agent to run the engine legwork in one pass.
