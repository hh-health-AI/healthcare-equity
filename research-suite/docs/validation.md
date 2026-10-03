# Validation record — v0.1.0 research preview

Validated on September 25, 2026. This record describes implementation checks and representative workflow exercises. It is not evidence of independently validated clinical accuracy, exhaustive data coverage or investment performance.

## Automated tests

42 tests passed locally under Python 3.12 with MCP SDK 1.30.0. The test suite covers:

- Citation resolution within packets, required source passages, missing evidence and retracted-only support.
- Trial identity, differences, missing fields and explicit separation of discrepancies from clinical conclusions.
- DOI normalization, conservative deduplication, transitive identifier matches, identifier conflicts, conflicting screening judgments and exclusion reasons.
- Watchlist scope, incomplete snapshots, date precision, timezone ordering and baseline preservation after a failed retrieval.
- A hand-calculated valuation case, equity/share bridge, probability bounds, nonfinite inputs, invalid share counts and missing equity-bridge inputs.
- Embargo timing, withholding nonpublic content and distinct cohorts under the same trial.
- API pagination, cap disclosure, duplicate pages, changing totals, wrong record identity, partial PubMed retrieval, CMS filter mismatches and unverified CMS completeness.
- Approved network targets, credential redaction, CLI execution and real stdio MCP initialization/listing/calculation/error handling.

The GitHub Actions workflow runs offline checks on Python 3.10 and 3.12 when executed. This statement describes configured CI coverage; it does not substitute for checking the latest workflow run.

## Live public API checks

Seven representative checks passed. Exact timestamps, query URLs, counts and response hashes are in [live-validation.json](live-validation.json).

| Check | Observed behavior |
|---|---|
| ClinicalTrials.gov exact NCT lookup | Requested identity returned |
| ClinicalTrials.gov capped search | Two returned records correctly marked partial |
| PubMed exact PMID search and fetch | Requested record reconciled |
| PubMed capped search and fetch | Returned records reconciled; search marked partial |
| openFDA label query | Bounded result and total reported; partial coverage disclosed |
| CMS catalog discovery | API distributions and vintages returned |
| CMS sample | Two rows returned; completeness remains explicitly false |

These tests do not validate every endpoint, field, drug alias, year, filter combination or edge case. CMS filtered-query behavior is tested offline for rejection of returned rows that violate exact filters; the live smoke run tests an unfiltered sample. No inference about a complete payer population is warranted.

## Skill and package checks

All nine skills passed the skill-creator frontmatter validation. Package validation checks project catalog consistency, nine skill metadata sets, Python syntax, local Markdown links and nine clearly labeled sample reports. The editable package installed successfully and generated all offline reports. An explicit-target skill-copy installer is included; host configuration and host-specific discovery remain the user's responsibility.

## Independent workflow exercises

Two independent agents received only the skill instructions and raw synthetic task inputs:

1. **Clinical Trial Analyst:** correctly distinguished extracted endpoint/population differences from clinical conclusions; identified historical protocol/SAP, denominator and source-text gaps. The exercise exposed a table issue where a missing source field masked a difference among available fields. The implementation was corrected to show both, and the regression test now verifies it. Fields absent from all sources are also explicitly shown.
2. **Biotech rNPV Modeler:** reproduced all three scenario values and independently checked a discounted row. It explained unconditional per-row probabilities, avoided a second global success multiplier, and disclosed omitted financing, terminal and abandonment assumptions.

These are limited synthetic exercises, not blinded clinical benchmarks or a general accuracy estimate. The other seven workflows have structural/utility tests and examples but have not undergone equivalent independent expert evaluation.

## Known boundaries

- AI-host reasoning and medical judgments are not automatically validated by the Python tests.
- Data completeness is specific to the queried endpoint and time; source systems and metadata can lag or change.
- Literature screening assistance does not establish systematic-review completeness or replace study-level reconciliation.
- Conference public-availability metadata must be checked against actual source publication/embargo details.
- rNPV inputs are user assumptions. No treatment outcome prediction, calibrated PoS model, automatic investment recommendation or trading execution is supplied.
- Monitoring runs only when invoked. One state file must have one writer; historical archiving is external.
- The MCP protocol is tested; every client application's installation and user interface are not.
