# Interactive projections

Read this file only when an HTML view needs an interactive relationship map, coordinated perspectives, or a guided sequence. This branch can support a report, plan, code change, comparison, architecture view, or any other lane when interaction materially improves the supplied reader outcome.

Use [visual reasoning](visual-reasoning.md) to decide whether a visual form is warranted and which supplied relationship should govern it. This reference owns the interaction contract only after that choice is made.

## Earn the interaction

Start with the smallest static representation that preserves the relationship. Add interaction only when it reduces real orientation or navigation cost, such as switching between distinct perspectives, following a non-obvious sequence, inspecting dense connected evidence, or moving between an overview and exact detail.

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

Use the current official API and an exact compatible package identity. If the dependency must be installed, configured, or upgraded, use `irinse`. For standalone output, bundle the required runtime; do not depend on a CDN merely for convenience. Apply [dependency policy](dependency-policy.md) and preserve a semantic static fallback when the renderer fails.

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

## Verify the exact model and runtime

Structural proof checks unique identities, valid relationship endpoints, valid guided-step targets, source attachments, escaped inline data, declared dependency identity, and absence of unrequested runtime hosts.

Browser proof is required when the interaction controls the artifact's usefulness. Check initial rendering, view switching, direction markers, selection/detail synchronization, tour navigation, search/filter behavior, zoom/pan/fit when present, keyboard/focus, narrow-width overflow, reduced motion, console/page errors, and the dependency-failure fallback. Report the view as unverified when required browser proof cannot run.
