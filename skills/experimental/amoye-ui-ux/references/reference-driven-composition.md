# Reference-driven composition

Load this branch only when current product/brand evidence and durable design judgment do not adequately answer a bounded visual or interaction question. The goal is to improve the direction through live concrete exemplars, not to maintain a catalogue of fashionable sites or components.

## Scout the missing decision

Name the exact uncertainty before searching: for example dashboard density, command palette composition, onboarding progress, empty-state treatment, motion between related states, data-card hierarchy, or mobile navigation behavior. Search only far enough to expose a small set of strong, materially different exemplars.

Search by the missing design decision rather than by a fixed source list. Include the actual platform/framework/product domain when it changes relevance. A useful query shape is:

```text
<platform/framework/domain> + <bounded design question> + <interaction/state/pattern>
```

Prefer evidence in this order when applicable:

1. the product's existing UI and approved design system;
2. first-party platform, framework, component, or design-system documentation and demos;
3. maintained open-source implementations with inspectable behavior;
4. comparable live product surfaces; and
5. inspiration galleries only to discover candidates that are then verified against stronger evidence when interaction behavior matters.

Do not assume any fixed source list remains useful. Component collections, design-system demos, product screenshots, motion libraries, and framework examples are candidates only when they answer the bounded question now.

## Extract, do not copy

For each useful exemplar, identify the transferable property rather than the visual identity:

- information hierarchy and grouping;
- component composition and density;
- interaction sequence and affordances;
- responsive transformation;
- loading, empty, error, disabled, focus, pressed, and recovery treatment;
- typography or spacing behavior;
- motion purpose, timing relationship, and reduced-motion implication; and
- accessibility or discoverability characteristics.

Do not reproduce distinctive layouts, illustrations, copy, logos, branding, proprietary assets, or a recognisable visual signature. A reference is evidence for a design principle, not a template to clone.

## Fit-check against the product

Reject an exemplar when its transferable property conflicts with the actual product's user job, brand, content shape, accessibility needs, platform conventions, density, existing component system, or implementation constraints. Prefer the smallest principle that improves the current direction without forcing a foreign design language into the product.

When several exemplars are useful, synthesize compatible properties into one coherent direction. Do not average unrelated aesthetics or assemble a collage of individually attractive components.

## Handoff

Return only the evidence that changes the direction:

```text
Bounded design question
Selected exemplars + source
Transferable principles adopted
Rejected mismatches and why
Resulting composition / interaction direction
Accessibility, responsive, state, and motion constraints
Implementation constraints for alaga
Remaining evidence gaps
```

When code is needed, `alaga` owns implementation and must still preserve the project's chosen component library, tokens, framework conventions, accessibility behavior, and the accepted design direction. Do not hand off copied source code unless its license and the user's authority explicitly permit reuse and reuse is preferable to implementing the derived principle with project-native primitives.
