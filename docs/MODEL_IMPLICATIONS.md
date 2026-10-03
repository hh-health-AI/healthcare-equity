# Evidence can justify retaining a forecast

Every evidence update must document a model implication: CHANGE, NO_CHANGE, UNCERTAINTY_ONLY, or NEEDS_DATA. State the affected assumption, prior and proposed values (or explicitly unavailable), rationale, source/locator, and next observable. Do not force a numerical change or double-count evidence already in the model.

| Status | Required reasoning |
|---|---|
| CHANGE | Prior and revised assumption, units, effective period, evidence bridge and double-count check |
| NO_CHANGE | Unchanged assumption, why the evidence is already reflected or immaterial, and reopening trigger |
| UNCERTAINTY_ONLY | Central assumption unchanged; specify how the range, confidence or scenario weights change |
| NEEDS_DATA | Identify the missing input, keep the prior explicitly provisional, and state the next diligence action |

## Worked NO_CHANGE example — synthetic

Source: the existing [synthetic evidence packet](../research-suite/examples/evidence.json), S1, results table 2. This is not a real clinical study.

The model already assumes a 50% commercial success probability. The reported confidence interval includes the null and adds no evidence beyond the information used to set that probability. **NO_CHANGE: 50% → 50%.** No new revenue, pricing or approval uplift is booked. The probability is an illustrative modeling assumption, not an estimate derived from the risk ratio. Reopen after reviewing the prespecified analysis, multiplicity plan and full results. Missing harms data prevent a safety conclusion.

A valid NO_CHANGE conclusion is useful research. It does not, by itself, establish a differentiated investment thesis; a claimed variant view still needs a demonstrable gap versus market assumptions and an observable falsifier.
