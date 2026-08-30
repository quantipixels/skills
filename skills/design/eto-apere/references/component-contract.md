# Component contract

Use when a reusable component property, variant, state, or theme behavior needs a design-system contract beyond semantic tokens. Derive the contract from confirmed product/design evidence, the selected component library, and current implementation constraints; do not begin from a QP component catalogue.

## Establish only real component meaning

For the component in scope, record only applicable fields:

```text
Component identity and purpose
Established anatomy / slots
Required variants
Required states
Property or state → semantic/component token alias
Theme/responsive differences
Implementation-library constraints
Evidence / approval source
Open gaps
```

A field may be omitted when the project/library already owns it or the product has not established it.

## Boundaries

- Do not invent default variants such as `secondary`, `success`, `warning`, `ghost`, or size tiers merely because common libraries expose them.
- Do not assign fixed heights, padding, colors, opacity, radii, focus-ring dimensions, animation durations, easing, spinner placement, or state priority without project/product evidence.
- Reuse semantic roles before adding component-specific aliases. Add a component alias only when the property/state is intentionally governed across implementations or themes.
- Preserve interaction/accessibility behavior owned by the selected primitive/library and current platform guidance. Record a design-system constraint only when the confirmed component contract materially changes or supplements that behavior.
- Keep implementation syntax, framework configuration, and library-specific component APIs with `asa-oju-ibanisoro` and the current project documentation.

## Review

A component contract is sufficient when an implementer can apply the confirmed design-system decisions without inventing a material visual/state requirement and without being forced into QP-default values. Report missing evidence rather than completing a familiar component schema for its own sake.
