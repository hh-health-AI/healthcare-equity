---
name: thesis
description: >
  This skill should be used when the user says "pressure-test my thesis", "steel-man
  the short", "pre-mortem this long", "variant perception on [TICKER]", "decompose the
  thesis into testable claims", "regime map", "build my disconfirmation plan", "my PM
  disagrees with me", or "prep me for IC pushback".
metadata:
  version: "0.1.0"
---

# Thesis Development & Pressure-Testing

Sharpen, attack, and defend an investment thesis — the goal is to be right, not confirmed. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/thesis/references/prompts.md`.

## Route by need

| Need | Prompt |
|---|---|
| Where can I differ from consensus? | INIT-03 variant perception generator |
| Before sizing up a long | THES-01 pre-mortem |
| The bull case feels obvious | THES-02 steel-man the short |
| Thesis feels right but unfalsifiable | THES-03 decomposition into testable claims |
| Macro/policy regime dependence | THES-04 regime map stress test |
| Formalize the search for contrary evidence | THES-05 disconfirming-evidence plan |
| 3+ notes dropped; map consensus dispersion | SS-01 multi-broker triangulation |
| Disagreement with the PM | PORT-05 constructive disagreement |
| Contrarian view into a hostile IC | PORT-06 IC defence plan |
| "Is this AI health story investable?" | SUB-DIG-02 investability test |

## Execution rules

1. Adversarial stance is the point: refuse to average bull and bear or split differences (INIT-03's instruction); demand mechanism, not valuation alone (THES-02); classify bear arguments as structural vs theoretical-without-evidence.
2. Every thesis claim gets a falsifier — the variant-perception test from the framework applies: disagreement must be an explicit market-implied variable, evidence must move that variable, the difference must survive probability weighting, a catalyst must be able to resolve it, and an observable must be able to break it. A thesis failing any leg is a narrative, not a thesis.
3. Source the attack surface from the engines: the smart short's clinical critique → clinical-catalysts readout-handicap; reimbursement fragility → cms-reimbursement; adoption-vs-story gaps → provider-adoption + procedure-exposure. Cite their EVIDENCE BRIEFs on both sides of the argument.
4. Monitoring outputs (THES-01's signals, THES-05's calendar) feed the sell-discipline skill's watchlist (SELL-02) — hand them over explicitly, with thresholds and pre-committed actions.
5. People-dynamics prompts (PORT-05/06) follow their scripts: separate the disagreement's components, steel-man first, minimum viable argument, falsification offer, commit-and-review rule, and write the one-paragraph record.
6. Standing instructions govern: disconfirming evidence and the fastest way to break the thesis appear in every output; end with the confidence score.

## Designation and access-friction rules (v0.2)

- **De-hype designations:** Breakthrough/Fast Track/RMAT are *timeline* evidence, never efficacy evidence — BTD compresses development ~3.2 years with no measured efficacy edge and smaller, more often single-arm pivotals (clinical-catalysts `base-rates.md`). A thesis leaning on a designation as quality signal is a red flag in INIT-03/THES-03 decomposition; re-price off trial design.
- **REMS/ETASU as a TAM haircut:** restricted-distribution programs (certification, registries, monitoring) are quantifiable launch friction — apply an explicit accessible-population/uptake-pace haircut rather than a qualitative caveat, and route the access mechanics to cms-reimbursement coverage-check.
- **Safety class contagion:** one class member's boxed warning or adverse readout is a class repricing event — when steel-manning (THES-02), check the whole class's safety calendar, not just the name's (clinical-catalysts quality-signals).
