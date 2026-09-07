# Module design

Use this when module, interface, seam, adapter, or dependency shape materially controls the architecture. The goal is leverage for callers, locality for maintainers, and a testable external surface—not abstraction for its own sake.

## Shared vocabulary

Use this vocabulary consistently in architecture reasoning. Do not force source-code renames merely to match it when established project/domain identifiers are already correct.

- **Module** — anything with an interface and an implementation: a function, class, package, subsystem, or tier-spanning slice.
- **Interface** — everything a caller must know to use the module correctly: type-level surface plus invariants, ordering constraints, error modes, required configuration, and material performance characteristics.
- **Implementation** — behavior and mechanism hidden behind the interface.
- **Depth** — leverage at the interface: how much useful behavior callers can exercise for how little interface they must understand.
- **Seam** — the place where a module's interface lives and behavior can be varied or isolated without editing its callers. Seam placement is a separate design choice from what the implementation contains.
- **Adapter** — a concrete implementation that satisfies an interface at a seam.
- **Leverage** — capability and policy callers receive without reconstructing it themselves.
- **Locality** — how strongly change, bugs, knowledge, and verification stay with the module that owns the reason for change.

Depth is not an implementation-lines/interface-lines score. A large implementation with a broad caller surface may still be shallow; a small implementation may still own a real consequential boundary.

## Prefer deep modules

A deep module exposes a small stable interface while hiding material behavior, policy, state, lifecycle, failure semantics, integration quirks, or coordination.

Good:

```text
PaymentProvider.charge(request)
```

The module may hide authentication, idempotency, retry/error translation, telemetry context, timeout semantics, and provider-specific sequencing.

Shallow:

```text
PaymentProvider.createHeaders()
PaymentProvider.sendHttp()
PaymentProvider.parseError()
PaymentProvider.retryDelay()
```

The caller now owns the provider workflow and must preserve its ordering and failure policy.

When designing an interface, ask:

```text
What outcome does the caller need?
What must the caller genuinely know?
What policy/state/lifecycle/failure detail can disappear behind the interface?
What change becomes local if this module owns it?
```

## Use the deletion test

Imagine deleting the proposed module or seam.

- If removal loses no required responsibility and no required complexity, policy, lifecycle, trust, compatibility, or coordination knowledge has to reappear elsewhere, the layer is probably pass-through.
- If required knowledge reappears across callers or another less-coherent owner, the module is providing leverage/locality.
- If removal would simply discard a required trust, authorization, protocol, compatibility, migration, lifecycle, or policy responsibility, the seam is real even when the implementation is small.

Do not keep a forwarding layer merely because it provides “an abstraction.” Do not delete a small module merely because its implementation is short when it owns a real trust, policy, compatibility, security, lifecycle, migration, or protocol boundary.

## Place seams deliberately

A seam is justified by a real reason to isolate or vary behavior, not by the existence of an interface keyword.

Two production/test adapters are strong evidence of a useful seam, but QP does not require two adapters when one adapter already owns an independently real external, trust, protocol, compatibility, lifecycle, migration, or operational boundary.

Keep internal seams private when only the module implementation or its focused tests need them. Do not expose internal collaborators through the external interface merely to make mocking easier.

## The interface is the durable behavior surface

Callers and durable behavioral tests should normally cross the same external interface. If proving behavior requires reaching past that interface into private choreography, first challenge the module shape or the proof strategy.

Internal implementation tests may use internal seams when they protect a distinct stable invariant, but they do not justify widening the public interface.

When a deepened interface completely and more stably owns a contract previously tested through several shallow modules, reassess the old tests. Remove them only when the new proof fully subsumes their material signal; do not delete a uniquely protective invariant merely because a higher-level test exists.

## Dependency-aware deepening

Classify dependencies only when the category changes seam or testing design.

### In-process

Pure computation or in-memory collaboration with no independently real boundary. Prefer direct composition inside the deep module; no external adapter is required merely for testing.

### Local-substitutable

A dependency has a fast faithful local stand-in, such as an embedded database or local filesystem substitute. Keep the seam internal when callers do not need to know about it; test the module through its external interface using the local substitute.

### Remote but owned

A separately deployed service or process is owned by the same system/team. When transport/lifecycle is a real boundary, define the narrow interface at that seam and keep business/coordination behavior on the owning side. Production and local test adapters may satisfy the same interface.

### True external

A third-party service, protocol, or resource is outside the system's control. Isolate its contract, trust, failure, compatibility, and translation behavior at the seam. Tests may use a controlled adapter/mock where real integration is unsuitable.

Dependency category does not mechanically require a port/interface. The interface must still earn its caller-facing cost.

## Deepen shallow clusters

When callers repeat sequencing, branching, validation, mapping, recovery, or foreign-state knowledge:

1. identify the repeated responsibility or invariant;
2. identify the owner that has enough knowledge to hide it;
3. place the seam where callers can ask for an outcome rather than implementation steps;
4. design the smallest interface that preserves required variation and failure semantics;
5. keep internal dependencies/seams private unless callers genuinely depend on them; and
6. verify that removing the proposed module would either lose a required responsibility or redistribute its hidden complexity/knowledge to callers or another worse owner.

Do not equate a module with a directory/package convention. Filesystem structure may help enforce or reveal a design, but it does not define depth.

## Explore alternative interfaces proportionately

When several materially different interface/seam designs remain credible and the choice has consequential architecture cost, compare genuinely different shapes. Consider:

- leverage/depth;
- locality/change amplification;
- seam placement;
- caller knowledge and common-case ergonomics;
- dependency/trust/failure ownership;
- migration/reversibility; and
- testability without public-surface inflation.

Use parallel agents or several candidate sketches only when the active host and decision justify that cost. Do not impose a fixed number of alternatives or turn every module question into a design tournament.

## Return for a bounded module-design question

State only what is material:

```text
Responsibility:
Interface:
Seam:
Hidden complexity / policy:
Dependencies / adapters:
Critical invariants:
Decisive trade-off / strongest alternative:
Limits or unresolved architecture gaps:
```
