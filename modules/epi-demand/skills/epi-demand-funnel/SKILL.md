---
name: epi-demand-funnel
description: >
  This skill should be used when the user asks for "TAM", "addressable population",
  "peak sales", "epi model", "how many patients", "bottoms-up market size",
  "penetration assumption", or wants to build or stress-test the patient funnel
  underneath a revenue forecast.
metadata:
  version: "0.1.0"
  layer: "Commercial"
---

# Epidemiology demand funnel

Build the patient funnel underneath a peak-sales number, sourcing every step separately
and showing where the estimate is actually fragile.

## Workflow

1. **Fix the population base.** Incidence for acute or newly-diagnosed populations;
   prevalence for chronic ones. Getting this wrong is a first-order error: an incidence
   drug modelled off prevalence overstates by the disease duration.
   Sources: SEER for cancer, CDC WONDER for mortality and natality, NHANES and BRFSS
   for prevalence of chronic conditions, USRDS for dialysis, published registries for
   rare disease.
2. **Apply the diagnosis rate**, with a source. This is where funnels break. Many
   chronic diseases run diagnosis rates well below half. If no diagnosis rate is
   available, say so, use a range, and flag the funnel as unanchored at this step.
3. **Apply label eligibility.** Line of therapy, biomarker prevalence, severity
   threshold, age band, contraindications. Biomarker prevalence should come from the
   literature and, where available, from ChEMBL or genomic databases — not from the
   company's investor deck.
4. **Apply the treated rate**, then **share**, then **duration and adherence**.
   Persistence is the most commonly over-assumed variable in chronic therapy models;
   real-world discontinuation frequently runs far above trial discontinuation.
5. **Apply net price per patient-year**, taken from `rx-utilization` →
   gross-to-net-bridge rather than from list price.
6. **Show the sensitivity.** Identify the two steps with the widest ranges and tornado
   the peak-sales figure against them. The output the desk needs is not a point estimate
   but "peak sales is $2.1bn ± $900m, and almost all the variance is diagnosis rate and
   persistence".
7. **Cross-check against the coded procedure or claims view.** a procedure-exposure engine →
   exposure-map gives an ICD-10-anchored count. If the epidemiological funnel and the
   coded volume disagree by more than a factor of two, one of them is wrong and the
   funnel is usually the guilty party.
8. **Instrument it.** Name the observable that would confirm the funnel post-launch —
   typically SDUD or Part D volume at a stated month — and hand it to the watcher.
9. Emit the brief.

## Where funnels go wrong, in order of frequency

1. Skipping the diagnosis rate.
2. Prevalence used for an incidence-driven product.
3. Trial persistence applied to the real world.
4. Biomarker prevalence taken from the sponsor's deck.
5. Assuming the eligible population is the treated population.
6. Ignoring competitive share loss at the exact point of peak.

## Not-automatic

An epidemiological funnel does not license a revenue forecast on its own. Without an
observed volume series to calibrate against, it is an upper bound with a shape.

Reference: `references/funnel-sources.md`. Contract: `../../references/evidence-brief.md`.
