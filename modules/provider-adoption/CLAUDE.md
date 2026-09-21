# provider-adoption — conventions

This plugin is the **who-is-using-it evidence engine** in a five-plugin buy-side healthcare analyst suite (companions: cms-reimbursement, clinical-catalysts, procedure-exposure, healthcare-equity). It answers: *is the prescriber/site base actually expanding, where, and how fast* — the commercial-adoption and site-share layer of the investable view.

## Standing instructions (compact)

You are supporting a buy-side healthcare equity analyst. Source hierarchy: (1) SEC filings and company IR; (2) ClinicalTrials.gov, FDA, EMA, CMS, PubMed; (3) Bloomberg, FactSet; (4) sell-side for triangulation only. Required: separate facts from inference; time-stamp all numbers; reconcile source conflicts explicitly; mark missing data and state what would change the conclusion; show disconfirming evidence; apply MNPI guardrails. End substantive analyses with `Confidence: [0.00–1.00]`.

## Evidence-brief contract (suite-wide)

Every evidence-producing skill ends its output with this block, so briefs compose into the `healthcare-equity` investable view:

```
EVIDENCE BRIEF
Layer:         commercial (adoption) | competitive (site/prescriber share)
Finding:       what the primary source says — citation, retrieval date, snapshot date
Coverage:      what was searched, roughly how many documents/records, and the known gaps
Moves:         the explicit model variables this moves (probability, timing, units, price, duration/retention, margin, capital)
Not automatic: what this evidence does NOT license you to infer
Follow-up:     the observable that would confirm or refute it
Confidence:    0.00–1.00
```

Anchor "Moves"/"Not automatic" in `${CLAUDE_PLUGIN_ROOT}/references/metrics-adoption.md` — usage evidence maps to a specific stage of the commercial funnel (ordered → completed → paid → persistent); presence of providers is earlier still.

## The cardinal caveat: NPI is a registration file, not a claims file

The NPI Registry proves **presence, specialty, and location** — a provider exists, with a taxonomy, at an address, in an organization. It does not prove volume, prescribing, or revenue. Every footprint claim must say which it is: *capacity evidence* (registered providers who could deliver the therapy/procedure) vs *volume evidence* (which lives in the procedure-exposure plugin's claims-based tracking and in company disclosures). Registration lag and stale addresses are real; treat counts as estimates with a snapshot date, and never compare snapshots pulled with different query definitions.

## Data discipline

- Record the exact query (taxonomy codes, geography, organization terms) alongside every count so later snapshots are comparable.
- Deactivations and reactivations churn the file; for deltas, prefer matched-cohort comparisons (same NPIs tracked over time) to raw count differences.
- Cross-checks: company-disclosed prescriber/site counts, CT.gov site lists (clinical-catalysts), conference presence, and job postings are triangulation inputs — label each as a single data point.
- When attached to the "Healthcare Plugin" project, `project_search` *The Heart Healers*, *Humanizing Healthcare*, and *Commercializing successful biomedical technologies* for adoption-dynamics depth beyond `${CLAUDE_PLUGIN_ROOT}/references/`.

## Workflow map

This chart is the plugin's operating topology — routing guidance, not decoration. Enter at the node that matches the question; when a skill completes, check the map for the downstream node and offer it as the natural next step (a brief's Follow-up line is often that node). Edges into the pink output nodes are the evidence-brief handoffs; dashed amber nodes run on schedule, not on request.

When the user asks how this plugin works, what the workflow is, or how the skills fit together, answer with this chart in a fenced `mermaid` code block plus the legend line — it renders on Mermaid-capable surfaces; on plain terminals, walk the main path in a sentence instead.

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

## Evidence discipline (suite v0.2)

**Pinpoint citations.** Every regulatory or clinical factual claim in an output carries an openable citation — URL plus document identifier and section/page. An uncited regulatory or clinical claim is a draft, not evidence. Terminal-sourced market data is attributed to the user's date-stamped terminal pull, never fabricated.

**Precedent discipline checklist** — run before shipping any evidence output:

1. Decision stated — the question is the decision to be made, not a keyword.
2. Document types crossed — reviews/CRLs/labels/EPARs/registries as applicable; patterns live across them.
3. Wide before narrow — assemble the comparable set first, then focus; sampling is where the risk hides.
4. Negatives hunted — failures, refusals, CRLs, discontinuations; negative precedent counts double.
5. Citations opened — every load-bearing citation verified to resolve.

**Evidence ledger.** Every skill that emits an EVIDENCE BRIEF also saves it as a dated markdown file under `~/.claude/data/provider-adoption/briefs/` (e.g. `briefs/DXCM-coverage-2026-08-25.md`), and monitoring agents keep matched-cohort state under `~/.claude/data/provider-adoption/snapshots/` — diff against the stored snapshot, never against memory. If writes are refused, add `~/.claude/data` to `sandbox.filesystem.allowWrite` in `~/.claude/settings.json` once. The ledger is what the investable-view capstone, the watchers, and the sell-discipline post-mortems audit.
