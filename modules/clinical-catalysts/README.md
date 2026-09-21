# clinical-catalysts

Science, trials, and FDA evidence engine for buy-side healthcare equity research. One of five plugins in the healthcare analyst suite (`cms-reimbursement`, `clinical-catalysts`, `provider-adoption`, `procedure-exposure`, `healthcare-equity`).

Answers: **does the science work, will FDA/EMA allow it, when is the binary event, and who else is coming** — delivered as evidence briefs the `healthcare-equity` plugin assembles into an investable view.

Built to institutional investor standards: rigorous and auditable. 

## Components

| Type | Name | Purpose |
|---|---|---|
| MCP server | Clinical Trials (hosted) | ClinicalTrials.gov search, trial details, endpoints, sponsors, investigators |
| MCP server | PubMed (hosted) | Biomedical literature search and metadata |
| Skill | catalyst-calendar | Readouts, PDUFA dates, AdComs → ranked 6-month event list |
| Skill | readout-handicap | Trial-design audit, base rates, PoS decomposition, outcome scenarios |
| Skill | adcom-label | AdCom preparation and 48-hour post-approval label-delta analysis |
| Skill | pipeline-landscape | Every asset in an indication/mechanism, ranked — the competitive brief |
| Skill | literature-kol | Conference abstract triage, evidence-momentum scans, KOL mapping |
| Skill | device-diligence | TPP, CMC/COGS, FTO, FDA meeting history, 510(k)/De Novo/PMA, LDT, CDx, combination products |
| Skill | precedent-pack | Named historical analogs for any binary event — wide-then-narrow, negatives hunted |
| Skill | quality-signals | 483/WL/import-alert facility risk + FAERS/MAUDE/recall safety signals |
| Agent | readout-watcher | Scheduled CT.gov delta scan + label-supplement and enforcement sweeps on the watchlist |

## Workflow

```mermaid
flowchart TD
    U(["Universe · ticker · pending binary event"]) --> CAL["catalyst-calendar<br/>readouts · PDUFA · AdCom · EPAR SOBs"]
    U --> PL["pipeline-landscape<br/>ranked field + negative-space sweep"]
    U --> LK["literature-kol<br/>abstract triage · evidence momentum · KOLs"]
    U --> DD["device-diligence<br/>pathways · FTO · CMC · combination products"]

    CAL -->|readout nears| RH["readout-handicap<br/>design audit → PoS → outcome scenarios"]
    CAL -->|decision date nears| AL["adcom-label<br/>AdCom prep · CRL-risk checklist · label delta"]
    PP["precedent-pack<br/>named analogs · negatives hunted"] -->|adjusted PoS| RH
    PP -->|expected label & vote| AL
    QS["quality-signals<br/>483/WL/import-alert lane + FAERS/MAUDE/recall lane"] -->|facility & safety risk| AL

    CT[("Clinical Trials connector")] --> CAL
    CT --> PL
    CT --> RH
    PM[("PubMed connector")] --> LK
    FDA[("Drugs@FDA · openFDA · web<br/>Rhizome connector when installed")] --> AL
    FDA --> DD
    FDA --> PP
    FDA --> QS

    RW["readout-watcher agent<br/>registry deltas · label supplements · enforcement hits"] -.-> CAL
    RW -.-> QS

    RH --> BRIEF[/"EVIDENCE BRIEFS<br/>clinical · regulatory (FDA) · competitive"/]
    AL --> BRIEF
    PL --> BRIEF
    LK --> BRIEF
    DD --> BRIEF
    PP --> BRIEF
    QS --> BRIEF
    BRIEF --> LEDGER[("evidence ledger<br/>~/.claude/data/clinical-catalysts/briefs/")]
    BRIEF --> HE["healthcare-equity<br/>thesis · model-valuation (rNPV) · investable-view"]

    classDef skill fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef agent fill:#fef3c7,stroke:#d97706,color:#111827,stroke-dasharray:5 5
    classDef brief fill:#fce7f3,stroke:#db2777,color:#111827
    classDef note fill:#f3f4f6,stroke:#6b7280,color:#111827
    classDef ext fill:#ede9fe,stroke:#7c3aed,color:#111827
    class CAL,PL,LK,DD,RH,AL,PP,QS skill
    class CT,PM,FDA,LEDGER data
    class RW agent
    class BRIEF brief
    class HE ext
```

*Blue = skills · green = data sources & stores · amber (dashed) = agents · pink = evidence outputs · violet = suite handoffs.*

<!-- standalone-install:start -->
## Installation

This standalone distribution is published as **HH-clinical-catalysts**; the plugin inside keeps its suite id `clinical-catalysts`. Two ways to install — **pick one**, not both (both distribute the same plugin under the same name):

**Standalone (this repo):**

```shell
/plugin marketplace add <your-github-username>/HH-clinical-catalysts
/plugin install clinical-catalysts@HH-clinical-catalysts
```

**As part of the five-plugin suite (recommended if you want the full evidence→investable-view chain):**

```shell
/plugin marketplace add <your-github-username>/claude-healthcare-analyst-suite
/plugin install clinical-catalysts@healthcare-analyst-suite
```

Updates: `/plugin marketplace update HH-clinical-catalysts` (standalone) or `/plugin marketplace update healthcare-analyst-suite` (suite). If you switch sources later, uninstall the plugin first, then remove the old marketplace.
<!-- standalone-install:end -->

## Setup

- No environment variables; both servers are hosted connectors.
- Install alongside the other four suite plugins; uninstall the old `healthcare`, `cms-coverage`, `npi-registry`, and deprecated/standalone `pubmed` + `clinical-trials` plugins so each connector registers once.
- Optional depth layer: install the **Rhizome AI** connector from the claude.ai connector directory — skills prefer it for FDA/EMA primary-document research (reviews, CRLs, predicates, designations) and fall back to web when absent.

## Usage

- "Build the catalyst calendar for the next 6 months" → catalyst-calendar
- "Handicap [TICKER]'s Phase 3 in [indication]" → readout-handicap
- "Prep the AdCom" / "analyze the approved label vs expectations" → adcom-label
- "Map everything in development for [indication/mechanism]" → pipeline-landscape
- "Triage the [ASCO/AHA/ESMO] abstracts" / "what's the literature saying about X" → literature-kol
- "Check the 510(k) predicate / FTO / CMC risk for [TICKER]" → device-diligence
- "Build the precedent pack for [event]" / "what has FDA actually accepted for X" → precedent-pack
- "Any warning letters / 483s / safety signals on [TICKER]?" → quality-signals
- "Watch my names for trial changes" → schedule the readout-watcher agent

## Smoke test

Ask: **"Build a 90-day catalyst calendar for [two or three covered tickers]."**
Pass: dated events carrying NCT IDs and registry timestamps (plus PDUFA/AdCom sources), with sponsor-guidance vs registry dates distinguished; deep-dived events end with an EVIDENCE BRIEF whose citations open. The output must move model variables (timing/probability), not merely list news.
Fail tell: event dates without NCT IDs or openable citations mean the Clinical Trials connector was not called.
