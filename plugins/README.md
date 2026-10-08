# HH Health AI — GitHub-managed plugin marketplace

This directory distributes **HH Health AI Research v0.1.0**, a skills-only workflow edition, through a GitHub-managed plugin marketplace. The catalog is at `.agents/plugins/marketplace.json` in the repository root; the package lives at `plugins/hh-health-ai-research/`.

For the other installation routes, see [portable skills and the Python CLI/local MCP](../README.md#installation). Importing this plugin does not install that separate runtime.

## Import into a ChatGPT workspace

A workspace administrator opens **Workspace settings → Plugins → Add → Import marketplace** and enters:

- **Source:** `https://github.com/hh-health-AI/healthcare-equity`
- **Path:** leave empty (the marketplace is at the repository root).
- **Branch, tag, or commit:** `main` for future updates.

Authorize GitHub access when prompted, inspect Import results, and review installation and required-app settings. Creating these repository files does not perform that administrator authorization or import. After import, new marketplaces have daily synchronization; use **Marketplaces → HH Health AI → Sync now** for an explicit refresh. Workspace policies and app access remain separately controlled.

## What is packaged

`hh-health-ai-research/` contains the adapted v0.1.0 instruction package and its `.codex-plugin/plugin.json` compatibility manifest. It retains the original license, attribution, provenance, 13 instruction skills, nine biomedical workflows and twelve evidence-module guides. The module guides summarize the canonical framework; they are not a complete import of every original subskill or reference library.

The [package README](hh-health-ai-research/README.md) describes current usage. [NOTICE](hh-health-ai-research/NOTICE.md) and `provenance.json` retain the original 2026-10-04 snapshot preparation and reviewed-source records. Snapshot adaptation describes how skills were prepared; GitHub synchronization describes how committed package files are distributed. These are separate processes.

The existing personal ChatGPT plugin is not modified or converted by this catalog. No personal plugin ID is embedded in the public repository. Workspace import creates a separately managed workspace installation unless an eligible same-workspace migration is configured explicitly.

## What this does not deploy

The upstream Python CLI, local stdio MCP server, paid data feeds, scheduled monitoring, and individual data-source account connections are not deployed or authorized by this package. This skills-only edition uses available host tools and user-supplied documents. No executable server or unverified app binding is declared.

## Update and validate

Edit the packaged files under `plugins/hh-health-ai-research/`, keep both manifest versions and identities synchronized, and run from the repository root:

```sh
python3 plugins/hh-health-ai-research/tests/validate_static.py
python3 scripts/validate_repository.py
```

Review and commit valid changes to the imported branch, then inspect the workspace sync result. Keep both manifests' identities, versions and skill paths consistent with the marketplace entry. Changes to the original `modules/`, top-level `skills/` or `research-suite/` do not automatically regenerate these adapted package files; review the adaptation and its provenance before updating the package.

Static checks validate structure and references, not live connector behavior or clinical/investment correctness. Run a source-backed research smoke test after installation. The package includes acceptance specifications but does not claim they were executed end-to-end.

Review [research cases](../examples/research-cases/README.md), [structural evaluation](../research-suite/evaluation/README.md) and [semantic evaluation](../research-suite/evaluation/semantic/README.md) for the distinct evidence and validation scopes.

## Official documentation

- [Importing and syncing plugin marketplaces from GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)

Prepared for GitHub distribution on 2026-10-05. GitHub remains the source; this is not a public OpenAI directory submission.
