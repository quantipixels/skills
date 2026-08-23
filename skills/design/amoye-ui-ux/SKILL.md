---
name: amoye-ui-ux
description: Use data-backed UI/UX design intelligence when designing or reviewing web and mobile interfaces, including product patterns, visual styles, color palettes, typography, responsive layout, accessibility, animation, charts, and stack-specific guidance. Trigger for visual or interaction decisions; skip pure backend, infrastructure, or non-visual work.
---

# Amọ̀ye Ojú Ìbánisọ̀rọ̀ àti Ìrírí Olùmúlò

Provide evidence-backed design recommendations from the bundled searchable database. The skill covers 84 styles, 192 color palettes, 74 font pairings, 192 product types, 98 UX guidelines, 104 icon entries, 16 motion presets, 25 chart types, and 22 implementation stacks.

## Core workflow

1. Inspect the project before recommending a stack. Check `package.json`, `pubspec.yaml`, `Package.swift` or Xcode projects, `composer.json`, and React Native markers. If no stack is detectable, ask or use `html-tailwind` only after stating the assumption.
2. For a new page or project, run the design-system search first. Combine product type, industry, audience, tone, and density in the query.
3. Run focused searches only where needed: `product`, `style`, `color`, `typography`, `google-fonts`, `chart`, `ux`, `landing`, `icons`, `gsap`, `react`, or `web`.
4. Run the matching stack search after the stack is known.
5. Synthesize the returned recommendations into tokens, layout rules, interaction behavior, implementation guidance, and a short anti-pattern list. Do not paste raw search output as a design.
6. Before delivery, read `references/pro-rules.md` for the canonical checklist. For detailed UX rationale, read `references/quick-reference.md` on demand.

When the recommendation will become React UI code, route implementation through `asa-oju-ibanisoro` and do not proceed until its UI component-library choice is confirmed.

## Running the bundled search

Resolve `<skill-root>` to this skill directory and use an absolute path when invoking scripts; never assume the project directory contains them:

```bash
python <skill-root>/scripts/search.py "saas analytics dashboard accessible" --design-system -p "Ops Console"
python <skill-root>/scripts/search.py "keyboard focus loading" --domain ux
python <skill-root>/scripts/search.py "streaming rerender bundle" --stack nextjs
```

The command supports `--design-system`, `--variance 1-10`, `--motion 1-10`, `--density 1-10`, `--domain`, `--stack`, `-n`, and `--json`. Text output uses one Markdown representation; JSON exposes the same structured result for composition. The calling workflow owns any durable plan, report, design-system file, or page override. This skill does not create a parallel state tree.

If a search returns no results, broaden the query once. If it is still empty, use the priority rules below and clearly say that the recommendation came from defaults, not a database match. Never fabricate a database result.

## Priority rules

1. Accessibility: 4.5:1 contrast, alt text, keyboard navigation, visible focus, and labels.
2. Touch and interaction: 44×44px targets, 8px spacing, loading feedback, and no hover-only behavior.
3. Performance: WebP/AVIF, lazy loading, reserved space, and no layout thrashing.
4. Style selection: match the product and keep the visual system coherent; use SVG icons rather than emoji.
5. Responsive layout: mobile-first breakpoints, viewport meta, and no horizontal scrolling.
6. Typography and color: 16px body baseline, readable line-height, semantic tokens, and sufficient contrast.
7. Animation: 150–300ms for ordinary transitions, meaningful motion, and reduced-motion support.
8. Forms and feedback: visible labels, nearby errors, helper text, and progressive disclosure.
9. Navigation: predictable back behavior, shallow hierarchy, and no overloaded bottom navigation.
10. Charts: legends, tooltips, accessible colors, and redundant encodings beyond color alone.

## Output contract

For a design recommendation, return the selected product pattern, style, palette, typography, effects, implementation stack, accessibility constraints, and anti-patterns. For a review, cite the violated rule, the affected UI behavior, and the smallest useful correction. Keep the database query and the synthesized decision distinct.

## Resources

- `references/quick-reference.md` — detailed UX rules and rationale.
- `references/pro-rules.md` — final UI polish and accessibility checklist.
- `data/` — searchable CSV knowledge base.
- `scripts/search.py` — primary search and design-system generator.
- `scripts/validate_data.py` — CSV/schema validation.
