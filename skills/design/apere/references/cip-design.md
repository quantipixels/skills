# Corporate identity program

Use this reference for bounded brand collateral and mockup concepts.

## Build the brief

Resolve `<design-skill-root>` to this skill directory:

```bash
python <design-skill-root>/scripts/cip/search.py "technology consulting" --cip-brief --brand "BrandName"
python <design-skill-root>/scripts/cip/search.py "business card letterhead" --domain deliverable
python <design-skill-root>/scripts/cip/search.py "luxury premium" --domain style
python <design-skill-root>/scripts/cip/search.py "office reception" --domain mockup
```

Select a bounded deliverable set, audience, industry, style, materials, logo state, and output format. Read `cip-deliverable-guide.md` and `cip-style-guide.md` for the selected items.

## Mockup workflow

1. Confirm the logo and brand rules; if missing, mark the mockup as concept-only.
2. Define the scene, camera, material, scale, lighting, logo placement, and what must not change.
3. Use image generation for scene mockups and label them as conceptual. Keep text short and proofread; image models are not a substitute for production artwork.
4. Keep production collateral editable and export print-ready files separately.
5. If a set of images exists, render an HTML contact sheet with the deterministic renderer:

```bash
python <design-skill-root>/scripts/cip/render-html.py --brand "BrandName" --images ./cip-output --output cip-preview.html
```

## Handoff

Return the brief, chosen deliverables, prompt constraints, generated files, production gaps, and approval state. Do not claim print readiness from a mockup alone.
