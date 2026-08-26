---
name: esg-stewardship
description: >
  This skill should be used when the user says "ESG materiality map for [TICKER]",
  "stewardship engagement plan", "access to medicine review", "healthcare climate
  risk assessment", "health equity / digital divide TAM check", or any ESG-integration
  and stewardship task on a healthcare name.
metadata:
  version: "0.1.0"
---

# ESG Integration & Stewardship

ESG materiality and stewardship without checklist ESG — financially material analysis only. Prompts in `${CLAUDE_PLUGIN_ROOT}/skills/esg-stewardship/references/prompts.md`.

## Route by need

| Need | Prompt |
|---|---|
| Materiality beyond MSCI/Sustainalytics (at initiation) | ESG-01 healthcare materiality map |
| Engagement arc on a material issue | ESG-02 stewardship engagement plan |
| Pharma access strategy (AtMI, EM pricing) | ESG-04 access to medicine review |
| Physical/transition climate risk (CSRD/TCFD/IFRS S2) | ESG-05 climate risk & decarbonisation pathway |
| Digital platform's real reach vs claimed TAM | SUB-DIG-03 health equity & digital divide |

(Drug pricing/IRA exposure = ESG-03, in the cms-reimbursement plugin.)

## Execution rules

1. **Financial materiality is the filter:** every E/S/G item carries a materiality score, disclosure-quality read, and the channel to cash flows (pricing power, TAM access, procurement eligibility, regulatory exposure) — items without a channel get dropped, per the "without descending into checklist ESG" mandate.
2. Frameworks referenced as the prompts specify: SASB/IFRS S1-S2, CSRD double materiality (ESRS E1 for climate), TCFD, UK Stewardship Code / SFDR Article 9 for reporting, CA100+/IIGCC where engagement escalates. UK/EU procurement angles (net-zero NHS, product carbon footprint in formularies) cross-reference the international skill's INTL-04.
3. Healthcare-specific materiality set (ESG-01): drug pricing/access, product safety and recalls, trial diversity, workforce; supply-chain climate exposure (API concentration, the Hurricane Maria IV-bag precedent in ESG-05); governance = capital allocation, comp alignment, board, audit.
4. Engagement plans (ESG-02) are investment documents: financial materiality case → specific ask → counterparty sequencing → 12–24 month milestones → escalation → reporting. Route milestone dates to the catalyst calendar; route engagement questions to meetings-experts.
5. Pairs with the separate sfdr-si-prompt-library account skill (if installed) for SFDR sustainable-investment classification language; this skill owns the company-level analysis.
