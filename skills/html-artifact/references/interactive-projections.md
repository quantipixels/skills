# Interactive projections

Read when coordinated views, a guided sequence, a supplied-model demonstration or reader feedback improves an HTML artifact's usefulness.

Use [visual reasoning](visual-reasoning.md) to decide whether a visual form is warranted and which supplied relationship should govern it. This reference owns the interaction contract only after that choice is made.

## Earn the interaction

Start with a faithful static representation. Add interaction when it helps the reader inspect relationships, understand a supplied model or express a precise response: compare perspectives, follow a sequence, inspect connected evidence, vary a model input or annotate a proposed change.

Do not force a graph, fixed view taxonomy, zoom, search, or tour into every artifact. A small input should remain compact. Multiple views must answer different questions without repeating the same explanation.

## Model meaning before rendering

Define each view from supplied evidence before choosing a renderer:

- stable view identity, label, governing question, and summary;
- items or nodes with stable identity, title, concise meaning, and source attachments;
- directed relationships with explicit source, target, and meaning when direction matters;
- optional guided steps with a target, title, and explanation; and
- coverage, freshness, and unavailable or omitted evidence.

Keep the source model independent from layout coordinates and runtime state. A renderer may position, filter, select, or navigate the model; it must not invent nodes, edges, sequence, causality, ownership, findings, or priority.

Keep supplied content as escaped data. Prefer inline structured data for a standalone local artifact. Do not use `fetch()` merely to read adjacent local data when `file://` restrictions would break the view. Give material views, items, relationships, and steps stable `data-*` hooks when automation or repeatable screenshots matter.

## Keep the dependency lane-neutral

Use native DOM/SVG/Canvas for a small bounded view. Use a focused renderer such as [D3](https://d3js.org/) when data joins, directed paths, zoom/pan, or coordinated selection materially reduce implementation or correctness cost.

The dependency belongs to the interactive capability, not to the report, code-review, plan, or other lane that first used it. Keep the data contract and artifact styling lane-owned so another lane can reuse the renderer without inheriting PR-specific views, names, colors, or content.

Use the current official API and an exact compatible package identity. If the dependency must be installed, configured, or upgraded, use its supported project/host path. For standalone output, bundle the required runtime; do not depend on a CDN merely for convenience. Apply [dependency policy](dependency-policy.md) and preserve a semantic static fallback when the renderer fails.

## Make interaction comprehensible

When applicable:

- expose visible view controls with current-state semantics;
- make every directed relationship visibly directional and label its meaning;
- keep selection synchronized with a persistent detail region;
- let search or filtering change visibility without changing source meaning;
- make tours user-controlled, finite, restartable, and tied to stable items;
- support keyboard access, visible focus, reduced motion, narrow widths, long labels, and touch; and
- keep essential content in reading order and print even when the interactive layer is unavailable.

Prefer source attachments in the detail layer rather than crowding the governing representation. Embed or use relative local visual assets when they are required evidence; do not hotlink them into an otherwise local artifact.

## Demonstrate a supplied model

Use controls when changing a parameter or stepping through a sequence reveals a mechanism the reader needs to understand. Pin the owner's rules, input domain, units, assumptions and expected examples. Show which result changed and why; preserve the baseline and provide reset. A model output is a calculated illustration, not a measurement or proof of the real system. Return missing model semantics to its owner; use `adanwo` when the task is to discover or evaluate new behavior rather than explain supplied behavior.

## Return the reader's response

When useful, let the reader annotate a specific section, select among supplied alternatives or adjust proposed values. Export a readable response with artifact identity/revision, stable targets and the proposed changes; make copy/download success or failure visible beside the control. Provide selectable text if clipboard access is unavailable.

Keep preview, proposal and accepted state distinct. Local selection, copying or an “approve” label does not update the canonical plan or grant implementation authority. The owning workflow receives and reconciles the response, including stale revision conflicts. Do not send content to a service or silently persist sensitive notes merely to support feedback.

## Small interaction details

Make controls respond immediately. Put feedback at the affected scope: changed count beside the filter, empty state within the result, copy result beside its button. Keep critical caveats and required actions persistent rather than in temporary toasts. Preserve focus and nearby context through updates.

Use motion to explain a state transition or spatial relationship when useful, not as a reading prerequisite. Reversible interactions should retarget from their current state; repeated actions must not queue decorative animation. CSS transitions usually suffice for a simple state change. Keep hover enhancements optional, touch/keyboard operation complete and reduced-motion results immediate and understandable.

## Verify the exact model and runtime

Structural proof checks unique identities, valid relationship endpoints, valid guided-step targets, source attachments, escaped inline data, declared dependency identity, and absence of unrequested runtime hosts.

Browser proof is required when interaction controls usefulness. Exercise only the introduced claims: for example paired highlighting, filtering/reset, a known model case, exported target/revision, rapid reversal, or selection/detail synchronization. Include relevant keyboard/touch, narrow-width and failure behavior. Report the interaction as unverified when required browser proof cannot run; do not run an unrelated interaction matrix.
