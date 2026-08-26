---
name: investable-view
description: >
  This skill should be used when the user says "build the investable view for [TICKER]",
  "assemble the evidence layers", "synthesize everything into a view", "run the full
  framework on X", "what's the falsifiable thesis here", or wants clinical, regulatory,
  commercial, competitive, and financial evidence converted into one underwriting
  statement.
metadata:
  version: "0.1.0"
---

# Investable View (capstone)

Convert the five evidence layers into a falsifiable underwriting statement — the suite's terminal output. Method reference: `${CLAUDE_PLUGIN_ROOT}/skills/investable-view/references/investable-view-builder.md`; framework tables in `../model-valuation/references/evidence-to-valuation.md`.

## Workflow

1. **Frame the name.** From filings/IR: the 1–3 revenue units that matter and the sub-sector — this selects the economic unit, dominant formula, scenario discriminator, and price-implied variable from the framework tables. State them up front.
2. **Collect the layer briefs.** Gather EVIDENCE BRIEF blocks from the engine plugins — clinical & regulatory(FDA) & competitive from clinical-catalysts; regulatory(access)/commercial(payment) from cms-reimbursement; commercial(adoption) from provider-adoption; commercial(volume/exposure) from procedure-exposure — plus the financial layer from filings/transcripts (Quartr/EDGAR). Reuse briefs already produced in the session, the project, or the evidence ledger (`~/.claude/data/<plugin>/briefs/` — check all five plugins' ledgers, citing brief dates); commission missing material ones (or offer the evidence-assembler agent to run the sweep). A layer skipped as immaterial is declared, not silent.
3. **Interrogate each layer** against the Investable View Builder's question / required model output / minimum evidence standard. Evidence below the minimum standard gets marked *thin* and generates a next-diligence item — not a silent assumption.
4. **Translate.** Push every brief through the evidence-translation rules: which of probability / timing / units / price / duration-retention / margin / capital moved, by how much, and what the "not automatic" column forbids inferring. Discard adjectives that move nothing.
5. **Build scenarios** on the sub-sector's primary discriminator: mechanism-distinct bear/base/bull with the matrix's boundary discipline, probabilities summing to 1.00 with ≥5% unknown-unknown residual, an early signal per scenario, and value/share per leaf (valuation formula for the economic unit).
6. **Reverse-engineer the price.** Solve for the price-implied variable (implied PoA, patient-years, utilization, MCR, NRR, margin) using current price and consensus **provided by the user** — request them; never fabricate market data. Run the five-leg variant-perception test: explicit market-implied variable · evidence moves it · survives probability weighting · catalyst can resolve it · observable falsifier exists. Fewer than five legs = narrative, not thesis; say so.
7. **State the view** in the template sentence — *"At the current price, the market appears to imply [X]. Evidence [E] changes model variable [Y] from [A] to [B]. That produces [Δ] under the base case. Catalyst [C] should resolve the disagreement within [horizon]. Observation [F] would falsify the thesis."* — then deliver the full output skeleton (what matters now → facts → inference → model impact → variant view → disconfirming evidence → next diligence → confidence), showing the five layer briefs as an appendix so every input is auditable.
8. **Hand off:** falsifiers and early signals → sell-discipline (SELL-02 watchlist); catalysts → the calendar; the view → comms-compliance (COMM-01 IC memo) when it goes to committee.
