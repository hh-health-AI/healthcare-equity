---
name: channel-check-prep
description: >
  This skill should be used when the user says "build an expert-call target list",
  "who should I talk to about [thesis]", "channel check plan for [TICKER]", "field
  diligence targets", or needs footprint data turned into a ranked human-diligence plan.
metadata:
  version: "0.1.0"
---

# Channel-Check Prep

Convert footprint and KOL-site data into a ranked, MNPI-safe human-diligence target list for expert calls and field checks.

## Workflow

1. Start from the thesis question — what claim needs human confirmation (adoption pace, usability friction, competitive displacement, reimbursement hassle, utilization reality) — and from footprint outputs (provider-footprint, site-adoption-tracker, kol-site-map) if available; run them first when absent.
2. Build the target list from the NPI Registry connector data: segment by role (evangelist KOL · high-volume community adopter · recent adopter · non-adopter/skeptic · former user) and by geography/site type. **Deliberately include non-adopters and churned sites** — confirmation-only lists are the classic channel-check failure.
3. Rank targets by information value: who can uniquely answer the thesis question × recency of direct experience × independence (trial investigators are informed but conflicted — label them). 8–12 targets with one line each: who, where, why them, the single question they can answer.
4. Frame the questions per usability/adoption drivers in `${CLAUDE_PLUGIN_ROOT}/references/usability-adoption-checklist.md` (workflow fit, training burden, staffing, economics at the site level) — these are the answerable, non-MNPI questions that predict adoption.
5. MNPI guardrail (non-negotiable): questions must stay within personal experience and general practice patterns — never solicit enrollment numbers in blinded trials, unreleased results, or confidential contract terms. Flag any question that skirts the line and rephrase.
6. Hand off execution to healthcare-equity meetings-experts (EN-01 call prep, EN-02 debrief, EN-03 network plan); this skill's product is the *who and why*, that skill's is the *how*.
7. End with the EVIDENCE BRIEF block only when the list itself embeds findings (e.g., footprint concentration discovered en route); otherwise deliver the ranked list with sources and dates.
