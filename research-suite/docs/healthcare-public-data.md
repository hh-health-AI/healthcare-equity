# Healthcare Public Data Toolkit

Use when retrieving ClinicalTrials.gov, PubMed, openFDA or CMS catalog and sample data, integrating public biomedical tools through MCP or checking query completeness and vintage. Never treat a sample, suppressed dataset or missing result as the full market or absence of events.

## Try it

- Retrieve this trial with provenance and source vintage.
- Find the CMS Part D distribution for the year I specify.
- Search PubMed and tell me whether the result set is capped.

## Run the reproducible utility

```bash
hh-research data trials --query "NCT04280705" --max-records 2 --out outputs/trial-query.json
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Match the question to its source and required population, period and identifiers. Read `references/methods.md` for coverage restrictions.
2. Use `hh-research data trial`, `trials`, `pubmed`, `fda`, `cms-discover` or `cms-sample`. Consult `hh-research data --help` and each subcommand's `--help`. Save JSON envelopes intact.
3. Check returned, total_reported, complete, query, provenance and limitations before interpretation. complete is relative to a source query, never all evidence on the question.
4. For CMS, discover the distribution ID and year first; inspect its dictionary, then provide exact field/value filters. cms-sample explicitly does not verify population completeness and cannot support national totals or market shares.
5. Treat empty results as a query outcome only. Inspect entity aliases, coding changes, missingness, suppression and data lag.
6. For MCP integration install the optional extra and start `hh-healthcare-mcp` over stdio. Use `docs/mcp.md` in the repository for configuration. No hosted endpoint is supplied.
7. Hand off normalized evidence and provenance to the requested workflow. Use existing specialized modules for deeper reimbursement/utilization work after verifying their current behavior.

## Existing platform handoff

[rx-utilization](../../modules/rx-utilization/), [fda-safety-signals](../../modules/fda-safety-signals/), [cms-reimbursement](../../modules/cms-reimbursement/)

[Skill instructions](../skills/healthcare-public-data/SKILL.md) · [Agent workflow](../agents/healthcare-public-data.md) · [Input contracts](input-contracts.md)
