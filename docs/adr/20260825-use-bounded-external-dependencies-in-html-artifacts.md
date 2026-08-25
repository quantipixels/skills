# Use bounded external dependencies in HTML artifacts

Status: Accepted

QP will use a bounded-open dependency policy for HTML artifacts. It will not maintain an allowlist and will not privilege particular libraries such as Tailwind or Mermaid. The information model, representation, and interaction are chosen before implementation technology.

Native browser capabilities remain the default for straightforward platform behavior. External dependencies are first-class implementation tools when they provide one distinct material capability or substantially reduce algorithmic, correctness, accessibility, interaction, or maintenance complexity. Existing dependencies are reused only when they are already part of the artifact's actual runtime and fit the required capability.

QP distinguishes build-time dependencies, bundled runtime dependencies, remote runtime dependencies, and live services. It also distinguishes enhancement, core-view, and core-tool criticality. Network availability is treated as normal, but remote execution, data disclosure, host compatibility, and dependency success are separate concerns.

Dependencies must be proportionate, non-overlapping, reproducibly identified, compatible with the actual artifact transport, and have explicit failure behavior. More than three executable runtime dependencies, overlapping capability owners, a framework in a document-shaped artifact, special worker/WebAssembly/serving requirements, remote code over non-public content, live-service data disclosure, material first-view delay, or an unpinnable dependency graph triggers architecture reconsideration rather than an automatic rejection.

When a dependency performs semantic transformation rather than merely drawing supplied values, the transformation configuration is preserved with the owner record or source map and changes to it stale faithfulness proof when meaning can change.

Artifacts report delivery shape, runtime-code mode, runtime-data mode, and evidence disposition independently.
