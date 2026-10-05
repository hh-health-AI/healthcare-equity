---
name: medical-evidence-skills
description: Use for a biomedical evidence question, PICO search, evidence table,
  critical appraisal, conflicting-evidence synthesis or plain-language explanation.
  Preserve source passages and uncertainty; do not turn research support into a personalized
  treatment decision.
---

# Medical Evidence Skills

## Workflow

1. Define population, intervention or exposure, comparator, outcomes, setting and date cutoff. State whether the requested answer is explanatory, evidence-mapping or decision-support research. Proceed with a stated scope when missing details are nonblocking.
2. Search the relevant primary evidence through PubMed, ClinicalTrials.gov and other available authoritative sources. Log exact query, database, date, filters, returned count, reported total and caps. Search for negative and conflicting results. Use the literature-review workflow for a substantial screening process.
3. Read the relevant full text, protocol, supplement and registry where available. Disclose abstract-only access. Record study design, prespecification, analysis population, endpoint/timepoint, effect size, uncertainty, harms and applicability. Do not fill unreported methods from a generic study template.
4. Make one source record per actual document and link reports belonging to the same study or cohort. Create a bounded claim for each material conclusion, with a precise locator and a short supporting passage. Separate what the source states from independent corroboration or your inference.
5. Appraise design limitations, bias, missing data, precision, consistency and applicability. Differentiate statistical significance, clinical importance and certainty. Do not average incompatible outcomes or populations to create spurious consensus. Explain unresolved conflicts and what source would resolve them.
6. Check each claim against its source and search boundary. Use the claim-checker workflow for a citation audit. Corrections or retractions, when relevant, belong in the assessment; an accessible DOI alone is not verification.
7. Deliver an answer, compact evidence table, interpretation, limitations and next evidence needed. Use accessible language suitable for the audience. Add investment interpretation only when requested. Confidence refers to the strength of this synthesis, not the probability that a patient will benefit.

## Evidence table

Include study/record ID, population, intervention/comparator, endpoint/timepoint, effect and uncertainty, harms, design limitations, source locator and applicability. Leave missing entries explicitly missing. The upstream CLI can validate a supplied evidence packet but cannot independently determine scientific truth; this plugin does not run or bundle it.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
