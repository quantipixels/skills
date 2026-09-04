# Icon direction

Use this reference for custom SVG icon sets. For ordinary product UI, prefer an established library and let `alaga` own implementation through the current product's UI-delivery path.

## Define the system

Set the grid, optical size, stroke/fill model, corner treatment, cap/join, color tokens, naming, sizes, and accessibility behavior before drawing variants. Keep the same geometry and visual weight across the set.

## Creation rules

- Use SVG for interface icons; provide viewBox, scalable paths, and no embedded raster images.
- Use `currentColor` or semantic tokens instead of hardcoded colors.
- Provide 16, 20, 24, and 32px variants only when the product needs them.
- Add accessible names in the consuming UI; decorative icons must be hidden from assistive technology.
- Never use emoji as a substitute for an icon.
- Use image generation only for visual exploration. Convert approved directions into hand-authored SVG and review at actual size.

## Handoff

Return the icon grid, style specification, filenames, exports, and a checklist covering alignment, optical balance, contrast, and accessibility. Treat generated concepts as unapproved until reviewed.
