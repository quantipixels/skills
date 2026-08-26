---
name: brand
description: Define, update, create, and review brand voice, messaging, visual identity, logos, corporate identity assets, custom icon language, colors, typography, asset organization, and consistency. Use when branded output needs a durable identity source of truth, approved identity assets, or an on-brand review.
---

# Brand

Own the project’s human-readable brand source of truth and its identity assets. Keep voice, visual identity, messaging, logo and icon-language rules, asset constraints, and approval criteria together. Keep implementation-token mutation with `eto-apere`.

## Workflow

1. Find existing brand guidance, logo files, identity assets, token files, and asset manifests. Treat existing approved guidance as authoritative unless the user explicitly changes it.
2. For a new or changed brand, define audience, positioning, voice, personality, color roles, typography, imagery, logo constraints, icon language when custom icons are required, and prohibited treatments. Use `templates/brand-guidelines-starter.md` as a starting point.
3. For an update, change the human-readable guidance and affected identity assets, and preserve unrelated decisions. When implementation tokens must change, give `eto-apere` the confirmed color roles, typography, source-guideline path, intended token targets, current consumers, and required compatibility.
4. For a logo or corporate identity program, load only the applicable logo or CIP references below. Search the bundled identity data before choosing a direction, keep exploratory concepts distinct from approved assets, and use image generation only for approved bitmap exploration or mockups.
5. For a custom icon language, read `references/icon-design.md` and define the grid, stroke/fill, corners, optical sizing, naming, and export rules. Product UI implementation remains with `asa-oju-ibanisoro`.
6. For a review, check voice, color, typography, logo use, icon consistency, asset naming, accessibility, and cross-surface consistency. Report evidence and corrections, not taste alone.
7. Validate assets and confirm the exact current brand guidance before a downstream handoff. When implementation tokens change, consume `eto-apere`’s exact-current token and validation result.

## Identity helpers

Resolve `<brand-skill-root>` to this skill directory. Keep scripts only for deterministic identity-data search and asset-contract validation:

```bash
python3 <brand-skill-root>/scripts/search.py "technology geometric minimal" --kind logo --domain style
python3 <brand-skill-root>/scripts/search.py "professional services premium" --kind cip --all --json
python3 <brand-skill-root>/scripts/search.py "rounded optical" --kind icon
node <brand-skill-root>/scripts/validate-asset.cjs assets/logo.svg --json
```

The search helper returns ranked source rows only. It does not generate a logo brief, corporate-identity brief, palette, recommendation, or approval result; synthesize those from the current task, guidance, and retrieved evidence. Read the human-readable brand guidelines directly rather than maintaining a second parser-generated context representation. Use the host’s image-analysis capability or an installed image tool to inspect bitmap palettes, then compare the result with the current guidelines. Confirm exact source and target paths before a handoff. Do not claim token synchronization until `eto-apere` returns validated output and readback.

## Project conventions

Unless the project already has different paths, use:

- `docs/brand-guidelines.md` — human-readable identity source of truth.
- `.assets/manifest.json` — optional asset registry.

## Decision rules

- Use semantic color roles, not color names, in UI guidance.
- Do not hand token work to `eto-apere` until primary, secondary, and accent roles are present. Include any confirmed neutral, foreground, background, destructive, and focus roles.
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

Identity production:

- `references/logo-design.md`
- `references/logo-style-guide.md`
- `references/logo-color-psychology.md`
- `references/logo-prompt-engineering.md` — only when an image-generation prompt is required.
- `references/cip-design.md`
- `references/cip-deliverable-guide.md`
- `references/cip-style-guide.md`
- `references/cip-prompt-engineering.md` — only when an image-generation prompt is required.
- `references/icon-design.md`
