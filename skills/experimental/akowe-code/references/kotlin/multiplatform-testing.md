# Kotlin multiplatform and testing

Use when code is shared across platforms or asynchronous/concurrent behavior needs durable proof.

<a id="kt-kmp-common-boundary"></a>
## `kt-kmp-common-boundary` — Keep common code genuinely platform-neutral

Do not leak JVM/Android/Apple APIs into common code. Introduce `expect`/`actual` or interfaces only when the shared capability is real and more than one platform benefits.

<a id="kt-kmp-no-speculative-abstraction"></a>
## `kt-kmp-no-speculative-abstraction` — Do not create multiplatform layers for a single platform need

A future platform possibility is not enough to justify common abstractions. Keep platform code local until a stable cross-platform contract exists.

<a id="kt-test-coroutines"></a>
## `kt-test-coroutines` — Use deterministic coroutine scheduling

Prefer coroutine test dispatchers/schedulers and explicit virtual-time advancement over sleeps or wall-clock waiting.

<a id="kt-test-cancellation"></a>
## `kt-test-cancellation` — Prove cancellation/lifecycle behavior where it matters

For scopes, flows, background work, and resource ownership, test that cancellation stops obsolete work and that failures reach the intended owner.

<a id="kt-test-boundary"></a>
## `kt-test-boundary` — Test framework/interop semantics at the real seam

When correctness depends on serializer, reflection, Java ABI, Android/iOS lifecycle, or platform-specific behavior, use the smallest real integration boundary that owns those semantics.

## Sources

- Kotlin Multiplatform: <https://kotlinlang.org/docs/multiplatform.html>
- kotlinx-coroutines-test: <https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/>
