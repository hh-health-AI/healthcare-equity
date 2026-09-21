---
name: precedent-pack
description: >
  This skill should be used when the user says "build the precedent pack for [event/
  asset]", "what has FDA actually accepted for [endpoint/population]", "find the
  analogs for this readout/filing", "what happened to comparable programs", "CRL
  precedents in [indication]", or when any binary event needs named historical analogs
  instead of class-average base rates.
metadata:
  version: "0.1.0"
---

# Precedent Pack

Assemble the named historical analogs for a pending decision — readout, filing, AdCom, label, pathway choice — and use them to adjust base rates with precedents instead of class averages. Governing rule: **guidance is descriptive; decisions are precedential.** Seed maps: `${CLAUDE_PLUGIN_ROOT}/references/endpoint-precedents.md`, `base-rates.md`, `crl-risk-rubric.md`.

## Method (six principles — follow in order)

1. **State the decision, not the keyword.** Frame the question as the decision it serves: "can [endpoint] support approval in [population/line]?", "what evidence bar cleared for [modality] in [indication]?", "what stability/E&L package cleared for comparable [format]?" (CMC-benchmarking mode).
2. **Query across document types simultaneously.** Patterns live across sources, in this value order: **review packages/discipline reviews first** (they record the disagreement), then CRLs (failure precedent), approval letters/labels/PMRs-PMCs, EPARs/CHMP opinions, AdCom materials and votes, trial registry records, designation records, guidance last. Rhizome connector when installed (carry its citation URLs); else Drugs@FDA, EMA, ClinicalTrials.gov (via the Clinical Trials connector), openFDA, web.
3. **Go wide before narrow.** Target the comparable *set* (~20–30 programs where the record allows) before focusing on the closest 3–5. Sampling is where the risk hides; if the set is capped by effort, say what was excluded.
4. **Hunt negatives deliberately.** CRLs, refusals/NSEs, clinical holds, discontinued programs, withdrawn designations, failed confirmatory trials. Negative precedent counts double and is systematically under-surfaced — a pack with zero negatives is presumptively incomplete ("negatives: none found after search for X, Y" is an acceptable answer; silence is not).
5. **Reconcile sources.** Reviews, publications, and registry entries disagree on dates, endpoints, and effect sizes — surface conflicts rather than picking silently (standing instructions, applied at corpus level).
6. **Open every citation** that carries weight before the pack ships (pinpoint-citation contract).

## Output

The pack: a table of named analogs — program/sponsor · indication/population · design & endpoint · outcome (approved with what label / CRL with what deficiency / failed on what) · regulator treatment · pinpoint citation — followed by: the pattern read (what the set says the bar *is*), the adjusted probability vs the `base-rates.md` prior (named-precedent adjustments, shown), the closest-analog deltas for the live case, and the disconfirming precedent a skeptic would cite. End with the EVIDENCE BRIEF block (layer: regulatory or clinical) and save to the evidence ledger.

## Wiring

Feeds readout-handicap (PoS adjustment), adcom-label (expected label/vote and the pre-decision checklist), device-diligence (pathway odds and CMC benchmarks), healthcare-equity thesis (variant perception vs consensus odds) and model-valuation (rNPV PoS provenance). Run the precedent discipline checklist (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`) before shipping.
