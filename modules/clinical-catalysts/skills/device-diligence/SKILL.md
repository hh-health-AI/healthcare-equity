---
name: device-diligence
description: >
  This skill should be used when the user asks about "510(k) predicate risk", "De Novo
  vs PMA pathway", "FDA meeting history for [asset]", "TPP assessment", "CMC/manufacturing
  scalability", "freedom to operate / IP risk", "LDT rule impact", or "companion
  diagnostic linkage" — the regulatory and technical diligence layer for drugs, devices,
  and diagnostics.
metadata:
  version: "0.1.0"
---

# Device & Regulatory Diligence

Deep regulatory and technical diligence: product profile, manufacturing, IP, FDA pathway and history, diagnostics regulation, and therapy–test coupling. Eight workflows, each a prompt in `${CLAUDE_PLUGIN_ROOT}/skills/device-diligence/references/prompts.md` — pick by question:

| Question | Prompt | Primary sources |
|---|---|---|
| Is the product profile differentiated or me-too? | SUB-BIO-04 (TPP interrogation) | Corporate deck, protocol, comparator labels |
| Can they make it at scale, at margin? | SUB-BIO-05 (CMC/COGS scalability) | Filings, manufacturing disclosures, CDMO contracts |
| Is the IP position durable? | SUB-BIO-06 (FTO analysis) | Patent databases, Orange/Purple Book, Para IV notices |
| What does the FDA interaction history signal? | SUB-BIO-07 (meeting history risk) | SEC filings, Drugs@FDA, correspondence disclosures |
| Is the 510(k) predicate sound? | SUB-MED-03 (predicate validity) | FDA 510(k) database, classification regs |
| De Novo or PMA — and what does the pathway cost? | SUB-MED-04 (pathway risk) | FDA classification, recent comparables |
| What does the LDT rule do to this diagnostic? | SUB-TLS-03 (LDT oversight impact) | FDA LDT final rule, company disclosures, litigation status |
| Does a companion diagnostic gate the therapy? | SUB-TLS-05 (CDx linkage) | Drugs@FDA labels, CDx approvals, guidelines |
| Does a delivery-format change (IV→SC, autoinjector, PFS) carry the thesis? | Combination-product module (below) | FDA combination-product precedents, ISO 11608, DMEPA/URRA records |

## Execution rules

1. Choose the workflow(s) from the table, load the prompt, and gather primary sources first: FDA databases via web research (Drugs@FDA, 510(k)/PMA/De Novo databases, warning letters), the Clinical Trials connector for supporting studies, PubMed for published validation data.
2. Ground pathway and development-stage judgments in `${CLAUDE_PLUGIN_ROOT}/references/fda-pathways-fto.md` and `${CLAUDE_PLUGIN_ROOT}/references/device-development-checkpoints.md` (includes the human-factors gate). For drug CMC, translate per the manufacturing row of references/evidence-translation-clinical.md: CMC progress moves launch probability, timing, yield, capacity, and capital — not patient demand or share.
3. For legal-adjacent outputs (FTO), state the analysis is an investment-diligence screen, not a legal opinion, and note that definitive FTO requires patent counsel.
4. End each workflow with the EVIDENCE BRIEF block (layer: regulatory; competitive for TPP/CDx where share-relevant). Route label/coverage consequences to adcom-label and cms-reimbursement; route pathway timelines to catalyst-calendar; route COGS/margin deltas to healthcare-equity model-valuation.

## Combination products & delivery-format changes

For IV→SC conversions, autoinjector/PFS launches, self-administration claims, and device changes on marketed drugs, work from `${CLAUDE_PLUGIN_ROOT}/references/combination-products.md`: place the change on the four-domain evidence ladder (HF/URRA · PK bridging 80–125% · clinical · CMC/EDDO, with the Humira-s381 → Repatha precedent range), check device qualification (ISO 11608, aged/shipped verification, PPQ at filing) and the autoinjector deficiency base rates (~10/12 recent BLAs flagged on essential-performance traceability), note that shelf-life/device-change supplements are PAS-clocked dated events, and translate per the "easier administration" evidence row — a format conversion moves initiation/site-of-care/persistence, never efficacy or TAM, and is not a new patient (case C05 rule). Post-launch, hand MAUDE use-error trajectories to the quality-signals skill.
