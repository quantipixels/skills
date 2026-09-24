# Interactive projections

Use when interaction makes a supplied relationship easier to inspect, a known model easier to understand, or an explicitly requested response easier to express. Preserve a complete static reading path first; do not turn every report into an application.

## Pick the reader benefit

- Compare: keep material alternatives aligned; a toggle alone must not force memorising hidden evidence.
- Inspect: select an item and reveal its details or highlight linked evidence while preserving overview.
- Follow: a finite, user-controlled walkthrough exposes meaningful transitions and resets.
- Narrow: category/text filtering provides a count, empty state and reset.
- Explore: labelled native inputs drive the owner's known model with units, baseline and a tested example.

Use existing view/filter/carousel/report assets or native HTML before inventing a widget. A disclosure is not a tab; selection buttons need not pretend to be ARIA tabs. Add complex keyboard semantics only for the actual widget. Keep artistic composition independent from reliable mechanics.

## No saved reader state by default

State may live in the DOM or memory while the page is open. Do not write localStorage, sessionStorage, IndexedDB, cookies, files, history/query/hash state or services to preserve selections. Reload returns to authored defaults, except an explicit navigation anchor. Do not add autosave, feedback or approval UX. This covers theme, filter, carousel, comparison, step and what-if values.

A living author-maintained document is not permission to retain reader state. Explicit persistence requests need a lifetime, destination, fields, privacy boundary and reset/removal. Export, copying a response and acceptance are separate acts; a click cannot mutate canonical decisions. Do not include feedback capture/export controls unless requested. For an authorised export bind the response to artifact/revision/target, show success/failure and offer selectable text when clipboard access fails.

## Model and data before layout

Keep stable IDs for meaningful items, relations and steps. Direction/labels come from the source; coordinates are presentation, not evidence. Keep rules, units, source cut, omitted coverage and uncertainty visible. Calculated output is illustration, not observed system behaviour. Missing rules return to their owner; discovering new behaviour belongs to adanwo.

Use escaped inline data for portable files. Do not fetch adjacent JSON merely to create a file:// failure. Use textContent for supplied text; do not concatenate executable markup. Stable data-* hooks can support repeatable inspection. Use the manifest's context-correct serialization example for script data, not HTML entity escaping.

## Readability and resilience

Keep essential information in reading order and print. Hide controls until initialization succeeds; without JS all semantic content remains. Preserve focus through selection/filtering; do not leave it inside a hidden panel. Prefer labelled, persistent-on-screen details to hover-only explanations. Reset is immediate; no match is distinct from absent data.

Expose state through appropriate labels, aria-pressed/expanded and polite result announcements. Support native keyboard activation and touch. Reserve space where changes would disorient reading. Motion may explain a transition but is never required; respect reduced motion and avoid queued decoration.

For dense graphs or coordinated views use a suitable renderer under [dependency policy](dependency-policy.md). Do not relax Mermaid security for callbacks or depend on its generated SVG internals. Put interaction beside it or select a renderer designed for the job. Render diagrams with a visible layout before placing them into initially hidden views, or staticize them.

## Prove the promise

Check stable IDs, targets, source attachments and escaped data. Exercise the introduced value: selection/reset, no-match, a known model result, or exact exported revision/target when requested. Check keyboard/focus, relevant breakpoints, print/no-JS fallback, reload and state-write APIs for shipped controls.

Static checks cannot prove arbitrary JavaScript never writes state. An intercepted renderer stub proves loader mechanics, not real-library rendering. Exercise the selected upstream runtime separately when its integration changes. No broad device matrix follows merely from document size; report unavailable execution honestly.
