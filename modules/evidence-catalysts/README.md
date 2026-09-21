# evidence-catalysts

Guidelines, conferences and literature velocity.

| Skill | Moves | Sub-sector | Ease/Impact |
|---|---|---|---|
| `guideline-inclusion` | Adoption curve / uptake; coverage mandate | #biopharma #tools-dx #medtech | 3 / 4 |
| `conference-abstract-handicap` | Catalyst-trade setup; readout handicap refinement | #biopharma | 3 / 4 |
| `kol-citation-velocity` | Thesis validation on scientific momentum | #biopharma #tools-dx | 3 / 3 |

**Agent:** `guideline-watcher` — USPSTF and ACIP meeting calendars, NCCN updates,
conference embargo calendar.

**Data:** USPSTF recommendations · CDC ACIP meeting materials and votes · NCCN
(open-access with registration), ADA Standards of Care, ACC/AHA guidelines · conference
abstract portals (ASCO, ASH, AACR, ESMO, ACC, AHA, TCT, SABCS, ADA, EASL) · OpenAlex
and Crossref bibliometrics · bioRxiv/medRxiv and Scholar Gateway via existing connectors.

**Embargoes are compliance boundaries.** See CLAUDE.md.

## Standard of evidence

Built to **institutional investor standards: rigorous and auditable.** 
In short: every finding carries a source, a retrieval
date and the vintage of the underlying data; confidence is gated by vintage rather
than conviction; scripts fail loudly on empty result sets so silence is never read as
a negative finding; known limitations travel in-line with the number; and evidence
stays separated from view, because this engine issues no recommendations.

## Setup

Open-data endpoints rate-limit unidentified and shared User-Agents, and SEC EDGAR
blocks them outright, so your contact string is required rather than defaulted:

```bash
export HH_CONTACT="Your Name (you@example.com)"
```

## Author

HH-health-ai

## Disclaimers

Not affiliated with, endorsed by, or connected to CMS, HHS, the FDA, the SEC, the
USPTO, the CDC, the EMA or any other government agency. All data is retrieved from
public endpoints subject to those agencies' own terms.

Nothing here is investment advice, and no output should be read as a recommendation to
buy or sell any security. These engines produce evidence for a human analyst to weigh.

Optional MCP servers are independent third-party projects under their own licenses.
Review them before use.

## License

MIT — see [LICENSE](LICENSE).
