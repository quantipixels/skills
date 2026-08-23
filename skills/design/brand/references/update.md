# Brand update

Use this reference when a user changes brand colors, typography, or visual direction. The brand guideline file remains the human-readable source of truth.

## Contract

Unless the project already uses another structure, reconcile:

- `docs/brand-guidelines.md`
- `assets/design-tokens.json`
- `assets/design-tokens.css`

Collect the theme name, primary/secondary/accent colors, mood, typography, and any changed usage rules. Preserve existing decisions that were not changed.

## Procedure

1. Inspect the current guidelines and token consumers.
2. Update the quick-reference palette, brand concept, typography, imagery, and prohibited treatments.
3. Extract the confirmed brand context as JSON and hand its color roles, typography, source path, and intended token targets to `eto-apere`.
4. Let `eto-apere` preserve unrelated tokens, validate references, generate the CSS variables, and read back both token artifacts.
5. Check contrast pairs and report exactly which files changed.

```bash
node <brand-skill-root>/scripts/inject-brand-context.cjs --json docs/brand-guidelines.md
```

Do not overwrite a user-edited token file without reviewing it first. Do not mark the update approved unless the user or project approval system says so.

## Example presets

| Preset | Primary | Secondary | Accent |
| --- | --- | --- | --- |
| ocean-professional | #3B82F6 | #F59E0B | #10B981 |
| electric-creative | #FF6B6B | #9B5DE5 | #00F5D4 |
| forest-calm | #059669 | #92400E | #FBBF24 |
| midnight-purple | #7C3AED | #EC4899 | #06B6D4 |
| sunset-warm | #F97316 | #DC2626 | #FACC15 |

These are starting points, not approvals. Validate contrast and fit against the actual brand and audience.
