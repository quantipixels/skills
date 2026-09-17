# Representation capabilities

Read after the reader job and representation shape are clear. Keep representation, capability and delivery as separate choices; use current project or host interfaces to resolve volatile implementation details.

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

## Select by problem fit

Choose the form that best exposes the reader's relationship or task: structured relationships, quantitative comparisons, source/change inspection, connected graphs, bespoke data-driven reasoning, code comprehension, maps, timelines, topology, scientific views or another real information shape.

Compare the strongest credible simple form and the available capability against decision-changing criteria: information fidelity, perceptual clarity, interaction/navigation value, correctness, accessibility, implementation reliability, build/runtime cost, portability, trust/data boundary and maintenance. Treat non-negotiable trust, authority, accessibility, privacy, compatibility and runtime boundaries as gates.

Prefer a mature focused capability when its representational leverage materially exceeds the credible simpler form. Preserve source-to-view transformations, accessible equivalent meaning and a semantic fallback. Do not turn current ecosystem results into a permanent product catalogue, and do not downgrade to prose merely because a specialized capability needs current selection.

## Delivery and dependency boundary

Apply [dependency policy](dependency-policy.md) to exact identity, fallback, runtime trust, disclosure, licensing and delivery. Revalidate current APIs, support and package details at use time. Installation, configuration, authentication and persistent runtime changes retain their own authority requirements.

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
