# Research suite development

This directory contains nine biomedical and healthcare research workflows and their deterministic support package. For non-investment research, do not force investment recommendations or model impacts into outputs. Skill-specific workflows control their artifact structure.

- Keep Python core runtime standard-library-only. MCP remains an optional extra.
- Preserve exact source/query provenance and explicit incompleteness. Never interpret failed/capped retrieval as absence or complete population coverage.
- Keep host-agent interpretation separate from deterministic calculations. Do not describe a structural validator as an automated clinical truth verifier.
- Use synthetic fixtures in offline tests; label examples. Live smoke tests are optional network checks.
- Run unit tests and package validation for changes; use MCP protocol tests when its optional dependency is installed.
- Do not install schedules, send messages, make trades, or change user host settings as a development side effect.
