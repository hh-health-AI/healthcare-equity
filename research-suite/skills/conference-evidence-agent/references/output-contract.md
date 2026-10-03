# Conference triage

Root: `as_of` with timezone, `abstracts` array, optional `synthetic`. Every abstract needs unique `id`, `title`, `source_url`. To be included it must have `public: true` and a timezone-aware `public_at` no later than the cutoff. Otherwise only the ID and exclusion reason enter structured blocked output; content is excluded from the report.

Included records require `material_level` of `title`, `abstract`, `poster`, `presentation` or `publication`. Optional `trial_id`, `cohort_id`, `data_cutoff`, `new_evidence`. The researcher must verify public availability; the utility only enforces supplied metadata.

Output: public records and potential overlapping cohort groups. A shared trial ID alone does not establish cohort overlap. Human review must check enrollment, dose, setting, sample size and cutoffs. Title-only material cannot support efficacy/safety conclusions.

Example: `examples/conference.json`.


Full examples: https://github.com/hh-health-AI/healthcare-equity/tree/feat/healthcare-research-suite-nine-tools/research-suite/examples . Example paths above are relative to that suite directory; they are not bundled inside this individual skill.
