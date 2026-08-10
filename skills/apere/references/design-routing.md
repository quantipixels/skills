# Design routing

This repository exposes seven design skills. Use `apere` as the end-to-end owner when the request spans multiple deliverables; otherwise invoke the narrowest owner directly.

| User outcome | Primary skill |
| --- | --- |
| UI/UX direction, patterns, palettes, typography, or stack rules | `amoye-ui-ux` |
| Brand voice, identity, assets, and consistency | `brand` |
| Tokens, variables, component specs, or token migration | `eto-apere` |
| UI implementation with Tailwind, shadcn/ui, or Radix | `asa-oju-ibanisoro` |
| Social, ad, web hero, cover, or print banner | `banner-design` |
| HTML presentation or pitch deck | `slides` |
| End-to-end visual work, logos, icons, corporate identity, or social graphics | `apere` |

## Common routes

- New product UI: `amoye-ui-ux` → `eto-apere` → `asa-oju-ibanisoro`.
- Existing brand to code: `brand` → `eto-apere` → `asa-oju-ibanisoro`.
- Social presence: `brand` + `banner-design`; add `apere` for logo or mockup concepts.
- Brand identity package: `brand` → `apere` (logo/CIP modes) → `slides` if a presentation is needed.
- Custom product icon set: `apere` (icon mode) + `eto-apere` when the icons must match product tokens.

Keep one primary outcome owner. Add a supporting skill only when it owns a concrete dependency. Do not route pure backend or infrastructure work here.
