---
name: pipeline-landscape
description: >
  This skill should be used when the user asks to "map the pipeline in [indication]",
  "who else is developing [mechanism]", "competitive landscape for [asset]", "rank every
  asset in development for X", or needs the competitive layer of an initiation or thesis.
metadata:
  version: "0.1.0"
---

# Pipeline Landscape

Map every asset in development for an indication or mechanism and rank the competitive threat — the competitive-evidence brief for the suite.

## Workflow

1. Define the battlefield precisely: indication (and line of therapy / population subset), mechanism class(es), and the reference asset if the ask is "who threatens [TICKER]".
2. Sweep the Clinical Trials connector three ways and union the results: by condition, by intervention/mechanism synonyms, and by sponsor (for known competitors' full programs). Capture per asset: sponsor, modality/mechanism, phase, trial design and comparator, N, primary completion window, and status changes. Supplement with PubMed for published data per asset and web research for company pipeline pages; use the chembl/open-targets connectors (if installed) for mechanism validation depth.
3. Build the ranked landscape table: stage-weighted (approved → filed → Ph3 → Ph2 → Ph1/preclinical), with a base-rate PoS per asset (references/base-rates.md), expected data/launch sequence, and differentiation vs the reference asset on the axes that decide share — efficacy bar, safety/tolerability, administration/convenience, biomarker restriction, and (flag for companions) reimbursement posture. **Sweep the negative space deliberately:** assets that failed, were refused, or were discontinued in the indication (CRLs, terminated/failed trials, withdrawn designations) — failures set the approvability bar the market may be mispricing, and negative precedent counts double; record "negative precedent: [found] / none-after-search" in the brief.
4. Read the temporal dynamics: who reads out first, whose trial design sets the comparator bar, where enrollment competition bites, and which entries change the standard of care a later entrant must beat.
5. State what the landscape does and does not prove — a crowded pipeline is a probability statement about future share erosion, not current revenue; per the translation rules, competitor evidence moves share curve, price erosion, and terminal-value assumptions.
6. End with the EVIDENCE BRIEF block (layer: competitive). Feed readout dates to catalyst-calendar, the share-curve implications to healthcare-equity model-valuation, and the "closest threats" list to thesis work (INIT-03 variant perception).
