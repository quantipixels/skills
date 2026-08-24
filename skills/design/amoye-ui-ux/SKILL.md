---
name: amoye-ui-ux
description: Recommend or review data-backed UI/UX direction for web and mobile interfaces, including product patterns, visual styles, color roles, typography, responsive layout, accessibility, animation, charts, and stack-specific guidance. Use for visual or interaction direction, not implementation tokens or UI code.
---

# Amọ̀ye Ojú Ìbánisọ̀rọ̀ àti Ìrírí Olùmúlò

Provide evidence-backed design direction from the bundled searchable database. Use the validated local datasets as the inventory source instead of copying row counts into the contract.

## Core workflow

1. Inspect the project before recommending a stack. Check `package.json`, `pubspec.yaml`, `Package.swift` or Xcode projects, `composer.json`, and React Native markers. If no stack is detectable, ask or use `html-tailwind` only after stating the assumption.
2. For a new page or project, run the design-system search first. Combine product type, industry, audience, tone, and density in the query.
3. Run focused searches only where needed: `product`, `style`, `color`, `typography`, `google-fonts`, `chart`, `ux`, `landing`, `icons`, `gsap`, `react`, or `web`.
4. Run the matching stack search after the stack is known.
5. Synthesize the returned recommendations into product pattern, visual style, semantic color roles, typography, density, layout rules, interaction behavior, implementation guidance, and a short anti-pattern list. Do not paste raw search output as a design and do not create the canonical token/component contract here.
6. Before native/mobile delivery, read `references/pro-rules.md`. Before web/desktop delivery, or when detailed UX rationale is needed, read `references/quick-reference.md`.

When the recommendation will become React UI code, route implementation through `asa-oju-ibanisoro`. When the confirmed direction needs canonical tokens, component specifications, generated CSS/configuration, or migration, route that implementation contract through `eto-apere`.

## Running the bundled search

Resolve `<skill-root>` to this skill directory and use an absolute path when invoking scripts; never assume the project directory contains them:

```bash
python3 <skill-root>/scripts/search.py "saas analytics dashboard accessible" --design-system -p "Ops Console"
python3 <skill-root>/scripts/search.py "keyboard focus loading" --domain ux
python3 <skill-root>/scripts/search.py "streaming rerender bundle" --stack nextjs
```

The command supports `--design-system`, `--variance 1-10`, `--motion 1-10`, `--density 1-10`, `--domain`, `--stack`, `-n`, and `--json`. Text output uses one Markdown representation; JSON exposes the same structured result for composition. The calling workflow owns any durable plan, report, design-system file, or page override. The result is confirmed visual/UX direction, not the canonical design-token or component-specification source, and this skill does not create a parallel state tree.

If a search returns no results, broaden the query once. If it is still empty, use the priority rules below and clearly say that the recommendation came from defaults, not a database match. Never fabricate a database result.

## Priority rules

1. Accessibility: 4.5:1 contrast, alt text, keyboard navigation, visible focus, and labels.
2. Touch and interaction: 44×44px targets, 8px spacing, loading feedback, and no hover-only behavior.
3. Performance: WebP/AVIF, lazy loading, reserved space, and no layout thrashing.
4. Style selection: match the product and keep the visual system coherent; use SVG icons rather than emoji.
5. Responsive layout: mobile-first breakpoints, viewport meta, and no horizontal scrolling.
6. Typography and color: 16px body baseline, readable line-height, semantic roles, and sufficient contrast.
7. Animation: 150–300ms for ordinary transitions, meaningful motion, and reduced-motion support.
8. Forms and feedback: visible labels, nearby errors, helper text, and progressive disclosure.
9. Navigation: predictable back behavior, shallow hierarchy, and no overloaded bottom navigation.
10. Charts: legends, tooltips, accessible colors, and redundant encodings beyond color alone.

## Output contract

For a design recommendation, return the selected product pattern, style, palette or semantic color roles, typography, effects, implementation stack, accessibility constraints, and anti-patterns. For a review, cite the violated rule, the affected UI behavior, and the smallest useful correction. Keep the database query, synthesized direction, and downstream implementation contract distinct.

## Resources

- `references/quick-reference.md` — detailed UX rules and rationale.
- `references/pro-rules.md` — final UI polish and accessibility checklist.
- `data/` — searchable CSV knowledge base.
- `scripts/search.py` — primary search and visual-direction generator.
- `scripts/validate_data.py` — CSV/schema validation.
