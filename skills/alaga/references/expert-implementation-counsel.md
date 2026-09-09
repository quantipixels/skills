# Expert implementation counsel

Load only when material implementation choices could be locally plausible yet wrong for the exact stack, lifecycle, compatibility boundary, ownership model, or proportionality of the current candidate. This is an `alaga` implementation path, not a second owner or review stage.

## Pin the counsel boundary

Pin the exact candidate/horizon, accepted architecture and domain constraints, material stack/runtime versions, touched mechanisms, proof expectations, and only the questions whose answers can change code or proof.

Use this authority order:

```text
system / developer / user / repository instructions
→ accepted task, architecture, domain, compatibility, and safety contracts
→ exact repository, runtime, and native-tool evidence
→ current owning specifications, documentation, release notes, source, and tests
→ relevant specialist results
→ cautious inference with an explicit evidence gap
```

Challenge consequential choices as they are made rather than producing a large up-front brief. A material counsel item must identify the exact seam and a concrete consequence: caller/operational failure, compatibility/lifecycle/safety/resource rule, stack-native improvement, removal of invalid state/hidden ownership/accidental complexity, or a proof seam for a material invariant.

## Close only material evidence gaps

Start with current repository, dependency, compiler, runtime, framework, IDE, and native-tool evidence. Do not begin from a fixed language/framework catalogue.

Use `architect`, `amose`, `root-cause`, `ro-wo`, `iwadi`, and `irinse` as needed.

## Load curated mechanism depth only from candidate cues

After establishing the exact stack, use a local mechanism reference only when the touched code exposes its trigger and the extra depth can change code or proof:

- Java concurrency/visibility, equality/ordering, absence/failure, or resource-lifetime semantics → [Java runtime mechanics](java-runtime-mechanics.md);
- Spring proxy/advice, transactions, JPA/Hibernate persistence, application lifecycle, or reactive execution semantics → [Spring runtime mechanics](spring-runtime-mechanics.md);
- Kotlin type/interop, coroutine/cancellation, Flow/shared-state, JVM ABI, or multiplatform-boundary semantics → [Kotlin runtime mechanics](kotlin-runtime-mechanics.md);
- Ktor application/plugin, HTTP/error, request-cancellation, client/resilience, streaming, or resource-lifecycle semantics → [Ktor runtime mechanics](ktor-runtime-mechanics.md);
- Elixir/OTP process ownership, GenServer state, supervision/Task failure, mailbox/ETS/resource, or configuration-lifecycle semantics → [Elixir and OTP mechanics](elixir-otp-mechanics.md);
- Phoenix/Ecto/LiveView routing/context, authorization, transaction/data, Channel/PubSub/Presence, LiveView-state, or background-work semantics → [Phoenix runtime mechanics](phoenix-runtime-mechanics.md).

These references are compact calibration distilled from earlier curated research, not hidden language/framework catalogues and not substitutes for current source truth. Load none merely because its ecosystem appears in the repository. Project contracts and exact-current first-party/runtime evidence override them; unfamiliar or version-sensitive behavior remains a bounded current-source question.

## Preserve shared-state invariants under concurrency

When correctness depends on mutable shared state, state the invariant, its authoritative owner, every relevant writer, and the smallest credible competing interleaving. A race exists because an invariant can be violated under overlap, not because traffic crossed a volume threshold.

Inspect the enforcement already present before prescribing a mechanism. A database transaction can make its own changes commit or roll back together, but that alone does not establish the isolation needed for a read/decide/write invariant. A single statement is also not general proof: its predicate may depend on absence, counts, ranges, or other rows that another transaction can change. Constraints, conditional mutations, version/compare-and-set checks, serialized ownership, locks, and isolation levels count only when they protect the same invariant across every relevant path.

Prefer the smallest sound mechanism at the authoritative owner. Use database-enforced constraints when they directly express the invariant; conditional mutation or optimistic versioning when the current row/version can safely decide the transition; and locking or stronger isolation when a multi-row/predicate invariant requires it. These are candidate mechanisms, not a hierarchy or universal recipe. Verify the exact database/provider semantics when isolation, predicate locking, conflict behavior, or ORM state can change the choice.

Interpret execution evidence narrowly. A successful statement or affected-row count establishes that statement's outcome within its transaction, not that an enclosing transaction committed. A zero-row result may combine missing target, failed business predicate, stale version, or another condition unless the contract distinguishes them.

Keep concurrency, retry, replay, and cross-system atomicity separate. When a serialization/deadlock conflict requires retry, rerun the decision from fresh authoritative state at the transaction boundary required by the database/framework rather than replaying an inner stale write. When the same logical request can arrive twice, design idempotency independently of the concurrency guard. A local database transaction cannot make an ordinary remote effect atomic; use durable intent/outbox, idempotent delivery, or an explicit compensation workflow when the accepted architecture requires it.

Use proof that can expose the claimed failure. When correctness depends on database concurrency semantics, prefer the real engine with independent transactions and a controlled interleaving over mocks or sequential tests. Add durable proof only when it is the cheapest stable owner of a material invariant; do not create a concurrency test by ceremony.

## Apply the proportionality gate

For each proposed abstraction, layer, dependency, queue, cache, interface, wrapper, pattern, or state object ask:

```text
What present contract or failure mechanism does it own?
Why are existing repository, language, platform, or framework mechanisms insufficient?
What state, dependency, navigation, migration, or operational burden does it add?
Is that burden proportionate to demonstrated risk?
What stable proof would justify it?
Can the same contract be expressed more directly?
```

No abstraction without a present responsibility. No pattern without a candidate-specific consequence. No dependency without a material capability gap. No research question that cannot change the implementation. No test without an invariant it proves.

Remove formatting preferences, speculative alternatives, deterministic tool concerns, and recommendations whose benefit cannot justify their cost.

## Refresh and finish

Refresh counsel only when the candidate, touched mechanism, stack/version, accepted contract, material premise, or controlling evidence changes. Return only what changed rather than regenerating a large brief.

Apply relevant counsel as implementation changes. Resolve material evidence gaps that can still change code or proof before independent review; do not create a separate counsel ledger or classify every ordinary implementation choice.
