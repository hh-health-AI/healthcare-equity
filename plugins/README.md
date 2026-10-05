# HH Health AI — GitHub-managed plugin marketplace

This directory publishes the existing **HH Health AI Research v0.1.0 workflow edition** as a GitHub-importable plugin. The catalog is at `.agents/plugins/marketplace.json` in the repository root.

## Import into a ChatGPT workspace

A workspace administrator opens **Workspace settings → Plugins → Add → Import marketplace** and enters:

- **Source:** `https://github.com/hh-health-AI/healthcare-equity`
- **Path:** leave empty (the marketplace is at the repository root).
- **Branch, tag, or commit:** `main` for future updates.

Authorize GitHub access when prompted, inspect Import results, and review installation and required-app settings. Creating these repository files does not perform that administrator authorization or import. After import, new marketplaces have daily synchronization; use **Marketplaces → HH Health AI → Sync now** for an explicit refresh. Workspace policies and app access remain separately controlled.

## What is packaged

`hh-health-ai-research/` contains the 101 files from the previously prepared v0.1.0 archive, unchanged, plus the matching `.codex-plugin/plugin.json` compatibility manifest. It retains the original license, attribution, provenance, 13 instruction skills, nine biomedical workflows, and twelve evidence-module guides. The module guides summarize the canonical framework; they are not a complete import of every original subskill or reference library.

The historical package README and NOTICE describe the original private snapshot preparation. This marketplace adds a distribution path; it does not rewrite those historical records. The existing personal ChatGPT plugin is not modified or converted by this catalog. No personal plugin ID is embedded in the public repository. Workspace import creates a separately managed workspace installation unless an eligible same-workspace migration is configured explicitly.

## What this does not deploy

The upstream Python CLI, local stdio MCP server, paid data feeds, scheduled monitoring, and individual data-source account connections are not deployed or authorized by this package. This skills-only edition uses available host tools and user-supplied documents. No executable server or unverified app binding is declared.

## Update and validate

Edit the packaged files under `plugins/hh-health-ai-research/`, keep both manifest versions and identities synchronized, and run from the repository root:

```sh
python3 plugins/hh-health-ai-research/tests/validate_static.py
python3 -m json.tool .agents/plugins/marketplace.json
```

Review and commit valid changes to `main`, then inspect the workspace sync result. Changes to the original `modules/`, top-level `skills/`, or `research-suite/` do not automatically regenerate these adapted package files. A future source-to-package build is a separate task.

Static checks validate structure and references, not live connector behavior or clinical/investment correctness. Run a source-backed research smoke test after installation. The package includes acceptance specifications but does not claim they were executed end-to-end.

## Official documentation

- [Importing and syncing plugin marketplaces from GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)

Prepared for GitHub distribution on 2026-10-05. GitHub remains the source; this is not a public OpenAI directory submission.
