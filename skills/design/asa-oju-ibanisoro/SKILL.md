---
name: asa-oju-ibanisoro
description: Implement polished, accessible, responsive React/web interfaces with an explicit component-library decision, project-native tooling, semantic tokens, and verified interaction behavior. Use for components, forms, navigation, tables, charts, themes, responsive layouts, product icons, and UI quality fixes.
---

# Àṣà Ojú Ìbánisọ̀rọ̀

Implement confirmed UI direction in application code. Preserve the project's framework, component system, tokens, and conventions; use accessible primitives rather than rebuilding mature interaction behavior.

## Before coding

1. Inspect the actual project, manifests, component conventions, configuration, and current tooling before assuming framework/tool versions or UI libraries. Use the project's own package manager/wrappers and current tool/project documentation rather than cached QP commands.
2. If visual direction is missing, use `amoye-ui-ux`. If canonical tokens/specifications are missing or changing materially, use `eto-apere`.
3. Read [component-library decision](references/ui-component-libraries.md) when the project/user has not already settled the library. Never silently introduce a competing library.
4. Load only applicable implementation references: accessibility, theming, or Tailwind customization. Use current official/project documentation for volatile component APIs and utility syntax instead of bundled manuals.

## Implementation rules

- Prefer confirmed library/native primitives for dialogs, menus, forms, tabs, popovers, comboboxes, tables and similar stateful interaction.
- Use semantic project tokens and existing utility conventions; do not scatter new raw color/spacing defaults through components.
- Build responsive behavior from content hierarchy and the project's breakpoints rather than adding QP-owned breakpoint scales.
- Give applicable controls visible hover/focus/pressed/disabled/loading/error behavior and accessible names.
- Preserve keyboard operation, sensible focus order, touch usability, reduced-motion behavior, and media-space reservation.
- Use an established icon library or confirmed Brand icon language; do not use emoji as structural UI icons.
- For charts, keep labels/units/legends/tooltips as needed and provide non-color distinctions for material series/status.

## Platform configuration

Use the active project's native configuration/tooling and version-specific documentation. Preview/inspect tool-driven changes when supported and follow the project's actual configuration model rather than inventing QP defaults or a competing config surface.

## Verification

Run the project's applicable native proof for the changed area, then inspect the rendered UI for accepted surfaces/states. Verify only supported platforms/viewports/states, including keyboard/focus, contrast, overflow, loading/empty/error behavior, and reduced motion where applicable.

## Resources

- `references/ui-component-libraries.md` — component-library selection method.
- `references/shadcn-accessibility.md` — non-obvious accessibility/interaction calibration when shadcn/Radix patterns apply.
- `references/shadcn-theming.md` — shadcn theme/token integration when selected.
- `references/tailwind-customization.md` — project-native Tailwind extension guidance.
