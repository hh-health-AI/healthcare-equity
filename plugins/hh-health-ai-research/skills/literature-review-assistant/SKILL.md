---
name: literature-review-assistant
description: Use for biomedical literature searches, deduplication, screening worklists,
  study extraction, evidence maps and systematic-review preparation. Preserve search
  logs and review decisions; do not label a capped or single-database retrieval comprehensive.
---

# Literature Review Assistant

## Workflow

1. Define the question, inclusion/exclusion criteria, outcomes, databases, language/time restrictions and cutoff before screening. State whether the deliverable is a rapid review, scoping review, evidence map or systematic-review support.
2. Develop reproducible queries and run the relevant available sources. Log exact query, database/interface, search date, filters, reported total, returned count and cap. Resolve truncation by appropriate pagination or scoped queries where available; otherwise disclose it.
3. Preserve original import identifiers alongside PMID, DOI, title, authors and year. Deduplicate exact normalized PMID/DOI matches conservatively. Flag contradictory identifiers and ambiguous title matches for review rather than merging them automatically.
4. Screen title/abstract and then full text against the stated criteria. Preserve exclusion reasons, uncertainties and human adjudication where needed. Inaccessibility alone is not an eligibility exclusion; mark it as not retrieved or awaiting assessment.
5. Link multiple publications to the same underlying trial, study or cohort before extracting evidence. Preserve separate follow-up reports without counting them as independent studies. Extract design, population, intervention/comparator, endpoints, effect size, uncertainty, harms, bias domains and source passages.
6. Synthesize only comparable evidence. Explain heterogeneity and conflicting results. Do not run an unrequested or unjustified pooled effect from incompatible estimates. Distinguish hypothesis-generating summaries from causal conclusions.
7. Reconcile counts of imported records, duplicates, screened records, reports retrieved and included studies. A PRISMA-style flow requires an explicitly reconciled counting process; do not certify a complete systematic review merely because a worklist exists.

## Deliverable

Provide the search log, source coverage statement, deduplicated worklist, eligibility decisions with reasons, study-linked extraction table, evidence gaps and confidence. Preserve reproducibility in a downloadable artifact only when a file has actually been created. The upstream utility assists with structured worklists; this workflow does not claim its execution or independent clinical verification.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
