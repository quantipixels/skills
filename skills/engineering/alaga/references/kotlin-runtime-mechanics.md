# Kotlin runtime mechanics

Load only when the exact Kotlin candidate touches one of these mechanisms and the choice can change correctness, lifecycle, compatibility, ownership, or proof. This is mechanism calibration, not a Kotlin style guide or version manual.

The repository's actual Kotlin, kotlinx.coroutines, JVM/Android/KMP, serialization, and framework baseline controls version-sensitive behavior. Use current owning documentation when compiler generation, library APIs, ABI, or platform integration can change the answer.

## Types should close uncertainty rather than move it

- Model nullability in Kotlin types and contain Java **platform-type** uncertainty at interop boundaries. A platform value is not made safe by assigning it optimistically to a non-null type.
- Prefer one explicit state model over parallel nullable values/booleans when the states are mutually exclusive and consequential; sealed hierarchies can make closed state spaces visible when the domain is genuinely closed.
- Use data/value classes for value semantics only when identity, mutability, boxing, reflection, serialization, persistence, and framework behavior agree with that model. Do not apply them mechanically to identity-bearing entities.
- Keep extension and scope-function use subordinate to ownership and control-flow clarity. Convenience syntax should not make a foreign operation appear to belong to the wrong concept or hide failure/null handling.

## Coroutine scopes own lifetime and failure

- Keep work in a scope whose lifecycle matches the operation. Detached/global scopes turn cancellation, completion, failure, and shutdown into somebody else's problem.
- Treat cancellation as control flow, not an ordinary failure to swallow or translate generically. Preserve `CancellationException` semantics unless the current boundary explicitly owns a different cancellation contract.
- Choose supervision deliberately: ordinary parent-child failure propagation and supervisor-style sibling isolation encode different failure meanings.
- Use dispatcher/context changes to cross real execution boundaries such as blocking I/O or CPU work; do not wrap code in `withContext` merely as ceremony.
- A suspending API is not proof of non-blocking behavior. Identify blocking calls and give them a bounded, owned execution boundary.

## Flow and shared state have different lifecycles

- A cold `Flow` is tied to collection; collector cancellation normally cancels upstream work. A hot `StateFlow`/`SharedFlow` has a producer lifetime independent of one subscriber and therefore needs an owned producing scope.
- Use state and event primitives according to semantics: `StateFlow` represents a latest state; `SharedFlow` broadcasts emissions. Replay/buffering changes observable contracts and must be intentional.
- Replace state rather than silently mutating a mutable object already stored in a state flow; otherwise equality/conflation and observation can hide changes.
- Use atomic update or another explicit synchronization mechanism when several coroutines can update shared state. Flow types do not make arbitrary surrounding state atomic.
- Bound buffering, sharing, fan-out, retries, and long-lived collectors. Asynchronous streams do not remove resource/cardinality limits.

## JVM interop and multiplatform boundaries are public contracts

- Treat Java nullability annotations/platform types, checked-exception translation, SAMs, wildcards, default arguments/overloads, `@Jvm*` annotations, reflection, and serialization as potential ABI/interoperability boundaries when exposed publicly.
- Keep KMP common code platform-neutral unless a real platform variation requires `expect`/`actual` or another explicit boundary. Do not invent a multiplatform abstraction for a single implementation with no independent variation.
- Test coroutine/time behavior with deterministic test schedulers and explicit cancellation/time advancement when those semantics matter; sleeps are not synchronization proof.

## Retrieval anchors

Use current first-party Kotlin documentation for structured concurrency/cancellation, Flow and hot-flow semantics, Java interoperability/platform types, multiplatform boundaries, and the matching kotlinx.coroutines API. These anchors establish semantics; they do not justify caching compiler-version tables or API recipes here.

## What not to preserve locally

Do not turn this reference into a Kotlin idiom catalogue, Android architecture guide, coroutine API index, serialization manual, Gradle recipe, or KMP platform matrix. Resolve exact APIs and generation-specific behavior from the project baseline and current owning sources.
