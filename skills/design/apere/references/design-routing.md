# Design routing

Use `apere` only when a visual request is broad, ambiguous, spans multiple deliverables or owners, or needs design-specific prerequisites, dependency order, shared constraints, or approval boundaries. Otherwise invoke the narrowest owner directly.

| User outcome | Primary skill |
| --- | --- |
| UI/UX direction, patterns, palettes, typography, persisted MASTER direction, or stack rules | `amoye-ui-ux` |
| Brand voice, identity, logos, corporate identity, custom icon language, assets, and consistency | `brand` |
| Feed posts, carousels, stories, reusable social templates, or multi-format social campaigns | `social-graphics` |
| Tokens, variables, component specs, generated configuration, or design-system migration | `eto-apere` |
| UI implementation with Tailwind, component primitives, or accessible product icons | `asa-oju-ibanisoro` |
| Banner, cover, header, web hero, display ad, or print banner | `banner-design` |
| Presentation or pitch deck | `slides` |
| Multi-owner or ambiguous visual work needing a route packet | `apere` |

## Common routes

- New product UI: `amoye-ui-ux` → `eto-apere` → `asa-oju-ibanisoro`.
- Existing brand to code: `brand` → `eto-apere` → `asa-oju-ibanisoro`.
- Social presence: `social-graphics` for post/carousel/story/template systems, `banner-design` for cover/header/ad surfaces, and `brand` only when identity rules are missing or changing.
- Brand identity package: `brand` owns logo and corporate identity assets; add `slides` only when a presentation is a separate requested outcome.
- Custom product icon system: `brand` defines the visual language; `asa-oju-ibanisoro` implements it in product UI; add `eto-apere` only when token contracts are affected.
- Multi-deliverable campaign or product launch: `apere` returns the owner/dependency route packet, then `alaga` owns actual integrated production when several artifacts must be delivered together.

Keep one primary outcome owner. Add a supporting skill only when it owns a concrete dependency. Do not route pure backend or infrastructure work here.
