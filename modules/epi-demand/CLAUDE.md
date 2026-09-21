# epi-demand — standing instructions

**Layers covered:** Commercial (TAM, epidemiology) + Competitive.
**Connector:** none hosted for CDC or NIH. ChEMBL and bioRxiv/medRxiv are already
connected elsewhere — reference them, never re-declare.

## What this engine is for

The denominator. Peak-sales estimates live or die on the addressable-population funnel,
and most sell-side funnels are built from a single secondary source with no diagnosis
or treatment rates attached.

## The discipline this engine enforces

**Prevalence is not the market.** The chain from disease to revenue has at least six
multiplicative steps, and each one is an assumption that must be sourced separately:

```
incidence or prevalence
  → diagnosed (the largest and most-ignored haircut in most diseases)
  → meets label / eligible (biomarker, line of therapy, severity, age)
  → treated (some diagnosed patients are never treated)
  → treated with THIS product (share)
  → duration and adherence (persistence, discontinuation, dose)
  → net price per patient-year
```

A funnel that skips the diagnosis rate overstates the market by a factor that in some
diseases exceeds three. State every step with its own source and its own confidence,
and show the peak-sales sensitivity to the two weakest steps.

## Data caveats to carry

- **CDC WONDER** is mortality, natality and some incidence data; the API accepts an XML
  POST with no authentication, but sub-national queries are restricted through the API
  even where the web interface allows them.
- **SEER** publishes free aggregate cancer incidence, prevalence and survival;
  microdata requires a data-use agreement. Aggregates are enough for a funnel.
- **FluView, NREVSS and wastewater** are weekly, provisional and revised, with voluntary
  laboratory participation that changes over time. A change in reporting coverage looks
  exactly like a change in disease activity.
- **NIH RePORTER** is grant obligations, not equipment purchases — a leading indicator
  with a long and variable lag.

## Chaining

a procedure-exposure engine (this engine supplies the epidemiology, that
one supplies the coded procedure volume) · `evidence-catalysts` → guideline-inclusion
(a screening recommendation changes the *diagnosed* step, which is where guideline
changes actually move a market) · `rx-utilization` (observed volume against the funnel's
predicted volume — the single best test of whether a funnel is right) ·
your view layer → model-valuation.
## Connector

Declares **`wonder`** (`hesscl/wonder-mcp`) for CDC WONDER. Chosen over the
alternatives because it returns the exact request XML plus replication scripts with
every query, which is what makes a mortality figure defensible in a research file
months later.

**PopHIVE** (Yale's harmonised US surveillance data) is an *account-level* connector in
the directory, authless, one click. It covers respiratory surveillance well enough to
carry most of `respiratory-surveillance` and is fresher than the scripted path. Connect
it at the account, not here.

**Hard constraint on WONDER — the API is national-only.** CDC blocks grouping or
filtering by state, county, MSA, census region and urbanisation server-side. This is
not a limitation of the server or of our script. Any sub-national demand work must come
from CDC PLACES or the Delphi Epidata API instead. `cdc_wonder.py` now rejects
sub-national group-by codes up front rather than letting CDC return an opaque
permissions error.

Counts under 10 come back suppressed. Never sum suppressed cells — the sum of a
suppressed set is not zero, and treating it as zero manufactures a clean trend.

## Standard of evidence

This engine is built to **institutional investor standards: rigorous and auditable.**
That is a claim about specific mechanisms, and the full list is in
`references/auditability.md`. The load-bearing ones:

- Every finding carries a source, a retrieval date and the **vintage of the underlying
  data** — a different and usually much earlier date.
- Confidence is gated by vintage, not by conviction.
- Scripts fail loudly on empty result sets. Silence is never a negative finding.
- Known limitations travel with the number, in-line, not in a footnote.
- Evidence and view stay separated. This engine does not issue recommendations.

## Desk conventions (all engines)

- **One connector, one plugin — for plugin-level servers only.** A self-hosted
  stdio server is declared in exactly one plugin's `.mcp.json`; co-installed
  plugins share every server session-wide, so a second declaration buys a
  duplicate process, not extra capability. **Account-level hosted connectors are
  different**: CMS Coverage, PopHIVE, ClinicalTrials.gov, PubMed, ChEMBL,
  bioRxiv and Scholar Gateway are connected once in the directory and are visible
  to every plugin. Plugins reference those; they never declare or own them.
  Full map in `references/mcp-setup.md`.
- **MCP for the analyst, scripts for the watcher.** Both paths ship in every
  plugin and they are not redundant. Interactive query refinement goes through
  the server; unattended scheduled evidence goes through the script, because a
  watcher has to be deterministic and re-runnable against the same vintage.
  Where the two disagree, the script wins for anything entering a brief — you
  cannot cite the internals of a third-party server.
- **Engines produce evidence, not views.** An engine skill ends at the brief. The
  your view layer is the only place a position
  is argued. Do not write a recommendation into an engine output.
- **Open data only.** Every input here is free and public. If an analysis needs
  IQVIA, Symphony, Definitive, EvaluatePharma or Citeline, say so and stop — do
  not silently substitute a proxy for the paid panel and present it as equivalent.
- **Cite the vintage every time.** See `references/evidence-brief.md`.
- **Chain, don't duplicate.** These eight engines cross-reference each other by
  name. Anything outside them — valuation models, single-name research, the
  portfolio view layer — is chained into, never reimplemented here. An engine
  that starts doing valuation has stopped being an engine.
- **Scripts are stdlib-only Python 3.** No pip installs. Every script takes
  `--help`, prints JSON or CSV to stdout, and fails loudly on an empty result set
  rather than returning silence that reads like a negative finding.
