---
name: adcom-label
description: >
  This skill should be used when the user says "prep the AdCom for [asset]", "what will
  the advisory committee vote", "analyze the approved label", "label delta vs
  expectations", or within 48 hours of an FDA/EMA approval when exact label language
  drives peak sales and payor reception.
metadata:
  version: "0.1.0"
---

# AdCom Prep & Label Delta

Two connected event workflows: prepare for an FDA advisory committee, and dissect an approved label against expectations.

## AdCom preparation

1. Gather primary materials via web research: the FDA briefing documents (usually posted ~2 days ahead), panel roster, draft questions, and class precedent votes. Use PubMed for the pivotal publications the panel will discuss.
2. Run SUB-BIO-02 (in `${CLAUDE_PLUGIN_ROOT}/skills/adcom-label/references/prompts.md`): expected discussion topics → panel composition and voting history → three likely FDA questions and vote split → stock-impact mapping → positioning.
3. Distinguish what an AdCom decides (advice on specified questions) from what it signals (FDA's areas of concern, revealed in the briefing book's framing). The briefing document's tone is often the tradable information before the vote.

## Post-approval label delta (within 48 hours of approval)

1. Pull the official label, approval letter, and posted review documents from Drugs@FDA — never FDALabel for exact language (search index only, per `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`).
2. Run SUB-BIO-08 (same references file): expected vs actual label side-by-side (indication scope, line of therapy, population subsetting, dosing, monitoring, boxed warnings, contraindications, PMCs/PMRs) → commercial unlock → commercial restriction (REMS, specialty channel, prior-auth burden, step therapy) → peak-sales model delta with per-element sensitivity → post-marketing overhang → precedent implications.
3. Route the restriction elements to companions: coverage/prior-auth implications → cms-reimbursement coverage-check; eligible-population resizing → procedure-exposure epi-funnel-input; CDx coupling → device-diligence (SUB-TLS-05).
4. Per the label translation row (references/evidence-translation-clinical.md): a broader label moves eligible population, launch timing, and commercial claims — it does **not** automatically move coverage, physician adoption, or paid demand.
5. End with the EVIDENCE BRIEF block (layer: regulatory); send model deltas to healthcare-equity model-valuation.

## Pre-decision approval-odds checklist (before any PDUFA/decision date)

Score the pending application against `${CLAUDE_PLUGIN_ROOT}/references/crl-risk-rubric.md`: the eight deficiency categories (CMC most common; facility/CGMP cited in ~12 of 20 sampled CRLs) and the named red flags — subgroup rescue, Hy's Law case counts, ex-US-heavy pivotal data, MTD-only oncology dosing, late CMC qualification, PPQ status, and named-facility enforcement state (commission the quality-signals skill for the facility axis). Anchor the prior on the pathway base rate (`base-rates.md`), adjust with named precedents (precedent-pack skill), and output: per-category verdict → CRL-probability adjustment → the 1–2 falsifiers to watch → EVIDENCE BRIEF. For approved-but-conditional assets, track FDORA confirmatory status and **ODAC scheduling as the withdrawal lead indicator**.

## Label-delta monitoring (prescribing-information supplements as signal)

Track PI/label supplements for covered and competitor products via Drugs@FDA supplement histories and DailyMed SPL version diffs (Rhizome connector for document depth when installed). Two signal classes: **cadence** — supplement frequency as a franchise-productivity KPI (the Dupixent pattern: ~15 supplements in 48 months ≈ a new indication every ~6 months; route the KPI to healthcare-equity earnings trackers); and **language deltas** — competitive and safety intelligence in the diff (the Ozempic pattern: removal of exclusive needle-compatibility language = third-party device-entry signal; new postmarketing AEs = pharmacovigilance trajectory). Shelf-life and device-change supplements are PAS-only and therefore dated, tradable events (see `${CLAUDE_PLUGIN_ROOT}/references/combination-products.md`). Emit material deltas as EVIDENCE BRIEFs; the readout-watcher agent runs this sweep on schedule.
