---
name: amoye-ui-ux
description: Recommend, compare, or review coherent UI/UX direction for web and mobile interfaces from current product evidence, including product patterns, visual style, semantic color roles, typography, responsive layout, accessibility, interaction, motion, charts, reference-driven composition, proportionate design exploration, and rendered convergence. Use for design direction and UX judgment, not implementation tokens or UI code.
---

# Amọ̀ye Ojú Ìbánisọ̀rọ̀ àti Ìrírí Olùmúlò

Own one coherent interface direction from current product/project evidence and durable UX/design judgment. Do not maintain a private framework/font/style catalogue or a coded recommendation layer.

## Workflow

1. Inspect the actual product, existing brand guidance, screenshots/designs, platform, component conventions, tokens, and relevant project manifests before recommending direction. Existing approved identity and product conventions outrank bundled examples.
2. Pin the user/job, primary surfaces, platform constraints, content/data shape, accessibility needs, density, and existing design decisions. When reviewing implementation, also pin the accepted direction and exact rendered candidate/evidence.
3. Read [quick reference](references/quick-reference.md) for the applicable interaction/layout/design branch. For native/mobile polish or a final app review, also read [professional app rules](references/pro-rules.md).
4. When a material direction is genuinely underdetermined, several materially different compositions remain credible, or an implemented result needs design convergence, read [design convergence](references/design-convergence.md). Explore only enough design space to expose a real choice; do not manufacture variants when current evidence already determines the direction.
5. When internal evidence does not adequately establish visual treatment, component composition, interaction detail, or polish, read [reference-driven composition](references/reference-driven-composition.md). Use live exemplars to strengthen judgment, not to outsource it or copy a design.
6. Resolve one direction: product pattern, visual character, semantic color roles, typography behavior, density, layout hierarchy, interaction/state behavior, motion policy, data/chart treatment, and a short anti-pattern list. Use current primary sources only for volatile platform/framework requirements that can change the recommendation; do not cache them here.
7. When a screenshot, mockup, prototype, or other visual reference materially controls acceptance, enumerate materially visible and interactive affordances separately from underlying semantic capability. For each, explicitly adopt, preserve, adapt, or reject it. Do not treat support for a semantic node/state/component as proof that its visible affordance, hierarchy, discoverability, or interaction matches the accepted direction.
8. When a recommendation becomes application UI code or a reusable token/component implementation contract, route delivery to `alaga` with the accepted direction, material affordance expectations, and any identity constraints that govern implementation. Use `brand` when durable identity itself is missing or changing.

## Decision rules

- Prefer current product/brand evidence over generic industry stereotypes.
- Treat approved product/brand constraints that the request does not reopen as invariants, not dimensions to vary for novelty.
- Explore alternatives only when a material decision is genuinely open; different palettes or cosmetic permutations of one composition are not meaningful alternatives.
- Use external references to answer a bounded design question; do not browse for novelty after the direction is already supported.
- Extract transferable hierarchy, composition, interaction, motion, density, and state-treatment principles. Do not reproduce distinctive layouts, illustrations, copy, branding, or proprietary assets.
- Use semantic color roles and accessible foreground/background pairs; do not invent a palette because a template says blue or green is conventional.
- For web surfaces, use current **WCAG** guidance as the accessibility baseline; for native/mobile surfaces, use current platform accessibility guidance plus applicable cross-platform principles. When custom/composed web widgets need interaction semantics beyond native/library behavior, use the current **WAI-ARIA Authoring Practices (APG)** as a reasoning/reference anchor rather than maintaining a bundled accessibility manual.
- Prefer established platform primitives and predictable interaction behavior over decorative novelty.
- Make normal, loading, empty, error, disabled, focus/pressed, and recovery states explicit when the surface needs them.
- Use responsive behavior from content and hierarchy, not fixed device-size folklore.
- Motion must explain state/relationship and respect reduced-motion preferences.
- Charts must make the intended comparison/relationship easier to understand and never rely on color alone.
- Treat framework/component-library specifics as implementation-owner/current-tool evidence, not durable UX truth.
- Review observed rendered behavior when visual/interaction fidelity is material; do not infer acceptance from source-code intent.

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

When a supplied visual reference materially shaped acceptance, also identify:

- semantic capability expectations;
- materially visible/interactive affordances;
- adopt | preserve | adapt | reject disposition for each; and
- any affordance whose acceptance still needs rendered/interaction proof.

When material exploration shaped the direction, also identify the unresolved design question, materially different candidates considered, selected direction and decision-changing rationale, and only rejected alternatives whose rejection constrains future implementation.

When external references materially shaped the direction, also identify:

- bounded design question;
- selected exemplars;
- transferable principles adopted;
- rejected mismatches; and
- any evidence gap.

### Review

Return:

- accepted direction or controlling evidence;
- exact rendered candidate/evidence when material;
- violated UX/design principle, direction constraint, or material affordance expectation;
- affected behavior;
- evidence;
- smallest useful correction; and
- any remaining material design deficiency or evidence gap.

Do not request another review pass when no material deficiency remains.
