# Native/mobile polish and delivery checks

Load for native/mobile UI or when a mobile interface looks technically correct but visually/interaction-wise unpolished. Use project/platform conventions first; these are cross-platform calibration cues.

## Visual and control consistency

- Use one coherent icon language per hierarchy level; prefer vector/system icons and official brand assets.
- Keep icon optical size, stroke/fill style, alignment, and surrounding hit area consistent.
- Interaction feedback must not shift surrounding layout unexpectedly.
- Use semantic theme roles rather than per-screen hardcoded colors.
- Keep disabled, selected, focused/pressed, loading, success, and error states visibly distinct.

## Native interaction

- Respect safe areas, keyboard/inset behavior, system navigation gestures, back/cancel expectations, and platform accessibility semantics.
- Give controls platform-appropriate touch targets; a small visible icon may use a larger invisible hit area.
- Prefer system/established primitives for high-interaction controls unless a confirmed product requirement justifies custom behavior.
- Keep animations responsive, interruptible, and reduced-motion aware.
- Avoid nested tap/drag/scroll gesture conflicts; provide a visible alternative for critical gesture-only actions.

## Theme and layout

- Verify text, icons, borders, focus/pressed states, scrims, and semantic status colors independently in each supported theme.
- Fixed headers/tab bars/CTA bars must not obscure scrolling content.
- Test narrow and large-device layouts plus landscape only where the product supports those environments; do not add arbitrary breakpoint requirements absent from the target.
- Let the project's spacing/type scale control rhythm. Audit inconsistency rather than imposing a new 4/8dp system.
- Support system text scaling/Dynamic Type where applicable without clipping required actions or content.

## Final check

Before native/mobile delivery, verify the relevant current surface rather than running a universal checklist:

- primary task and navigation remain operable with keyboard/system text/large content settings applicable to the platform;
- touch targets, labels, focus/reading order, and critical gesture alternatives are sound;
- light/dark or other supported themes preserve contrast and state clarity;
- safe areas, keyboard, fixed bars, scroll regions, and orientation behave correctly;
- loading/empty/error/permission/recovery states required by the actual flow are present;
- supplied brand assets and the selected icon language remain consistent; and
- reduced-motion behavior preserves meaning.

Do not claim platform compliance from a generic checklist alone. Use current platform documentation or implementation-owner proof when a specific API/HIG/Material requirement materially controls acceptance.
