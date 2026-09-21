# evidence-catalysts — standing instructions

**Layers covered:** Clinical + Competitive (adoption catalysts).
**Connectors:** none declared. bioRxiv/medRxiv, Scholar Gateway, PubMed and
ClinicalTrials.gov are already connected through other plugins — reference them, never
re-declare. OpenAlex and Crossref are open REST APIs called by the scripts here.

## What this engine is for

The catalysts that are *published on a calendar* and change adoption without any new
clinical trial: a guideline body adding a recommendation, an abstract dropping at an
embargo time, a body of literature reaching a tipping point.

These are the most systematically under-modelled catalysts on the buy side because they
do not appear on a company's own calendar.

## The mechanism that makes guidelines matter financially

For US-listed names the linkage is specific, not vague:

- A **USPSTF A or B grade** obliges most non-grandfathered private plans to cover the
  service with no cost sharing under ACA §2713 — the demand step change comes from the
  removal of patient cost sharing, not from clinician persuasion.
- An **ACIP recommendation** adopted by the CDC director drives both private coverage
  and the Vaccines for Children programme, which is a large share of paediatric volume.
- **NCCN category 1 or 2A** listing is the practical gate for oncology reimbursement,
  because CMS and most commercial payers reference the compendia for off-label use.

**Governance caveat, and it is material.** During 2025 the composition and independence
of both ACIP and the USPSTF were disrupted, which weakens the historical reliability of
the recommendation-to-coverage linkage. Do not model the linkage as mechanical any
more. Every brief touching USPSTF or ACIP must carry an explicit governance-risk line
stating that the coverage consequence is now conditional on the panel process holding.

## Embargo discipline

Conference abstracts are released at published embargo times. Working with material
before its embargo lifts is not a data-access question, it is a compliance question.
Never seek, accept or act on pre-embargo abstract content. Work from the published
release time forward, and record the release timestamp in the brief's vintage field.
Route any doubt to your view layer → comms-compliance.

## Chaining

a catalyst engine → catalyst-calendar and readout-handicap (this engine supplies the
abstract read; that one owns the trial handicap) · a reimbursement engine → coverage-check
(what a guideline change does to coverage policy in practice) · `epi-demand` →
epi-demand-funnel (a screening recommendation moves the *diagnosed* step) ·
a provider-adoption engine.
## Connector

**Declares nothing.** No MCP server exists for USPSTF, ACIP or NCCN, and none is
likely — guideline bodies publish documents, not APIs. Detection here is
`page_snapshot_diff.py` against published pages plus `openalex_kol.py` for citation
velocity.

That makes the snapshot diff load-bearing rather than incidental: it is the only
detector in the plugin. Keep the baselines under version control, and treat a page
restructure as an alert to re-baseline by hand, not as a guideline change.

The embargo rule in this plugin is not softened by any connector: conference abstracts
under embargo stay out of a brief until release, whatever surfaced them.

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
