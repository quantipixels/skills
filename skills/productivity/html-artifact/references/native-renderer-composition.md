# Native renderer composition

Read only after the representation and renderer/capability are already selected and the artifact needs build-time rendering, a bundled browser runtime, or task-specific renderer composition. This reference is about using mature capabilities safely without turning HTML Artifact into a renderer framework.

## Keep the boundary simple

```text
semantic owner + HTML Artifact
  → choose the reader job, representation, labels, emphasis, source mapping, and accessible equivalent

selected renderer/build tools
  → own their native grammar, layout/drawing, compilation, bundling, and runtime mechanics

QP-maintained code
  → exists only for a recurring mechanical guarantee that native tools cannot already carry cleanly
```

Do not introduce a QP intermediate representation merely to make different renderers look alike. Use Mermaid syntax as Mermaid syntax, Vega-Lite specifications as Vega-Lite specifications, Cytoscape elements/styles/layout as Cytoscape inputs, and so on. A native representation/configuration that changes meaning belongs in the artifact source map and stales faithfulness proof when changed.

## Build path

1. **Reuse the host project first.** If the containing project already has the selected renderer, package manager, bundler, CSP, component shell, or test harness, use those directly. Do not create a parallel artifact toolchain.
2. **Otherwise use a task-local build context.** Create a disposable or artifact-owned working directory, initialize only the dependencies the selected representation needs, pin exact versions, and retain a lockfile when the artifact/build will be revisited. Record the resolved versions even when the build context is disposable.
3. **Author task-specific implementation against the native capability.** Layout, styles, classes, interactions, transforms, and responsive behavior belong to the artifact being built. Do not hide information-design choices inside a generic QP wrapper.
4. **Treat supplied content as data.** Encode or serialize source-derived labels/values into safe data channels. Never execute raw source HTML/JS, interpolate untrusted text into code, or treat source metadata as renderer configuration without an explicit authoring decision.
5. **Staticize or bundle using mature tooling.** Prefer the renderer's official build/static export when runtime interaction adds no value. For browser interaction, use the project's existing bundler or a focused mature bundler; avoid hand-rolled dependency concatenation.
6. **Publish only after proof.** Generate a candidate first, verify the applicable semantic/runtime claims, then publish through the caller's normal artifact path or Akọsílẹ̀ when its shared-workspace contract applies.

## Example: interactive network view

If Cytoscape is the selected capability, author the view against Cytoscape's native element/class/style/layout/event APIs. A compound ownership view may use `data.parent`; a status-aware dependency view may use classes or data-backed style selectors; a reader-specific inspection view may choose a layout different from a simple dependency tree. Those are artifact decisions, not fields in a permanent QP graph schema.

Keep a meaningful DOM fallback outside the renderer canvas: the human-critical nodes/relationships, conclusions, states, and provenance needed to interpret the view. The fallback does not need visual parity; it must preserve the decision-relevant meaning when JavaScript or the renderer is unavailable.

When embedding the view into an existing document, scope component CSS and event behavior to the component root. Do not write global `html`, `body`, heading, theme, or navigation rules unless this artifact owns the complete document shell.

## Mechanical checks worth keeping

For the actual artifact, test only claims introduced by the selected capability and delivery shape:

- exact dependency/build identity is reproducible enough for the artifact lifecycle;
- build output opens in the intended `file:` or HTTP context;
- static/bundled delivery performs no unexpected network request when offline delivery is claimed;
- the material selection/filter/zoom/navigation interaction works with keyboard and at the important narrow-width state;
- disabled JavaScript or renderer failure preserves the semantic fallback;
- component embedding does not overwrite the containing document's global styles or behavior.

Do not create a renderer matrix or QP-owned conformance suite merely because several libraries are possible. The artifact proves the capability it actually uses.

## When custom QP code becomes justified

After repeated artifacts expose the same mechanical defect or reconstruction cost, evaluate that exact seam with Kọ Skill's script boundary. Good candidates are small pure transforms or safety kernels such as an exact compiler step, script-safe embedding transform, or reproducible asset packager. Representation choice, renderer configuration, visual composition, and semantic fallback design stay with the capable agent/artifact even then.
