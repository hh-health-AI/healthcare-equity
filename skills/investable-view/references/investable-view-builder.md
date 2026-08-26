# Investable View Builder (from the project framework)

From `Healthcare_Evidence_to_Valuation_Framework.xlsx` — "Convert clinical, regulatory, commercial, competitive and financial evidence into a falsifiable underwriting statement." Full framework tables (evidence translation, scenario matrix, valuation map) live in `../../model-valuation/references/evidence-to-valuation.md`.

## The six layers

| Evidence layer | Question | Required model output | Minimum evidence standard |
|---|---|---|---|
| Clinical | How differentiated is the product, and against which comparator? | PoA; eligible population; share; persistence | Endpoint hierarchy, effect size, multiplicity, safety and external validity |
| Regulatory | What exact label, restrictions and timing are probable? | Launch date; accessible population; monitoring burden | Agency feedback, filing status, CMC and label precedent |
| Commercial | How does eligibility become paid recurring demand? | Funnel conversion; net price; utilization; retention | Diagnosed → referred → authorized → started → paid → persistent |
| Competitive | Why should share and economics persist? | Share curve; price erosion; switching; terminal growth | Active-comparator profile, pipeline timing, contracting and workflow |
| Financial | What cash remains after delivery and reinvestment? | Contribution margin; capex; working capital; dilution | Unit economics, capacity, cash burn, leverage and runway |
| Valuation | What does the current price already assume? | Implied PoA; units; MCR; NRR; utilization or margin | Reverse DCF/rNPV and consensus bridge |

**Suite mapping:** Clinical, Regulatory(FDA), Competitive(pipeline) → clinical-catalysts · Regulatory(access)/Commercial(payment) → cms-reimbursement · Commercial(adoption) → provider-adoption · Commercial(volume/exposure) → procedure-exposure · Financial + Valuation → this plugin.

## Probability-weighted scenario builder

| Scenario | Probability | Value/share | Weighted value | Notes |
|---|---|---|---|---|
| Bear | — | — | — | Failure, delay or uneconomic conversion |
| Base | — | — | — | Most probable coherent outcome |
| Bull | — | — | — | Superior conversion with profitable economics |
| **Expected value** | Σ = 1.00 | | Σ(p × v) | Probability check must pass |

Scenario tree: Clinical/technical evidence → **CORE GATE CLEARS?** (clinical/technical + regulatory threshold) — No/major delay → Bear · Yes → **COMMERCIAL CONVERSION?** (access × adoption × realized economics) — weak/uneconomic → Bear · normal → Base · superior/profitable → Bull. Terminal leaves mutually exclusive; probabilities sum to 100%; every evidence update must change probability, timing, units, price, duration, margin, or capital.

## Variant-perception test (score each leg; all five required)

1. Disagreement is an explicit market-implied variable — evidence: reverse-engineered PoA, units, MCR, NRR, utilization or margin.
2. Evidence directly changes that variable — evidence: causal bridge from fact to assumption.
3. The difference matters after probability weighting — evidence: expected-value impact exceeds uncertainty and friction.
4. A catalyst can resolve the disagreement — evidence: dated trial, regulatory, reimbursement or operating update.
5. The thesis has an observable falsifier — evidence: predefined observation that forces re-underwriting.

## The template sentence

> "At the current price, the market appears to imply **[X]**. Evidence **[E]** changes model variable **[Y]** from **[A]** to **[B]**. That produces **[Δ revenue / margin / FCF / rNPV]** under the base case. Catalyst **[C]** should resolve the disagreement within **[time horizon]**. Observation **[F]** would falsify the thesis."
