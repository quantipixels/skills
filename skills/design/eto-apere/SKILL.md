---
name: eto-apere
description: Create or review a maintainable design-token and component-specification system, including primitive, semantic, and component tokens, CSS variables, states, Tailwind integration, and checked token usage. Use when confirmed visual direction must be formalized into a reusable implementation contract.
---

# Ètò Àpẹrẹ

Own the implementation contract between confirmed visual decisions and reusable tokens/specifications. Keep the three-layer architecture intact:

```text
primitive values → semantic purpose aliases → component properties/states
```

## Workflow

1. Read `references/token-architecture.md`, then inspect existing tokens, theme files, component conventions, and any confirmed `amoye-ui-ux` MASTER/page direction before adding new values. Treat Amọ̀ye direction and approved `brand` roles as visual inputs, not as a token schema or generated artifact.
2. For React projects, confirm the UI component library with `asa-oju-ibanisoro` before defining component-level tokens. The library choice must be explicit before implementation.
3. Define primitives for raw colors, spacing, type, radius, shadows, and durations.
4. Map primitives to semantic roles such as background, foreground, primary, muted, destructive, and focus.
5. Add component tokens only where a component needs a stable property or state override. Define default, hover, active, focus, disabled, loading, and error behavior when applicable.
6. Generate CSS or framework configuration from JSON rather than hand-copying values. Resolve each reference target to its canonical CSS name and emit `var(--target)`; do not flatten semantic or component aliases to raw primitive values. Preserve dark-mode overrides.
7. Validate the changed project area for hardcoded values, invalid references, contrast, and missing states. Read the relevant component, state, and Tailwind references on demand.

## Token helpers

Run from the skill root or substitute its absolute path:

```bash
node <skill-root>/scripts/generate-tokens.cjs --config tokens.json --output tokens.css
node <skill-root>/scripts/validate-tokens.cjs --dir src/
```

The generator accepts JSON token objects and validates `{path.to.token}` references, cycles, and CSS-name collisions. It emits primitive raw values and preserves semantic and component aliases. Review generated output before committing. Do not replace an existing source-of-truth token file without checking its consumers.

This skill owns all declarations in project-level `assets/design-tokens.json` and generated `assets/design-tokens.css`, including `component.slide.*`. The `slides` skill consumes this token contract and returns here when required aliases are missing. `amoye-ui-ux` MASTER/page files remain the visual-direction record and are not duplicated into this contract.

## Decision rules

- Prefer semantic aliases in components; raw hex values belong in primitives.
- Keep naming stable and put state last: `--color-primary`, `--color-primary-hover`, `--button-bg`, `--button-bg-hover`.
- Prefer a small coherent scale over one-off values.
- Make theme switching an alias change, not a component rewrite.
- Treat focus and disabled states as first-class, not optional polish.
- If the request is only to implement UI code, hand implementation to `asa-oju-ibanisoro` after the token contract is clear.

## Resources

- `references/token-architecture.md` — three-layer model and naming.
- `references/primitive-tokens.md` — raw scales.
- `references/semantic-tokens.md` — purpose aliases and themes.
- `references/component-tokens.md` — component-level values.
- `references/component-specs.md` — reusable component specification format.
- `references/states-and-variants.md` — state and variant coverage.
- `references/tailwind-integration.md` — mapping to Tailwind.
- `templates/design-tokens-starter.json` — starter token configuration.
