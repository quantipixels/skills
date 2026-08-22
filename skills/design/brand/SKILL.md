---
name: brand
description: Define, update, create, and review brand voice, messaging, visual identity, logos, corporate identity assets, custom icon language, colors, typography, asset organization, and consistency. Use when branded output needs a durable identity source of truth, approved identity assets, or an on-brand review.
---

# Brand

Own the project’s human-readable brand source of truth and its identity assets. Keep voice, visual identity, messaging, logo and icon-language rules, asset constraints, and approval criteria together. Keep implementation-token mutation with `eto-apere`.

## Workflow

1. Find existing brand guidance, logo files, identity assets, token files, and asset manifests. Treat existing approved guidance as authoritative unless the user explicitly changes it.
2. For a new or changed brand, define audience, positioning, voice, personality, color roles, typography, imagery, logo constraints, icon language when custom icons are required, and prohibited treatments. Use `templates/brand-guidelines-starter.md` as a starting point.
3. For an update, read `references/update.md`, change the human-readable guidance and affected identity assets, and preserve unrelated decisions.
4. For a logo or corporate identity program, load only the applicable logo or CIP references below. Search the bundled identity data before choosing a direction, keep exploratory concepts distinct from approved assets, and use image generation only for approved bitmap exploration or mockups.
5. For a custom icon language, read `references/icon-design.md` and define the grid, stroke/fill, corners, optical sizing, naming, and export rules. Product UI implementation remains with `asa-oju-ibanisoro`.
6. For a review, check voice, color, typography, logo use, icon consistency, asset naming, accessibility, and cross-surface consistency. Report evidence and corrections, not taste alone.
7. Validate assets and confirm generated context. When implementation tokens must change, give `eto-apere` the approved visual roles, current token consumers and paths, and required compatibility; consume its exact-current token and validation result.

## Identity helpers

Resolve `<skill-root>` to this skill directory. The moved logo and CIP search helpers retain their relative data layout:

```bash
python3 <skill-root>/scripts/logo/search.py "technology geometric minimal"
python3 <skill-root>/scripts/cip/search.py "professional services premium"
node <skill-root>/scripts/inject-brand-context.cjs --json docs/brand-guidelines.md
node <skill-root>/scripts/validate-asset.cjs assets/logo.svg --json
node <skill-root>/scripts/extract-colors.cjs --palette --brand-file docs/brand-guidelines.md
```

These helpers inspect or generate design direction; they do not own design-token mutation.

## Project conventions

Unless the project already has different paths, use:

- `docs/brand-guidelines.md` — human-readable identity source of truth;
- `.assets/manifest.json` — optional asset registry.

## Decision rules

- Use semantic color roles, not color names, in UI guidance.
- Define accessible text/background pairs and dark-mode behavior.
- Limit typefaces and document fallback fonts.
- Keep logo lockups, clear space, minimum size, and prohibited changes explicit.
- Keep a custom icon language coherent across grid, stroke/fill, corners, optical sizing, naming, and exports.
- Use consistent filenames and metadata for assets.
- Do not claim an asset is approved without a recorded approval signal.

## Resources

Core brand guidance:

- `references/voice-framework.md`
- `references/visual-identity.md`
- `references/messaging-framework.md`
- `references/consistency-checklist.md`
- `references/brand-guideline-template.md`
- `references/asset-organization.md`
- `references/color-palette-management.md`
- `references/typography-specifications.md`
- `references/logo-usage-rules.md`
- `references/approval-checklist.md`
- `references/update.md`

Identity production:

- `references/logo-design.md`
- `references/logo-style-guide.md`
- `references/logo-color-psychology.md`
- `references/logo-prompt-engineering.md` — only when an image-generation prompt is required;
- `references/cip-design.md`
- `references/cip-deliverable-guide.md`
- `references/cip-style-guide.md`
- `references/cip-prompt-engineering.md` — only when an image-generation prompt is required;
- `references/icon-design.md`.
