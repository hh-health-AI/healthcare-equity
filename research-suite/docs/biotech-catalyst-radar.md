# Biotech Catalyst Radar

Use to monitor a defined biotech trial watchlist, compare registry versions, build a catalyst calendar or explain changed enrollment, status or completion estimates. Keep registry dates separate from sponsor readout guidance and regulatory decision dates.

## Try it

- Track changes in these NCT records since the last snapshot.
- Build a catalyst calendar that separates confirmed dates from estimates.
- Explain the significance and uncertainty of these registry changes.

## Run the reproducible utility

```bash
hh-research catalysts --before examples/snapshot-before.json --after examples/snapshot-after.json --out outputs/biotech-catalyst-radar.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Resolve the watchlist to exact NCT IDs; record ticker/sponsor mapping as an attributed mapping, not an assumption.
2. Run `hh-research watch --ids NCT04280705 --state outputs/watch-state.json --out outputs/watch-report.md` with the requested IDs. First run establishes a baseline; later runs compare the same set.
3. On a failed or incomplete retrieval, retain the old state and report a monitoring gap. Never infer a trial disappeared from a failed search.
4. Inspect each changed field in the primary record and relevant sponsor disclosure. Explain plausible interpretations and what cannot be inferred.
5. For FDA milestones and sponsor readout guidance, separately cite the announcement, date precision, source date and whether confirmed or estimated. The registry utility does not discover or verify PDUFA dates.
6. When a watchlist changes, establish a separately named baseline; do not overwrite incompatible state silently. For supplied snapshots use `hh-research catalysts --before old.json --after new.json --out changes.md`.
7. Produce changes, sources, implications, uncertainty and next checks. Scheduling is opt-in and host-specific; the package does not activate a background task or send messages.

## Existing platform handoff

[clinical-catalysts](../../modules/clinical-catalysts/)

[Skill instructions](../skills/biotech-catalyst-radar/SKILL.md) · [Agent workflow](../agents/biotech-catalyst-radar.md) · [Input contracts](input-contracts.md)
