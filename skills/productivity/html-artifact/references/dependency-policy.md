# External dependency policy

Read this only when an HTML artifact uses external build/runtime code, a worker, WebAssembly, widget, or live service.

## Capability before technology

Choose the information model, representation, and interaction first. Use native browser capabilities for straightforward behavior. Use a dependency when it provides one material specialized capability or substantially reduces algorithmic, correctness, accessibility, interaction, or maintenance complexity.

For a standalone artifact prefer:

```text
native HTML/CSS/JS
→ focused dependency
→ framework only for application-like complexity
```

Inside an existing application, reuse a suitable dependency only when it is already part of the artifact's actual runtime. No library is privileged and QP maintains no allowlist.

## Admission boundary

For each nontrivial dependency establish:

- distinct capability with no substantial overlap;
- compatibility with the actual file/HTTP/runtime environment;
- an exact or reproducible identity appropriate to how it is delivered;
- proportionate runtime and maintenance cost;
- accessible output or equivalent accessible meaning;
- explicit failure behavior;
- no unrequested telemetry, credential use, or data disclosure.

Network availability is normal. Remote execution trust, host compatibility, data disclosure, and successful loading are separate concerns.

Classify delivery as:

- `Build-time` — absent when the artifact runs;
- `Bundled runtime` — shipped with the artifact;
- `Remote runtime` — loaded over the network at view time;
- `Live service` — exchanges runtime data with an external service.

## Failure behavior

Preserve essential meaning rather than rebuilding the dependency:

- enhancement failure → base content remains usable;
- core-view failure → conclusions, source, units, and accessible data/text remain;
- core-tool failure → show an explicit unavailable state and recovery requirement;
- live-service failure → show unavailable/stale state with the evidence cutoff.

## Complexity trigger

Reconsider the architecture when dependencies overlap; a framework is added to a document-shaped artifact; several executable runtime dependencies accumulate; workers/WebAssembly/special serving requirements appear; remote code can inspect non-public content; a live service receives artifact content; loading materially delays first useful view; or the dependency graph cannot be reproduced.

A framework is normally unjustified for a report, plan projection, static diagram, small filter, tab set, disclosure set, or bounded comparison.

## Semantic transformation

When a dependency aggregates, bins, sorts, clusters, interpolates, changes time zones, filters graphs, performs statistics, or otherwise changes source-to-view meaning, preserve that configuration with the owner record/source map. Changing it stales faithfulness proof as well as presentation proof.

## Disclosure

Report independently:

```text
Delivery shape: Single HTML | Companion bundle
Runtime code: None | Embedded | Bundled | Remote
Runtime data: Static | Live service
Evidence: Embedded | Linked | Mixed
```

Keep dependency details in a quiet technical disclosure: exact identity, capability, delivery mode, data access, failure behavior, and verification. Licensing is outside this policy.
