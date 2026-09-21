---
name: procedure-volume-tracker
description: >
  This skill should be used when the user asks "are [procedure] volumes growing or
  recovering", "procedure volume trends for [category]", "utilization trend behind
  [TICKER]", "track surgical/diagnostic volumes", or needs the volume evidence behind
  a medtech, provider, or diagnostics thesis.
metadata:
  version: "0.1.0"
---

# Procedure Volume Tracker

Track code-keyed procedure volumes and triangulate the utilization trend behind a name or category.

## Workflow

1. Fix the code set first (from exposure-map, or build it): the CPT/HCPCS and DRG codes that define the procedure/category, with the ICD-10 dx families that gate them (ICD10 Codes connector). Record the set with the output — comparability depends on it.
2. Run the SUB-MED-01 prompt (in `${CLAUDE_PLUGIN_ROOT}/skills/procedure-volume-tracker/references/prompts.md`): claims-data trend → hospital operator commentary → site-of-service shift → capacity constraints → 4-quarter forward outlook → leveraged names. Benchmark against the industry's ~3–5% procedure-volume growth anchor.
3. Sources, each labeled with universe and vintage: CMS public utilization files (Medicare FFS — annual, lagged; state both), hospital operator prints and transcripts (HCA/THC/UHS as the fastest quarterly read — cross-read via healthcare-equity earnings SUB-SVC-01), device-maker procedure disclosures (e.g., robotics procedure counts), and society/registry publications via web research. Reconcile disagreements explicitly rather than averaging.
4. Decompose the trend: volume vs acuity/mix vs site-of-service migration (HOPD→ASC repricing the same case — pull payment context from cms-reimbursement) vs backlog/recovery effects. Name which component the thesis actually needs.
5. Apply funnel discipline (`${CLAUDE_PLUGIN_ROOT}/references/funnel-discipline.md`): performed procedures are not paid procedures are not revenue — state the stage observed, and for diagnostics use paid tests × cash contribution, never ordered tests.
6. End with the EVIDENCE BRIEF block (layer: commercial-volume). Feed utilization deltas to healthcare-equity model-valuation (razor-blade and capex-cycle models) and pair with provider-adoption's capacity evidence before concluding demand inflection.
