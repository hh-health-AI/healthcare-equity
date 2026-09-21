---
name: nih-reporter-endmarket
description: >
  This skill should be used when the user asks about "NIH funding", "RePORTER",
  "academic end market", "research budgets", "tools demand", "instrument placements",
  "capex cycle for tools", or is modelling a life-science tools or reagents company's
  academic exposure. Anchors prompt-library IDs MOD-06 and SUB-TLS-02.
metadata:
  version: "0.1.0"
  layer: "Commercial"
---

# NIH RePORTER end-market read

Read federal research funding as a leading indicator of life-science tools and reagents
demand, with the lag structure made explicit.

## Workflow

1. **Pull the funding series** (`scripts/nih_reporter.py`) by fiscal year, split by:
   - **Institute** — NCI, NIAID, NHGRI and NIGMS have very different equipment intensity.
   - **Activity code** — this is the important cut. R01s fund consumables and reagents;
     **S10 shared-instrumentation grants fund capital equipment directly** and are the
     cleanest open proxy for instrument demand; P30 and U54 centre grants fund core
     facilities, which are the largest single buyers of high-end instruments.
   - **Institution** — concentration in the top research universities and institutes.
   - **Text search** — the technology itself (single-cell, spatial, cryo-EM, long-read
     sequencing, mass spectrometry) to isolate a platform's academic pull.
2. **Distinguish obligations from outlays.** RePORTER reports awards. Money is spent
   over the grant period, so the demand effect is spread over years with a lag that is
   long and variable — typically one to three years for consumables, front-loaded for
   instrument grants.
3. **Watch the appropriations cycle separately.** The NIH budget is set in Congress;
   continuing resolutions, rescissions, indirect-cost-rate policy changes and shutdowns
   affect actual spending regardless of what RePORTER shows about prior awards. Policy
   risk to the academic end market is not visible in the award data at all and must be
   tracked separately.
4. **Build the exposure map.** For a listed tools company, estimate academic and
   government revenue share from its own disclosures, then apply the funding trend only
   to that share. Pharma and biotech end-market demand moves on a completely different
   cycle — biotech funding conditions and pharma R&D budgets — and blending them
   destroys the signal.
5. **Cross-read the other end markets.** Biotech funding (venture and follow-on issuance)
   drives the biotech end market; `sec-forensics` can supply the issuance picture.
6. Emit the brief.

## Interpretation

- **S10 instrument grant counts** falling year over year is one of the earlier open
  signals of an academic capital-equipment downturn, and it typically precedes tools
  companies' own guidance revisions.
- Rising **total dollars** with flat **new award counts** means larger grants to fewer
  labs — consolidation into big centres, which favours high-end instrument vendors over
  broad-line consumables suppliers.
- A technology-specific text search with rapidly rising award counts identifies a
  platform in its academic-adoption phase, which typically precedes the clinical and
  commercial phase by several years.

## Not-automatic

Grant obligations do not license a revenue forecast. They set the direction and
approximate timing of one end market, which is usually a minority of a tools company's
revenue.

Framework anchor: Davies, *The $1,000 Genome* (project-KB; 2010 vintage, useful as
history of how sequencing demand cycles actually behaved, not as current data).
Contract: `../../references/evidence-brief.md`.
