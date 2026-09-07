# UI/UX decision reference

Load only the sections that materially control the current recommendation or review. These are durable judgment cues, not platform/API defaults; current project and authoritative platform guidance outrank examples.

## Accessibility and interaction

- Every interactive control needs an accessible name, visible focus/pressed state where applicable, and an operable keyboard/touch path.
- Do not communicate status or selection by color alone; pair color with text, shape, iconography, pattern, or position.
- Preserve predictable back/cancel/escape routes. Do not trap users inside custom interaction models without a clear recovery path.
- Use touch targets large enough for the active platform and adequate spacing between adjacent actions; expand the hit area rather than visually inflating every icon.
- Prefer semantic/native controls and established accessible primitives for dialogs, menus, forms, tabs, lists, and other stateful interaction.
- Keep loading/error feedback near the action or field that caused it; do not make the user infer whether an action succeeded.

**Counterexample:** a visually polished icon-only toolbar with 20px hit targets and no accessible labels is not professional UI.

## Layout, hierarchy, and responsiveness

- Let content priority determine layout collapse/reflow. Preserve the primary task before secondary context at narrow widths.
- Maintain readable text measure and explicit hierarchy through spacing, size, weight, grouping, and contrast rather than decorative color alone.
- Avoid horizontal overflow for ordinary application content. When wide relationships such as tables/diagrams genuinely require width, change representation or provide intentional contained scrolling.
- Reserve space for async/media content that would otherwise cause material layout shift.
- Respect safe areas/system chrome on native/mobile surfaces and keep fixed controls from covering scroll content.
- Use a coherent spacing rhythm derived from the current design system rather than importing a generic 4/8px scale as a new project rule.

## Typography and color

- Choose type from brand/product requirements, reading conditions, language support, variable-font/weight needs, and current delivery constraints. Do not select a font because it ranks highly in a bundled catalogue.
- Body text needs comfortable size/line-height and sufficient contrast; test actual foreground/background pairs in both themes when themes exist.
- Semantic roles (`background`, `surface`, `foreground`, `primary`, `muted`, `destructive`, `focus`) matter more than hue names.
- Keep functional states distinguishable in every supported theme.

## Forms and application states

- Labels remain visible when values are entered; placeholders are hints, not label replacements.
- Validate at a moment that helps correction without punishing every keystroke; keep errors specific and adjacent to their cause.
- A consequential async action should expose pending and terminal feedback and prevent accidental duplicate submission where duplicate effects are unsafe.
- Design empty, loading, partial, error, offline/degraded, permission-denied, and recovery states only when they are credible for the surface.
- Destructive operations need appropriate confirmation or undo/recovery based on consequence and reversibility—not a universal modal for every delete.

## Motion

- Motion should explain cause/effect, hierarchy, continuity, or direct manipulation. Decorative motion that competes with the task is a cost.
- Keep ordinary micro-interactions responsive and interruptible. Do not block input merely because an animation is running.
- Prefer transform/opacity when animating browser layout and avoid animation that causes layout instability.
- Respect reduced-motion preferences by preserving meaning with simpler transitions rather than merely making animation faster.

## Performance as UX

- Prevent avoidable layout shifts; size media/async regions and avoid late structural movement.
- Defer/lazy-load work only when doing so improves the user's actual startup or interaction path; do not fragment code/data blindly.
- Keep feedback latency perceptibly immediate for taps/controls. Long operations need progress or useful intermediate state rather than an indefinite spinner.
- Treat framework-specific performance mechanisms as current implementation evidence, not durable UX rules.

## Navigation and information architecture

- Users should understand where they are, what is primary, and how to go back or move forward without memorizing custom gestures.
- Deep hierarchies need orientation; flat flows do not need breadcrumbs merely because a checklist says so.
- Keep primary navigation choices bounded by the product's real top-level tasks. Avoid overloading bottom/tab navigation with infrequent destinations.

## Charts and data

Select a representation from the relationship the reader must perceive:

- comparison → bars/dot plots/common-scale comparisons;
- trend → line/area when continuity is meaningful;
- distribution → histogram/box/strip depending evidence/detail;
- composition → stacked forms only when parts-to-whole is the actual question;
- correlation → scatter when paired quantitative relationships matter;
- exact lookup → table when reading values is more important than visual pattern.

Use truthful scales, labels/units, accessible colors, and redundant encodings where series/status must remain distinguishable without color. Avoid decorative 3D, truncated axes that distort magnitude, or pie/donut charts when close comparison is the task.

## Review calibration

Good finding: `The primary action becomes unreachable when the keyboard opens; keep the CTA in the scrollable/keyboard-safe layout or provide an equivalent completion path.`

Bad finding: `Use a 24px gap because professional UI uses 24px spacing.`

Good recommendation: `Reuse the existing semantic tokens and component library, increase state contrast, and make the async submission state explicit.`

Bad recommendation: `Adopt blue, Inter, 8px spacing, and shadcn/ui because they are modern defaults.`
