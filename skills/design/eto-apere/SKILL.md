---
name: eto-apere
description: Create or review a maintainable design-token and component-specification system, including primitive, semantic, and component tokens, CSS variables, states, Tailwind integration, and checked token usage. Use when a visual system must be formalized or implemented consistently.
---

# Ètò Àpẹrẹ

Own the contract between visual decisions and reusable implementation tokens. Keep the three-layer architecture intact:

```text
primitive values → semantic purpose aliases → component properties/states
```

## Workflow

1. Read `references/token-architecture.md`, then inspect existing tokens, theme files, and component conventions before adding new values.
2. For React projects, confirm the UI component library with `asa-oju-ibanisoro` before defining component-level tokens. The library choice must be explicit before implementation.
3. Define primitives for raw colors, spacing, type, radius, shadows, and durations.
4. Map primitives to semantic roles such as background, foreground, primary, muted, destructive, and focus.
5. Add component tokens only where a component needs a stable property or state override. Define default, hover, active, focus, disabled, loading, and error behavior when applicable.
6. When `brand` supplies confirmed visual roles, validate that every required role has a value and reconcile them into the existing token hierarchy without discarding unrelated tokens.
7. Validate all references before replacing token artifacts. Generate JSON and CSS to temporary targets, validate both, then install them as one accepted change. If either output fails, leave the current artifacts unchanged and do not claim partial output as synchronized.
8. Validate the changed project area for hardcoded values, invalid references, contrast, and missing states. Read the generated artifacts back, then read the relevant component, state, and Tailwind references on demand.

## Token helpers

Run from the skill root or substitute its absolute path:

```bash
node <skill-root>/scripts/generate-tokens.cjs --config tokens.json --output tokens.css
node <skill-root>/scripts/validate-tokens.cjs --dir src/
```

The generator accepts JSON token objects and resolves `{path.to.token}` references. Review generated output before committing. Do not replace an existing source-of-truth token file without checking its consumers, preserving unrelated tokens, validating references, and reading back both the JSON source and generated CSS.

Slide datasets, slide search, slide validation, background fetching, and HTML generation belong to the `slides` skill. Use its local `data/` and `scripts/` resources through the `slides` route. The token contract is the project-level `assets/design-tokens.json` and generated `assets/design-tokens.css` consumed by both skills.

## Decision rules

- Prefer semantic aliases in components; raw hex values belong in primitives.
- Keep naming stable: `--color-primary`, `--color-primary-hover`, `--button-bg`, `--button-bg-hover`.
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
