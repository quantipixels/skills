---
name: brand
description: Define, update, create, and review brand voice, messaging, visual identity, logos, corporate identity, custom icon language, approved assets, and consistency. Use when branded output needs a durable human-readable identity source of truth or an on-brand review.
---

# Brand

Own the project's durable human-readable brand meaning and approved identity assets. Existing approved guidance is authoritative unless the user explicitly changes it. Keep implementation-token mutation with `eto-apere` and product UI implementation with `asa-oju-ibanisoro`.

## Workflow

1. Inspect existing brand guidance, identity assets, product surfaces, token files, language/message evidence, and asset conventions before proposing change. Do not infer a brand from an industry/style catalogue.
2. For a new or materially revised identity, define only what current evidence/approval establishes: audience, positioning, voice/personality, messaging/claims, semantic color roles, typography direction, imagery, logo constraints, icon language when needed, and prohibited treatments. Read [language and messaging](references/language-and-messaging.md) when that branch is material. Use [the minimal brand scaffold](templates/brand-guidelines-starter.md) only when the project lacks an existing source of truth.
3. For an update, preserve unrelated approved identity decisions and change only the affected guidance/assets. When confirmed roles must become implementation tokens, use `eto-apere`.
4. For logo/corporate-identity work, load only the applicable logo/CIP references. Explore directions from the current brand brief, constraints, supplied evidence, and current visual research when needed; do not search a bundled style/industry database.
5. For custom icon language, read [icon design](references/icon-design.md) and define grid, stroke/fill, corners, optical sizing, naming, and export behavior.
6. For asset review, inspect the actual project/brand convention and use native file/image/manifest evidence. Do not impose generic filename types, dimensions, formats, or size limits.
7. For an on-brand review, check voice, claims/messages, semantic color roles, typography, logo/icon use, imagery, accessibility, asset provenance/approval, and cross-surface consistency. Report evidence and smallest correction, not taste alone.

## Decision rules

- Prefer project/user evidence over generic color psychology, industry stereotypes, trend catalogues, brand-archetype formulas, or AI-prompt keyword lists.
- Use semantic color roles in guidance; exact implementation values belong to the confirmed identity/token contract.
- Define accessible foreground/background pairs and supported theme behavior.
- Keep logo lockups, clear space/minimum-size rules, prohibited transformations, and approved variants explicit only when they are actually established for this brand.
- Do not claim an asset, claim, tagline, differentiator, or message is approved without evidence/approval.
- When generating visual exploration, derive prompts from the confirmed brand brief directly; do not maintain a parallel generic prompt catalogue.

## Durable destination

Preserve the project's existing brand source-of-truth location and asset conventions when they exist. Do not invent a default `docs/...` path, `.assets` registry, manifest, or repository layout merely because Brand needs durable guidance.

When no durable destination exists, return the proposed brand source plus the unresolved destination/authority boundary rather than silently choosing one. Use `akosile` only when the caller explicitly chooses a `.qp` owner record/artifact as the persistence mode; Brand still owns the semantic content.

## Resources

Core identity:

- `references/language-and-messaging.md`
- `references/consistency-checklist.md`
- `references/asset-organization.md`
- `references/color-palette-management.md`
- `references/typography-specifications.md`
- `references/logo-usage-rules.md`
- `references/approval-checklist.md`

Identity production:

- `references/logo-design.md`
- `references/cip-design.md`
- `references/icon-design.md`
