# Changelog — HH-healthcare-equity

**HH-healthcare-equity** is the standalone distribution of the `healthcare-equity` plugin — the synthesis engine of the suite. Versions track the canonical copy in the `claude-healthcare-analyst-suite` monorepo (`github.com/<your-github-username>/claude-healthcare-analyst-suite`); this file carries the plugin-relevant slice of the suite changelog.

## [0.2.2] — 2026-08-26

- Workflow chart embedded in `CLAUDE.md` as a runtime **Workflow map**: the four-stage analyst lifecycle (Discover → Underwrite → Decide → Monitor) as routing guidance — enter at the node matching the question, offer the downstream node when a skill completes, engine briefs and the evidence ledger feed the investable-view capstone, and sell-discipline lessons loop back into thesis. Includes show-on-request behavior for "how does this plugin work".

## [0.2.1] — 2026-08-26

- README gains a **Workflow** section with the same Mermaid flowchart (skills in blue, data sources and the evidence ledger in green, the evidence-assembler agent in dashed amber, the investable-view capstone in pink, co-installed engine plugins in violet). Render-verified with mermaid-cli.

## [0.2.0] — 2026-08-25

- New references: `data-stack-map.md` (breadth-vs-depth taxonomy of the paid data stack — Cortellis-class, IQVIA-class, Rhizome-class, terminals, this suite — for "should we buy tool X" decisions) and model-valuation `loe-mechanics.md` (Orange Book × tentative-docket generic-entry forecasting, BE bounds 80.00–125.00%, 180-day exclusivity, the 351(k) three-tier biosimilar framework with the functional-rescue precedent, CGT 15-year registry tail liabilities, post-approval change tiers).
- thesis gains designation de-hype, REMS/ETASU TAM-haircut, and safety class-contagion rules.
- international gains NMPA conditional-approval numbers, CHMP qualification-opinion tiers, and EU CTR Article 81 transparency unlocks.
- investable-view now assembles from the evidence ledger rather than from conversation memory.
- Suite-wide evidence discipline: evidence-brief contract adds the `Coverage` line (master definition lives in this plugin's CLAUDE.md); pinpoint-citation rule ("an uncited regulatory or clinical claim is a draft, not evidence"); five-point precedent discipline checklist; evidence ledger under `~/.claude/data/healthcare-equity/briefs/` and `.../snapshots/`; README smoke test; optional Rhizome AI connector added to the routing map as the FDA/EMA primary-document depth layer.

## [0.1.0] — 2026-08-25

Initial release.

- No MCP servers by design — this plugin consumes the four engine plugins' connectors plus a transcripts/filings connector (e.g. Quartr) and web/EDGAR.
- 12 skills: initiate, earnings, model-valuation, thesis, screen-themes, portfolio, meetings-experts, sell-discipline, international, comms-compliance, esg-stewardship, and the **investable-view** capstone.
- evidence-assembler agent (ticker → runs the engines' skills → drafts the investable view).
- Full standing instructions (role, source hierarchy, required behaviours, output skeleton, connector routing map, Appendix C source-fidelity caveats).
- References: the Healthcare Evidence-to-Valuation framework distillation, 24-case library, and commercial-metrics glossary.
- Carries 94 of the 113 prompts from the Healthcare Equity Analyst Prompt Library v1.4 (the other 19 live beside their data sources in the engine plugins).
