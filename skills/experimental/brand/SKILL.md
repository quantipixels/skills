---
name: brand
description: Define, update, create, and review brand voice, messaging, visual identity, logos, corporate identity, custom icon language, approved assets, and consistency. Use when branded output needs a durable human-readable identity source of truth or an on-brand review.
---

# Brand

Own the project's durable human-readable brand meaning and approved identity assets. Existing approved guidance is authoritative unless the user explicitly changes it. Keep implementation tokens and product UI implementation outside this semantic identity result.

## Workflow

1. Inspect existing brand guidance, identity assets, product surfaces, language/message evidence, and asset conventions before proposing change. Do not infer a brand from an industry/style catalogue.
2. For a new or materially revised identity, define only what current evidence/approval establishes: audience, positioning, voice/personality, messaging/claims, semantic color roles, typography direction, imagery, logo constraints, icon language when needed, and prohibited treatments. Read [language and messaging](references/language-and-messaging.md) when that branch is material. Use [the minimal brand scaffold](templates/brand-guidelines-starter.md) only when the project lacks an existing source of truth.
3. For color or typography decisions that require reusable depth, read [color palette management](references/color-palette-management.md) or [typography specifications](references/typography-specifications.md) only when that branch is active.
4. For logo/corporate-identity work, read only the relevant [logo design](references/logo-design.md), [corporate identity design](references/cip-design.md), and [logo usage rules](references/logo-usage-rules.md). Explore from the current brief/evidence rather than a bundled style database.
5. For custom icon language, read [icon design](references/icon-design.md) and define only the grid, stroke/fill, corners, optical sizing, naming, and export behavior the identity needs.
6. For asset organization/review, preserve the project's existing convention; read [asset organization](references/asset-organization.md) only when organization itself is unresolved. Do not impose generic filenames, dimensions, formats, or size limits.
7. For an on-brand review, use [consistency checklist](references/consistency-checklist.md) and [approval checklist](references/approval-checklist.md) only when their deeper checks are useful. Report evidence and the smallest correction, not taste alone.

## Decision rules

- Prefer project/user evidence over generic color psychology, industry stereotypes, trend catalogues, brand-archetype formulas, or AI-prompt keyword lists.
- Use semantic color roles in guidance; exact implementation values belong to the confirmed implementation contract.
- Define accessible foreground/background pairs and supported theme behavior.
- Keep logo lockups, clear space/minimum-size rules, prohibited transformations, and approved variants explicit only when they are actually established for this brand.
- Do not claim an asset, claim, tagline, differentiator, or message is approved without evidence/approval.
- Derive visual exploration from the confirmed brief; do not maintain a parallel prompt/style catalogue.

## Durable destination

Preserve the project's existing brand source-of-truth location and asset conventions when they exist. Do not invent a default docs path, registry, manifest, or repository layout merely because Brand needs durable guidance.

When no durable destination exists, return the proposed brand source plus the unresolved destination/authority boundary rather than silently choosing one. Persistence mechanics do not own Brand semantics.
