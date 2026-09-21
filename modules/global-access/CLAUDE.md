# global-access — standing instructions

**Layers covered:** Regulatory + Commercial (ex-US).
**Connector:** none. Nearly every source here publishes through HTML rather than a clean
API, so this engine runs on `page_snapshot_diff.py` plus disciplined reading.

## What this engine is for

Ex-US launch timing and ex-US price. For most large-cap pharma and medtech, roughly half
of revenue is ex-US, and it is systematically under-modelled because the sources are in
several languages, on several calendars, and behind no API.

## The three things that actually move numbers

1. **Timing.** Approval is not access. In several major markets the gap between
   regulatory approval and reimbursed availability runs one to two years, and it varies
   enormously by country. A model that starts ex-US revenue at approval is wrong by that
   gap.
2. **The reference-pricing cascade.** A low price agreed in one country propagates to
   every country that references it, and there are many. A single German or Japanese
   price decision can therefore reset a much larger revenue base than the local market.
   Never treat a country price as a local event without checking who references it.
3. **Volume-for-price trades.** China's NRDL is the clearest case: large negotiated
   price reductions in exchange for nationwide reimbursement, with volume increases that
   can more than offset. The net revenue effect can be positive even when the headline
   is a large price cut — model both sides or do not model it.

## Source caveats

- **NICE** — search nice.org.uk directly. Published work has found HTA aggregators miss
  a large share of NICE output; do not rely on an aggregator.
- **EMA** — CHMP monthly meeting highlights are the timely source; the EPAR follows.
- **G-BA / IQWiG** — the AMNOG benefit-assessment category drives the price negotiation
  that follows; the assessment, not the approval, is the financial event.
- **HAS** — the ASMR/SMR ratings play the same role in France.
- **Japan MHLW / Chuikyo** — NHI price listing, and price revisions on a cycle that has
  moved toward annual for many products; also special repricing rules for products whose
  sales far exceed forecast, which is a specific and repeated risk for successful launches.
- **China NMPA / CDE** — approvals, breakthrough designations and IND acceptances;
  NRDL negotiation results land in an annual cycle, typically announced late in the year
  and effective from the following January.

## Language

Japanese and Chinese sources are primary and are not always mirrored in English. Where a
finding rests on a translated source, say so in the brief and cite the original.

## Chaining

your view layer → international (this engine feeds it, and that skill owns the
view) and → model-valuation (ex-US revenue line) · a reimbursement engine (the US
comparison, and IRA international-reference-pricing debates) · a catalyst engine
(EMA and PMDA decisions are catalysts in their own right).

## Anchored prompt-library IDs

INTL-01 (European HTA Pathway Mapping) · INTL-02 (Japanese Reimbursement Cycle and Price
Revision) · INTL-03 (Chinese Biotech Licensing Economics and BIOSECURE Pass-Through).
## Connector

Declares **`ema`** (`openpharma-org/ema-mcp`) — EU approvals, EPARs, orphan
designations, PSUSAs, DHPCs, shortages.

**EMA approval is not EU market access, and the server only gives you the first half.**
No MCP exists for NICE, G-BA/IQWiG, HAS, SMC, AIFA, the Japanese NHI cycle or the China
NRDL, and the gap between authorisation and reimbursement is where this plugin earns
its keep — Germany grants access at authorisation while NICE, HAS and the others each
impose their own lag and their own evidence test. `hta_tracker.py` and
`page_snapshot_diff.py` carry all of it.

So: use the server to fix the regulatory anchor date, then use the scripts for
everything downstream of it. An EPAR date presented as an access date is the specific
error this plugin exists to prevent.

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
