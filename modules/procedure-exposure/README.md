# procedure-exposure

Volume-and-exposure evidence engine for buy-side healthcare equity research. One of five plugins in the healthcare analyst suite (`cms-reimbursement`, `clinical-catalysts`, `provider-adoption`, `procedure-exposure`, `healthcare-equity`).

Answers: **which diagnoses and procedures does this company monetize, how much of that happens, and is the coding basis shifting** — volume-side commercial evidence delivered as briefs the `healthcare-equity` plugin assembles into an investable view. (Capacity-side adoption evidence lives in `provider-adoption`.)

Built to institutional investor standards: rigorous and auditable. 

## Components

| Type | Name | Purpose |
|---|---|---|
| MCP server | ICD10 Codes (hosted) | ICD-10 code lookup and diagnosis landscape |
| Skill | exposure-map | Company/franchise → the code landscape it monetizes → revenue-by-code scaffold |
| Skill | procedure-volume-tracker | Code-keyed procedure volume trends → the volume brief |
| Skill | epi-funnel-input | Code-keyed epidemiology → patient-funnel top for TAM/rNPV models |
| Skill | code-shift-monitor | New/revised codes, NTAP awards, category moves as early signals |
| Agent | code-update-watcher | Annual ICD-10 update (Oct 1) + quarterly CPT/NTAP sweep on tracked exposures |

## Workflow

```mermaid
flowchart TD
    Q(["What does the company bill against,<br/>and how much of it actually happens?"]) --> EM["exposure-map<br/>revenue units → dx + procedure code stack"]
    ICD[("ICD10 Codes connector")] --> EM
    EM -->|code set, recorded| PVT["procedure-volume-tracker<br/>volume · acuity/mix · site-of-service"]
    EM -->|dx definition| EPI["epi-funnel-input<br/>population → diagnosed → eligible funnel top"]
    EM -->|immature/unlisted codes| CSM["code-shift-monitor<br/>coding-ladder promotions · NTAP · redefinitions"]
    CMSF[("CMS utilization & fee-schedule files<br/>+ hospital-operator commentary")] --> PVT
    EPIDATA[("surveillance & published epi<br/>via PubMed / web")] --> EPI
    CUW["code-update-watcher agent<br/>Oct 1 ICD-10 · CPT · NTAP sweeps"] -.-> CSM

    PVT --> FUNNEL{{"funnel discipline:<br/>ordered → completed → paid → persistent"}}
    EPI --> FUNNEL
    EM --> FUNNEL
    FUNNEL --> BRIEF[/"EVIDENCE BRIEF<br/>commercial (volume / exposure)"/]
    BRIEF --> LEDGER[("evidence ledger")]
    CSM -->|dated code events| CATS["clinical-catalysts catalyst calendar"]
    BRIEF --> HE["healthcare-equity<br/>rNPV funnels · razor-blade & utilization models · TAM"]

    classDef skill fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef agent fill:#fef3c7,stroke:#d97706,color:#111827,stroke-dasharray:5 5
    classDef brief fill:#fce7f3,stroke:#db2777,color:#111827
    classDef note fill:#f3f4f6,stroke:#6b7280,color:#111827
    classDef ext fill:#ede9fe,stroke:#7c3aed,color:#111827
    class EM,PVT,EPI,CSM skill
    class ICD,CMSF,EPIDATA,LEDGER data
    class CUW agent
    class BRIEF brief
    class FUNNEL note
    class CATS,HE ext
```

*Blue = skills · green = data sources & stores · amber (dashed) = agents · pink = evidence outputs · violet = suite handoffs.*

<!-- standalone-install:start -->
## Installation

This standalone distribution is published as **HH-procedure-exposure**; the plugin inside keeps its suite id `procedure-exposure`. Two ways to install — **pick one**, not both (both distribute the same plugin under the same name):

**Standalone (this repo):**

```shell
/plugin marketplace add <your-github-username>/HH-procedure-exposure
/plugin install procedure-exposure@HH-procedure-exposure
```

**As part of the five-plugin suite (recommended if you want the full evidence→investable-view chain):**

```shell
/plugin marketplace add <your-github-username>/claude-healthcare-analyst-suite
/plugin install procedure-exposure@healthcare-analyst-suite
```

Updates: `/plugin marketplace update HH-procedure-exposure` (standalone) or `/plugin marketplace update healthcare-analyst-suite` (suite). If you switch sources later, uninstall the plugin first, then remove the old marketplace.
<!-- standalone-install:end -->

## Setup

- No environment variables; the ICD10 Codes server is a hosted connector.
- Install alongside the other four suite plugins; uninstall the old `healthcare`, `cms-coverage`, `npi-registry`, and deprecated `pubmed` plugins so each connector registers once.

## Usage

- "What codes does [TICKER] actually bill against?" → exposure-map
- "Are [procedure] volumes recovering / growing?" → procedure-volume-tracker
- "Build the patient funnel top for [indication]" → epi-funnel-input
- "Any new codes or NTAP awards relevant to my names?" → code-shift-monitor
- "Watch the code updates for my exposures" → schedule the code-update-watcher agent

## Smoke test

Ask: **"Which ICD-10 code families define heart failure, and what would I track to follow procedure volumes for it?"**
Pass: concrete code families from the connector, the code system named on every claim (ICD-10-CM vs CPT/HCPCS/DRG), volume-source vintages stated, and an EVIDENCE BRIEF with a named funnel stage. Fail tell: generic prose without code lists means the ICD10 Codes connector was not called.
