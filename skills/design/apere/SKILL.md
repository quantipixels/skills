---
name: apere
description: Route broad or multi-deliverable visual work to the narrowest design owners. Use when a design request is ambiguous, spans several deliverables, or needs design-specific prerequisites, dependency order, shared constraints, or approval boundaries; use the exact specialist directly for a focused deliverable.
---

# Àpẹrẹ

Own design-domain decomposition and routing. Return one route packet; do not create design artifacts, maintain delivery state, or copy specialist procedures.

Use the exact specialist directly when one owner fully covers the request:

| Request | Owner |
| --- | --- |
| Brand voice, identity, logo, corporate identity, assets, custom icon language, or consistency | `brand` |
| Feed posts, carousels, stories, reusable post templates, or multi-format social campaigns | `social-graphics` |
| Tokens, CSS variables, component specs, or design-system implementation/migration | `eto-apere` |
| React/web components, UI icon implementation, Tailwind, responsive UI, or accessibility fixes | `asa-oju-ibanisoro` |
| UI/UX recommendation, style, palette, typography, interaction direction, or stack guidance | `amoye-ui-ux` |
| Banner, cover, header, web hero, display ad, or print banner | `banner-design` |
| Presentation or pitch-deck narrative | `slides` |

Use `apere` when the request needs more than one of those owners, the correct owner is not yet clear, or design-specific ordering and shared constraints must be established. Read [design-routing.md](references/design-routing.md) only for that route.

Return one design route packet with:

- requested outcome and audience;
- deliverables and one primary owner for each;
- shared prerequisites and dependency order;
- safe parallel work;
- shared visual, brand, accessibility, and approval constraints;
- required output formats and exact specialist results; and
- open input gaps and the route completion boundary.

When several routed artifacts must actually be produced and integrated, hand the exact route packet to `alaga` as the build job. `apere` does not become the delivery owner.
