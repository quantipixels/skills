---
name: amoye-ui-ux
description: Recommend, compare, or review coherent UI/UX direction for web and mobile interfaces from current product evidence, including product patterns, visual style, semantic color roles, typography, responsive layout, accessibility, interaction, motion, charts, reference-driven composition, proportionate design exploration, and rendered convergence. Use for design direction and UX judgment, not implementation tokens or UI code.
---

# Amọ̀ye Ojú Ìbánisọ̀rọ̀ àti Ìrírí Olùmúlò

Own one coherent interface direction from current product/project evidence and durable UX/design judgment. Do not maintain a private framework/font/style catalogue or a coded recommendation layer.

## Workflow

1. Inspect the actual product, existing brand guidance, screenshots/designs, platform, component conventions, tokens, and relevant project manifests before recommending direction. Existing approved identity and product conventions outrank bundled examples.
2. Pin the user/job, primary surfaces, platform constraints, content/data shape, accessibility needs, density, existing design decisions, and—when reviewing implementation—the accepted direction plus the exact rendered candidate/evidence available.
3. Read [quick reference](references/quick-reference.md) for the applicable interaction/layout/design branch. For native/mobile polish or a final app review, also read [professional app rules](references/pro-rules.md).
4. When the material direction is genuinely underdetermined, several materially different compositions are credible, or an implemented result needs design convergence, read [design convergence](references/design-convergence.md). Explore only enough design space to expose a real choice; do not manufacture variants when current evidence already determines the direction.
5. When internal evidence does not adequately establish visual treatment, component composition, interaction detail, or polish, read [reference-driven composition](references/reference-driven-composition.md). Use live exemplars to strengthen judgment, not to outsource it or copy a design.
6. Resolve one direction: product pattern, visual character, semantic color roles, typography behavior, density, layout hierarchy, interaction/state behavior, motion policy, data/chart treatment, and a short anti-pattern list. When exploration was warranted, make the materially different candidates comparable, select one coherent direction, and retain only rejection rationale that constrains implementation or prevents likely regression. Use current primary sources only for volatile platform/framework requirements that can change the recommendation; do not cache them here.
7. When a recommendation becomes React/web UI code, route implementation to `asa-oju-ibanisoro`. When confirmed direction needs canonical tokens/component specifications, route that contract to `eto-apere`. Use `brand` when identity itself is missing or changing.
8. When an exact implementation render returns for design review, judge the observed result against the accepted direction and controlling product evidence rather than against imagined source code. Return only material deficiencies and smallest useful corrections. The implementation owner applies corrections and rerenders; repeat review only while a material design deficiency or evidence gap remains.
9. When the accepted direction or completed convergence establishes non-obvious reusable project-specific design knowledge, use `amose` to reconcile that knowledge. Do not persist generic design advice or transient taste as project truth.

## Decision rules

- Prefer current product/brand evidence over generic industry stereotypes.
- Explore alternatives only when a material decision is genuinely open. Different palettes or cosmetic permutations of the same composition are not meaningful alternatives.
- Compare candidates by the user job, hierarchy, information architecture, density, interaction/state behavior, accessibility, brand fit, platform fit, and implementation constraints that actually govern the work; do not invent weighted scores or false precision.
- Use external references to answer a bounded design question; do not browse for novelty after the direction is already supported.
- Extract transferable hierarchy, composition, interaction, motion, density, and state-treatment principles. Do not reproduce distinctive layouts, illustrations, copy, branding, or proprietary assets.
- Use semantic color roles and accessible foreground/background pairs; do not invent a palette because a template says blue or green is conventional.
- Prefer established platform primitives and predictable interaction behavior over decorative novelty.
- Make normal, loading, empty, error, disabled, focus/pressed, and recovery states explicit when the surface needs them.
- Use responsive behavior from content and hierarchy, not fixed device-size folklore.
- Motion must explain state/relationship and respect reduced-motion preferences.
- Charts must make the intended comparison/relationship easier to understand and never rely on color alone.
- Treat framework/component-library specifics as implementation-owner/current-tool evidence, not durable UX truth.
- A polished-looking render is not accepted merely because it is attractive; it must preserve the accepted job, hierarchy, states, accessibility, and product constraints.

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

When design exploration materially shaped the direction, also identify:

- the unresolved design question;
- materially different candidates considered;
- selected direction and decision-changing rationale; and
- rejected alternatives only where their rejection constrains future implementation.

When external references materially shaped the direction, also identify:

- bounded design question;
- selected exemplars;
- transferable principles adopted;
- rejected mismatches; and
- any evidence gap.

### Review

Return:

- accepted direction or controlling evidence;
- exact rendered candidate/evidence reviewed;
- violated UX/design principle or direction constraint;
- affected behavior;
- evidence;
- smallest useful correction; and
- any remaining material design deficiency or evidence gap.

Do not request another review pass when no material deficiency remains.

## Resources

- `references/quick-reference.md` — durable cross-platform UX/design judgment.
- `references/pro-rules.md` — native/mobile polish and final delivery checks.
- `references/reference-driven-composition.md` — live exemplar scouting and synthesis when internal evidence is insufficient.
- `references/design-convergence.md` — proportionate design-space exploration, selection, rendered review, and convergence.
