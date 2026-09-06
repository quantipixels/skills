# External dependency policy

Read after a nontrivial renderer/build/runtime dependency, worker, WebAssembly component, widget, remote executable, or live service has been selected or is under serious consideration.

This policy governs delivery, trust, reproducibility and failure behavior. It must not bias representation selection toward native HTML when a mature capability provides materially better information fidelity, perceptual clarity, interaction, correctness, accessibility, or implementation reliability.

## Representation and delivery are separate

Choose the reader job and representation first. Use [representation capabilities](representation-capabilities.md) when a mature renderer/tool can improve that form. Then choose the lightest sound delivery:

```text
build-time/staticized output
→ focused bundled runtime
→ existing trusted host-application runtime
→ remote executable runtime only when the outcome genuinely needs it
→ live service only when the supplied outcome itself is live
```

Native HTML/CSS/JS remains an excellent implementation when it is also the strongest credible representation mechanism. It is not a preference that overrides a materially stronger specialized grammar/renderer.

Inside an existing application, reuse a suitable capability already owned by that runtime when it serves the same representational job. No renderer allowlist is maintained; named anchors are non-exclusive expert entry points.

Bind a dependency to the capability it provides, not to the lane that first selected it. A renderer chosen for a diff, chart, graph, diagram, map, or another representation may support any HTML Artifact lane when the same capability and admission boundary apply.

## Native integration before wrappers

When the selected capability already exposes a suitable CLI, API, grammar, or browser library, use that native surface first. Reuse the containing project's dependency manager, bundler, renderer, and lockfile when they already own the build. Otherwise create a task-local build context, pin exact dependency identities there, and record the resolved versions with the artifact evidence. Do not vendor `node_modules` or other install trees into a skill.

Keep source material as data. Renderer configuration, styles, transforms, event handlers, and build code authored for the artifact are implementation and may use the renderer's native surface directly. Do not forward untrusted source markup or arbitrary source fields into executable configuration.

A QP wrapper/helper must independently earn its place through the Kọ Skill script boundary: recurring use, a bounded mechanical guarantee, a real consumer, and falsifiable proof. Do not create a generic renderer adapter, universal artifact schema, or per-renderer application merely to make native tools look uniform.

## Admission boundary

For each nontrivial dependency establish:

- representation/capability gain over the strongest credible simpler form;
- compatibility with the actual file/HTTP/runtime environment;
- exact or reproducible identity appropriate to delivery;
- proportionate build/runtime and maintenance cost;
- accessible output or equivalent accessible meaning;
- explicit failure/fallback behavior;
- data/credential/telemetry boundary; and
- licensing/usage constraints when they can affect delivery or redistribution.

Treat security, privacy/data disclosure, required accessibility, authority, and accepted compatibility boundaries as gates. Do not average a gate failure against visual or implementation benefits.

## Staticize when runtime adds no reader value

A generation-time dependency may produce static SVG/HTML/CSS/PNG or another durable representation and disappear before delivery. Prefer staticization when the renderer materially improves the representation but runtime interaction does not improve the reader's job.

Use a bundled runtime when zoom, selection, filtering, brushing, coordinated perspectives, virtualization, live layout, or another browser behavior materially improves comprehension/navigation. Runtime is not a failure state when it is part of the representation's value.

## Remote runtime and live services

Availability from a CDN does not justify remote execution. Remote executable code requires an explicit reason self-contained/build-time/bundled delivery is unsuitable plus a clear trust/data/failure boundary. A live service requires the supplied outcome itself to be live; HTML Artifact must not turn static source material into a service-backed application on its own.

If the task has crossed into building or operating an application/service, keep that responsibility with the applicable implementation/deployment owner.

Classify delivery as:

- `Build-time` — renderer/tool absent when the artifact runs;
- `Bundled runtime` — executable resources ship with the artifact;
- `Existing host runtime` — trusted containing application already owns the capability;
- `Remote runtime` — executable resources load over the network at view time;
- `Live service` — artifact exchanges runtime data with an external service.

## Failure behavior

Preserve essential meaning rather than rebuilding the dependency:

- enhancement failure → base content remains usable;
- core-view failure → conclusions/source/units and accessible data/text remain;
- core-tool failure → explicit unavailable state and recovery requirement;
- live-service failure → unavailable/stale state with evidence cutoff.

A semantic fallback may be simpler than the primary representation; it must preserve the human-critical meaning and provenance, not the same visual sophistication.

## Complexity trigger

Reconsider architecture when dependencies overlap without distinct value; a general framework appears only to host a document; several runtime renderers accumulate; workers/WebAssembly/special serving appear; remote code can inspect non-public content; a live service receives artifact content; loading materially delays first useful view; or the dependency graph cannot be reproduced.

Do not reject a single focused dependency merely because native code could reproduce it with more bespoke implementation. Total semantic/implementation burden matters more than dependency count.

## Semantic transformation

When a dependency aggregates, bins, sorts, clusters, interpolates, changes time zones, filters graphs, performs statistics, computes layouts that carry meaning, or otherwise changes source-to-view interpretation, preserve the transformation/configuration with the source map. Changing it stales faithfulness proof as well as presentation proof.

## Disclosure

Report independently:

```text
Delivery shape: Single HTML | Companion bundle
Runtime code: None | Embedded | Bundled | Remote
Runtime data: Static | Live service
Evidence: Embedded | Linked | Mixed
```

Keep exact dependency identity, capability, delivery mode, data access, failure behavior, accessibility fallback, and verification in a quiet technical disclosure.
