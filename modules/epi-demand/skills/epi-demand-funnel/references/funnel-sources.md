# Open epidemiology sources, by question

| Question | Source | Access | Caveats |
|---|---|---|---|
| Cancer incidence, prevalence, survival by site and stage | SEER (SEER*Explorer) | free aggregate tables and XLSX; microdata under DUA | Registry coverage is a subset of the US population, scaled up; stage-shift over time is real and matters |
| Mortality by cause, age, geography | CDC WONDER | XML POST API, no key | Sub-national queries restricted through the API; suppression on small cells |
| Births and maternal characteristics | CDC WONDER natality | same | Useful for paediatric and obstetric funnels |
| Prevalence of chronic conditions, risk factors | NHANES, BRFSS | free downloads | Self-report bias in BRFSS; NHANES is examination-based and better but smaller |
| Dialysis and kidney disease | USRDS annual data report | free | Annual, comprehensive |
| Respiratory activity, in season | FluView, NREVSS, NWSS wastewater | weekly CSV / Socrata / Delphi Epidata | Provisional, revised, voluntary lab participation |
| Rare disease prevalence | Published registries, Orphanet, natural-history studies | literature | Wide ranges; always model a band, never a point |
| Procedure counts | Medicare utilisation files, HCUP where open | free / partly free | Medicare-only skews age; HCUP state files vary in openness |
| Diagnosis rates | Peer-reviewed literature; screening studies | PubMed, Scholar Gateway | The hardest step to source and the one most often skipped |

## Standard haircuts worth remembering

These are orders of magnitude to sanity-check against, not substitutes for a sourced
estimate:

- Diagnosis rates in chronic asymptomatic disease are frequently under 50%, and in some
  conditions far lower.
- Screening-detected disease populations move sharply when a guideline body changes a
  recommendation — this is the mechanism by which `evidence-catalysts` →
  guideline-inclusion moves a TAM, and it acts on the *diagnosed* step.
- Real-world persistence at 12 months in chronic oral therapy is commonly well below
  trial persistence; in some classes half of starters are off therapy within a year.
- Biomarker-defined subsets shrink further at the testing step: a biomarker present in
  30% of patients is only actionable in the share who are actually tested.

## The calibration loop

A funnel is a hypothesis. Post-launch, replace each step with an observation:

1. **Volume**: `rx-utilization` → sdud-trx-proxy and Part D.
2. **Breadth**: `rx-utilization` → partd-prescriber-share (writer count answers the
   diagnosis-and-treatment step better than any secondary source).
3. **Coded population**: a procedure-exposure engine → exposure-map.
4. **Testing rates** for biomarker-gated products: literature plus company disclosure.

Re-emit the funnel brief each time a step is replaced by an observation, and state
which steps remain assumptions.
