---
name: amoye-ui-ux
description: Recommend or review coherent UI/UX direction for web and mobile interfaces, including product patterns, visual style, semantic color roles, typography, responsive layout, accessibility, interaction, motion, charts, and reference-driven composition. Use for design direction and UX judgment, not implementation tokens or UI code.
---

# Amọ̀ye Ojú Ìbánisọ̀rọ̀ àti Ìrírí Olùmúlò

Own one coherent interface direction from current product/project evidence and durable UX/design judgment. Do not maintain a private framework/font/style catalogue or a coded recommendation layer.

## Workflow

1. Inspect the actual product, existing brand guidance, screenshots/designs, platform, component conventions, tokens, and relevant project manifests before recommending direction. Existing approved identity and product conventions outrank bundled examples.
2. Pin the user/job, primary surfaces, platform constraints, content/data shape, accessibility needs, density, and any existing design decisions.
3. Read [quick reference](references/quick-reference.md) for the applicable interaction/layout/design branch. For native/mobile polish or a final app review, also read [professional app rules](references/pro-rules.md).
4. When internal evidence does not adequately establish visual treatment, component composition, interaction detail, or polish, read [reference-driven composition](references/reference-driven-composition.md). Use live exemplars to strengthen judgment, not to outsource it or copy a design.
5. Resolve one direction: product pattern, visual character, semantic color roles, typography behavior, density, layout hierarchy, interaction/state behavior, motion policy, data/chart treatment, and a short anti-pattern list. Use current primary sources only for volatile platform/framework requirements that can change the recommendation; do not cache them here.
6. When a recommendation becomes React/web UI code, route implementation to `asa-oju-ibanisoro`. When confirmed direction needs canonical tokens/component specifications, route that contract to `eto-apere`. Use `brand` when identity itself is missing or changing.

## Decision rules

- Prefer current product/brand evidence over generic industry stereotypes.
- Use external references to answer a bounded design question; do not browse for novelty after the direction is already supported.
- Extract transferable hierarchy, composition, interaction, motion, density, and state-treatment principles. Do not reproduce distinctive layouts, illustrations, copy, branding, or proprietary assets.
- Use semantic color roles and accessible foreground/background pairs; do not invent a palette because a template says blue or green is conventional.
- Prefer established platform primitives and predictable interaction behavior over decorative novelty.
- Make normal, loading, empty, error, disabled, focus/pressed, and recovery states explicit when the surface needs them.
- Use responsive behavior from content and hierarchy, not fixed device-size folklore.
- Motion must explain state/relationship and respect reduced-motion preferences.
- Charts must make the intended comparison/relationship easier to understand and never rely on color alone.
- Treat framework/component-library specifics as implementation-owner/current-tool evidence, not durable UX truth.

## Output

### Recommendation

Return:

- user/job;
- selected product/interaction pattern;
- visual direction;
- semantic color, typography, and layout rules;
- state, motion, and accessibility constraints;
- chart/data direction when relevant;
- implementation handoff constraints; and
- anti-patterns.

When external references materially shaped the direction, also identify:

- bounded design question;
- selected exemplars;
- transferable principles adopted;
- rejected mismatches; and
- any evidence gap.

### Review

Return:

- violated UX/design principle;
- affected behavior;
- evidence; and
- smallest useful correction.

## Resources

- `references/quick-reference.md` — durable cross-platform UX/design judgment.
- `references/pro-rules.md` — native/mobile polish and final delivery checks.
- `references/reference-driven-composition.md` — live exemplar scouting and synthesis when internal evidence is insufficient.
