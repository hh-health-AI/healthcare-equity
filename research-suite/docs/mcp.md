# Local MCP configuration

Install from the checked-out `research-suite` directory:

```bash
python -m pip install '.[mcp]'
```

The optional dependency intentionally uses `mcp>=1.12,<2`, the official SDK v1 API. The development validation records the installed version. Do not remove the upper bound without adapting and testing the server against SDK v2.

An example client configuration (replace the executable path with the Python executable in your actual environment):

```json
{
  "mcpServers": {
    "hh-healthcare-research": {
      "command": "/absolute/path/to/.venv/bin/python",
      "args": ["-m", "hh_research.mcp_server"]
    }
  }
}
```

On Windows, use the virtual environment's `Scripts/python.exe`. Client configuration syntax and configuration-file location are host-specific. The server runs over stdio; do not expect a browser URL. The package must be installed in the environment named in `command`.

Tools: `search_pubmed`, `search_clinical_trials`, `get_clinical_trial`, `query_openfda`, `discover_cms_datasets`, `sample_cms_dataset`, `calculate_rnpv`, `audit_evidence_packet`, `compare_trial_documents`, `prepare_literature_review`, `triage_conference`, `compare_catalyst_snapshots`, `prepare_journal_club`.

Data tools call the same allowlisted public endpoints as the CLI. Analytical tools accept structured objects matching [input contracts](input-contracts.md). No tool reads arbitrary local paths, accepts arbitrary fetch URLs, modifies a remote service, sends messages or executes a trade. The client/AI host still controls tool invocation. Optional API keys should be provided through the environment, not pasted into research prompts.

A successful stdio initialization, tool listing and an analytical tool call are checked by `tests/test_mcp.py` when the optional dependency is installed. Host-specific UI installation is not part of that protocol check.
