---
name: healthcare-public-data
description: Use to retrieve official biomedical or healthcare public records, choose
  between ClinicalTrials.gov, PubMed, FDA and CMS sources, inspect data vintage and
  query completeness, or explain the optional upstream local CLI/MCP setup. Never
  equate a sample or missing result with the full market or absence of events.
---

# Healthcare Public Data

## Retrieval workflow

1. Match the question to an authoritative source and define entity IDs, population, geography, period and required grain. Read the connector map and inspect the actual available tool schema before querying.
2. Resolve ambiguous drug, provider, trial or coding identifiers using appropriate official mappings. Do not mix ingredient, brand, strength, formulation, organization and person identifiers.
3. Retrieve through an available specialized connector or authorized primary-source browsing. Preserve the source envelope and provenance where returned: query, record IDs, source version, dates, reported total, returned count, pagination/cap, completeness scope and limitations. Do not fabricate a missing hash or timestamp.
4. For CMS aggregate data, discover the exact dataset/distribution and reporting year, inspect the dictionary and grain, then apply valid fields/filters. Separate a sample from a complete query result. Capped rows cannot justify national totals, prevalence or market-share estimates. Suppressed data remain suppressed, not zero.
5. Treat an empty response as a query result only. Check aliases, changed codes, date filters, publication lags, pagination and access failures before interpreting absence. Completeness relative to one query is not completeness of the research question.
6. Hand off source-bounded observations to the relevant trial, evidence or financial workflow. State units, denominator, dataset vintage and material gaps. Do not extrapolate beyond supported coverage without an explicit model and labeled assumptions.

## Optional upstream software setup

Read [upstream runtime](references/upstream-runtime.md) only for a separately requested local CLI or MCP setup task. This skills plugin does not include the Python package, new data credentials, a hosted server, or registered MCP tools. Do not invoke a command by name merely because upstream documentation mentions it.

## Shared controls and output

Read [evidence controls](references/evidence-controls.md) before executing this workflow and use the [connector map](references/connector-routing.md) for source selection. Use the [evidence brief](references/evidence-brief.md) when producing investment-related evidence. The workflows use the host's available tools; upstream Python utilities and the local MCP server are not included or deployed by this plugin.
