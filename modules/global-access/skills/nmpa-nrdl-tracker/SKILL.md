---
name: nmpa-nrdl-tracker
description: >
  This skill should be used when the user asks about "China approval", "NMPA", "CDE",
  "NRDL", "China reimbursement", "China licensing deal", "BIOSECURE", "out-licensing
  from China", or is assessing China revenue or China-origin asset value. Anchors
  prompt-library ID INTL-03.
metadata:
  version: "0.1.0"
  layer: "Regulatory"
---

# China NMPA and NRDL tracker

Track Chinese regulatory and reimbursement events, and the licensing flow that has made
China-origin assets a global pricing input.

## Workflow

1. **Track the regulatory pipeline.** NMPA approvals, CDE breakthrough therapy
   designations, priority-review listings and IND acceptances. Since China's ICH
   accession the process has converged substantially on international norms, and IND
   timelines in particular have shortened materially.
2. **Track NRDL.** The National Reimbursed Drug List negotiation runs on an annual
   cycle, typically concluding late in the year with the new list effective from the
   following January.
   - **Model both sides.** Negotiated price reductions in recent cycles have commonly
     been reported in the range of roughly half of list price, in exchange for
     nationwide reimbursement, with subsequent volume increases that have frequently
     been several-fold within the first year. The net revenue effect is often positive.
     A brief that reports only the price cut is misleading.
   - Note the separate commercial insurance and self-pay channels, and the provincial
     supplementary lists, which cover part of the gap for products not on the NRDL.
3. **Track volume-based procurement (VBP)** for off-patent molecules and, increasingly,
   for devices and diagnostics. VBP is a much harsher mechanism than NRDL negotiation
   and the price outcomes are severe. For any name with a mature China portfolio this is
   the larger risk.
4. **Assess the licensing flow, which is now the bigger investment question for many
   desks.** China-origin assets are being out-licensed to Western developers at scale.
   For each relevant deal, extract: upfront, total biodollars, geographic split,
   development stage, and — most importantly — what the deal implies about the price of
   comparable assets. This flow is a direct valuation input for Western biotechs whose
   pipelines compete with a cheaper, faster source of clinical-stage assets.
5. **Overlay the policy risk.** BIOSECURE-type legislation, export controls and data
   restrictions affect both the CRO/CDMO supply chain and the licensing flow itself.
   Track the legislative status rather than the commentary, and be explicit that this is
   a policy variable with a wide outcome range rather than a base case.
6. **Verify against the primary source.** NMPA, CDE and chinadrugtrials.org.cn publish
   in Chinese. English secondary coverage is often delayed and sometimes wrong on
   specifics. Cite the original and flag translation.
7. Emit the brief.

## Not-automatic

An NRDL price cut does not license a revenue cut, and an NMPA approval does not license
a revenue start without the reimbursement route. A licensing deal headline number does
not license a valuation read-across without the stage, geography and structure.

Reference: `references/china-mechanics.md`. Contract: `../../references/evidence-brief.md`.
