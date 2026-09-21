# European HTA mechanics by market

| Market | Body | What it decides | Financial consequence |
|---|---|---|---|
| Germany | G-BA, advised by IQWiG | Additional benefit category vs an appointed comparator | Free price at launch, then a negotiated price applying from a fixed month post-launch. "No additional benefit" caps the price at the reference group |
| England and Wales | NICE | Cost-effectiveness against a threshold, with severity and end-of-life modifiers | Positive appraisal triggers a funding obligation within a set period; confidential patient access schemes mean the list price is not the net price |
| Scotland | SMC | Cost-effectiveness, faster process | Often precedes NICE and can be read as a leading indicator |
| France | HAS Transparency Committee | SMR (reimbursement rate) and ASMR (improvement level, I–V) | ASMR I–III supports a premium; ASMR IV–V pushes toward comparator pricing |
| Italy | AIFA | Reimbursement class and negotiated price, often with managed-entry agreements | Long timelines; registries and payment-by-result are common |
| Spain | Ministry plus regions | National price then regional access | Regional variation is material; national approval is not access |
| EU-wide | EU HTA Regulation joint clinical assessment | Shared clinical assessment across member states | Sequencing and evidence requirements change; pricing stays national |

## What actually determines the price

1. **The comparator the authority appoints**, not the one the sponsor chose for its
   trial. This single choice usually explains more of the price outcome than the data.
2. **The endpoint hierarchy the authority accepts.** Overall survival and mortality
   outrank progression-free survival and surrogate endpoints in most European
   assessments, which is why trials designed for FDA sometimes underperform in Europe.
3. **Comparative evidence.** Placebo-controlled data against an appointed active
   comparator forces indirect comparison, which authorities discount heavily.
4. **Budget impact**, formally or informally, for large populations.

## Timing to model

Approval-to-access gaps vary widely across European markets and are among the most
persistent structural features of the region: Germany is at the fast end because of free
pricing at launch, while several southern European markets and the regional layers in
Spain and Italy run far longer. Build the gap per country from the specific asset's
observed HTA submissions rather than from a regional average, and state the source.

## Framework anchors

Your own valuation framework, for translating an HTA
outcome into the model variable it moves; published HTA methods literature for the
threshold and modifier mechanics.
