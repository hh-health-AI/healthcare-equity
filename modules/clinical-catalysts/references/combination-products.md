# Combination Products & Delivery-Format Changes — diligence reference

The device-format layer of drug theses (IV→SC conversions, autoinjectors, prefilled syringes/pens, on-body injectors). Sits under the suite case-library patterns C02 (Merck SC Keytruda) and C05 (argenx PFS). Seed patterns compiled Aug 2026 from secondary reviews of FDA combination-product decisions — verify at use.

## Why it moves models

Format changes move initiation, site of care, persistence, and servicing cost (evidence-translation "easier administration" row) — never efficacy or TAM by themselves. The regulatory evidence burden determines the *timing* and *probability* of those unlocks.

## The device-change gap analysis (four domains)

For any delivery-device change or self-administration claim, FDA expects a gap analysis across: **(1) Human factors/URRA** — critical tasks are severity-defined, not likelihood-defined; **(2) PK bridging** — 80–125% equivalence bounds; **(3) Clinical** — sometimes outcome data; **(4) CMC/EDDO** — essential drug delivery outputs, aging, shipping. The precedent ladder to place a change on:

- **User-invisible change** → near-zero evidence (Humira Pen s381 pattern).
- **Format conversion with PK bridge** → PK + HF validation typically suffice — but a PK bridge without HF has drawn CRLs (Kloxxado pattern).
- **New route/setting with outcome sensitivity** → clinical data required (Repatha device change carried Phase 3 LDL-C data).
- **Emergency-use products** → roughly double the evidence burden; reliability expectations reach 99.999%/95%-confidence sampling classes.

## Base rates & mechanics (as of Aug 2026 — verify at use)

- **Autoinjector/PFS BLA deficiencies:** essential-performance-requirement traceability flagged in ~10 of 12 recent BLAs; shelf-life and shipping-condition verification ~6 of 12; PPQ gaps ~4 of 12. Full verification reports (not summaries), 3-lot aged testing, ASTM D4169 preconditioning expected.
- **ISO 11608 is de facto mandatory** for assembled injection systems (11040 covers components only); device qualification adds ~6–12 months to programs that started late.
- **URRA revisions are routine, not exceptional** — DMEPA required revisions in ~10–11 documented cases 2021–24; revisions cascade into repeat HF validation (delay channel).
- **Shelf-life extensions are PAS-only** (prior-approval supplement — never CBE-30/annual report): approval precedes distribution, making extensions dated, tradable events.
- **Self-administration evidence norms:** HF validation n≈15–58/arm; supervised-first-dose labels common at launch (Dupixent pattern); actual-use home studies increasingly embedded in EU CTIS protocols; disposal errors an emerging FDA focus. Self-administration approvals have been *reversed* (EMA leuprorelin precedent) — persistence of the claim is itself a risk.
- **Part 4 cGMP:** drug-only dossiers get templated rejections — 820.20/820.30/820.100/820.50 content expected in Module 3.2.R; QMSR transition (ISO 13485 incorporation, effective Feb 2026) is the live compliance overlay.
- **E&L thresholds:** AET/SCT ~1.5 µg/day genotoxic, ~5 µg/day general (parenterals); ≥3 registration batches with leachables through shelf life; late E&L is a recurring CRL/PMC driver.

## Diligence checklist for a format-conversion thesis

1. Which rung of the evidence ladder does the change sit on, and does the sponsor's package match it?
2. Device qualification status (ISO 11608 verification after aging/shipping) and PPQ at filing?
3. URRA/HF validation done with representative users — or a revision-and-repeat risk?
4. Supplement type and its clock (PAS vs CBE-30) — does the model's launch date respect it?
5. Post-launch: MAUDE use-error trajectory (see quality-escalation-ladder.md) and servicing/complaint burden vs the persistence assumption.
6. Translate: conversion ≠ new patients (case C05 rule); chair-time/site economics are where the P&L moves (case C02 rule).
