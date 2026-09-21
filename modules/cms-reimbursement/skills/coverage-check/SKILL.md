---
name: coverage-check
description: >
  This skill should be used when the user asks "is [drug/device/procedure] covered by
  Medicare", "check the NCD/LCD for X", "what's the coverage status of X", "any coverage
  restrictions on X", or "did coverage change for X". Produces a cited Medicare coverage
  brief with the model variables it moves.
metadata:
  version: "0.1.0"
---

# Coverage Check

Determine the Medicare coverage position for a named drug, device, diagnostic, or procedure and translate it into model variables.

## Workflow

1. **Frame the ask.** Identify the product, the clinical use, the likely site of service (inpatient, HOPD, ASC, office, lab, home), and the ticker(s) exposed. If ambiguous, state the assumption and proceed.
2. **Search the Medicare Coverage Database** via the CMS Coverage connector: national coverage first (NCDs), then local (LCDs and coverage articles by MAC). Capture: policy ID and title, national vs local, effective/retirement dates, covered indications and restrictions (patient criteria, physician/site requirements, frequency limits, documentation), and Coverage with Evidence Development (CED) conditions if any.
3. **Classify the position** — one of: covered nationally · covered locally (name the MACs and note geographic gaps) · covered with restrictions/CED · explicitly non-covered · silent (no policy — contractor discretion; for new technology, silence plus a new code often means case-by-case review).
4. **Check for motion.** Look for proposed NCDs/reconsiderations, draft LCDs, or recent coverage articles that signal a change window; note the comment/decision dates as catalysts for the catalyst calendar.
5. **Label the universe.** State clearly this is Medicare FFS coverage; note that MA plans must cover what NCDs/LCDs cover (but can add utilization management), and commercial coverage is separate — if the thesis needs it, do targeted web research on the top commercial payors' medical policies and mark that as a separate evidence line.
6. **Translate.** Per the coverage row of `${CLAUDE_PLUGIN_ROOT}/references/metrics-payor.md`: coverage evidence moves authorization, abandonment, **paid conversion**, and net price/accessible population. It does **not** automatically move clinical adoption or prescribing — say so.
7. **End with the EVIDENCE BRIEF block** (contract in the `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`), with retrieval date and policy vintages. For payment rates, hand off to the reimbursement-impact skill — coverage and payment are different questions.

## Quality bar

Quote restriction language exactly when it drives the model (e.g., patient-criteria clauses that halve the eligible population). Never infer coverage from the absence of a policy without labeling it "silent/contractor discretion". If results are thin or ambiguous, say "missing" and name the data point that would settle it (e.g., MAC call, payor policy portal).

## REMS/ETASU friction check (v0.2)

For drug products, check whether a REMS program — especially ETASU elements (prescriber/pharmacy certification, patient registries, required monitoring, restricted distribution) — sits between coverage and paid demand. REMS friction is quantifiable access friction: per the coverage translation row, it moves **authorization, abandonment, and paid conversion**, and functions as an accessible-population/uptake-pace haircut in the funnel (not a qualitative caveat). Note REMS *changes* (additions, modifications, removals) as dated demand-side events for the catalyst feed, and cross-reference the clinical-catalysts quality-signals skill when a safety development could trigger one.
