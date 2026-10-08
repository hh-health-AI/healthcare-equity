# provider-adoption

Provider and site adoption evidence workflows for healthcare equity research. This directory is the flagship's integrated `provider-adoption` module; the [standalone source](https://github.com/hh-health-AI/provider-adoption) remains available.

Answers: **is the prescriber/site base actually expanding, where, and how fast** — capacity-side adoption evidence delivered as briefs the `healthcare-equity` plugin assembles into an investable view. (Volume-side evidence lives in `procedure-exposure`.)

Instructions organize source evidence and explicit model implications; their output requires researcher appraisal.

## Components

| Type | Name | Purpose |
|---|---|---|
| Optional connector | NPI Registry | US National Provider Identifier registry — providers, taxonomies, locations, organizations |
| Skill | provider-footprint | Prescriber/specialist counts by taxonomy and geography → addressable base |
| Skill | site-adoption-tracker | Snapshot-and-compare of sites/programs over time → adoption-curve evidence |
| Skill | kol-site-map | NPI × trial investigators × publication authors → trial-to-commercial site overlap |
| Skill | channel-check-prep | Footprint → ranked expert-network and field-call target lists |
| Agent | footprint-refresh | Quarterly matched-cohort refresh of tracked footprints |

## Workflow

```mermaid
flowchart TD
    Q(["Who could deliver it? Is the<br/>prescriber/site base actually growing?"]) --> PF["provider-footprint<br/>taxonomy × geography counts,<br/>recorded query definition"]
    NPI[("NPI Registry connector")] --> PF
    PF -->|capacity denominator| SAT["site-adoption-tracker<br/>matched-cohort adds / drops / net"]
    SNAP[("snapshots store<br/>~/.claude/data/provider-adoption/snapshots/")] <--> SAT
    FR["footprint-refresh agent<br/>quarterly re-run, query unchanged"] -.-> SAT
    SAT -->|S-curve stage read| KSM["kol-site-map<br/>trial sites × commercial sites overlap"]
    XREF[("CT.gov investigators + PubMed authors<br/>via clinical-catalysts connectors")] --> KSM
    KSM -->|priority targets incl. non-adopters| CCP["channel-check-prep<br/>ranked, MNPI-safe call list"]

    PF --> BRIEF[/"EVIDENCE BRIEF<br/>commercial (adoption) · competitive (site share)"/]
    SAT --> BRIEF
    KSM --> BRIEF
    BRIEF --> CAVEAT{{"presence ≠ volume —<br/>pair with procedure-exposure"}}
    BRIEF --> LEDGER[("evidence ledger")]
    CCP -->|who & why + question bank| ME["healthcare-equity meetings-experts<br/>(EN-01 prep → EN-02 debrief)"]
    BRIEF --> HE["healthcare-equity<br/>adoption variables → investable-view"]

    classDef skill fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef agent fill:#fef3c7,stroke:#d97706,color:#111827,stroke-dasharray:5 5
    classDef brief fill:#fce7f3,stroke:#db2777,color:#111827
    classDef note fill:#f3f4f6,stroke:#6b7280,color:#111827
    classDef ext fill:#ede9fe,stroke:#7c3aed,color:#111827
    class PF,SAT,KSM,CCP skill
    class NPI,SNAP,XREF,LEDGER data
    class FR agent
    class BRIEF brief
    class CAVEAT note
    class ME,HE ext
```

*Blue = skills · green = data sources & stores · amber (dashed) = agents · pink = evidence outputs · violet = suite handoffs.*

## Installation

Choose one of three routes. The [flagship installation guide](https://github.com/hh-health-AI/healthcare-equity#installation) describes their separate scope.

| Route | What you get | Instructions |
|---|---|---|
| Portable instruction skills | The skills in this repository, read directly or copied into a host-configured location | Your host discovers `SKILL.md` files; browsing and data tools remain separate |
| Python CLI and optional local MCP | The flagship's broader biomedical retrieval, comparison and calculation utilities | [Python quickstart](https://github.com/hh-health-AI/healthcare-equity/blob/main/research-suite/README.md#quickstart) and [local MCP guide](https://github.com/hh-health-AI/healthcare-equity/blob/main/research-suite/docs/mcp.md); not every connector in this module's workflow is supplied by that runtime |
| Workspace instruction plugin | Thirteen adapted skills with guides for twelve evidence modules | [GitHub marketplace import](https://github.com/hh-health-AI/healthcare-equity/blob/main/plugins/README.md); this skills-only edition does not import every module subskill or deploy data connections |

For the separate Python package, use Python 3.10+:

```sh
git clone https://github.com/hh-health-AI/healthcare-equity.git
cd healthcare-equity/research-suite
python3 -m venv .venv
# macOS / Linux; Windows PowerShell: .venv\Scripts\Activate.ps1
. .venv/bin/activate
python -m pip install .
python scripts/run_demo.py
```

The demo writes nine synthetic reports to `outputs/demo/`. The optional local MCP uses stdio and supplies no hosted URL. Configure source-required contact identity or credentials in the runtime environment; upstream documents `HH_CONTACT`, `NCBI_API_KEY` and `OPENFDA_API_KEY`. These values do not belong in prompts or committed files. Installation does not start monitoring jobs.

## Setup

Provider research can use a supported NPI Registry connector, the public registry or supplied exports. Availability, authorization and pagination behavior depend on the host and source. Keep taxonomy, geography, provider type, query and coverage limits with each result.

Other evidence modules can be used when the research question needs them; installing all five original suite plugins is not required. Keep any useful existing integrations and configure only the tools your host supports. Review duplicate connector names in the host configuration if needed; no automatic uninstall or account-permission change is part of this setup.

The workflow diagram describes logical handoffs. Connector nodes, host-specific ledger paths and scheduled agents are configuration examples, not resources created by installing instructions. Use an explicit storage location supported by your host, and configure a monitoring schedule only when requested.

## Usage

- "How many [specialists] could deliver [therapy/procedure], and where?" → provider-footprint
- "Track the sites offering [procedure/program] over time" → site-adoption-tracker
- "Which trial sites became commercial accounts?" / "map the KOLs' institutions" → kol-site-map
- "Build me an expert-call target list for [thesis]" → channel-check-prep
- "Refresh my tracked footprints quarterly" → schedule the footprint-refresh agent

## Smoke test

Ask: **"How many clinical cardiac electrophysiologists are registered in Texas, and where are they concentrated?"**
Pass: a count with the recorded query definition (taxonomy codes, geography, Type 1/2), a snapshot date, the presence-not-volume caveat, and an EVIDENCE BRIEF. Fail: a bare number without query definition, source and coverage limits cannot be reproduced, whether retrieval used a connector, browsing or an export.
