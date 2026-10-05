# Validation scope

This release is tested for **package structure**, not for biomedical truth or investment performance.

The local checks verify the root manifest schema and expected fields; strict release version; matching folder and skill names; thirteen nonempty skills; twelve module references; fourteen reviewed-source records with syntactically valid blob IDs; at most three default prompts; a subtitle no longer than thirty characters; valid YAML metadata; all internal Markdown references resolving within the package; a single-root archive; no symlinks, credentials or host-specific persistence paths; and no unverified app/MCP registration.

`python tests/validate_static.py` reruns the standard-library structural checks. The build process also uses YAML and JSON Schema validators when available. `tests/smoke-cases.json` contains twelve acceptance specifications with expected routing and safeguards. These specifications are **not** represented as executed LLM or connector tests.

Not performed: live medical-data requests, upstream Python unit tests, clinical validation, priced investment examples, automatic scheduling, remote-server deployment, or end-to-end execution of every skill in ChatGPT. Successful account creation establishes a saved private plugin, not proof of live data connectivity.

A machine-readable report accompanies the distributed archive.
