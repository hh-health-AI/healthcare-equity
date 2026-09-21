---
name: provider-footprint
description: >
  This skill should be used when the user asks "how many [specialists] are there",
  "who could prescribe/deliver [therapy/procedure]", "addressable prescriber base for
  [TICKER]", "provider footprint by geography", or needs the capacity denominator for
  an adoption or TAM model.
metadata:
  version: "0.1.0"
---

# Provider Footprint

Size and map the provider base that could deliver a therapy, device, or procedure — the capacity denominator for adoption models.

## Workflow

1. Translate the clinical reality into taxonomy terms: which specialties (and sub-specialties) actually deliver this product — including realistic adjacent deliverers (e.g., NPs/PAs in the specialty, interventionalists vs general specialists) — and whether delivery is individual-provider or facility-gated (certification programs, capital equipment). Use `${CLAUDE_PLUGIN_ROOT}/references/npi-data-notes.md` for taxonomy mapping.
2. Query the NPI Registry connector: counts and lists by taxonomy × geography (state/CBSA as needed), individual (Type 1) vs organizational (Type 2) NPIs, and organization affiliations where relevant. Record the exact query definition with the results (mandatory for later comparability).
3. Structure the output: total base → distribution by geography → concentration (top states/metros, academic vs community skew) → the realistic *early-adopter subset* (e.g., specialists at centers matching the therapy's site requirements). Where facility-gating exists, count facilities separately from clinicians.
4. Cross-check against company-disclosed prescriber/account numbers and label the divergence: registered capacity is the ceiling; disclosed actives are penetration of it. Penetration = disclosed actives ÷ footprint is the useful adoption metric — show it when both numbers exist.
5. State limits explicitly (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`): presence not volume; registration lag; stale records. This brief is **capacity evidence** — volume lives in procedure-exposure.
6. End with the EVIDENCE BRIEF block (layer: commercial-adoption). Feed the denominator to healthcare-equity model-valuation (funnel top for rNPV/TAM via procedure-exposure epi-funnel-input) and the geography skew to channel-check-prep.
