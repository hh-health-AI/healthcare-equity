# Conference Evidence Agent

Use to analyze public ASCO, AACR, ASH, ESMO or other medical conference abstracts, posters and presentations, identify updated evidence and reconcile overlapping cohorts. Verify public availability and respect embargoes and access restrictions.

## Try it

- Triage the public abstracts relevant to this oncology watchlist.
- Which conference reports update the same patient cohort?
- Compare the poster with the earlier abstract without double-counting patients.

## Run the reproducible utility

```bash
hh-research conference examples/conference.json --out outputs/conference-evidence-agent.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Define conference, indication/mechanism, watchlist and an explicit timezone-aware cutoff.
2. Verify the material is public as of the cutoff. Store only authorized materials. A title listing is not permission to access or analyze embargoed results.
3. Record abstract ID, title, public timestamp, source URL, material level, NCT ID, cohort ID and data cutoff when available.
4. Compare each public record with earlier public reports. Extract genuinely new follow-up, patients, endpoint results and safety observations; attribute every claim.
5. Run `hh-research conference conference.json --out conference-brief.md --json-out conference-results.json`. Records with unconfirmed/future public availability are withheld from the brief.
6. Review cohort groups. Shared NCT IDs may contain distinct cohorts; shared trial and cohort IDs suggest overlap, not independent replication.
7. Rank scientific relevance using transparent criteria tied to the user's question. Do not generate automatic investment recommendations or infer results from titles.
8. Report public evidence, incremental contribution, comparison limitations and what to revisit when full materials are released.

## Existing platform handoff

[evidence-catalysts](../../modules/evidence-catalysts/)

[Skill instructions](../skills/conference-evidence-agent/SKILL.md) · [Agent workflow](../agents/conference-evidence-agent.md) · [Input contracts](input-contracts.md)
