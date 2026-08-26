# Prompts — Thesis Development & Pressure-Testing

From the Healthcare Equity Analyst Prompt Library v1.4. Standing instructions apply (`${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`). Fill bracketed inputs.

## INIT-03 · Variant Perception Generator
Tags: `#initiation #thesis #cross-sector #sell-side #pm-level #senior-judgment`
**When to use.** When consensus is well-formed and you need to identify where you can have a differentiated view.
**Inputs.** Consensus summary or 3–5 sell-side notes; current price target distribution.
**Output.** Structured matrix followed by ranked top-three list with falsification tests.

PROMPT:
> I am initiating on [TICKER]. Below is the consensus view from the most recent five sell-side notes. Act as an adversarial adjudicator — refuse to simply average the bull and bear cases or split the difference. For each dimension — (a) revenue growth trajectory, (b) gross margin durability, (c) opex leverage, (d) terminal value assumptions, (e) competitive intensity, (f) regulatory or reimbursement risk, (g) management quality — state: the consensus assumption, the strongest contrary view I could defend, the specific evidence required, and where I would source it. Categorise each bear argument into structural vulnerabilities vs theoretical vulnerabilities lacking empirical support. Rank dimensions by price-target impact. End with the top three variant perceptions and the falsification test for each.

## THES-01 · Pre-Mortem on a Long Thesis
Tags: `#thesis #cross-sector #senior-judgment #pm-level`
**When to use.** Before sizing up or initiating a long.
**Inputs.** Thesis memo and entry rationale.
**Output.** Three-path failure map with monitoring signals.

PROMPT:
> Imagine 24 months from today the long thesis on [TICKER] has failed — stock down 40%. Write the post-mortem. (1) Three most likely paths to failure; (2) operational signals in months 3–9; (3) disconfirming question for each quarterly check-in; (4) re-underwrite trigger level. Favour name-specific failure modes.

## THES-02 · Steel-Man the Short Case
Tags: `#thesis #risk #cross-sector #sell-side #senior-judgment`
**When to use.** When the bull case feels obvious.
**Inputs.** Long thesis; short reports if any.
**Output.** Steel-manned short memo, 800–1,200 words.

PROMPT:
> I am long [TICKER] with thesis [paste]. Steel-man the short as if running a tactical short book. (1) Central mechanism in two sentences; (2) supporting data ranked by recency; (3) catalysts for downward revision; (4) time horizon and holding cost; (5) bull response and rebuttal — two layers deep; (6) 90-day evidence to look for. Demand mechanism, not valuation alone.

## THES-03 · Thesis Decomposition into Testable Claims
Tags: `#thesis #cross-sector #senior-judgment`
**When to use.** When a thesis feels right but you cannot articulate falsification.
**Inputs.** Thesis memo.
**Output.** Claim-by-claim decomposition with bias flags.

PROMPT:
> Decompose thesis on [TICKER] into claims. For each: (1) one-sentence claim; (2) classify as factual/forecast/judgment; (3) confirmation source; (4) leading indicator and change threshold; (5) alternative judgments; (6) load-bearing rank; (7) claims asserted without basis — that's where bias hides.

## THES-04 · Regime Map Stress Test
Tags: `#thesis #thematic #cross-sector #pm-level #senior-judgment`
**When to use.** When thesis depends on macro or policy regime continuity.
**Inputs.** Thesis, sub-sector context, macro environment.
**Output.** Regime matrix with exit triggers.

PROMPT:
> Regime map for [TICKER]. Define 4 distinct world-states, each with a different dominant mechanism. For each: probability, 3-year path, equity value, early signal. Do NOT assign 'wins in every scenario'. End with probability-weighted value and the regime forcing exit.

## THES-05 · Disconfirming Evidence Search Plan
Tags: `#thesis #risk #cross-sector #expert-network #senior-judgment`
**When to use.** When formalising the search for evidence against your thesis.
**Inputs.** Thesis claims, expert network coverage, subscriptions.
**Output.** 30-day calendar with prioritisation.

PROMPT:
> 30-day disconfirmation plan for [TICKER]. Top 5 claims: (1) falsifying evidence type; (2) source; (3) cost; (4) prioritisation. Output a 30-day calendar with escalation rule.

## SS-01 · Multi-Broker Note Triangulation
Tags: `#sell-side-synth #cross-sector #sell-side #senior-judgment`
**When to use.** When 3+ notes drop on the same name.
**Inputs.** 3–8 sell-side notes; my model.
**Output.** Triangulation note, 600–1,000 words.

PROMPT:
> Triangulate [N] sell-side notes on [TICKER]. (1) Consensus map with dispersion; (2) differentiated takes per broker; (3) coverage gap; (4) reading priority; (5) source attribution. Extract signal, not paraphrase.

## PORT-05 · Constructive Disagreement with Portfolio Manager on Sizing or Thesis
Tags: `#portfolio #people-dynamics #cross-sector #senior-judgment`
**When to use.** When the analyst's view on sizing, entry, exit, or thesis materially differs from the PM's, and the disagreement should improve the decision rather than damage the relationship.
**Inputs.** My thesis or sizing recommendation; PM's stated view; any context on book-level factors the PM may be weighting.
**Output.** Structured approach with steel-man, minimum viable argument, falsification test, and documentation plan.

PROMPT:
> I have a material disagreement with my PM on [TICKER / decision]. My view: [state view]. PM view: [state view]. Structure my approach to this disagreement. (1) Separate the disagreement into components — is the divergence about (a) the underlying facts and what the filings say, (b) the interpretation of those facts into thesis claims, (c) the probabilities attached to scenarios, (d) the sizing implications given a shared thesis, or (e) the risk tolerance of the book? Each component calls for a different kind of conversation. A factual disagreement is resolvable by returning to primary sources; a risk-tolerance disagreement is not. (2) Steel-man the PM's position — before preparing my argument, write out the strongest version of the PM's case in at least 200 words, including any information advantage the PM may have (other names in the book, factor exposures I cannot see, client constraints, prior experience with similar situations). If I cannot articulate the PM's view charitably, I am not ready to argue my own. (3) Identify the minimum viable argument — what is the smallest claim I need the PM to accept for my recommended action to follow? Arguing for the full maximalist thesis is a losing strategy if a narrower claim is sufficient. (4) Identify the falsification test I would accept — what would I have to see to change my mind toward the PM's view? Offering a specific falsification condition in advance both signals good faith and forces my own calibration. (5) Structure the conversation — lead with the shared assumption (where we agree), then the narrow divergence (where we differ), then the falsification test, then the recommended action. Avoid building the case chronologically or walking through my entire reasoning; the PM does not have time. (6) Commit-and-review rule — if the PM decides against my recommendation, define in advance the observable signal that would make me return to the topic (a specific KPI miss, a specific data point) versus accepting the decision and moving on. This avoids both repeated re-litigation and quiet resentment. (7) Document the disagreement — a short written note (one paragraph) capturing my view, the PM's view, and what I will watch. This serves both my own learning (SELL-04 post-mortem later) and professional record if the decision matters. End with my action for the conversation.

## PORT-06 · Defending a Contrarian Thesis at Investment Committee
Tags: `#portfolio #people-dynamics #client-comms #cross-sector #senior-judgment #pm-level`
**When to use.** Before presenting a thesis to IC where the mood runs the opposite direction, and the analyst needs to defend without becoming defensive.
**Inputs.** Thesis memo; IC member views where known; recent IC track record for similar decisions; my own history at IC.
**Output.** IC defence plan with anticipated attacks, evidence hierarchy, emotional regulation, calibrated confidence, and verbatim opening.

PROMPT:
> I am presenting [TICKER] to IC on [date]. My view: [long / short / contrarian hold]. IC mood appears to be: [opposite direction]. Prepare me to defend the view. (1) Anticipate the three sharpest attacks — for each, state the attack in the IC member's own voice (not my charitable reframing), the strongest rebuttal I have, and the point at which the rebuttal becomes weak. Prepare the concession language for the weak points in advance. Acknowledging a real weakness strengthens credibility more than denying it. (2) Evidence hierarchy — identify the single piece of evidence most likely to shift a sceptical IC member's view, and the piece most likely to be dismissed. Lead with the former; hold the latter in reserve. (3) Emotional regulation plan — what is the most likely emotional failure mode for me in this specific IC? Defensiveness, over-elaboration, conceding too readily, or doubling down too hard? Pre-commit to the counter-move. If I feel defensiveness rising, slow down and ask what specifically the challenger would need to see. If I feel the urge to over-elaborate, cut the explanation at 30 seconds and ask if more detail would help. (4) Calibrated confidence — state my confidence level (0.00–1.00) up front rather than defending the view uniformly. A confident statement of moderate confidence is more credible than an uncertain statement of high confidence. Distinguish the parts of the thesis I hold with high confidence (specific facts) from the parts I hold with moderate confidence (inferences) from the parts I hold with low confidence (forward estimates). (5) The one question I want IC to answer — what is the specific question I need the IC to weigh in on, as distinct from the overall rating? IC's time is best spent on the judgment calls I cannot resolve independently. Frame the question to focus IC attention there. (6) Exit conditions in advance — state the observable conditions under which I would reverse this view. Pre-committing to exit conditions both strengthens the initial case and protects against anchoring if the thesis breaks. (7) Post-IC plan — if the IC concludes against my view, what do I do next? Accept the decision? Return to it in 60 days if a specific signal arrives? Maintain a smaller position? Clarity on this before the IC prevents post-meeting ambiguity. End with the opening 90 seconds of my presentation, verbatim.

## SUB-DIG-02 · AI/ML in Healthcare Investability Test
Tags: `#digital-health #thematic #thesis #senior-judgment #pm-level`
**When to use.** When filtering genuine AI moat from buzzword.
**Inputs.** Company materials, clinical evidence, regulatory status.
**Output.** Investability assessment with verdict.

PROMPT:
> Investability test for [TICKER]. (1) Use-case specificity with evidence; (2) data moat; (3) regulatory pathway (SaMD, CE mark); (4) reimbursement (CPT, NTAP); (5) distribution; (6) unit economics; (7) verdict: conviction / basket / pass.
