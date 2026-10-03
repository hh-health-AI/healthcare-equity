# Public data envelopes

Every client returns `source`, `query`, `retrieved_at`, `returned`, `total_reported`, `complete`, `completeness_scope`, `provenance`, `limitations`, `records` and schema version.

`complete` is narrowly relative to a source query. For ClinicalTrials.gov and PubMed it depends on reconciled counts and retrieval. openFDA compares the bounded result with reported total. CMS samples always set `complete: false` and `total_reported: null`: short pages do not prove population completeness. Catalog discovery completeness applies only to title matches in that catalog and API distributions.

`provenance` records query URLs, UTC timestamps and SHA-256 hashes of responses (except a recognized openFDA no-matches response, which records its HTTP status). API keys are redacted. Envelopes preserve raw registry data for exact NCT lookup; searches retain normalized fields. PubMed returns metadata and abstracts, not full text. Source availability, syntax and licensing may change.

Example offline coverage artifact: `examples/data-sample.json`. Use `hh-research data --help` for live commands.


Full examples: https://github.com/hh-health-AI/healthcare-equity/tree/feat/healthcare-research-suite-nine-tools/research-suite/examples . Example paths above are relative to that suite directory; they are not bundled inside this individual skill.
