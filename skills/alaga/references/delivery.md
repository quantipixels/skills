# Deliver an accepted coding change

Within an `atona` initiative, reuse its assignment and return the candidate, proof, and any blocker or scope change. Atọ́nà owns initiative progression; Alága owns the assigned change and its integration. Direct requests need no Atọ́nà plan.

If delivery exposes a controlling gap, return it with evidence to the same caller: domain meaning or rule applicability to `amose`, unsettled desire or trade-offs to `arojinle`, substantive external facts to `iwadi`, and structure or technical fitness to `architect`. For direct work, consume the necessary owned result and resume. Reopen only affected decisions and proof; do not invent a business rule or turn a settled change into a new initiative.

Before choosing the implementation, trace the existing related behavior from entry points through its authoritative owner, shared mechanisms and affected consumers to its proof. Find nearby implementations by behavior and domain vocabulary, not just the proposed name. Establish what already satisfies the request, what can be extended, and the actual gap. Reuse current investigation. Search relevant existing decisions, incidents or lessons when they can change the approach; verify current applicability. Keep discovery scoped to the change, with useful source pointers rather than a repository inventory or full knowledge-store read.

Apply DRY to shared knowledge, not incidental code similarity: extend the existing owner when semantics fit; justify a separate implementation by correctness, ownership, compatibility or maintenance needs. Apply YAGNI to custom state and coordination; check existing language, framework and provider guarantees first. Make the smallest idiomatic causal fix, preserving data and unrelated work; surface consequential scope expansion. For a consequential deliberate limit, state its ceiling and observable revisit condition near its owner. Preserve calibration where physical or environmental variation requires it; do not add speculative configuration.

Follow the project’s formatter and surrounding code style. Optimize readability, not line count; preserve useful whitespace and explicit control-flow blocks, and separate distinct logical steps.

Use a rerunnable codemod, query or script when it materially improves transformation consistency or verification; prefer existing tooling. Check it on a representative case and make replay safe or its preconditions explicit. Retain it only when future use or verification earns maintenance; ordinary edits need no tool artifact.

For new or changed domain values, types or states, inspect how comparable concepts are defined and actually used by callers and users. Before adding one, trace an analogous value across the same boundary—declaration, converter/mapper/serializer or registration, persistence/wire/configuration, consumers and proof—and reuse the established mechanism when its semantics fit. Follow the authoritative project's naming, representation and lifecycle conventions. For enums or statuses, trace applicable transitions, persistence/wire values, defaults, unknown-value handling and consumer mappings; a new declaration is not the whole change. Distinguish internal identifiers from user-facing labels and preserve compatibility. If existing patterns conflict, resolve the relevant owner and intended behavior rather than copy an arbitrary example or silently invent a convention.

Before choosing how to persist a new Java enum field, inspect a comparable entity field and its mapping:

```java
// Bad: immediately choose a mapping without inspecting existing entities.
@Enumerated(EnumType.STRING)
private OrderStatus status;

// Good: inspect a comparable enum field and its @Converter first.
// If the codebase has an existing pattern for @Convert mappings, adopt it.
@Convert(converter = OrderStatusConverter.class)
private OrderStatus status;
```

The lesson is to discover the established pattern before implementing; neither annotation is inherently preferred. Reuse or extend the existing pattern when its semantics fit, preserving its stored values and null/unknown handling. A different contract can justify a different implementation.

For a change spanning consumers, persisted data, framework-managed behavior, authorization or external effects, read [integration obligations](integration-obligations.md). Resolve the applicable obligations before editing and reconcile them against the final candidate; ordinary local changes need no separate assessment.

Reconsider established choices when recurring friction or a concrete new capability changes their fit. Use `architect` for a consequential design choice; report wider opportunities without silently expanding delivery. Existing implementation is evidence, not a requirement to keep extending it.

Discover commands, APIs, runtime mechanics, and conventions from the current project and authoritative documentation when needed. Use [diagnosis](diagnosis.md) for an unresolved causal mechanism and `architect` for unresolved technical structure.

For an accepted improvement to an existing test suite, read [test-suite improvement](test-suite-improvement.md). Keep independent proof judgment with `atunwo`; Alága owns the resulting test changes and verification.

Use TDD when executable feedback materially improves behavior discovery, defect reproduction or implementation confidence. Work in small Red → Green → Refactor cycles at a faithful, stable boundary, preserving established constraints. Select by feedback value and behavior, not file extension or change category; explicit user/project test-first requirements still govern. For reproducible defects, prefer capturing the intended failure before repair when practical. Confirm that Red represents missing behavior or a required interface, not broken setup, zero selected tests or an irrelevant failure. Make the smallest passing change within established constraints, then refactor code and tests where useful; neither full architectural preapproval nor a fixture-specific hack is required.

Useful TDD tests normally remain as regression protection. Consolidate, relocate or remove them only when their obligation is obsolete or retained proof covers it at least as well, applying the existing [test-quality rules](test-suite-improvement.md) when an obligation, boundary, brittleness, overlap or material cost changes. Do not add a per-test retention stage. Report the order and checks actually executed; test-after work is not retroactively TDD.

Verify the changed contract with evidence that could detect a plausible failure. Prefer existing affected checks or a focused probe; add a test when it protects a material regression existing proof would miss. Confirm that the intended checks actually executed against the candidate: zero selected tests, skips, stale results and successful submission are not passing proof. Establish relevant pre-existing failures when they affect attribution; never weaken acceptance to make the result green. Exercise browser-dependent behavior when acceptance requires it. Inspect the final diff for unintended changes and incomplete consumer updates; remove temporary scaffolding and fix failures caused by the change. Rerun only affected checks.

When the change affects dependency resolution, generated outputs or incremental builds, verify the selected target's resolved inputs and relevant invalidation path; a declaration or passing warm build can hide a different dependency or stale output. Distinguish executed, skipped and cached actions. Vary a representative input and verify valid recomputation or new-input cache retrieval plus downstream consumption; a physical rerun or changed output is not always required. Restore owned probe changes.

For a useful invariant over an input domain, read [property-based testing](property-based-testing.md). For numeric conversions or scaled arithmetic, read [units and scaling](units-and-scaling.md). For a material persistence, concurrency or recovery gap, read [stateful proof](stateful-proof.md). Use an applicable installed project verification specialist for its actual API, persistence and assembled journeys, retaining integration of the changed-contract proof here. Otherwise exercise the required boundary directly; generated tests and tool metrics do not replace it.

Treat affected documentation as a delivery consumer. Use `akowe` in `sync` when changed contracts, setup paths or operational instructions need reconciliation across a documentation set; keep local factual edits direct. Include its corrections, checks and unresolved conflicts in the delivery evidence.

Use `atunwo` when requested or independent judgment is materially useful; respect a request to skip review. Supply the candidate, acceptance, proof and risks. Resolve warranted findings and refresh only affected evidence.

Finish when the behavior and necessary documentation are delivered and verified, or a specific gap prevents further progress. Report the change, decisive verification, and limitations. Use `seda-pr` in publication mode for authorized commit/push/publication; delivery alone does not authorize it.

An explicit `scope-only` request returns the intended outcome, boundaries, relevant existing evidence and gaps, and the verification needed after implementation. Distinguish checks already performed from proposed checks; do not claim unbuilt behavior is verified. Make no implementation changes in this mode.
