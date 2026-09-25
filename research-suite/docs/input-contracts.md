# Input and output contracts

Version 0.1.0. All example inputs in `examples/` are synthetic teaching fixtures. Never cite them as medical evidence. Live data commands generate separate provenance envelopes. JSON numbers must be finite; use null for missing observations, never a fabricated zero.

## Medical evidence, claim checker and journal club

Required root fields: `question` (string), `sources` (array), `claims` (nonempty array). Optional `synthetic` boolean; `methods`, `limitations`, `open_questions`, `model_impact` are arrays of strings. `slides` maps string keys `1` through `8` to source-linked slide text.

Each source requires unique string `id`, `title`, `url` (HTTP(S) or local file URI), timezone-aware ISO `retrieved_at`, `vintage` (document/data date or explicitly unknown), and `kind`. `locator` and `excerpt` are mandatory for sources used in supported, partially-supported or contradicted assessments. Optional `status` can flag retraction, corrections or unverified status. Preserve short excerpts consistent with source reuse rights.

Each claim requires unique `id`, `text`, `verdict`, `rationale` and an array `source_ids` referring to source IDs. Verdicts: `supported`, `partially-supported`, `unsupported`, `contradicted`, `unverifiable`. An inaccessible source must not receive a confident supported verdict merely because its reference resolves. The validator checks structure and selected consistency rules; the researcher/AI host must actually read the evidence and make the judgments.

Output: Markdown report and optional JSON containing the validated packet. Journal club adds an eight-slide Markdown outline; it does not export PPTX. Sources and supplied judgments remain distinct.

Example: `examples/evidence.json`.

## Trial comparison

Root: `trial_id`, `documents` (at least two), optional `synthetic`. Each document requires unique `id`, matching `trial_id`, `kind`, `url`, `vintage`, and a `fields` object.

Supported fields: `primary_endpoints`, `secondary_endpoints`, `population`, `sample_size`, `analysis_population`, `masking`, `comparator`, `follow_up`, `primary_completion`, `status`. Normalize units and meanings before comparison. Values can be JSON scalars, objects, arrays or null. Include outcome/timepoint and estimand in the extraction. Preserve full extraction provenance in an accompanying evidence packet.

Output: field-level differences and source table. Equality is structural, not semantic validation. Missing fields are disclosed. Differences do not prove outcome switching, selective reporting or misconduct. Historical registry/protocol/SAP versions are necessary when prespecification matters.

Example: `examples/trial.json`.

## Literature worklist

Root: `search_log` object, `records` array, optional `synthetic`. Search log records database, exact query, search date, filters, cap and counts. Each record requires a unique import-specific `id` and `title`. Optional `doi`, `pmid`, `decision`, `reason` and additional extraction fields.

Decision values: `include`, `exclude`, `uncertain`, `unscreened`; exclusions require reasons. Exact shared DOI/PMID identifiers form duplicate groups. Conflicting identifiers retain every record. Title similarity only generates review candidates. Removed records remain in the structured duplicate audit; the retained representative is the first imported record, and conflicting include/exclude decisions set the retained record to uncertain and are flagged for adjudication. Other annotations in duplicate records remain available for reviewer reconciliation.

Output: retained records, duplicate map, identifier conflicts, title-match candidates and record-level screening counts. Counts are not automatically a PRISMA flow or study-level meta-analysis population.

Example: `examples/literature.json`.

## Catalyst snapshots

Root: `scope` (identical structured query/watchlist identity in both snapshots), `as_of` (ISO timestamp with timezone), `complete: true`, nonempty `records`. Each record has unique `id`; source `url` is strongly recommended. Remaining fields are compared except retrieval metadata.

Both snapshots must cover the exact same IDs and have increasing timestamps. The CLI watcher retrieves every specified NCT record and writes a baseline on the first run. Failed fetches, changed scope or missing records stop the comparison and preserve the old state. A state file is the latest baseline, not a historical archive. Archive it separately when a full audit trail is required. Do not run concurrent writers to one state file.

Output: field changes with before/after values and source links. Month/quarter precision stays unchanged. Registry completion is never represented as a sponsor-announced readout or FDA decision date.

Examples: `examples/snapshot-before.json`, `examples/snapshot-after.json`.

## Public data envelopes

Every client returns `source`, `query`, `retrieved_at`, `returned`, `total_reported`, `complete`, `completeness_scope`, `provenance`, `limitations`, `records` and schema version.

`complete` is narrowly relative to a source query. For ClinicalTrials.gov and PubMed it depends on reconciled counts and retrieval. openFDA compares the bounded result with reported total. CMS samples always set `complete: false` and `total_reported: null`: short pages do not prove population completeness. Catalog discovery completeness applies only to title matches in that catalog and API distributions.

`provenance` records query URLs, UTC timestamps and SHA-256 hashes of responses (except a recognized openFDA no-matches response, which records its HTTP status). API keys are redacted. Envelopes preserve raw registry data for exact NCT lookup; searches retain normalized fields. PubMed returns metadata and abstracts, not full text. Source availability, syntax and licensing may change.

Example offline coverage artifact: `examples/data-sample.json`. Use `hh-research data --help` for live commands.

## rNPV

Root: `as_of` (valuation date), `currency`, `units`, nonempty `scenarios`, optional `synthetic`. Each scenario needs unique `name`, `discount_rate` between 0 and 1, and nonempty `cashflows`. Optional nonnegative `cash`, `debt`, `unallocated_overhead_pv`, and positive `diluted_shares`. Equity value is calculated only when all three bridge components are explicitly supplied; missing components do not default to zero. Per-share value also requires diluted shares.

Each row requires nonnegative numeric `year` (years from valuation date, fractional allowed), signed `cashflow`, `probability` between 0 and 1, `kind` (`development`, `commercial`, `other`), and an `assumption` note with source or explicit modeling rationale.

Formula: PV = cashflow × unconditional probability / (1 + discount rate)^year. Sum rows for asset rNPV; add cash and subtract debt and overhead for equity. Use compatible units for cash and shares. Do not preweight cash flows and then weight them again. No terminal value, automatic probability estimation, scenario weighting or cross-asset correlation is assumed. Run alternate input scenarios for sensitivity analysis.

Output: scenario values plus every row's expected cash flow and discounted contribution. Enterprise value interpretation requires unlevered after-tax cash flows.

Example: `examples/valuation.json`.

## Conference triage

Root: `as_of` with timezone, `abstracts` array, optional `synthetic`. Every abstract needs unique `id`, `title`, `source_url`. To be included it must have `public: true` and a timezone-aware `public_at` no later than the cutoff. Otherwise only the ID and exclusion reason enter structured blocked output; content is excluded from the report.

Included records require `material_level` of `title`, `abstract`, `poster`, `presentation` or `publication`. Optional `trial_id`, `cohort_id`, `data_cutoff`, `new_evidence`. The researcher must verify public availability; the utility only enforces supplied metadata.

Output: public records and potential overlapping cohort groups. A shared trial ID alone does not establish cohort overlap. Human review must check enrollment, dose, setting, sample size and cutoffs. Title-only material cannot support efficacy/safety conclusions.

Example: `examples/conference.json`.
