---
name: guideline-inclusion
description: >
  This skill should be used when the user asks about "guidelines", "USPSTF", "ACIP",
  "NCCN", "compendia listing", "screening recommendation", "vaccine recommendation",
  "guideline catalyst", or wants to know whether a guideline change will move adoption
  or coverage for a product.
metadata:
  version: "0.1.0"
  layer: "Clinical"
---

# Guideline inclusion tracker

Track guideline-body decisions as dated adoption catalysts and translate them into
coverage and volume consequences.

## Workflow

1. **Identify the relevant body and the exact mechanism** for the product:
   - Preventive service or screening test → **USPSTF** (A/B grade triggers no-cost-share
     coverage under ACA §2713, generally effective for plan years beginning after the
     recommendation).
   - Vaccine → **ACIP** vote, then CDC director adoption, then the VFC resolution.
   - Oncology therapy or off-label use → **NCCN** category, because payers reference
     the compendia.
   - Chronic disease management → specialty society standards (ADA Standards of Care
     each January; ACC/AHA; GOLD; KDIGO), which move practice but carry no coverage
     mandate — a slower and weaker catalyst that is often over-modelled.
2. **Get the calendar.** These bodies publish meeting dates, draft-comment windows and
   publication schedules in advance. Draft recommendations are posted for public comment
   before finalisation, which usually gives one to three months of visibility on the
   likely outcome — the single most useful and least used feature of this catalyst class.
3. **Read the draft, not the rumour.** The draft's evidence statement and the comment
   volume tell you how contested it is. Monitor the page with
   `scripts/page_snapshot_diff.py` so a change is detected the day it happens.
4. **Trace the coverage consequence explicitly.** Which payer types are obliged, from
   which plan-year date, and with what cost-sharing change. Then hand it to
   a reimbursement engine → coverage-check for the Medicare position, which does not follow
   automatically from a USPSTF grade.
5. **Apply the governance-risk overlay.** State plainly that the 2025 disruption to
   ACIP and USPSTF composition weakened the mechanical reliability of this linkage, and
   handicap the coverage consequence accordingly rather than assuming it.
6. **Quantify through the funnel.** A screening recommendation acts on the **diagnosed**
   step of the `epi-demand` funnel, not on share. Re-run the funnel with the new
   diagnosis rate rather than applying a growth rate to revenue.
7. **Check the lag.** Guideline-to-practice change is slow and uneven: coverage changes
   at the plan-year boundary, clinician behaviour over quarters to years. Model a ramp,
   never a step, unless the mechanism is pure cost-sharing removal at a fixed date.
8. Emit the brief.

## Not-automatic

A guideline recommendation does not license a revenue step change. It licenses a change
to the coverage terms and to one specific step of the demand funnel, with a lag, and
now with governance risk attached.

Reference: `references/guideline-bodies.md`. Contract: `../../references/evidence-brief.md`.
