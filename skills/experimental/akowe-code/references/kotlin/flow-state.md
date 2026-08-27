# Kotlin Flow and shared state

Use when the candidate models asynchronous streams, shared observable state, events, backpressure, or lifecycle-aware collection.

<a id="kt-flow-state-event"></a>
## `kt-flow-state-event` — Distinguish state from events

Use `StateFlow` for current state and `SharedFlow`/other event mechanisms only with deliberate replay/buffer/loss semantics. Do not make one shared stream carry both durable state and one-shot events ambiguously.

<a id="kt-flow-cold-hot"></a>
## `kt-flow-cold-hot` — Make cold versus hot ownership explicit

Plain `Flow` is normally cold and starts work per collector; shared/state flows have independent lifetimes. Choose sharing/start policy from the actual owner and subscriber lifecycle.

<a id="kt-flow-backpressure"></a>
## `kt-flow-backpressure` — Bound buffering and concurrency

Operators such as buffer/flatMap/merge can increase concurrency and memory. Set bounds from the downstream/resource contract rather than treating flow pipelines as cost-free.

<a id="kt-flow-collection"></a>
## `kt-flow-collection` — Collect at an owned lifecycle boundary

A collector is active work. Tie long-lived collection to a component/application lifecycle and cancel it when that owner ends.

<a id="kt-flow-simple-data"></a>
## `kt-flow-simple-data` — Do not wrap ordinary values in Flow without asynchronous value

Keep finite synchronous values/collections synchronous unless suspension, repeated emissions, cancellation, or backpressure meaningfully improves the contract.

## Sources

- Kotlin Flow: <https://kotlinlang.org/docs/flow.html>
- StateFlow and SharedFlow API docs: <https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/>
