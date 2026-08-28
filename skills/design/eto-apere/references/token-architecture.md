# Token architecture

Use three ownership layers when the project needs a reusable token system:

```text
primitive confirmed values
→ semantic purpose aliases
→ component property/state aliases
```

The layers are responsibilities, not a prescribed palette or scale.

## Primitive

Primitive tokens hold raw confirmed design values without UI meaning:

```json
{
  "primitive": {
    "color": {
      "brand": { "$value": "<confirmed-color>", "$type": "color" }
    }
  }
}
```

Use project/brand values. Do not introduce QP default blues, grays, spacing scales, font families, radii, or shadows.

## Semantic

Semantic tokens express purpose and may change by theme:

```json
{
  "semantic": {
    "color": {
      "primary": { "$value": "{primitive.color.brand}", "$type": "color" }
    }
  }
}
```

Prefer semantic roles that consumers can understand without knowing the underlying hue/value.

## Component

Component tokens exist only where a component needs a stable property/state contract beyond the semantic layer:

```json
{
  "component": {
    "button": {
      "bg": { "$value": "{semantic.color.primary}", "$type": "color" }
    }
  }
}
```

Do not mirror every CSS property into a token. A component token earns its place when the property/state is intentionally governed across implementations/themes.

## References and themes

Preserve semantic/component references as aliases; do not resolve them to raw primitive values in generated CSS. Theme overrides normally remap semantic roles while component references stay stable.

## Canonical CSS names

When the project has no stronger naming convention, the bundled compiler maps layer paths without the layer name:

- `primitive.color.brand` → `--color-brand`
- `primitive.spacing.compact` → `--space-compact`
- `semantic.color.primary-hover` → `--color-primary-hover`
- `component.button.bg-hover` → `--button-bg-hover`

Use kebab case and keep state/variant suffixes consistent. Detect collisions before generation.

## Review questions

- Is each raw value confirmed by the project/brand rather than inherited from a starter?
- Can components depend on semantic roles instead of primitives?
- Does every component token govern a real reusable property/state?
- Can theme changes occur by alias remapping rather than component rewrites?
- Are cycles, unresolved references, and generated-name collisions impossible?
- Is the active project's own token compiler/configuration a better natural owner than the bundled fallback?
