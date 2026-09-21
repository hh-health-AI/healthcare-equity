# Regulatory Base Rates

Anchors for handicapping and catalyst dating. **Always scope the rate** (phase, indication, modality, pathway, era) and prefer indication-specific rates when available. Seed figures below were compiled Aug 2026 from secondary regulatory-intelligence reviews of primary FDA/EMA records — tag them `(as of Aug 2026 — verify at use)` in outputs and update from primary sources when they drive a decision.

## Clinical phase-transition anchors

The library's working anchors: **~70% of Phase 2 and ~50% of Phase 3 trials fail to meet primary endpoints** — use indication-specific rates where available (BIO/PhRMA-style phase-transition studies).

- Decompose PoS explicitly: **technical × regulatory × commercial** (INIT-06 discipline); quote each factor's basis.
- Phase 2→3 translation is the highest-loss step. Discount harder when: Phase 2 was single-arm or small-N; the Phase 3 endpoint differs; the effect size barely cleared powering; multiplicity was loose; the comparator strengthened since Phase 2 ran; or (post-Project Optimus, oncology) dosing was MTD-only with no randomized dose comparison.
- Upgrade cautiously when: validated mechanism in the indication; biomarker-selected population with large effect; agency engagement signals — noting the designation reality-check below.
- Direction-of-bias notes (verify current figures before quoting numbers): oncology historically below-average phase-transition success; biomarker-driven rare disease above; neuro/psychiatry below.

## Designation reality-check (as of Aug 2026 — verify at use)

**Designations are timeline evidence, never efficacy evidence.** Breakthrough Therapy compresses oncology development ~3.2 years (≈5.6 vs 8.8), but BTD drugs show **no efficacy edge** vs non-BTD comparators (response rates ~parity), with smaller pivotal trials (median n≈149 vs 326) and ~53% single-arm; grant rate runs ~35–47%; BTD associates with *lower* later withdrawal risk (OR ≈0.26). Fast Track = "potential"; BTD = "substantial improvement on preliminary clinical evidence"; RMAT = regen-med lower bar; Priority Review = 6 vs 10 months post-filing. Designations are rescindable — a downside-surprise channel. Re-price efficacy off trial design, not the label on the program.

## Review-timeline base rates (empirical medians; as of Aug 2026 — verify at use)

| Pathway | Median | Spread (IQR/notes) |
|---|---|---|
| 510(k) | ~128 days | ~70–228 |
| De Novo | ~299 days | ~170–423 |
| PMA (from filing) | ~252 days | ~180–520; panel-track >3 years |
| NDA priority / standard | ~240 / ~347 days | 60-day filing review precedes the clock |
| BLA priority / standard | ~243 / ~408 days | — |

Use the **mean–median gap** as the CRL/major-deficiency tail-risk flag: pathways with long right tails deserve wider catalyst date-windows.

## Regulatory-stage anchors

- Filing-to-approval success is high relative to clinical stages, but CRLs cluster on CMC/facility issues and single-country data packages — check FDA meeting history (SUB-BIO-07), facility status (quality-signals skill), and the CRL rubric (`crl-risk-rubric.md`) before assuming a clean review.
- **Accelerated approval:** FDORA requires confirmatory trials underway at approval; oncology verification median ~3 years; **ODAC scheduling is the months-ahead lead indicator of withdrawal risk**. Treat conversion to full approval as its own gated event.
- AdCom votes usually, not always, presage FDA action; divergences are informative. Track class precedent votes.
- **Meeting clocks (catalyst dating):** FDA Type A 30d · Type B 60d · Type B(EOP) 70d · Type C 75d · Type D 50d to meeting/response; written preliminary responses can collapse meetings (an acceleration signal). Ex-US: PMDA fee-bearing consultations; MHRA ~6-week EAMS; China CDE Type I/II/III at 3/10/20 working days.
- **China NMPA conditional approval:** ~36% of 2021 priority-review applications met conditional criteria; 2026 revisions tighten post-approval obligations — a sponsor filing a 3-month confirmatory-trial extension is the revocation early-warning (route to healthcare-equity INTL-03).

## Post-LOE erosion anchors (handoff to model work)

- Small molecules: **80–90% revenue loss within ~18 months** of generic entry.
- Biologics: **30–50% erosion over 3–5 years** (biosimilar dynamics vary with interchangeability, contracting, channel — SUB-PHA-05 in healthcare-equity; entry timing mechanics in its `loe-mechanics.md`).

## Discipline

Every probability in output shows: base rate used → scope → named adjustments (prefer named precedents via the precedent-pack skill over class averages) → final PoS. If the honest answer is a range, give the range. Reserve a non-zero unknown-unknown residual in any scenario set (MOD-10 rule).
