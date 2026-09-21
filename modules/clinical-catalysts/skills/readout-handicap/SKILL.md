---
name: readout-handicap
description: >
  This skill should be used when the user says "handicap this readout", "pre-mortem the
  Phase 3", "what are the odds this trial works", "assess the trial design for [TICKER]",
  or before any binary clinical data event where probability of success and outcome
  scenarios drive positioning.
metadata:
  version: "0.1.0"
---

# Readout Handicap

Handicap an upcoming clinical readout: audit the design, set base rates, decompose probability of success, and map outcome scenarios to positioning.

## Workflow

1. Pull the trial from the Clinical Trials connector: design (randomization, blinding, comparator, N, endpoints and hierarchy, powering assumptions where inferable), status and date history. Retrieve the prior-phase data (company disclosures, PubMed publication of the Phase 2) and any protocol publication. Note registry-vs-guidance timing divergence.
2. Run the SUB-BIO-01 prompt (in `${CLAUDE_PLUGIN_ROOT}/skills/readout-handicap/references/prompts.md`): trial design → phase-transition base rate → comparator → outcome distribution with probabilities → stock implications including "wins but disappoints" → positioning.
3. Anchor probabilities in `${CLAUDE_PLUGIN_ROOT}/references/base-rates.md`; adjust for indication-specific rates, endpoint quality (surrogate vs clinical, effect size vs powering, multiplicity), the Phase 2→3 translation gap (single-arm or small-N Phase 2s inflate expectations), and enrollment/timing signals. Show the PoS decomposition explicitly: technical × regulatory × commercial.
4. Build the outcome distribution as mutually exclusive scenarios per the scenario discipline in `${CLAUDE_PLUGIN_ROOT}/references/evidence-translation-clinical.md` — including clean win, statistical-win/clinical-shrug ("wins but disappoints"), mixed/subgroup, miss, and safety surprise — each with a probability and expected stock reaction vs what's implied.
5. State the smart short's critique of the design (the criticisms a skeptic would raise) before concluding.
6. End with the EVIDENCE BRIEF block (layer: clinical). Pass the PoS and scenario set to healthcare-equity model-valuation (MOD-03 rNPV) and portfolio (PORT-02 catalyst concentration).
