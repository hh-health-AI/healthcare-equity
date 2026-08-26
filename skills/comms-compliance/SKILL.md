---
name: comms-compliance
description: >
  This skill should be used when the user says "draft the IC memo", "write the quarterly
  letter section", "translate this biology for my PM", "MNPI scrub this draft",
  "disclosure check before publishing", "pre-flight my conference talk", or any
  client/internal communication and compliance-guardrail task.
metadata:
  version: "0.1.0"
---

# Client Communication & Compliance

Internal memos, IC briefings, client letters, translations, and the compliance guardrails around them. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/comms-compliance/references/prompts.md`.

## Route by output

| Output | Prompt |
|---|---|
| IC-ready memo (≤1,000 words) | COMM-01 |
| Quarterly LP letter healthcare section (600 words) | COMM-02 |
| Biotech science for generalist PMs (~500 words) | COMM-04 |
| MNPI scrub of an outbound draft | COMM-05 |
| Disclosure & conflict checklist | COMM-06 |
| Public speaking / media pre-flight | COMM-07 |

(Quick-reaction earnings notes = COMM-03, in the earnings skill.)

## Execution rules

1. **Compression is the craft:** COMM-01 caps at 1,000 words with the recommendation in three bullets up front; COMM-02 holds 600 words including "what we got wrong" (honesty is a feature, not a risk); COMM-04 requires an accurate analogy for the mechanism and two reasons a statistically positive result could be clinically irrelevant. Resist padding.
2. **The compliance chain runs before anything leaves the desk:** COMM-05 (flag statements derived from non-public sources; remove / rephrase-with-attribution / retain-with-compliance-review; err on caution) → COMM-06 (position disclosures long/short/none, personal holdings, meeting/call log, dated PTs, disclaimer) → COMM-07 when public-facing (restricted-window check, forward statements grounded in public data, investment-advice boundary). Run it whenever recent expert calls or management meetings touched the draft's subject.
3. Inputs come from the other skills — thesis memos, model outputs, post-print updates, EN-02's anonymised quotes — and every number keeps its time-stamp and source through the compression (standing instructions).
4. Structure of the IC memo mirrors the plugin's output skeleton (what matters now → facts → inference → model impact → variant view → disconfirming evidence); the "one question I want IC to answer" device from PORT-06 (thesis skill) belongs in every contested memo.
5. UK/EU stewardship-code and SFDR-adjacent reporting language pairs with the esg-stewardship skill (and the separate sfdr-si-prompt-library account skill if installed).
