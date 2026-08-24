# Create a slide deck

Use this reference as the standalone entry point for slide work. The `slides` skill owns the narrative, local datasets, search, validation, and HTML generation.

## Workflow

1. Confirm audience, decision or action, delivery format, target viewport, slide count, brand constraints, source data, and output directory.
2. Search the local knowledge base for relevant layouts, strategies, copy patterns, typography, colors, charts, and backgrounds:

```bash
python3 <skill-root>/scripts/search-slides.py "investor roadmap" --max-results 5
```

3. Build a slide-by-slide outline with one claim, evidence, visual role, and transition per slide.
4. Before generation, require complete project token files at `assets/design-tokens.json` and `assets/design-tokens.css`, including the slide aliases declared by `eto-apere`. Stop and route to `eto-apere` when the contract is missing or incomplete.
5. Validate token usage and semantic color rules, render at the target viewport, and check overflow, contrast, keyboard access, and reduced-motion behavior.

For deterministic generation, run:

```bash
python3 <skill-root>/scripts/generate-slide.py --json deck.json --project-root <project-root> --output assets/designs/slides/deck.html
```

The generator keeps output inside `--project-root`, honors an explicit `--output`, and writes the stylesheet path relative to the generated file. If the project token contract is absent or incomplete, create or repair it through `eto-apere` first.
