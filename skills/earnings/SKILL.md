---
name: earnings
description: >
  This skill should be used when the user says "preview the print", "build a KPI
  tracker", "live-call triage sheet", "post-print update for [TICKER]", "decompose
  the guide", "MLR bridge", "quarterly cash and catalyst refresh", "cross-read
  [peer]'s call", or anything in the healthcare earnings cycle.
metadata:
  version: "0.1.0"
---

# Earnings Workflows

The full earnings cycle — preview, live, post-print, and sub-sector quarterly reads. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/earnings/references/prompts.md`.

## Route by moment

| Moment | Prompt |
|---|---|
| Once per name (systematize the metrics) | EARN-02 KPI tracker build |
| T-7 before the print | EARN-01 earnings preview |
| On the call | EARN-03 live-call triage sheet |
| Within 24h of the print | EARN-04 post-print thesis update |
| Guidance issued/revised | EARN-05 guide decomposition & path-to-number |
| Within 60 minutes (internal flash) | COMM-03 quick-reaction note |
| Clinical-stage biotech quarter | EARN-06 cash & catalyst refresh |
| Payor quarter | EARN-07 managed-care MLR bridge |
| Pharma commercial momentum | SUB-PHA-03 TRx/NRx divergence monitor |
| Hospital operator reported | SUB-SVC-01 cross-read (medtech/pharma/payor implications) |
| Peer reported | SS-03 conference-call cross-read |

## Execution rules

1. Transcripts, releases, and filings come from the Quartr connector (or EDGAR/web); consensus figures from the user's terminal — request them, never invent them. Time-stamp every number with its reporting period (standing instructions).
2. Use the sub-sector metric definitions in `${CLAUDE_PLUGIN_ROOT}/skills/model-valuation/references/commercial-metrics.md` (NRx/TRx/NBRx, placements/installed base/pull-through, procedure volume/reorder/ASP, lives/MLR/PMPM) so KPI trackers use the right ladder per name.
3. Payor prints: normalize prior-period development before reading MLR (the managed-care discipline in model-valuation's references); biotech prints: distinguish gross from net burn (EARN-06's rule); hospital prints: read contribution per adjusted case, not revenue per case.
4. Route earnings-revealed evidence outward: coverage/rate commentary → cms-reimbursement; trial/timeline updates → clinical-catalysts; site/volume disclosures → provider-adoption / procedure-exposure. Pull their EVIDENCE BRIEFs back into EARN-04's model-impact section.
5. Verdict discipline in EARN-04: thesis pillar by pillar — confirmed / intact / weakened / broken — then action. Excel model updates hand off to the earnings-reviewer plugin.
6. Chain: EARN-02 (once) → EARN-01 → EARN-03 → EARN-04 → EARN-05 (if guided) → EARN-06/07 (sub-sector) → COMM-03.
