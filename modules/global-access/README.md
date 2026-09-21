# global-access

International HTA, pricing and approvals.

| Skill | Moves | Sub-sector | Ease/Impact |
|---|---|---|---|
| `ema-nice-hta` | Ex-US launch timing and price | #biopharma #medtech | 3 / 4 |
| `japan-nhi-cycle` | Japan price and volume | #biopharma #medtech | 2 / 3 |
| `nmpa-nrdl-tracker` | China revenue and licensing-deal read-through | #biopharma | 2 / 4 |

**Agent:** `access-watcher` — CHMP monthly highlights, NICE appraisal calendar, G-BA
and HAS publication dates, Japan NHI revision cycle, China NRDL cycle (Q4).

**Data:** EMA (CHMP highlights, EPARs) · NICE technology appraisals (search nice.org.uk
directly — aggregators are incomplete) · G-BA and IQWiG · HAS · Scottish SMC · Japan
MHLW and Chuikyo NHI price lists, PMDA · China NMPA and CDE, NRDL results,
chinadrugtrials.org.cn.

Most sources are HTML, so the workflow is snapshot-and-diff plus reading. Set up watch
targets with `scripts/hta_tracker.py --init`.

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
