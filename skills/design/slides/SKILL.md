---
name: slides
description: Create strategic HTML presentations and pitch decks with coherent narrative, design tokens, responsive layouts, accessible charts, and data-backed slide strategies. Use for presentations, investor decks, marketing decks, and data-driven storytelling.
---

# Slides

Turn a message into a persuasive, visually coherent presentation. Keep the narrative and the visual system aligned; a slide is not a document page with paragraphs pasted onto it.

## Workflow

1. Confirm audience, decision or action, delivery format, slide count, source data, brand, and whether the output is HTML, PPTX, PDF, or another format. For native PowerPoint work, hand off to the host’s presentations capability after the content/design contract is ready.
2. Read `references/create.md`, then load only the relevant layout, strategy, copywriting, and template references.
3. Search the local slide datasets with `scripts/search.py`; treat those rows as evidence, then choose strategy, layout, copy formula, chart, typography, colors, and background direction through the current task context rather than a coded recommendation layer.
4. Build an outline where each slide has one job, one headline claim, supporting evidence, and a clear transition. Use charts only when they make the relationship easier to understand.
5. Consume the project token contract when one exists. `eto-apere` owns token declarations, aliases, generated CSS, and token-system validation; route there when the required contract or aliases are missing. Do not maintain a second Slides-specific token-policy scanner. Build HTML with the host’s normal artifact/code capabilities and verify the rendered deck against its actual token, contrast, state, and accessibility obligations.
6. Select imagery and backgrounds from current task evidence or the host’s image/search capabilities rather than a bundled fixed URL catalog. Render or preview the deck at the target viewport, check overflow and contrast, and revise before delivery. Include source files and an export when requested.

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
- `scripts/search.py` — bounded local retrieval that returns ranked source rows.
