---
name: epi-funnel-input
description: >
  This skill should be used when the user asks to "build the patient funnel for
  [indication]", "size the addressable population", "epi inputs for the rNPV/TAM",
  "prevalence and incidence for [disease]", or needs the disease-burden top of a
  revenue model.
metadata:
  version: "0.1.0"
---

# Epidemiology Funnel Input

Build the code-anchored disease-burden top of the patient funnel — the defensible input to TAM and rNPV work.

## Workflow

1. Define the indication in code terms via the ICD10 Codes connector: the ICD-10-CM family and the clinically relevant subsets (severity, line-of-therapy, biomarker restrictions the label imposes — pull exact label language from clinical-catalysts adcom-label when a label exists). The code definition disciplines the epidemiology search and later lets claims data validate the estimate.
2. Assemble prevalence/incidence from graded sources via PubMed connector and web research: national surveillance (CDC/registries) > published epi studies > society estimates > company decks (label company TAM claims as claims-to-test, not inputs). Time-stamp and geography-stamp every figure; US vs global funnels are separate builds.
3. Construct the funnel explicitly, one conversion per line with its source: population → prevalent/incident cases → diagnosed (diagnosis rate is the classic overestimate — seek claims-based validation) → treatment-eligible under the actual/expected label → presenting to the relevant specialty (link provider-adoption's footprint as the capacity check) → realistic peak-penetration band anchored on analog launches. Show ranges, not points, where sources disagree.
4. Sanity-check against observed reality: does the implied treated population reconcile with current claims volumes (procedure-volume-tracker) and reported patient counts of incumbents? An epi funnel that implies more treated patients than the claims data shows is wrong at the diagnosis or presentation step — reconcile before shipping. This is the THM-02 bottoms-up discipline (the full TAM prompt lives in healthcare-equity screen-themes; this skill produces its healthcare-specific top).
5. State what the funnel does not prove (funnel-discipline reference): disease burden is a ceiling, not demand; eligibility is not paid demand.
6. End with the EVIDENCE BRIEF block (layer: commercial-volume/exposure). Hand the funnel to healthcare-equity model-valuation (MOD-03 rNPV patient funnel) with every conversion assumption exposed for scenario work.
