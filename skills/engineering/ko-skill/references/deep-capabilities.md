# Deep capability placement

Use this when deciding where substantial skill depth should live. A deep capability exposes a small semantic surface backed by enough expertise or machinery to carry a material part of the owned outcome. Depth may be reference-backed, native/tool-backed, engine-backed, or a deliberate combination.

## Separate control shape from capability depth

```text
Control shape:    lightweight | workflow
Capability depth: native | reference-backed | tool-backed | engine-backed
```

Control shape describes lifecycle/orchestration. Capability depth describes where the useful implementation or expertise comes from. A lightweight skill may still be deep.

- `native` — the host/model/repository already expresses the result adequately.
- `reference-backed` — selectively loaded expert guidance carries recurring non-obvious judgment.
- `tool-backed` — an existing project/provider/ecosystem tool owns the mechanics.
- `engine-backed` — QP-owned deterministic code carries a substantial portion of the skill's native outcome.

## Prefer the natural owner

Before adding machinery, test this order:

```text
short owner guidance or deep reference
→ readable repository/source/config truth
→ native language/compiler/build/framework capability
→ existing project/provider/IDE/tool capability
→ focused mature library/tool
→ narrow QP script
→ QP engine only when the outcome boundary is genuinely high
```

Do not replace a custom implementation with a permanent command catalogue. Discover current project/tool commands from wrappers, task/help output, current owning documentation, or `irinse` when operating the tool is itself material.

## Guidance can be deep

Do not treat executable code as the only form of depth. A substantial selectively loaded reference is correct when it materially improves the owning skill's judgment and passes [reference quality](reference-quality.md).

Good: Solution Architect loads a cohesive module-depth reference only when module/seam design is material.

Bad: delete useful architectural calibration merely because the model could reconstruct some of it from general knowledge.

## Hold scripts to the deterministic seam

A small script is justified when a narrow mechanical `X → Y` result is materially safer, more reproducible, or externally useful than repeating the operation as guidance. Apply [bundled-script boundary](script-boundary.md).

Good: exact snapshot plus lock-held compare-and-swap replacement.

Bad: encode a five-line lifecycle checklist into a CLI whose result is immediately reinterpreted by the model.

## Hold engines to the outcome boundary

An engine is not several scripts in a directory. It earns its maintenance/runtime cost when deterministic machinery carries a substantial portion of the skill's native result rather than producing helper metadata for another reasoning step.

A credible engine often owns a bounded vertical such as:

```text
domain semantic model
→ deterministic validation/diagnostics
→ realization/transformation
→ inspect/compare/use
→ exact machine or human artifact
```

The result does not need to be a separate public product. It must, however, remove a meaningful class of owned implementation or defect variance from the agent.

Usually below the engine bar:

- search/filter over prompt/reference content;
- a tiny frontier or graph calculation;
- Markdown/frontmatter validation whose pass cannot establish semantic readiness;
- generic card/table/page rendering while the model still owns information architecture and representation;
- normalization that exists only to feed the next model step;
- wrappers around native commands.

## Decision questions

For a material capability ask:

```text
What part of the owned outcome is difficult or failure-prone?
Who naturally owns that truth or mechanic now?
Can clear guidance or a deep reference carry it reliably?
Can an existing tool/library carry it better?
If code remains, what exact deterministic seam does it own?
If proposing an engine, what substantial part of the native outcome moves behind its semantic interface?
What new maintenance/runtime/freshness burden does that introduce?
What proof demonstrates the chosen boundary is better than the smaller alternative?
```

Prefer the smallest placement that preserves correctness, judgment quality, authority, and useful depth.