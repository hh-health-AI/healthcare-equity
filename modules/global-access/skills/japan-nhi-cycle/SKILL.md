---
name: japan-nhi-cycle
description: >
  This skill should be used when the user asks about "Japan pricing", "NHI price",
  "Chuikyo", "MHLW", "PMDA", "Japanese reimbursement", "price revision", "foreign
  average price", or is modelling Japanese revenue for a pharma or medtech name.
  Anchors prompt-library ID INTL-02.
metadata:
  version: "0.1.0"
  layer: "Regulatory"
---

# Japan NHI cycle

Model Japanese price and volume through the NHI listing and revision machinery, which is
more mechanical — and therefore more forecastable — than most markets.

## Workflow

1. **Track the approval.** PMDA review and MHLW approval, then NHI price listing, which
   generally follows within a defined window after approval. Listing, not approval, is
   when revenue starts.
2. **Understand how the initial price is set.** Two routes:
   - **Similar efficacy comparison** — priced against a comparator drug, with premiums
     available for innovativeness, usefulness, marketability, paediatric use and orphan
     status. The premium categories are published and their criteria are explicit.
   - **Cost calculation** — used when no comparator exists.
   Then the **foreign average price adjustment** compares against a set of reference
   countries and adjusts toward that average, which is why the US and European prices
   feed directly into the Japanese one.
3. **Model the revisions, because they are the main event.** NHI prices are revised on a
   regular cycle and the direction is essentially always down. Model a recurring price
   decline rather than a flat price — a flat Japanese price line is a modelling error,
   not a conservative assumption.
4. **Watch the special repricing rules.** Products whose sales substantially exceed the
   forecast used at listing are subject to price cuts scaled to the overshoot. This
   creates the counter-intuitive result that a strongly outperforming launch in Japan
   triggers a larger price cut — a specific and repeated risk for successful products.
5. **Track Chuikyo.** The Central Social Insurance Medical Council deliberates and
   publishes materials on listings, premiums, repricing and system reform. Its published
   materials are the primary source and are in Japanese; cite the original.
6. **For medtech**, the functional-category reimbursement system works differently from
   drugs: devices are reimbursed within functional categories with their own revision
   cycle and foreign-price adjustment. Do not apply the drug rules to a device.
7. Emit the brief, noting where a finding rests on a translated source.

## Not-automatic

Japanese approval does not license a revenue start, and a listed price does not license
a stable price. Both the scheduled revision and the overshoot repricing must be in the
model.

Contract: `../../references/evidence-brief.md`.
