---
name: slides
description: Create strategic HTML presentations and pitch decks with coherent narrative, design tokens, responsive layouts, accessible charts, and data-backed slide strategies. Use for presentations, investor decks, marketing decks, and data-driven storytelling.
---

# Slides

Turn a message into a persuasive, visually coherent presentation. Keep the narrative and the visual system aligned; a slide is not a document page with paragraphs pasted onto it.

## Workflow

1. Confirm audience, decision or action, delivery format, slide count, source data, brand, and whether the output is HTML, PPTX, PDF, or another format. For native PowerPoint work, hand off to the host’s presentations capability after the content/design contract is ready.
2. Read `references/create.md`, then load only the relevant layout, strategy, copywriting, and template references.
3. Search the local slide datasets with `scripts/search-slides.py`; use the results to choose strategy, layout, copy formula, chart, typography, colors, and background direction.
4. Build an outline where each slide has one job, one headline claim, supporting evidence, and a clear transition. Use charts only when they make the relationship easier to understand.
5. Require the project token contract at `assets/design-tokens.json` and `assets/design-tokens.css`. `eto-apere` owns all declarations, including required `component.slide.*` aliases; route there when either file or any required alias is missing. This skill owns HTML generation, background selection, and token validation, and generation must stop on an incomplete token contract.
6. Render or preview the deck at the target viewport, check overflow and contrast, and revise before delivery. Include source files and an export when requested.

## Quality rules

- One dominant idea per slide.
- Prefer a specific claim over a topic label.
- Use visual hierarchy and whitespace; do not shrink type to rescue an overloaded slide.
- Preserve brand voice and token relationships.
- Respect reduced motion and provide meaningful alt text or equivalent descriptions for non-text visuals.

## Resources

- `references/layout-patterns.md` — slide composition.
- `references/html-template.md` — HTML structure.
- `references/copywriting-formulas.md` — headline and narrative formulas.
- `references/slide-strategies.md` — strategy selection.
- `references/create.md` — creation entry point.
- `data/` — slide strategies, layouts, copy, charts, typography, colors, and backgrounds.
- `scripts/search-slides.py` — local BM25 search across the slide datasets.
- `scripts/generate-slide.py` — token-linked HTML deck generator; accepts `--project-root` and contained `--output`.
- `scripts/embed-tokens.cjs` — inline token CSS helper for standalone HTML decks.
- `scripts/html-token-validator.py` — HTML token compliance validator; accepts `--project-root`.
- `scripts/fetch-background.py` — background selector and overlay helper; accepts `--project-root`.
