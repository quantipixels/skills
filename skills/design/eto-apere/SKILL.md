---
name: eto-apere
description: Create or review a maintainable design-token and component-specification contract, including primitive, semantic, and component aliases, states, themes, and deterministic CSS realization. Use when confirmed visual direction must become a reusable implementation contract.
---

# Ètò Àpẹrẹ

Own the implementation contract between confirmed visual decisions and reusable tokens/component specifications:

```text
confirmed raw values → semantic purpose aliases → component properties/states
```

Do not seed a project with default colors, fonts, spacing, radii, shadows, component variants, dimensions, state treatments, animation timings, or framework mappings.

## Workflow

1. Read [token architecture](references/token-architecture.md), then inspect the project's existing tokens, theme files, component conventions, selected UI library, and confirmed `brand` / `amoye-ui-ux` direction. Existing project values and approved brand roles are inputs; do not replace them with starter defaults.
2. Define only required primitives for confirmed raw values. Map them to semantic roles such as background, foreground, primary, muted, destructive, focus, and product-specific roles.
3. Add component tokens/specifications only when a component property, variant, or state needs a stable reusable contract beyond the semantic layer. Read [component contract](references/component-contract.md) when that detail is material. Do not invent component anatomy, variants, states, sizes, timings, or accessibility behavior that the product/library has not established.
4. Preserve aliases rather than flattening semantic/component references to primitive values. Theme switching should normally remap semantic aliases rather than rewrite components.
5. Validate all token references, cycles, and CSS-name collisions before installing generated output. Prefer a current project-native token compiler when one already owns the representation; otherwise use the bundled narrow compiler.
6. Install generated artifacts through the project's normal mutation/proof path. Framework integration belongs to the active project/version and its current documentation; Ètò Àpẹrẹ supplies the token/component contract, not a cached Tailwind/shadcn/framework recipe.
7. Review changed consumers for inappropriate hardcoded values, missing required states, contrast, and broken aliases through project-native lint/typecheck/build/render proof. A raw literal is evidence to inspect, not automatically a violation.

## Token compiler

Fallback compiler usage:

```bash
node <skill-root>/scripts/generate-tokens.cjs <tokens.json> > <temporary-tokens.css>
```

The compiler owns only token-graph validation and canonical CSS realization. It validates `{path.to.token}` references, cycles, and CSS-name collisions; preserves semantic/component aliases as `var(...)`; and emits optional dark semantic overrides. The caller owns temporary/output paths, installation, framework mapping, and readback.

For one compatibility release, the compiler also accepts legacy `--config`, `--output`, and `--format css|tailwind` forms; those operational flags emit a deprecation notice. `--help` remains ordinary help. Move callers to positional input, redirected CSS stdout, and project-owned framework mapping before the next breaking release.

## Decision rules

- Prefer semantic aliases in components; raw values belong in primitives.
- Use naming from purpose/ownership, not a generic color scale.
- Keep naming stable and state last where the project has no stronger convention.
- Prefer a small coherent project-specific scale over one-off values, but do not invent a generic scale merely because it is common.
- Treat focus, disabled, loading, error, selected, and other credible states as first-class only when the component/product actually supports them.
- If the request is only UI implementation, hand it to `asa-oju-ibanisoro` after the token/spec contract is clear.
