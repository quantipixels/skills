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

Apply information hiding and tell-don’t-ask: a deep module owns policy, state, lifecycle, failures and integration details behind a small stable interface. Callers request outcomes rather than reconstruct policy. Preserve legitimate queries; depth is reduced caller burden, not fewer public methods.

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

Two production/test adapters are strong evidence of a useful seam, but two adapters are not required when one adapter already owns an independently real external, trust, protocol, compatibility, lifecycle, migration, or operational boundary.

Keep internal seams private. Apply the Liskov substitution principle (LSP) to adapters and test doubles: preserve caller preconditions, guarantees, errors and effects. A matching signature or passing mock test does not establish equivalence at an unexercised boundary.

## The interface is the durable behavior surface

Callers and durable behavioral tests should normally cross the same external interface. If proving behavior requires reaching past that interface into private choreography, first challenge the module shape or the proof strategy.

Use command/query separation (CQS) to make observation and mutation distinguishable; preserve atomic read-modify-write and useful command results. CQS does not require CQRS infrastructure. Internal tests may protect stable invariants without widening the public interface.

When a deepened interface completely and more stably owns a contract previously tested through several shallow modules, reassess the old tests. Remove them only when the new proof fully subsumes their material signal; do not delete a uniquely protective invariant merely because a higher-level test exists.

## Dependency-aware deepening

Classify dependencies only when the category changes seam or testing design.

### In-process

Use a functional core and imperative shell where separating deterministic decisions from effects improves proof and cohesion. Keep both inside the deep module when appropriate; no new layer or adapter is required merely for testing. Pure-core tests do not establish shell integration.

### Local-substitutable

A dependency has a fast faithful local stand-in, such as an embedded database or local filesystem substitute. Keep the seam internal when callers do not need to know about it; test the module through its external interface using the local substitute.

### Remote but owned

A separately deployed service or process is owned by the same system/team. When transport/lifecycle is a real boundary, define the narrow interface at that seam and keep business/coordination behavior on the owning side. Production and local test adapters may satisfy the same interface.

### True external

A third-party service, protocol, or resource is outside the system's control. Isolate its contract, trust, failure, compatibility, and translation behavior at the seam. Tests may use a controlled adapter/mock where real integration is unsuitable.

Dependency category does not mechanically require a port/interface. The interface must still earn its caller-facing cost.

## Deepen shallow clusters

Apply DRY to shared knowledge, not merely similar code. Give the repeated responsibility or invariant to the owner able to enforce it. Expose the outcome through a small interface preserving required variation and failures; keep internal seams private. Apply the deletion test to verify that the module owns necessary complexity rather than forwarding it.

Favor high cohesion, low coupling and locality of reasoning: keep related policy and lifecycle knowledge with their owner. Directory conventions can reveal or enforce boundaries; they do not define module depth.

## Component and policy boundaries

Use component principles as diagnostic lenses at the affected boundary. Name the concrete ownership, dependency or change-cost consequence; an acronym alone is not a finding or a reason to add an interface.

- **Change cohesion:** the single responsibility principle (SRP) and common closure principle (CCP) group responsibility by its real reason for change. Repeated co-change warrants investigation; one shared commit does not prove components should merge.
- **Consumer cohesion:** the common reuse principle (CRP) challenges dependencies that make consumers take unrelated capability. Inspect actual use without manufacturing release partitions.
- **Dependency cycles:** the acyclic dependencies principle (ADP) directs attention to cycles in the relevant component/dependency graph and their change cost. Runtime callbacks or collaboration alone do not prove a packaging cycle.
- **Stability and policy:** the stable dependencies principle (SDP), stable abstractions principle (SAP), and dependency inversion principle (DIP) help assess dependency impact and separation of policy from replaceable details. Infrequent edits do not establish sound dependency direction; appropriate abstraction does not mean abstracting every class.
- **Domain-visible structure:** make business/use-case ownership discoverable where it helps real consumers. A cohesive framework-native layout can be sound; do not force renaming or a universal directory convention.
- **Deferred details:** defer replaceable choices only while their uncertainty can safely remain open. Investigate storage, performance, trust and deployment constraints early when they can invalidate the direction.

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

## Represent the invariant where it is needed

Parse, don’t validate: convert raw input into a representation that retains established invariants. Make invalid states unrepresentable where that removes caller burden:

| Current burden | Candidate representation | Limit |
| --- | --- | --- |
| `completed` flag and optional completion time can disagree | A completed variant carries its required timestamp; other variants carry their own data. | Preserve real lifecycle and wire compatibility; names alone do not enforce transitions. |
| Repeatedly take the first element after asserting a sequence is nonempty | Construct a nonempty sequence from a first element and a remainder at the boundary requiring it. | A total operation such as summation can still accept an ordinary empty sequence. |
| Same-type identifiers are repeatedly swapped at a consequential boundary | Use the language's distinct domain representation where it prevents that mistake. | Do not wrap every primitive or spread conversion burden into unrelated callers. |

Choose the native idiom and name the invalid operation or repeated check eliminated. Keep validation for untrusted input, mutable-state constraints and guarantees the representation cannot enforce; a parsed value does not freeze permissions, balances or concurrent state.

## Misuse resistance at trust boundaries

When an interface controls a security-sensitive effect, try plausible caller mistakes: omitted configuration, zero/negative limits, invalid enum values, swapped same-type arguments and conflicting configuration sources. Trace the actual default, precedence and error path to the protected effect. Does a rejected value stop the operation, or merely warn while continuing? Are required checks enforced at the owning boundary or dependent on every caller remembering them?

Prefer secure defaults and fail-closed enforcement at the owning boundary, consistent with the contract. Documentation is not enforcement; existing validation or types may already close the path. In review, use these as bounded hypotheses under atunwo's evidence standard, not automatic findings.
