# Journal Club Agent

Use to prepare a journal club, teach critical appraisal, create a study discussion guide or draft an eight-slide medical research presentation. Read the paper and methods, preserve evidence boundaries and distinguish a slide outline from an exported presentation file.

## Try it

- Prepare an eight-slide journal club on this paper.
- Create a discussion guide emphasizing endpoints, bias and applicability.
- Explain this trial to medical students with source-linked speaker notes.

## Run the reproducible utility

```bash
hh-research journal-club examples/evidence.json --out outputs/journal-club-agent.md
```

Run from `research-suite` after installation. The offline examples are explicitly synthetic; public API outputs carry retrieval metadata.

## Workflow

1. Identify audience, paper, clinical question and discussion time. Default to a concise eight-slide briefing if no format is specified.
2. Read the paper and supplement; retrieve registry/protocol when relevant. Record gaps and source locators. Use the Clinical Trial Analyst workflow for interventional trials.
3. Build a medical evidence packet with bounded claims, short passages, appraisals, limitations and questions. Do not manufacture methods not reported in the paper.
4. Fill slides 1–8: clinical question; design; intervention/comparator; endpoints/analysis; effects/uncertainty; harms/missingness; validity/applicability; conclusions/open questions.
5. Run `hh-research journal-club packet.json --out journal-club.md --json-out journal-club.json`.
6. Add speaker notes, three discussion questions and a short explanation of the most consequential statistical concept. Label any synthetic teaching example.
7. The command exports Markdown, not PowerPoint. If the user requests PPTX/PDF, use an available presentation/document tool and preserve citations. Never claim a deck was created when only an outline exists.
8. Close with what the study supports, what it cannot establish and which evidence would change the conclusion.

## Existing platform handoff

[clinical-catalysts](../../modules/clinical-catalysts/), [evidence-catalysts](../../modules/evidence-catalysts/)

[Skill instructions](../skills/journal-club-agent/SKILL.md) · [Agent workflow](../agents/journal-club-agent.md) · [Input contracts](input-contracts.md)
