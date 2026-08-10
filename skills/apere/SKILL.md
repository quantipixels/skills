---
name: apere
description: Route end-to-end visual design work across brand identity, design systems, UI styling, logos, corporate identity mockups, banners, presentations, social graphics, and icons. Use when the user asks to design or generate a visual deliverable and the correct specialist needs to be selected.
---

# Àpẹrẹ

Own the end-to-end design request and route each deliverable to the narrowest available owner. Keep design direction, brand constraints, and output requirements explicit.

## Routing

| Request | Owner |
| --- | --- |
| Brand voice, identity, assets, or consistency | `brand` |
| Tokens, CSS variables, component specs, or design-system migration | `eto-apere` |
| React/web components, Tailwind, shadcn/ui, responsive UI, or accessibility fixes | `asa-oju-ibanisoro` |
| UI/UX recommendation, style, palette, typography, or stack guidance | `amoye-ui-ux` |
| Social, ad, web hero, cover, or print banner | `banner-design` |
| HTML presentation or pitch-deck narrative | `slides` |
| Logo, corporate identity program, icon, or social graphic | This skill’s built-in design modes and the references below |

Use one primary owner. Add a supporting design skill only when it owns a concrete missing input, such as `brand` before `eto-apere` or `eto-apere` before `asa-oju-ibanisoro`. Do not turn a focused request into a full brand program without user authorization.

## Shared workflow

1. Confirm the deliverable, audience, platform, dimensions or format, source assets, brand constraints, and approval boundary.
2. Inspect the project and existing design source of truth. Run `amoye-ui-ux` for new UI direction; use `brand` when brand rules are missing or changing.
3. Choose an art direction, hierarchy, palette, typography, interaction model, and implementation/output format. For React UI implementation, use `asa-oju-ibanisoro`'s UI component-library decision gate before creating components. State important assumptions.
4. Create the artifact in its native editable format. Use the host’s image-generation capability for bitmap assets, mockups, illustrations, or logo explorations; use code/SVG/HTML for vector or interface-native output.
5. Verify dimensions, contrast, hierarchy, accessibility, responsive behavior, export quality, and source-file editability before delivery.

## Built-in design modes

### Logo

Read `references/logo-design.md`, `logo-style-guide.md`, and `logo-color-psychology.md` as needed. Search the bundled logo data before choosing a style or industry direction. Generate multiple clearly differentiated concepts, keep prompts free of unapproved claims, and deliver a vector-friendly direction with clear-space and one-color guidance. If a bitmap concept is requested, use image generation and show the result for review.

### Corporate identity program

Read `references/cip-design.md` and `cip-deliverable-guide.md`. Build a brief first, select a bounded deliverable set, and use image generation for mockup scenes only after the brand and logo constraints are known. Record which items are concepts versus approved production assets.

### Icons

Read `references/icon-design.md`. Prefer an existing icon library for product UI; generate a custom SVG set only when a distinct visual language is needed. Define grid, stroke/fill, corner, optical-size, naming, and export rules before making variants. Never use emoji as icons.

### Social graphics

Read `references/social-photos-design.md`. Confirm each platform’s ratio and crop, preserve a consistent visual system, keep text readable on mobile, and export platform-specific variants.

## References

- `references/design-routing.md` — detailed routing and multi-skill boundaries.
- `references/banner-sizes-and-styles.md` — banner constraints.
- `references/logo-design.md`, `logo-style-guide.md`, `logo-color-psychology.md` — logo direction.
- `references/cip-design.md`, `cip-deliverable-guide.md`, `cip-style-guide.md` — identity programs.
- `references/icon-design.md` — custom icon sets.
- `references/slides.md` — presentation design.
- `references/social-photos-design.md` — social assets.
- `asa-oju-ibanisoro` → `references/ui-component-libraries.md` — React component-library decision gate.
- `data/` and `scripts/` — deterministic searches for logo and CIP decisions.

## Output contract

Return the chosen owner or built-in mode, the design decisions and assumptions, the files created, and the verification performed. Keep exploratory concepts distinct from approved production assets.
