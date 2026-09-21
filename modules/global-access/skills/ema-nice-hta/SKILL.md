---
name: ema-nice-hta
description: >
  This skill should be used when the user asks about "EMA", "CHMP opinion", "NICE",
  "G-BA", "AMNOG", "HAS", "European launch", "HTA", "EU pricing", "reimbursement in
  Europe", or wants ex-US launch timing and price for a launching asset. Anchors
  prompt-library ID INTL-01.
metadata:
  version: "0.1.0"
  layer: "Regulatory"
---

# EMA and European HTA mapping

Map an asset from EMA opinion through national HTA to reimbursed price and date, per
major market.

## Workflow

1. **Establish the regulatory position.** CHMP opinion date (monthly meeting highlights
   are the timely source), then European Commission decision roughly two months later.
   Note any accelerated assessment, conditional marketing authorisation or orphan
   designation, each of which changes both the timeline and the later HTA reception.
2. **Then map HTA country by country**, because approval and access are different events:
   - **Germany** — free pricing on launch, then the AMNOG process: G-BA benefit
     assessment with IQWiG input, then price negotiation with the GKV-SV, with the
     negotiated price effective from a fixed month after launch. The **benefit category**
     is the financial event; a finding of no additional benefit forces reference pricing.
   - **England** — NICE technology appraisal, with the ICER threshold, the severity
     modifier, and confidential commercial arrangements. NICE timing relative to
     marketing authorisation is the practical determinant of NHS uptake.
   - **France** — HAS transparency committee, with SMR determining reimbursement rate
     and ASMR determining the price premium against comparators.
   - **Scotland** — SMC, faster than NICE and sometimes a leading indicator.
   - **Italy and Spain** — AIFA and the regional processes, both slower; model the lag.
3. **Build the access timeline** per country: approval date, HTA submission, HTA
   outcome, price agreement, first reimbursed sale. The gap between the first and last
   of these is the number the model needs and is routinely omitted from sell-side models.
4. **Trace the reference-pricing cascade.** Identify which countries reference the
   price being set. A German or French price feeds a long list of external reference
   pricing systems, so a national negotiation can reset a far larger revenue base.
5. **Read the comparator choice.** In both AMNOG and HAS the comparator selected by the
   authority determines the achievable price more than the trial data does. If the
   comparator is a cheap generic, the premium is capped regardless of efficacy.
6. **Watch the EU HTA Regulation joint clinical assessment**, which centralises part of
   the clinical assessment across member states — it changes the sequencing and the
   evidence requirements, and pricing remains national.
7. Emit the brief with per-country dates and price outcomes, and the cascade named.

## Not-automatic

A positive CHMP opinion does not license an ex-US revenue start date. Without the HTA
outcome and the price agreement, the revenue line has no date and no level.

Reference: `references/hta-mechanics.md`. Contract: `../../references/evidence-brief.md`.
