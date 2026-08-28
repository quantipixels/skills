# Module depth

Use this when module, interface, seam, adapter, or dependency boundaries materially shape the architecture. The goal is not to maximize abstraction. It is to concentrate useful complexity behind small stable interfaces and keep change local to the owner that understands it.

## Vocabulary

Use these terms consistently in this reference:

- **Module** — one owner of a coherent responsibility and its hidden behavior.
- **Interface** — what callers must know or depend on to use the module.
- **Implementation** — the hidden policy, state, lifecycle, integration detail, or mechanism behind the interface.
- **Depth** — the ratio between useful hidden complexity and caller-facing interface burden.
- **Seam** — a boundary where responsibilities, dependencies, trust, lifecycle, or change can be isolated.
- **Adapter** — a seam that translates one real boundary into another contract.
- **Leverage** — how much caller complexity or repeated policy one small interface removes.
- **Locality** — how strongly a change stays within the module that owns the reason for change.

The terms are reasoning aids, not scoring metrics.

## Prefer deep modules

A deep module exposes a small stable interface while hiding material behavior, policy, lifecycle, failure semantics, integration quirks, or state.

Good:

```text
PaymentProvider.charge(request)
```

The module owns authentication, retries, idempotency, provider error translation, telemetry context, and timeout/failure semantics.

Bad:

```text
PaymentProvider.createHeaders()
PaymentProvider.sendHttp()
PaymentProvider.parseProviderError()
PaymentProvider.retryDelay()
```

The caller must understand the provider's implementation lifecycle and reconstruct policy itself.

## Use the deletion test

Ask:

```text
If this seam disappeared and callers used the underlying owner directly,
what real responsibility, policy, isolation, lifecycle, compatibility,
or proof boundary would be lost?
```

If the answer is only “fewer direct calls” or “we may swap implementations later,” the seam is probably speculative or shallow.

Good seam: deleting the adapter would expose provider authentication, retry/error rules, version translation, or trust boundaries to callers.

Bad seam: deleting the interface removes only forwarding methods and a factory for one stable implementation.

## One adapter can still be real

Do not require two implementations before a seam is valid. A single adapter is justified when it owns a real external, trust, compatibility, lifecycle, migration, policy, or operational boundary.

Good: one S3 adapter isolates credentials, request signing, retry semantics, key naming, and provider failures.

Bad: one repository interface mirrors an in-process data structure and exists only because “repositories are good architecture.”

## Prefer local change

A good boundary keeps the knowledge required for a change near the owner that has it.

Good: adding a provider-specific retry condition changes only the provider integration module and its proof.

Bad: every caller branches on provider codes and must be edited when retry semantics change.

## Avoid forwarding layers

A forwarding layer adds navigation, naming, testing, configuration, and dependency cost. Keep it only when it owns something material.

Good: façade reduces a complex subsystem to the small contract the application needs and owns translation/recovery semantics.

Bad: service → manager → coordinator → client where each method forwards the same arguments and no layer owns policy.

## Prefer interfaces that match caller knowledge

Callers should depend on the minimum concepts required to ask for an outcome, not on the implementation steps used to produce it.

Good: `reserveInventory(orderId)`.

Bad: caller must invoke `loadStock()`, `calculateAvailability()`, `writeReservation()`, and `emitReservationEvent()` in the correct sequence.

## Counterexamples

A shallow-looking module can be correct when its small behavior owns a material boundary:

- a tiny authorization gate that centralizes security policy;
- a narrow compatibility shim during a staged migration;
- a protocol adapter whose translation is small but trust/version ownership is real;
- a test seam required by an independently meaningful runtime boundary.

Do not remove a seam merely because its current implementation is short.

Likewise, a large implementation is not automatically deep. A module with a huge API, many unrelated reasons to change, or caller-visible internal states may still be shallow or divergent.

## Architecture decision questions

For each proposed module or seam, answer only what is material:

```text
What responsibility does it own?
What must callers know?
What policy/state/lifecycle/failure detail becomes hidden?
What change becomes more local?
What real boundary justifies an adapter or interface?
What burden does the seam add?
What smaller direct design is the strongest credible alternative?
What proof demonstrates the boundary's value?
```

Prefer the smaller direct shape when the seam cannot answer these questions with current evidence.
