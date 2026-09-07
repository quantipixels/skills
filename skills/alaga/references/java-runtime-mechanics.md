# Java runtime mechanics

Load only when the exact Java candidate touches one of these mechanisms and the choice can change correctness, lifecycle, compatibility, resource use, or proof. This is curated reasoning depth, not a Java style guide or version manual.

The repository's actual JDK baseline and current first-party JLS/JDK documentation control version-sensitive behavior. Use this reference to notice the non-obvious question; verify current details when they can change the implementation.

## Concurrency is an ownership and visibility contract

- Prefer confined or immutable state. Shared mutable state needs one complete synchronization/ownership policy across every access and lifecycle transition.
- Require a real **happens-before** edge for cross-thread publication/visibility. Timing, call order, sleeps, or "assigned first" are not synchronization.
- Treat compound state transitions as compound. A thread-safe variable/collection does not make check-then-act or read-modify-write sequences atomic.
- Give executors, task groups, queues, and background workers an explicit lifecycle owner: admission, bounds, cancellation, shutdown, and unfinished-work behavior.
- Preserve interruption as cooperative cancellation. When translating `InterruptedException`, propagate it or restore interrupt status unless the current boundary explicitly owns a different interruption policy.

Use current project/runtime evidence before choosing platform threads, virtual threads, structured concurrency, pools, atomics, locks, or reactive/evented alternatives. The mechanism is secondary to the ownership, visibility, cancellation, and resource contract.

## Equality, hashing, and ordering define collection behavior

- If value equality is implemented, `equals` and `hashCode` must use compatible, stable state for the period an object participates in hashed collections.
- Do not let mutable equality/hash state silently invalidate a map key or set member.
- Treat inheritance-based value equality as suspect when subclasses add equality state; composition, records/final values, or an explicit identity model are often clearer.
- A comparator's zero-equivalence controls uniqueness in sorted sets/maps. Decide deliberately whether comparison is consistent with `equals`, preserve transitivity, and add stable tie-breakers when distinct values must remain distinct.
- Arrays are identity values unless content comparison is chosen explicitly.

Entity identity may have different semantics from value equality. Follow the persistence/domain model instead of importing a generic value-object rule.

## Model absence and failure once at each boundary

- Choose whether absence is impossible, nullable, optional, empty, or exceptional and keep that meaning consistent across one contract.
- Use `Optional` where return-value absence benefits from explicit composition; do not spread it mechanically into fields, parameters, collections, persistence models, or serialization without a real additional state.
- Do not immediately reopen an Optional with an unchecked presence assumption when the absence contract is still live.
- Keep fallbacks lazy when they allocate, perform I/O, mutate state, or can fail.
- Preserve the original failure/cancellation meaning when translating exceptions. A wrapped exception should not silently turn retryable cancellation, validation, authorization, or invariant failure into one generic error path.

Nullness annotations/checkers are useful only when they form one coherent project/tool contract; they do not replace validation of external input.

## Resources need one lifetime owner

Treat files, streams, sockets, executors, transactions, native handles, temporary state, and other closeable resources as ownership problems. Prefer lexical/scoped lifetime where available; otherwise make transfer, close, cancellation, and failure cleanup explicit. Do not rely on finalization, process exit, or incidental framework shutdown for a resource whose lifetime matters to correctness.

## Retrieval anchors

Use current first-party sources appropriate to the project baseline, especially the Java Language Specification's Threads and Locks / memory-model chapter and the current JDK API contracts for `Object`, `Comparator`, `Optional`, `ExecutorService`, `Thread`, and `InterruptedException`. These anchors establish semantics; they do not require copying version-specific API recipes into this reference.

## What not to preserve locally

Do not turn this reference into a catalogue of JDK APIs, language syntax, collection choices, style rules, framework recipes, or version-specific feature tables. Resolve unfamiliar or version-sensitive behavior from the exact project baseline and current owning sources.
