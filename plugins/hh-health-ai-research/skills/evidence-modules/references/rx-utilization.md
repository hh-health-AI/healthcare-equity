# Drug utilization

## Decision

What do published utilization and launch proxies imply about demand?

## Primary evidence

CMS Open Data and relevant official published utilization files; validated RxNorm mappings; issuer disclosures.

## Procedure

Resolve drug/form/strength, geography, payer and period. Inspect units, grain, suppression and lags. Separate prescription counts, patients, spending and net revenue. Use matched definitions for growth comparisons.

Record the entity mapping, date cutoff, source vintage, material query filters and coverage limitations. Present direct observations separately from inference. For current policy, clinical, legal or financial facts, verify current primary records rather than treating this reference as evidence.

## Model bridge

Potentially affected variables: Treated patients, treatment intensity, duration/adherence, mix and the observable launch trajectory.

For every proposed implication use CHANGE, NO_CHANGE, UNCERTAINTY_ONLY or NEEDS_DATA. State the prior and proposed assumption values or unavailable, the supporting locator, the causal reasoning, what is already in the model and the next observable. Do not manufacture a numerical change merely to fill the template.

## Boundary

A prescription is not a unique patient; gross spending is not manufacturer net revenue; Medicare is not the whole market.

## Output

A concise source-linked answer and an evidence brief showing coverage, model implication and confidence. Separate hypotheses from conclusions and expose the fastest test of the interpretation. For purely scientific or policy questions, omit investment interpretation unless requested.

## Provenance and deeper methods

This brief is an adaptation of the module's role in the canonical root README and standing evidence contract, not a full import of its individual skills. The integrated module lives at https://github.com/hh-health-AI/healthcare-equity/tree/main/modules/rx-utilization. The standalone repository is https://github.com/hh-health-AI/rx-utilization; the monorepo is the canonical integration source. Inspect the current source before reproducing exact upstream methods.
