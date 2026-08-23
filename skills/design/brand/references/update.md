# Brand update

Use this reference when a user changes brand colors, typography, or visual direction. The brand guideline file remains the human-readable source of truth.

## Contract

Unless the project already uses another structure, update:

- `docs/brand-guidelines.md`

Collect the theme name, primary/secondary/accent colors, mood, typography, and any changed usage rules. Preserve existing decisions that were not changed.

## Procedure

1. Inspect the current guidelines and affected brand consumers.
2. Update the quick-reference palette, brand concept, typography, imagery, and prohibited treatments.
3. Re-extract the approved brand context and check its contrast pairs.
4. When tokens must change, give the approved roles, existing token paths and consumers, and compatibility constraints to `eto-apere`. Require its changed artifacts and validation result.
5. Report the brand file changed and any exact-current specialist result accepted.

```bash
node <brand-skill-root>/scripts/inject-brand-context.cjs --json docs/brand-guidelines.md
```

Do not mark the update approved unless the user or project approval system says so.

## Example presets

| Preset | Primary | Secondary | Accent |
| --- | --- | --- | --- |
| ocean-professional | #3B82F6 | #F59E0B | #10B981 |
| electric-creative | #FF6B6B | #9B5DE5 | #00F5D4 |
| forest-calm | #059669 | #92400E | #FBBF24 |
| midnight-purple | #7C3AED | #EC4899 | #06B6D4 |
| sunset-warm | #F97316 | #DC2626 | #FACC15 |

These are starting points, not approvals. Validate contrast and fit against the actual brand and audience.
