---
name: kol-citation-velocity
description: >
  This skill should be used when the user asks about "KOL", "citation velocity",
  "who are the key opinion leaders", "is the science gaining momentum", "publication
  trend for [target]", "bibliometrics", or wants evidence on the scientific trajectory
  of a mechanism, target or platform.
metadata:
  version: "0.1.0"
  layer: "Competitive"
---

# KOL and citation velocity

Measure the scientific momentum behind a target, mechanism or platform, and identify
the people whose opinion moves adoption.

## Workflow

1. **Define the concept precisely.** A target, a mechanism, a modality or a platform —
   not a company. Build a query with synonyms and, where OpenAlex supports it, concept
   identifiers rather than free text (`scripts/openalex_kol.py --concept "GLP-1 receptor"`).
2. **Trend publication and citation counts by year.** The useful measure is not volume
   but **acceleration**: second derivative of publications, and citations per
   publication in the first 24 months after appearance. A field entering rapid growth
   shows both rising.
3. **Segment by work type.** Reviews rising faster than primary research means a field
   consolidating rather than discovering — often a late-stage signal. Rising clinical
   trial publications relative to preclinical means translation is under way.
4. **Identify the authors.** Rank by first and last authorship on highly cited work in
   the last three years, not by lifetime citations, which just finds emeritus figures.
   Join to institution.
5. **Cross-link the KOLs to the commercial map.** Join the author list to trial
   investigators via a catalyst engine and to sites via
   a provider-adoption engine. An author list that overlaps heavily with one
   sponsor's investigator network tells you whose science it is.
6. **Check the preprint leading edge** through the connected bioRxiv/medRxiv server.
   Preprints lead journal publication by months and are the earliest visible signal
   of a field turning.
7. **Convert to a thesis statement.** Scientific momentum matters commercially when it
   precedes guideline change, competitive entry, or a platform's move from academic to
   clinical use. Say which of those the trend implies and on what horizon.
8. Emit the brief.

## Honest limits

Bibliometrics measure attention, not truth or commercial value. Fields with high
citation velocity and no viable clinical path are common. This skill is corroborating
evidence for a thesis built elsewhere — it should not carry a position on its own, and
a brief from this skill should say so.

Citation counts are also slow: a two-year lag between publication and citation
accumulation makes this a structural rather than a timely signal.

## Not-automatic

Citation velocity does not license a probability revision on any specific trial.

Contract: `../../references/evidence-brief.md`.
