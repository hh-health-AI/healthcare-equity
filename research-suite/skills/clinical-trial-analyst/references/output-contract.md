# Trial comparison

Root: `trial_id`, `documents` (at least two), optional `synthetic`. Each document requires unique `id`, matching `trial_id`, `kind`, `url`, `vintage`, and a `fields` object.

Supported fields: `primary_endpoints`, `secondary_endpoints`, `population`, `sample_size`, `analysis_population`, `masking`, `comparator`, `follow_up`, `primary_completion`, `status`. Normalize units and meanings before comparison. Values can be JSON scalars, objects, arrays or null. Include outcome/timepoint and estimand in the extraction. Preserve full extraction provenance in an accompanying evidence packet.

Output: field-level differences and source table. Equality is structural, not semantic validation. Missing fields are disclosed. Differences do not prove outcome switching, selective reporting or misconduct. Historical registry/protocol/SAP versions are necessary when prespecification matters.

Example: `examples/trial.json`.


Full examples: https://github.com/hh-health-AI/healthcare-equity/tree/feat/healthcare-research-suite-nine-tools/research-suite/examples . Example paths above are relative to that suite directory; they are not bundled inside this individual skill.
