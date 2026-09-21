---
name: kol-site-map
description: >
  This skill should be used when the user asks "which trial sites became commercial
  accounts", "map the KOLs' institutions", "trial-to-commercial overlap for [TICKER]",
  "where are the centers of excellence", or wants influence-weighted geography for an
  adoption thesis.
metadata:
  version: "0.1.0"
---

# KOL–Site Map

Join the influence graph to the delivery map: which institutions ran the trials and publish the evidence, and how that overlaps the commercial footprint.

## Workflow

1. Build the influence list: trial investigators and sites from the Clinical Trials connector (search_investigators / trial locations for the asset's studies) and, where the clinical-catalysts plugin's literature-kol skill has run, its KOL shortlist; else pull key authors via the PubMed connector (both connectors ship with clinical-catalysts — this skill assumes the suite is co-installed).
2. Resolve people and institutions to NPIs via the NPI Registry connector (individual NPIs for the clinicians, organizational NPIs for their centers). Note ambiguities honestly (common names, multi-site affiliations).
3. Produce the overlap map: trial sites that are now commercial delivery sites (early-adopter conversion) · trial sites not yet converted (pipeline of likely next accounts) · commercial sites with no trial history (true diffusion beyond the evangelist base — the strongest adoption signal, per the S-curve reference).
4. Read the pattern per `${CLAUDE_PLUGIN_ROOT}/references/adoption-scurve-vignettes.md`: adoption still confined to trial centers = evangelist stage (fragile, KOL-dependent); spread into non-trial community sites = crossing into the mainstream. State which pattern the data shows and what would falsify it.
5. Flag competitive reads: rival assets sharing the same trial sites/KOLs (enrollment and mindshare competition — cross-reference clinical-catalysts pipeline-landscape).
6. End with the EVIDENCE BRIEF block (layer: commercial-adoption / competitive). Feed unconverted high-influence sites to channel-check-prep as priority targets, and the diffusion read to healthcare-equity thesis work.
