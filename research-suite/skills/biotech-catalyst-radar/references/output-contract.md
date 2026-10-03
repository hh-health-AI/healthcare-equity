# Catalyst snapshots

Root: `scope` (identical structured query/watchlist identity in both snapshots), `as_of` (ISO timestamp with timezone), `complete: true`, nonempty `records`. Each record has unique `id`; source `url` is strongly recommended. Remaining fields are compared except retrieval metadata.

Both snapshots must cover the exact same IDs and have increasing timestamps. The CLI watcher retrieves every specified NCT record and writes a baseline on the first run. Failed fetches, changed scope or missing records stop the comparison and preserve the old state. A state file is the latest baseline, not a historical archive. Archive it separately when a full audit trail is required. Do not run concurrent writers to one state file.

Output: field changes with before/after values and source links. Month/quarter precision stays unchanged. Registry completion is never represented as a sponsor-announced readout or FDA decision date.

Examples: `examples/snapshot-before.json`, `examples/snapshot-after.json`.


Full examples: https://github.com/hh-health-AI/healthcare-equity/tree/feat/healthcare-research-suite-nine-tools/research-suite/examples . Example paths above are relative to that suite directory; they are not bundled inside this individual skill.
