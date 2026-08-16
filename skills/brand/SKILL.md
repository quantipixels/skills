---
name: brand
description: Define, update, and review brand voice, messaging, visual identity, colors, typography, logo usage, asset organization, and consistency. Use when branded UI or creative output needs a durable source of truth or an on-brand review.
---

# Brand

Own the project’s brand source of truth. Keep voice, visual identity, messaging, asset rules, and approval criteria together, then synchronize design tokens when the brand changes.

## Workflow

1. Find existing brand guidance, logo files, token files, and asset manifests. Treat the existing guidance as authoritative unless the user explicitly changes it.
2. For a new brand, define audience, positioning, voice, personality, color roles, typography, imagery, logo clear space, and prohibited treatments. Use `templates/brand-guidelines-starter.md` as a starting point.
3. For an update, read `references/update.md`, change the human-readable guidelines first, then synchronize machine-readable tokens and CSS. Preserve unrelated tokens and note breaking changes.
4. For a review, check voice, color, typography, logo use, asset naming, accessibility, and cross-surface consistency. Report evidence and corrections, not taste alone.
5. Validate assets and confirm generated context before handing off to `eto-apere`, `asa-oju-ibanisoro`, `banner-design`, or `slides`.

## Project conventions

Unless the project already has different paths, use:

- `docs/brand-guidelines.md` — source of truth.
- `assets/design-tokens.json` — generated token source.
- `assets/design-tokens.css` — generated CSS variables.
- `.assets/manifest.json` — optional asset registry.

Run helpers with the skill-root path resolved explicitly:

```bash
node <skill-root>/scripts/inject-brand-context.cjs --json docs/brand-guidelines.md
node <skill-root>/scripts/validate-asset.cjs assets/logo.svg --json
node <skill-root>/scripts/extract-colors.cjs --palette --brand-file docs/brand-guidelines.md
node <skill-root>/scripts/sync-brand-to-tokens.cjs
```

The sync helper writes two generated project files: `assets/design-tokens.json` and `assets/design-tokens.css`. The workflow edits `docs/brand-guidelines.md` separately before sync. Check all three paths and the intended project root first. The helper does not generate image assets.

## Decision rules

- Use semantic color roles, not color names, in UI guidance.
- Define accessible text/background pairs and dark-mode behavior.
- Limit typefaces and document fallback fonts.
- Keep logo lockups, clear space, minimum size, and prohibited changes explicit.
- Use consistent filenames and metadata for assets.
- Do not claim an asset is approved without a recorded approval signal.

## Resources

- `references/voice-framework.md` — tone and voice.
- `references/visual-identity.md` — visual language.
- `references/messaging-framework.md` — message hierarchy.
- `references/consistency-checklist.md` — consistency review.
- `references/brand-guideline-template.md` — detailed template.
- `references/asset-organization.md` — naming and structure.
- `references/color-palette-management.md` — palette rules.
- `references/typography-specifications.md` — type specs.
- `references/logo-usage-rules.md` — logo constraints.
- `references/approval-checklist.md` — approval gate.
- `references/update.md` — brand color, typography, or visual-direction updates.
