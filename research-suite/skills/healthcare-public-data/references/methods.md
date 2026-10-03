# Methodology

ClinicalTrials.gov: sponsor-reported registry, public records, lagging updates, dates retain type/precision. Full queried coverage does not imply every trial is registered or reported.
PubMed: indexed metadata and abstracts, query translation retained, capped retrievals flagged; full-text availability and retraction metadata vary.
openFDA: bounded search and total, no silent population claim. Spontaneous reports cannot establish incidence or causality; duplicate reports and reporting biases need separate analysis.
CMS: catalog discovery yields distribution IDs, dictionary, vintage and temporal fields. Sampling validates returned exact-match filters and marks completeness false even for a short page. National/state, payer, suppressed cells and changing distributions are not interchangeable.

Optional keys: NCBI_API_KEY and OPENFDA_API_KEY via environment; never place them in artifacts. The network client limits requests to approved HTTPS hosts, uses retries and SHA-256 response hashes. Queries still go to external public services, so do not include confidential patient data. Public data licenses and reuse limits remain source-specific.
