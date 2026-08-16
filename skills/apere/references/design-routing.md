# Design routing

This repository exposes seven design skills. Use `apere` as the end-to-end owner when the request spans multiple deliverables; otherwise invoke the narrowest owner directly.

| User outcome | Primary skill |
| --- | --- |
| UI/UX direction, patterns, palettes, typography, or stack rules | `amoye-ui-ux` |
| Brand voice, identity, assets, and consistency | `brand` |
| Tokens, variables, component specs, or token migration | `eto-apere` |
| UI implementation with Tailwind, shadcn/ui, or Radix | `asa-oju-ibanisoro` |
| Banner, cover, header, web hero, display ad, or print banner | `banner-design` |
| HTML presentation or pitch deck | `slides` |
| Multi-deliverable visual work, logos, custom icons, corporate identity, or non-banner social systems | `apere` |

## Common routes

- New product UI: `amoye-ui-ux` → `eto-apere` → `asa-oju-ibanisoro`.
- Existing brand to code: `brand` → `eto-apere` → `asa-oju-ibanisoro`.
- Social presence: use `apere` for feed/carousel/template systems, `banner-design` for cover/header/ad surfaces, and `brand` only when brand rules are missing or changing.
- Brand identity package: `brand` → `apere` (logo/CIP modes) → `slides` if a presentation is needed.
- Custom product icon set: `apere` (icon mode) + `eto-apere` when the icons must match product tokens.

Keep one primary outcome owner. Add a supporting skill only when it owns a concrete dependency. Do not route pure backend or infrastructure work here.
