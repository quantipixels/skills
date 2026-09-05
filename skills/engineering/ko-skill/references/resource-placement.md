# Capability and resource placement

Read when adding a resource, changing its responsibility, or investigating a placement problem.

Choose the least burdensome implementation that preserves the useful capability: instructions or selective expert guidance, native/project tooling, a focused mature library, or justified bundled code. Compare correctness, judgment quality, context, maintenance, portability, and trust; fewer files or dependencies is not the objective.

## Expertise and capability anchors

Keep domain knowledge when it changes a recurring non-obvious decision. Execution skills may own that expertise behind a simple entry point; a new public identity must satisfy the main skill's identity test.

A named mature tool or conceptual model can prevent repeated rediscovery. Retain its distinctive problem fit and authoritative retrieval surface, while verifying volatile versions/APIs at use time. A small non-exclusive anchor is useful expertise, not an allowlist.

Example: Vega-Lite can anchor declarative quantitative visualization without forbidding a better-fitting renderer. If it does not fit, discover alternatives rather than hand-building a weaker result or choosing from a frozen vendor list.

Use [reference quality](reference-quality.md) for the judgment carried by expert text and [knowledge catalogues](knowledge-catalogues.md) when maintaining a researched corpus.

## Executable capability

Leave ordinary discovery, routing, provider facts, Git/filesystem orchestration, and authorization with their natural owners. If code still provides a material advantage, use [script boundary](script-boundary.md).

An engine must carry a substantial deterministic part of the outcome and reduce real defect/implementation variance. Several convenience wrappers do not meet that bar. A focused mature library may be better than bespoke code; assess total burden, not dependency count.

A public install/bootstrap/uninstall entry point may earn its place by providing one safe, stable user invocation even when native tools own its internals.

## Templates, data, and assets

Keep a template when a stable recurring shape prevents costly omissions and no project/native scaffold already owns it. Remove arbitrary defaults, optional-empty sections, and duplicated procedure.

Bundle data only when maintaining it supports the result, with an explicit freshness boundary. Reusable UI assets must provide useful shared behavior or representation, including applicable accessibility; their existence does not make every feature mandatory.

Prefer existing project artifacts. Split resources only where callers can independently select the branches. If several tiny files always load together, they may belong together.

## Decide

Identify what the resource uniquely improves and the consequence of removing or replacing it. Preserve worthwhile operational anchors, expertise, and deterministic boundaries. Report only material trade-offs and proof gaps; no separate placement report or fixed disposition vocabulary is required.
