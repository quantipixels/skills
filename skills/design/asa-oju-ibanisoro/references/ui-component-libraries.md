# React UI component-library decision

Load only when the library choice is not already settled.

## Detect current reality

Inspect `package.json`, lockfiles, imports, component directories, theme files, and registry/config files such as `components.json`. Treat an existing established library as the default candidate for reuse, not an automatic mandate.

If the user already selected reuse, a named library, or custom components, preserve that choice unless it conflicts with a material project constraint.

Otherwise:

1. State what library/primitives are currently present, or that none were detected.
2. Compare only credible current options against:
   - framework/version compatibility;
   - accessibility and interaction primitives;
   - styling/token/theming model;
   - ownership model (package-owned vs copy-owned source);
   - bundle/runtime implications;
   - component breadth actually needed;
   - design-system fit and customization cost;
   - maintenance/release horizon and licensing when relevant.
3. Keep the choice inside Àṣà Ojú Ìbánisọ̀rọ̀ when it is a bounded implementation selection inside settled technical architecture. When introducing or switching a library materially changes system-wide source ownership, runtime/bundle architecture, compatibility/migration, or long-term integration boundaries, route that technical decision to `architect` and consume its exact-current result before implementation.
4. Ask for the choice when it is a material user/product preference, or recommend one when the user delegates a bounded implementation choice.
5. Confirm the current option from official/project sources before installation; do not rely on a bundled dated inventory.

## Decision signals

- Reuse the current library when it already satisfies required components, accessibility, theming and maintenance constraints.
- Prefer unstyled/accessibility primitives when the project owns a custom visual system and needs behavior without a prescribed look.
- Prefer a broader styled system when product speed/component breadth matters more than source-level visual ownership.
- Prefer copy-owned primitives when the team explicitly values source ownership and is prepared to maintain the copied components.
- Choose custom interaction only when established primitives cannot satisfy a real requirement; do not rebuild complex accessibility behavior for visual uniqueness alone.

## Output

Record the detected evidence, selected library/custom decision or delegated architecture decision, why it fits the actual project, integration/theming constraints, migration/lock-in implications, and the first components/primitives affected.

Use the selected library's current docs/CLI/project installation for component names and commands. Do not maintain a component catalogue.
