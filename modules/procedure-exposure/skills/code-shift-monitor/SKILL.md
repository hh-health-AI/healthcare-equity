---
name: code-shift-monitor
description: >
  This skill should be used when the user asks "any new codes for [technology]", "did
  [product] get a Category I CPT / NTAP", "code changes affecting my names", "is the
  coding basis shifting", or wants coding milestones treated as early adoption and
  reimbursement signals.
metadata:
  version: "0.1.0"
---

# Code-Shift Monitor

Track coding-system changes as early, dated signals of adoption and reimbursement maturation.

## Why codes are signal

New technologies climb a coding ladder — unlisted/miscellaneous → temporary codes (Category III CPT, HCPCS C/G-codes) → permanent Category I CPT / dedicated ICD-10 codes with volume-based criteria — and each rung is a public, dated event that precedes broad reimbursement and screens-in claims trackability. Category I promotion requires demonstrated clinical use and evidence: the promotion itself is third-party validation of volume. Code retirements, redefinitions, and DRG reassignments similarly reprice or re-gate existing revenue.

## Workflow

1. Inventory the watched exposures (from exposure-map or the user): products on temporary codes, products billing unlisted codes, and mature code families where redefinition would matter.
2. Sweep the change surfaces via the ICD10 Codes connector (dx-side updates) and web research: annual ICD-10-CM/PCS updates (effective Oct 1), quarterly-to-annual CPT editorial actions (new Category I/III codes, effective dates), HCPCS updates, NTAP/TPT application and award cycles inside the IPPS/OPPS rules (coordinate with cms-reimbursement rule-cycle-calendar), and MedPAC/contractor coding guidance where relevant.
3. For each change: what changed · effective date · which names are exposed · the mechanism (new trackability, payment-path opening, repricing, gating) · direction and rough magnitude. Distinguish *signal* value (validation of adoption) from *economic* value (payment change — quantify with cms-reimbursement reimbursement-impact).
4. Translate honestly: a new code is access infrastructure, not demand — per funnel discipline, it moves the authorization/paid-conversion stage and trackability, not clinical adoption.
5. End with the EVIDENCE BRIEF block (layer: commercial-volume/exposure). Feed dated milestones to the suite catalyst calendar; recommend scheduling the code-update-watcher agent for standing coverage (annual Oct 1 window plus quarterly sweeps).
