---
name: asa-oju-ibanisoro
description: Implement polished, accessible, responsive React interfaces with an explicit UI component-library choice, shadcn/ui or other established primitives, Tailwind CSS, and token-driven visual patterns. Use for components, forms, navigation, tables, charts, themes, dark mode, responsive layouts, and UI quality fixes in web projects.
---

# Àṣà Ojú Ìbánisọ̀rọ̀

Implement the approved visual system in application code. Preserve existing project conventions and use accessible primitives rather than rebuilding interaction behavior from scratch.

## Before coding

1. Detect the framework, Tailwind version, component registry, token source, and existing layout conventions.
2. If the project is new or the visual direction is unclear, run `amoye-ui-ux` first and record the chosen system. If tokens are missing, use `eto-apere` to define them before broad implementation.
3. For React work, read `references/ui-component-libraries.md`. Inspect the project for an existing library, then ask the user to confirm reuse or choose a library before creating components. Offer the listed libraries plus a custom-components option; never introduce a competing library silently.
4. Read only the other references needed for the requested surface: component accessibility, theming, responsive behavior, utilities, or canvas design.

## UI component library decision

Ask one concise question before implementation:

> I found [existing library / no library]. Which UI component library should I use: reuse [detected library], choose from the project’s library list, or build custom components?

If the user asks for a recommendation, compare the shortlist against the project’s framework, accessibility requirements, ownership model, theming, bundle/performance budget, design-system fit, and maintenance horizon. Record the confirmed choice and use that library consistently.

## Implementation rules

- Prefer primitives from the confirmed library for dialogs, menus, forms, tabs, popovers, and similar stateful UI. Use shadcn/ui and Radix only when that is the selected project choice.
- Use semantic tokens and Tailwind utilities; do not scatter raw colors or arbitrary spacing through components.
- Build mobile-first and verify at 375px, 768px, 1024px, and 1440px or the project’s stated breakpoints.
- Give every interactive element a visible hover, focus, active, disabled, and loading treatment where applicable.
- Keep touch targets at least 44×44px, preserve keyboard navigation, and pair icon-only controls with accessible names.
- Respect `prefers-reduced-motion`, reserve media space, and avoid layout-shifting animation.
- Use SVG or an established icon library. Never use emoji as UI icons.
- For charts, include labels, legends/tooltips, accessible colors, and non-color encodings beyond color alone.

## Platform configuration

Use the active project’s package manager and official component-library or framework tooling. For shadcn/ui, inspect `components.json`, confirm the target workspace, preview the native CLI change when supported, and add components through the current `shadcn` CLI. Do not overwrite existing components unless the user explicitly accepts that replacement.

Detect the Tailwind major version before changing configuration. For Tailwind CSS v4, extend the project’s existing CSS-first theme and token imports. For Tailwind CSS v3, update the existing `tailwind.config.*` through the version’s official guidance. Do not create or replace a configuration file merely because a legacy helper expects one. Validate every change through the project’s own build, lint, and type-check commands.

## Verification

Run the project’s lint/typecheck/test commands, then inspect the rendered UI at the required breakpoints. Check focus order, keyboard operation, contrast, reduced motion, empty/loading/error states, and no-horizontal-scroll behavior. For visual artifacts or bitmap assets, use the host’s image-generation capability; do not add a provider-specific API key or hardcoded secret to the project.

## Resources

- `references/shadcn-accessibility.md` — accessible component rules.
- `references/shadcn-components.md` — component patterns.
- `references/shadcn-theming.md` — themes and token mapping.
- `references/ui-component-libraries.md` — React library inventory and required selection gate.
- `references/tailwind-customization.md` — Tailwind extension.
- `references/tailwind-responsive.md` — responsive rules.
- `references/tailwind-utilities.md` — utility patterns.
- `references/canvas-design-system.md` — canvas-first visual composition.
