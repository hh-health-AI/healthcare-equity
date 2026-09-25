# Medical evidence, claim checker and journal club

Required root fields: `question` (string), `sources` (array), `claims` (nonempty array). Optional `synthetic` boolean; `methods`, `limitations`, `open_questions`, `model_impact` are arrays of strings. `slides` maps string keys `1` through `8` to source-linked slide text.

Each source requires unique string `id`, `title`, `url` (HTTP(S) or local file URI), timezone-aware ISO `retrieved_at`, `vintage` (document/data date or explicitly unknown), and `kind`. `locator` and `excerpt` are mandatory for sources used in supported, partially-supported or contradicted assessments. Optional `status` can flag retraction, corrections or unverified status. Preserve short excerpts consistent with source reuse rights.

Each claim requires unique `id`, `text`, `verdict`, `rationale` and an array `source_ids` referring to source IDs. Verdicts: `supported`, `partially-supported`, `unsupported`, `contradicted`, `unverifiable`. An inaccessible source must not receive a confident supported verdict merely because its reference resolves. The validator checks structure and selected consistency rules; the researcher/AI host must actually read the evidence and make the judgments.

Output: Markdown report and optional JSON containing the validated packet. Journal club adds an eight-slide Markdown outline; it does not export PPTX. Sources and supplied judgments remain distinct.

Example: `examples/evidence.json`.


Full examples: https://github.com/hh-health-AI/healthcare-equity/tree/feat/healthcare-research-suite-nine-tools/research-suite/examples . Example paths above are relative to that suite directory; they are not bundled inside this individual skill.
