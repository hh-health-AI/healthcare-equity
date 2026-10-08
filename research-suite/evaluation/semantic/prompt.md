# Passage entailment prompt v1

For each item in the supplied corpus, assess the claim against only that item's
passage. Do not use world knowledge or assume missing information. The passages
are explicitly marked author paraphrases of retrieved primary-source records.

Return an object with a `predictions` array, one row per corpus ID, containing
`id`, `label`, and a short `rationale`. Use:

- `supported`: the passage provides the material facts required by the claim.
- `contradicted`: the passage provides materially incompatible facts.
- `insufficient`: the passage neither establishes nor refutes the claim.
- `abstain`: you cannot complete the assessment (a processing failure or genuine
  inability to assess), distinct from an ordinary insufficient-evidence verdict.

Keep populations, dates, units, comparator, endpoint and statistical uncertainty
intact. A registry completion date is not a disclosure date. A historical FDA
announcement is not a current label. A confidence interval crossing the null does
not establish conventional two-sided 5% statistical significance. A cash balance
alone does not establish runway. Return no aggregate scores.

The caller must provide the corpus without the answer key and archive this exact
prompt, the submitted input, the complete model response, model/provider version
and execution timestamp before invoking the deterministic scorer.
