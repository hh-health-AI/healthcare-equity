# Healthcare Equity Research Platform — Biotech, Pharma, Medtech, Managed Care & Healthcare Investing

<!-- geo:start -->
## Open-source healthcare equity research for investors and AI agents

This repository is an integrated **healthcare equity research platform** for **biotech, pharmaceuticals, medtech, life sciences tools, managed care, healthcare services, diagnostics, and digital health**.

It connects scientific and clinical evidence to commercial assumptions and valuation:

**clinical trials → regulatory probability → epidemiology → utilization → reimbursement → revenue → margins → DCF / rNPV / scenario analysis → investment thesis**

Use it for questions such as:
- How should a Phase 2 or Phase 3 readout change probability of success and rNPV?
- What do FDA, CMS, FAERS, Medicare Part D, provider, procedure, epidemiology, or SEC data imply for a healthcare stock?
- How do reimbursement, market access, LOE, provider adoption, safety, or utilization change revenue forecasts?
- How can public healthcare data be turned into auditable buy-side investment research?
- How can AI research agents support institutional-quality healthcare due diligence?

**Primary research entities:** ClinicalTrials.gov, FDA, EMA, CMS, Medicare, Medicaid, NPI Registry, CDC, NIH, SEC EDGAR, Orange Book, Purple Book, NICE, NMPA, and public company filings.

**Core methods:** fundamental equity research, clinical-trial interpretation, catalyst analysis, market sizing, revenue forecasting, DCF, rNPV, scenario analysis, valuation, long/short research, and evidence synthesis.

Start with the module map below or visit the [HH Health AI profile](https://github.com/hh-health-AI).

<!-- geo:end -->

<!-- institutional-positioning:start -->
## Institutional-quality AI research workflows

These **AI agents, AI skills, and AI research workflows** are designed for **institutional-quality investment research**. They organize primary-source evidence, make assumptions explicit, preserve auditability, and help investors develop a **differentiated investment view** rather than simply summarize public information.

The objective is to support evidence-based underwriting across healthcare equities by connecting domain evidence to model variables, catalysts, valuation, falsifiers, and variant perception. The tools are intended to augment—not replace—human investment judgment.

<!-- institutional-positioning:end -->

Flagship monorepo for buy-side healthcare equity research: a synthesis engine plus modular evidence pipelines spanning clinical/regulatory catalysts, utilization, reimbursement, provider adoption/economics, procedure exposure, IP/LOE, safety, epidemiology, international access, evidence/KOL signals, and SEC forensics.

The repository is organized as a **monorepo**. Permanent research capabilities live under `modules/`; Git branches are reserved for temporary feature, fix, refactor, and experiment work. The original standalone repositories remain available during migration, but this repository is the canonical integration point.

## Monorepo modules

| Layer | Module | Primary research question |
|---|---|---|
| Clinical / regulatory | [clinical-catalysts](modules/clinical-catalysts/) | What changes approval probability, label, timing, or clinical differentiation? |
| Evidence / KOL | [evidence-catalysts](modules/evidence-catalysts/) | How are publications, guidelines, abstracts, and KOL signals evolving? |
| Safety | [fda-safety-signals](modules/fda-safety-signals/) | Are FDA/FAERS/MAUDE signals changing the risk profile? |
| Utilization | [rx-utilization](modules/rx-utilization/) | What do prescribing, state utilization, and launch proxies say about demand? |
| Epidemiology | [epi-demand](modules/epi-demand/) | What population and disease-burden evidence drives the demand funnel? |
| Reimbursement | [cms-reimbursement](modules/cms-reimbursement/) | How do coverage, payment, IRA, and MA policy affect economics? |
| Provider adoption | [provider-adoption](modules/provider-adoption/) | Is site/prescriber capacity translating into adoption? |
| Provider economics | [provider-economics](modules/provider-economics/) | What do hospital, MA, and nonprofit economics imply for customers/payors? |
| Procedure exposure | [procedure-exposure](modules/procedure-exposure/) | How do codes and procedure volumes map into addressable exposure? |
| IP / exclusivity | [ip-exclusivity](modules/ip-exclusivity/) | When and how can LOE, biosimilars, or PTAB events alter the revenue curve? |
| International access | [global-access](modules/global-access/) | How do ex-US HTA, pricing, and approvals affect launch and value? |
| Financial forensics | [sec-forensics](modules/sec-forensics/) | What do SEC filings, insider activity, and accounting signals imply? |

These evidence modules feed the core synthesis layer in this repository: models, theses, scenario analysis, portfolio framing, and the investable-view capstone.

Built to institutional investor standards: rigorous and auditable. 
## Components

| Type | Name | Purpose (prompt IDs carried) |
|---|---|---|
| Skill | initiate | New-name coverage: scoping → full memo → sub-sector layers (INIT-01/02/04/05/06/07, SS-02) |
| Skill | earnings | Preview → live triage → post-print → guide decomposition + sub-sector quarterly reads (EARN-01…07, SS-03, COMM-03, SUB-PHA-03, SUB-SVC-01) |
| Skill | model-valuation | DCF stress, SOTP, rNPV, LOE, razor-blade, capex-cycle, MA Stars, digital-health UE, forensics, scenarios + sub-sector models (MOD-01…10, SUB-PHA-01/04/05, SUB-MED-05, SUB-SVC-03/04, SUB-TLS-02/04) — carries the Evidence-to-Valuation and Commercial Metrics distillations |
| Skill | thesis | Variant perception, pre-mortem, steel-man, decomposition, regime map, PM/IC dynamics (INIT-03, THES-01…05, SS-01, PORT-05/06, SUB-DIG-02) |
| Skill | screen-themes | Idea screens, thematic validation → TAM → baskets, terminal syntax (SCR-01/03/04/05, THM-01…03, SUB-PHA-02, SUB-TLS-01, TECH-01/03/04) |
| Skill | portfolio | Sleeve review, catalyst concentration, pairs, shorts, 13F, correlations, EDGAR monitoring (PORT-01…04, SCR-06/07, TECH-05) |
| Skill | meetings-experts | 1-on-1s, site visits, KOL days, expert-network arc (MGMT-01…04, EN-01…04, SUB-DIG-01) |
| Skill | sell-discipline | Scorecards, watchlists, post-mortems, annual audit (SELL-01…05) |
| Skill | international | EU HTA/JCA, Japan, China/BIOSECURE, UK (INTL-01…04) |
| Skill | comms-compliance | IC memos, LP letters, generalist translation, MNPI scrub, disclosures (COMM-01/02/04/05/06/07) |
| Skill | esg-stewardship | Materiality, engagement, access, climate (ESG-01/02/04/05, SUB-DIG-03) |
| Skill | investable-view | **Capstone:** assembles the five evidence layers → scenario matrix → valuation map → falsifiable view |
| Agent | evidence-assembler | Ticker → runs the engines' skills → drafts the investable view |

## Workflow

```mermaid
flowchart TD
    subgraph DISC["1 · Discover"]
        ST["screen-themes"] --> IN["initiate<br/>scoping → memo → sub-sector layers"]
    end
    subgraph ENG["Evidence engines (co-installed plugins)"]
        E1["cms-reimbursement"]
        E2["clinical-catalysts"]
        E3["provider-adoption"]
        E4["procedure-exposure"]
    end
    FIN[("Financial layer<br/>filings & transcripts · Quartr / EDGAR")]
    subgraph UW["2 · Underwrite"]
        MV["model-valuation<br/>economic unit → formula → scenarios"] <--> TH["thesis<br/>variant perception · steel-man · pre-mortem"]
        ME["meetings-experts<br/>1-on-1s · expert calls, MNPI-safe"] --> TH
        INTL["international<br/>HTA · Japan · China · UK"] --> MV
        ESG["esg-stewardship"] --> TH
    end
    IN --> MV
    ENG -->|EVIDENCE BRIEFS| IV
    FIN --> IV
    LEDGER[("evidence ledger<br/>briefs from all five plugins")] --> IV
    EA["evidence-assembler agent<br/>runs the engines end-to-end for a ticker"] -.-> IV
    MV --> IV["investable-view capstone<br/>6 layers → scenario matrix → price-implied<br/>→ falsifiable underwriting statement"]
    TH --> IV
    subgraph DEC["3 · Decide & communicate"]
        CO["comms-compliance<br/>IC memo · MNPI scrub · disclosures"]
        PO["portfolio<br/>sizing · catalyst concentration · pairs"]
    end
    IV --> CO
    IV --> PO
    subgraph MON["4 · Monitor & learn"]
        EARN["earnings<br/>preview → live triage → post-print"] --> SD["sell-discipline<br/>scorecards · watchlists · post-mortems"]
    end
    PO --> EARN
    IV -->|falsifiers & early signals| SD
    SD -->|lessons → base rates & thresholds| TH

    classDef skill fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef agent fill:#fef3c7,stroke:#d97706,color:#111827,stroke-dasharray:5 5
    classDef brief fill:#fce7f3,stroke:#db2777,color:#111827
    classDef note fill:#f3f4f6,stroke:#6b7280,color:#111827
    classDef ext fill:#ede9fe,stroke:#7c3aed,color:#111827
    class ST,IN,MV,TH,ME,INTL,ESG,CO,PO,EARN,SD skill
    class FIN,LEDGER data
    class EA agent
    class IV brief
    class E1,E2,E3,E4 ext
```

*Blue = skills · green = data sources & stores · amber (dashed) = agents · pink = evidence outputs · violet = suite handoffs.*

<!-- standalone-install:start -->
## Installation

This standalone distribution is published as **HH-healthcare-equity**; the plugin inside keeps its suite id `healthcare-equity`. Two ways to install — **pick one**, not both (both distribute the same plugin under the same name):

**Standalone (this repo):**

```shell
/plugin marketplace add <your-github-username>/HH-healthcare-equity
/plugin install healthcare-equity@HH-healthcare-equity
```

**As part of the five-plugin suite (recommended if you want the full evidence→investable-view chain):**

```shell
/plugin marketplace add <your-github-username>/claude-healthcare-analyst-suite
/plugin install healthcare-equity@healthcare-analyst-suite
```

Updates: `/plugin marketplace update HH-healthcare-equity` (standalone) or `/plugin marketplace update healthcare-analyst-suite` (suite). If you switch sources later, uninstall the plugin first, then remove the old marketplace.
<!-- standalone-install:end -->

## Setup

- **No MCP servers by design** — this plugin consumes the engines' connectors (install all five together), the Quartr connector for transcripts/filings, and web/EDGAR. Optional depth layer: the Rhizome AI connector for FDA/EMA primary-document research (routed via the CLAUDE.md connector map); the breadth-vs-depth buying taxonomy lives in `references/data-stack-map.md`.
- Excel builds hand off to model-builder / financial-analysis; earnings model updates to earnings-reviewer.
- Uninstall the old `healthcare`, `cms-coverage`, `npi-registry`, and deprecated `pubmed` plugins after installing the suite.

## Usage

Say what you'd say to a junior analyst: "initiate on [TICKER]", "preview the print", "build the rNPV", "steel-man my short case", "screen for hidden compounders", "prep my 1-on-1", "run the quarterly scorecards", "map the EU HTA path", "draft the IC memo" — or "**build the investable view for [TICKER]**" to run the capstone end to end.

## Smoke test

Ask: **"Run the sell-discipline scorecard on [TICKER]; here is my thesis: …"** — pass: six 0–3 scores with the banded verdict and a confidence score. Then ask: **"Build the investable view for [TICKER]"** — pass: five layer briefs (or declared skips) with openable citations, a scenario set whose probabilities sum to 1.00 with a ≥5% unknown-unknown residual, and the template sentence with a dated catalyst and falsifier.
The universal pass condition, per the suite contract: an output must **move a model variable with an openable citation** — an output that merely informs, or cites without resolving, fails.
