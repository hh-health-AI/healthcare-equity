# cms-reimbursement

Access and payment evidence workflows for healthcare equity research. This directory is the flagship's integrated `cms-reimbursement` module; the [standalone source](https://github.com/hh-health-AI/cms-reimbursement) remains available.

Answers: **will Medicare pay for it, at what rate, and what is changing** — and converts the answer into model variables via a standard evidence brief that the `healthcare-equity` plugin assembles into an investable view.

Instructions organize source evidence and explicit model implications; their output requires researcher appraisal.

## Components

| Type | Name | Purpose |
|---|---|---|
| Optional connector | CMS Coverage | Medicare Coverage Database — NCDs, LCDs, coverage articles |
| Skill | coverage-check | Coverage status for a drug/device/procedure, cited to policy text |
| Skill | reimbursement-impact | CMS rule change → per-procedure dollar delta → revenue impact |
| Skill | ma-bid-cycle | MA rate notice / Stars → payor implications by name |
| Skill | drug-pricing-ira | IRA negotiation, Part D redesign, inflation-rebate exposure |
| Skill | rule-cycle-calendar | Standing CMS calendar as a catalyst feed |
| Agent | rule-watcher | Scheduled sweep of CMS release windows for covered names |

## Workflow

```mermaid
flowchart TD
    Q(["Is it covered? What does the rule do?<br/>MA cycle? IRA exposure? What's coming?"]) --> R{route}
    R -->|coverage status| CC["coverage-check<br/>NCD / LCD / MAC position<br/>+ REMS/ETASU friction"]
    R -->|rule to dollars| RI["reimbursement-impact<br/>rate delta → revenue delta"]
    R -->|MA rates & Stars| MA["ma-bid-cycle<br/>notice → issuer implications"]
    R -->|drug pricing| IRA["drug-pricing-ira<br/>negotiation & Part D exposure"]
    R -->|standing calendar| CAL["rule-cycle-calendar<br/>CMS release rhythm as catalyst feed"]

    MCD[("CMS Coverage connector<br/>Medicare Coverage Database")] --> CC
    FILES[("cms.gov rules &<br/>fee-schedule files")] --> RI
    FILES --> MA
    FILES --> IRA
    RW["rule-watcher agent<br/>scheduled sweep of release windows"] -.->|what dropped, who's touched| CAL

    CC --> TRIAD{{"discipline: coverage ≠ coding ≠ payment<br/>Medicare universe labeled"}}
    TRIAD --> BRIEF[/"EVIDENCE BRIEF<br/>regulatory (access) · commercial (payment)"/]
    RI --> BRIEF
    MA --> BRIEF
    IRA --> BRIEF
    BRIEF --> LEDGER[("evidence ledger<br/>~/.claude/data/cms-reimbursement/briefs/")]
    CAL -->|dated CMS events| CATS["clinical-catalysts<br/>suite catalyst calendar"]
    BRIEF --> HE["healthcare-equity<br/>model-valuation · investable-view · SELL-02 watchlists"]

    classDef skill fill:#dbeafe,stroke:#2563eb,color:#111827
    classDef data fill:#dcfce7,stroke:#16a34a,color:#111827
    classDef agent fill:#fef3c7,stroke:#d97706,color:#111827,stroke-dasharray:5 5
    classDef brief fill:#fce7f3,stroke:#db2777,color:#111827
    classDef note fill:#f3f4f6,stroke:#6b7280,color:#111827
    classDef ext fill:#ede9fe,stroke:#7c3aed,color:#111827
    class CC,RI,MA,IRA,CAL skill
    class MCD,FILES,LEDGER data
    class RW agent
    class BRIEF brief
    class TRIAD note
    class CATS,HE ext
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

Medicare Coverage Database research can use a supported CMS Coverage connector, public CMS policy pages or supplied policy files. Configure any connector in your actual host and verify its policy vintage; importing the aggregate instruction plugin does not create that connection.

Other evidence modules can be used when the research question needs them; installing all five original suite plugins is not required. Keep any useful existing integrations and configure only the tools your host supports. Review duplicate connector names in the host configuration if needed; no automatic uninstall or account-permission change is part of this setup.

The workflow diagram describes logical handoffs. Connector nodes, host-specific ledger paths and scheduled agents are configuration examples, not resources created by installing instructions. Use an explicit storage location supported by your host, and configure a monitoring schedule only when requested.

## Usage

- "Is TAVR / [device] / [drug] covered by Medicare?" → coverage-check
- "What does the OPPS final rule do to [TICKER]?" → reimbursement-impact
- "Walk the MA rate notice / bid cycle for [year]" → ma-bid-cycle
- "Map [TICKER]'s IRA exposure" → drug-pricing-ira
- "What CMS releases are coming?" → rule-cycle-calendar
- "Watch the CMS calendar for my coverage list" → schedule the rule-watcher agent

## Smoke test

Ask: **"Is transcatheter aortic valve replacement covered by Medicare, and under what conditions?"**
Pass: the answer cites NCD/LCD policy IDs with openable Medicare Coverage Database links, states the retrieval date and policy vintage, and ends with an EVIDENCE BRIEF (including the Coverage line). The brief must document a model implication (accessible population / paid conversion), not merely inform.
Fail: an answer without policy IDs, policy vintage or openable source links is not reviewable, regardless of the retrieval route.
