# Representation capabilities

Read after the reader job and representation shape are clear. This reference preserves strategic capability knowledge so the agent can reach a strong renderer quickly without turning the known set into an allowlist.

## Separate three choices

```text
Representation
→ what form best exposes the relationship?

Renderer / capability
→ what mature system expresses that form reliably?

Delivery
→ static output, bundled runtime, existing host runtime, or exceptional remote runtime?
```

Do not let delivery cost choose a weaker representation before comparing representational value.

## Strategic anchors, not a closed catalogue

These are durable problem-fit anchors. Revalidate current APIs, package identity, support, and delivery details at use time.

### Mermaid — structured diagrams

Authoritative entry: https://mermaid.js.org/

Strong fit for structured relationships that its current grammar expresses naturally: flow/sequence/state, architecture/boundary, requirement/traceability, timelines and other supported diagram forms. Prefer static SVG/build-time rendering when runtime adds no reader value; bundle/reuse runtime when live rendering or interaction materially helps. Preserve source plus accessible equivalent meaning.

### Vega-Lite — quantitative/statistical grammar

Authoritative entry: https://vega.github.io/vega-lite/

Strong fit for declarative quantitative views: comparison, distribution, time series, faceting, transforms, aggregation and interactive selections. Preserve the data/transform/encoding specification when it changes source-to-view meaning. Staticize when interaction is unnecessary; use the runtime when selection/brushing/coordinated views materially help.

### Pierre Diffs — exact source/change inspection

Authoritative entry: https://diffs.com/docs

Strong fit for syntax-aware multi-file diffs, annotations, selection, virtualization, and exact source-change browsing. It renders evidence; it does not acquire provider candidates, decide review completeness, or own findings/verdicts. Follow [code-change review](code-change-review.md) for exact-candidate semantics.

### Cytoscape.js — large graph/network views

Authoritative entry: https://js.cytoscape.org/

Strong fit when connected structure is too large/dense for a simple structured diagram and the reader benefits from layout, selection, filtering, zoom/pan, neighborhood inspection, or graph-oriented navigation: dependency/call/ownership/impact/traceability/evidence graphs.

### D3 — bespoke data-driven visual reasoning

Authoritative entry: https://d3js.org/

Use as the expressive escape hatch when higher-level grammars cannot represent the relationship faithfully or coordinated custom encodings/interactions materially improve the reader job. Prefer the higher-level grammar when it already fits: unrestricted D3 implementation freedom is more code and therefore more opportunity for visual/semantic defects.

### Shiki — code-to-HTML representation

Authoritative entry: https://shiki.style/

Use when syntax materially improves comprehension of code itself. Prefer build-time highlighted HTML. Use a diff/source-navigation renderer when the job is exact change inspection rather than static code display.

## Unsupported representation needs

The anchors above must never become a ceiling. When none fits:

1. Name the missing representational capability and reader need precisely: geographic/spatial map, specialist timeline, very high-volume plotting, topology, scientific visualization, tree/layout engine, 3-D, or another real information shape.
2. Search current authoritative ecosystem evidence for a mature focused capability whose information/data model matches that relationship.
3. Compare the strongest credible simple form and candidate capability against decision-changing criteria: information fidelity, perceptual clarity, interaction/navigation value, correctness, accessibility, implementation reliability, build/runtime cost, portability, trust/data boundary, and maintenance.
4. Treat non-negotiable trust, authority, accessibility, privacy, compatibility, or runtime boundaries as gates, not scoreable trade-offs.
5. Prefer the mature capability when its representational leverage materially exceeds the credible simpler form. Do not downgrade to prose/`<pre>` merely because the capability is not named here.
6. Use `irinse` when installation/configuration/readiness itself requires material work; HTML Artifact retains representation judgment.
7. Apply [dependency policy](dependency-policy.md) to delivery, exact identity, fallback, runtime trust and disclosure.

Do not turn current ecosystem search results into a permanent library catalogue. Add another named anchor only when recurring use shows a stable problem fit worth avoiding repeated rediscovery.

## Selection result

Keep the decision compact:

```text
Reader relationship/job
Chosen representation
Selected capability + why it fits
Credible simpler alternative + why insufficient, when non-obvious
Delivery mode
Semantic fallback
Material runtime/data/accessibility limits
```
