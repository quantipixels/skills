# UI delivery

Read when an Alága build job materially changes a user-facing web/mobile interface, component system, design-token contract, responsive behavior, or rendered interaction.

UI work remains one software-delivery job unless a separate design/identity/architecture judgment is independently useful. Alága owns implementation, exact candidate identity, native proof, and convergence. A confirmed `amoye-ui-ux` direction or `brand` identity is controlling input when present; do not invoke either merely because UI exists. Use `amoye-ui-ux` when the visual/interaction direction itself is materially underdetermined or needs independent rendered judgment, and `brand` only when durable identity itself is missing/changing. A component-library decision belongs to `architect` only when it materially changes system-wide ownership, runtime/bundle architecture, compatibility/migration, or another architecture boundary.

## Start from current product reality

Inspect the actual project before choosing UI mechanism: framework/runtime, manifests/lockfiles, existing component primitives/library, tokens/themes, layout conventions, supported platforms, current rendered surfaces, and accepted product/design evidence. Reuse the established system when it satisfies the job. Do not introduce a competing UI library, token system, breakpoint scale, icon language, or style vocabulary by convenience.

If a component-library choice is genuinely unsettled, compare only credible current options against the needs that can change the decision: framework/version compatibility, accessible interaction primitives, theming/token model, source ownership, runtime/bundle impact, component breadth actually needed, customization burden, maintenance horizon, migration/lock-in, and licensing where material. Confirm volatile APIs/install steps from current project/first-party sources.

## Implement behavior and presentation together

- Prefer native or established accessible primitives for dialogs, menus, forms, tabs, popovers, comboboxes, tables, and similar stateful interaction instead of rebuilding mature behavior for visual novelty.
- Preserve accessible names, keyboard/touch operation, visible focus and applicable pressed/disabled/loading/error states, sensible focus order, reduced-motion behavior, and recovery/cancel paths.
- Let content hierarchy and the project's existing responsive model drive reflow. Do not import generic device breakpoints or spacing scales as project truth.
- Use semantic project tokens and existing utility/style conventions rather than scattering new raw values through components.
- Reserve media/async space where layout shift matters and verify overflow at the supported narrow/wide boundaries relevant to the job.
- For charts/data views, choose the representation from the comparison/relationship the user must perceive; preserve labels/units and non-color distinctions when material.

Use current WCAG guidance as the web accessibility baseline when accessibility claims are material. For custom/composed web widgets whose semantics are not already owned by native/library primitives, use current WAI-ARIA APG guidance rather than cached interaction recipes.

## Token and component contracts

When the job needs reusable design-system structure, use three ownership layers:

```text
confirmed primitive values
→ semantic purpose aliases
→ component property/state aliases only when needed
```

The layers describe responsibilities, not a default palette or scale.

- Primitive values come from accepted project/brand evidence; do not seed colors, typography, spacing, radii, shadows, motion, or dimensions from QP defaults.
- Semantic aliases describe purpose and are the normal theme-switching boundary.
- Add a component alias only when a real reusable property/state must remain governed across implementations/themes; do not tokenise every CSS property or mirror a component catalogue.
- Preserve semantic/component aliases rather than flattening them to raw values.
- Define component anatomy, variants, states, responsive/theme differences, and token relationships only where current product/library evidence establishes them. Missing evidence stays a gap rather than being completed from familiar design-system schemas.
- Prefer the active project's existing token/compiler/configuration path. If none exists, choose the smallest current project-native or mature focused capability that realizes the accepted contract; do not add a QP-specific fallback compiler merely to make token generation deterministic.

## Prove the rendered result proportionately

Run the project's native code/build/type/lint/test proof appropriate to the changed seam. Add rendered inspection when visual hierarchy, responsive behavior, interaction state, accessibility behavior, or fidelity is part of acceptance and cannot be established cheaply from other proof.

Inspect only relevant supported surfaces/states: normal plus credible loading/empty/error/disabled/recovery states, narrow/wide layouts, keyboard/focus, contrast, overflow, reduced motion, and changed integration boundaries as applicable. Do not mechanically test every dimension for every UI change.

When a confirmed `amoye-ui-ux` direction materially governs acceptance and independent design judgment can still change the result, return the exact rendered evidence plus the accepted direction/affordance constraints for review. Apply accepted corrections through Alága's normal implementation/proof path and request another design pass only when the new render can materially change the previous verdict or clear an evidence gap.

The implementation must remain startable and reviewable without reconstructing hidden design intent from source code, but design review does not become a second delivery lifecycle.
