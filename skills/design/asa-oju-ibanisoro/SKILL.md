---
name: asa-oju-ibanisoro
description: Implement polished, accessible, responsive React/web interfaces with an explicit component-library decision, project-native tooling, semantic tokens, verified interaction behavior, and rendered design convergence when an accepted UI direction materially governs the result. Use for components, forms, navigation, tables, charts, themes, responsive layouts, product icons, and UI quality fixes.
---

# Àṣà Ojú Ìbánisọ̀rọ̀

Implement confirmed UI direction in application code. Preserve the project's framework, component system, tokens, and conventions; use accessible primitives rather than rebuilding mature interaction behavior.

## Before coding

1. Inspect the actual project, manifests, component conventions, configuration, and current tooling before assuming framework/tool versions or UI libraries. Use the project's own package manager/wrappers and current tool/project documentation rather than cached generic commands.
2. If visual direction is missing, use `amoye-ui-ux`. When implementation follows a confirmed Amọ̀ye direction, retain the exact direction/controlling evidence needed to review the rendered result without reconstructing intent from code. If canonical tokens/specifications are missing or changing materially, use `eto-apere`.
3. Read [component-library decision](references/ui-component-libraries.md) when the project/user has not already settled the library. Never silently introduce a competing library. When introducing or switching a library materially changes system-wide source ownership, runtime/bundle architecture, compatibility/migration, or long-term integration boundaries, use `solution-architect` for that technical decision before implementation.
4. For accessibility, component APIs, theming, utility/framework configuration, and version-specific behavior, use the selected library/framework's current official documentation plus current project conventions. Do not rely on bundled framework manuals.

## Implementation rules

- Prefer confirmed library/native primitives for dialogs, menus, forms, tabs, popovers, comboboxes, tables and similar stateful interaction.
- Use semantic project tokens and existing utility conventions; do not scatter new raw color/spacing defaults through components.
- Build responsive behavior from content hierarchy and the project's breakpoints rather than adding repository-owned breakpoint scales.
- Give applicable controls visible hover/focus/pressed/disabled/loading/error behavior and accessible names.
- Preserve keyboard operation, sensible focus order, touch usability, reduced-motion behavior, and media-space reservation.
- Use an established icon library or confirmed `brand` icon language; do not use emoji as structural UI icons.
- For charts, keep labels/units/legends/tooltips as needed and provide non-color distinctions for material series/status.

## Platform configuration

Use the active project's native configuration/tooling and version-specific documentation. Preview/inspect tool-driven changes when supported and follow the project's actual configuration model rather than inventing defaults or a competing config surface.

## Verification and design convergence

1. Run the project's applicable native proof for the changed area, then inspect the rendered UI for accepted surfaces/states. Verify only supported platforms/viewports/states, including keyboard/focus, contrast, overflow, loading/empty/error behavior, and reduced motion where applicable.
2. When an accepted `amoye-ui-ux` direction materially governs the result and visual/interaction fidelity remains consequential or uncertain, return the exact current render/evidence plus the accepted direction to Amọ̀ye for review. Do not ask Amọ̀ye to infer the result from source code when a rendered surface can establish it.
3. Apply accepted material corrections through the implementation's normal proof path, then rerender the affected surfaces/states. Re-run only proof invalidated by the correction.
4. Request another design-review pass only when the changed render can materially alter the prior verdict or clear an evidence gap. Stop when no material design deficiency remains against the accepted direction; do not loop indefinitely for subjective polish alternatives.

The implementation owner retains code, framework, native proof, and candidate identity. Amọ̀ye retains design judgment. Neither owner absorbs the other's lifecycle or result.

## Resources

- `references/ui-component-libraries.md` — component-library selection method when the choice is not already settled.
