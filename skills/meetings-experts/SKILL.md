---
name: meetings-experts
description: >
  This skill should be used when the user says "prep my 1-on-1 with management",
  "build a question stack", "site visit brief", "KOL day pre-read", "prep this expert
  call", "debrief the call", "plan my expert network arc", or "the expert contradicted
  management".
metadata:
  version: "0.1.0"
---

# Management Meetings & Expert Networks

Make every 30-minute slot and $1,500 expert hour earn its cost. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/meetings-experts/references/prompts.md`.

## Route by moment

| Moment | Prompt |
|---|---|
| Before a management 1-on-1 | MGMT-01 tiered question stack |
| Draft questions ready — dedupe vs public record | MGMT-02 already-asked filter |
| Before a site visit | MGMT-03 site visit brief |
| Before a KOL day / capital markets day | MGMT-04 pre-read |
| Before any expert call | EN-01 call prep brief |
| Within 24h after a call | EN-02 debrief & triangulation |
| Designing the 8-week expert arc | EN-03 scoping plan |
| Expert contradicts management | EN-04 divergence triangulation |
| Enterprise health-tech sales-cycle diligence | SUB-DIG-01 |

## Execution rules

1. **MNPI guardrails are structural, not decorative** (EN-01/EN-02 carry them verbatim): flag questions that could elicit material non-public information and rephrase to stay within public or general industry knowledge; audit debriefs for insights that appear to stem from non-public information and route them to compliance review, not the model. EN-04's rule: if the expert's information would be MNPI sourced from management, it cannot be acted on regardless of credibility.
2. Question stacks exclude anything with a public answer — run MGMT-02 against the last four transcripts and three conference appearances (Quartr connector) before finalizing MGMT-01's stack.
3. Target selection comes from the engines: provider-adoption channel-check-prep supplies ranked call targets and MNPI-safe usability questions; clinical-catalysts literature-kol supplies the KOL shortlist and their unique-answer questions.
4. Debriefs (EN-02) score credibility, log 1–2 surprises vs prior, and end in a thesis update — route the update into thesis (claim-level) and sell-discipline (watchlist signals). EN-04 divergences get the full protocol: specify the divergence dimension, credibility audit (recency/specificity/scope/consistency 0–3), management incentive audit, verification path, and pre-committed decision rule.
5. Every prep output includes what a *wrong* vs *right* answer looks like per question (EN-01's discipline) — otherwise the call cannot move a model variable.
