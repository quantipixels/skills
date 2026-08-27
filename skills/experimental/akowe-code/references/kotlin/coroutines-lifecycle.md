# Kotlin coroutines and lifecycle

Use when the candidate launches, scopes, cancels, supervises, or crosses dispatcher/lifecycle boundaries.

<a id="kt-cor-structured-owner"></a>
## `kt-cor-structured-owner` — Give every coroutine a real lifecycle owner

Prefer caller-, component-, request-, or application-owned scopes. Avoid `GlobalScope`, ad-hoc orphan scopes, and detached work whose failure/result/shutdown owner is unclear.

<a id="kt-cor-cancellation"></a>
## `kt-cor-cancellation` — Preserve cooperative cancellation

Do not consume `CancellationException` as ordinary failure. Broad recovery must rethrow cancellation or use APIs whose contract preserves it.

<a id="kt-cor-dispatcher-boundary"></a>
## `kt-cor-dispatcher-boundary` — Use dispatchers as execution boundaries, not decoration

Use `withContext` when work genuinely changes execution requirements. Do not wrap arbitrary functions in dispatcher switches or assume a dispatcher removes downstream resource limits.

<a id="kt-cor-supervision"></a>
## `kt-cor-supervision` — Choose failure propagation deliberately

Use ordinary structured failure when sibling cancellation is correct; use supervision when independent child failure is explicitly part of the contract. Supervision is not a blanket way to hide failures.

<a id="kt-cor-blocking"></a>
## `kt-cor-blocking` — Keep blocking work explicit

Blocking persistence, file, or remote calls must run at a boundary that owns blocking and capacity. Coroutines do not make blocking APIs non-blocking.

## Sources

- Kotlin coroutines guide: <https://kotlinlang.org/docs/coroutines-guide.html>
- Coroutine context and dispatchers: <https://kotlinlang.org/docs/coroutine-context-and-dispatchers.html>
- Cancellation: <https://kotlinlang.org/docs/cancellation-and-timeouts.html>
