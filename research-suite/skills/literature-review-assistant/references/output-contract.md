# Literature worklist

Root: `search_log` object, `records` array, optional `synthetic`. Search log records database, exact query, search date, filters, cap and counts. Each record requires a unique import-specific `id` and `title`. Optional `doi`, `pmid`, `decision`, `reason` and additional extraction fields.

Decision values: `include`, `exclude`, `uncertain`, `unscreened`; exclusions require reasons. Exact shared DOI/PMID identifiers form duplicate groups. Conflicting identifiers retain every record. Title similarity only generates review candidates. Removed records remain in the structured duplicate audit; the retained representative is the first imported record, and conflicting include/exclude decisions set the retained record to uncertain and are flagged for adjudication. Other annotations in duplicate records remain available for reviewer reconciliation.

Output: retained records, duplicate map, identifier conflicts, title-match candidates and record-level screening counts. Counts are not automatically a PRISMA flow or study-level meta-analysis population.

Example: `examples/literature.json`.


See the repository suite examples for complete synthetic input files.
