---
name: conference-abstract-handicap
description: >
  This skill should be used when the user asks about "ASCO abstracts", "ASH", "AACR",
  "ESMO", "late breaker", "abstract titles are out", "conference readout", "what does
  the abstract tell us", or wants to position around a conference presentation.
metadata:
  version: "0.1.0"
  layer: "Clinical"
---

# Conference abstract handicap

Extract signal from published abstract material at the moment the embargo lifts, and
convert it into a probability revision on the full readout.

## Embargo rule, before anything else

Work only with material that has been publicly released. Never seek, accept or act on
pre-embargo content. Record the release timestamp in the brief. If a source's provenance
is unclear, stop and route to your view layer → comms-compliance.

## Workflow

1. **Work the title-release stage first.** Most large conferences release titles before
   full abstracts. Titles alone carry real information:
   - **Presentation slot**: oral > rapid oral > poster discussion > poster. Slot is
     assigned by the scientific committee on perceived importance and is one of the
     cleanest early signals available.
   - **Late-breaker status**: data arrived after the deadline, which usually means an
     event-driven analysis read out. Neutral in direction, high in variance.
   - **Title wording**: a title stating a result ("improves overall survival") versus
     one stating a design ("a study of X in Y") is informative. Companies generally do
     not put a negative result in the title.
2. **At abstract release, read the design before the numbers.** Apply the trial-reading
   checklist in `references/abstract-checklist.md`: population, comparator, primary
   endpoint, statistical plan, and — critically — whether the reported analysis is the
   pre-specified primary or something else.
3. **Check the data cut-off date** against the trial's expected event accrual. An early
   cut-off with immature survival data is the most common way an abstract looks better
   than the eventual full dataset.
4. **Anchor on base rates before adjusting.** Start from published phase-transition
   probabilities by phase and therapeutic area (BIO/Informa/QLS; Wong, Siah and Lo),
   then adjust for what the abstract shows. Analysts systematically over-update on
   abstract-level detail; the base rate should still be doing most of the work.
5. **Handicap the presentation.** The abstract is a subset. Name specifically what will
   be shown live that is not in the abstract — subgroup analyses, updated cut-off,
   safety detail, quality-of-life data — and what each would have to show to change
   the view. That list is the actual deliverable.
6. **Position the trade shape, not the direction.** Conference readouts are variance
   events. State the historical move distribution for this name around this conference,
   and note whether the setup argues for an options expression.
7. Hand the probability revision to a catalyst engine → readout-handicap and emit
   the brief.

## Not-automatic

An abstract does not license a conclusion about the full dataset. Abstracts are
prepared months ahead, from an earlier data cut, and are edited by sponsors.

Reference: `references/abstract-checklist.md`. Contract: `../../references/evidence-brief.md`.
