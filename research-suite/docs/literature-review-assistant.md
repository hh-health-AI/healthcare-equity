# Literature Review Assistant

Use for biomedical literature searches, deduplication, screening assistance, study extraction, evidence maps and systematic-review preparation. Preserve search logs and human screening decisions; do not label a capped or single-database retrieval as comprehensive.

## Try it

- Prepare a reproducible literature review on this PICO question.
- Deduplicate these exports and create an auditable screening worklist.
- Build a study-level evidence map with reasons for exclusion.

## Run the reproducible utility

```bash
hh-research literature examples/literature.json --out outputs/literature-review-assistant.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Define question, inclusion/exclusion criteria, outcomes, databases and cutoff before screening. State whether the task is rapid, scoping or systematic review support.
2. Create reproducible queries and run relevant databases. `hh-research data pubmed --query "your exact query" --max-records 100 --out pubmed.json` reports the cap and total. If partial, refine/exhaust searches or state the limitation.
3. Convert records into the input contract, retaining import-specific IDs and identifiers. Record exact queries, dates, counts and coverage in search_log.
4. Run `hh-research literature review.json --out review-worklist.md --json-out review-worklist.json`. Exact DOI/PMID duplicates are grouped; ambiguous titles and identifier conflicts remain for review.
5. Apply eligibility criteria to title/abstract, then full text. Keep excluded records with reasons and uncertain decisions for human adjudication. Never exclude solely because an article is inaccessible.
6. Link multiple publications to studies/cohorts before extraction. Extract methods, effects, uncertainty, harms and bias domains with passages.
7. Report record counts separately from study/report counts. Use a recognized PRISMA flow only after its counting stages have been reconciled. This utility creates a screening worklist, not a certified systematic review.

## Existing platform handoff

[evidence-catalysts](../../modules/evidence-catalysts/)

[Skill instructions](../skills/literature-review-assistant/SKILL.md) · [Agent workflow](../agents/literature-review-assistant.md) · [Input contracts](input-contracts.md)
