# Optional upstream runtime — not bundled

The reviewed repository README describes Python 3.10+ utilities under research-suite and an optional **local stdio** MCP server. The following commands describe that separate upstream package, not an environment installed by this plugin. Verify current upstream instructions before performing setup, use an isolated environment, and execute only after the user requests local software installation and the host permits it.

```sh
git clone https://github.com/hh-health-AI/healthcare-equity.git
cd healthcare-equity/research-suite
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
hh-research --help
```

For the optional local MCP extra, upstream documents:

```sh
python -m pip install '.[mcp]'
hh-healthcare-mcp
```

This is stdio transport, not a hosted URL or an HTTP listener. No server is deployed or registered by the private workflow plugin. Host-specific connection steps require the actual target client's current documentation and a verified runtime. A running local process is not evidence of a successful ChatGPT connection.

The reviewed upstream README describes thirteen read-only data/analytical MCP tools and Python utilities for evidence packets, trial/claim comparisons, literature worklists, fixed-watchlist diffs, rNPV calculations, conference briefs and Markdown journal clubs. None of these executable tools is copied into this archive. The Python package does not call an LLM to determine clinical truth. Synthetic demos are formatting/calculation examples, not clinical evidence.

Source: https://github.com/hh-health-AI/healthcare-equity/blob/main/research-suite/README.md (reviewed 2026-10-04). Optional keys belong in the user's secure environment, never in plugin files, prompts or committed source. Local setup, live API behavior and end-to-end host connectivity were not tested as part of this skills-only package.
