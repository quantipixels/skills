# General coding guards

Load this file for every Èèwọ̀ run. Apply a pattern only when its trigger exists in the candidate.

## `general.failure.swallowed` — Silent failure (`BLOCK`)

**Avoid:** Empty catches, ignored `Result`/error return values, success responses after failed work, or fallback values that erase the failure.

**Why:** The caller and operations layer receive a false success signal while state may be partial or stale.

**Prefer:** Propagate, translate, aggregate, or explicitly observe the failure. A deliberate best-effort boundary must log/measure the loss and state what is allowed to fail.

## `general.work.unbounded` — Unbounded work admission (`BLOCK`)

**Avoid:** Unbounded task spawning, queues, retries, fan-out, result collection, or input-sized memory growth on externally controlled workloads.

**Why:** A valid or hostile workload can exhaust memory, threads, connections, file descriptors, or scheduler capacity.

**Prefer:** Bound concurrency and queue depth; reject, shed, paginate, stream, or apply backpressure. State the operational limit and overload behavior.

## `general.background.unowned` — Unowned background work (`BLOCK`)

**Avoid:** Fire-and-forget work whose completion, cancellation, failure, and shutdown behavior have no owner.

**Why:** Work can be lost at shutdown, fail invisibly, outlive its request, or mutate state after the caller assumes completion.

**Prefer:** Retain a task/future/process handle, supervise it, await or join it where required, and define cancellation and failure reporting.

## `general.resource.unclosed` — Implicit resource lifetime (`BLOCK`)

**Avoid:** Relying on garbage collection/finalization for files, sockets, locks, transactions, streams, cursors, or other scarce resources.

**Why:** Release becomes delayed or nondeterministic and failure paths can leak capacity.

**Prefer:** Lexical ownership, context/try-with-resource constructs, RAII, `after`/`finally`, or a documented lifecycle owner.

## `general.retry.unsafe` — Retry without a bounded idempotency contract (`BLOCK`)

**Avoid:** Retrying non-idempotent work, nested retries at several layers, or retry loops without limits, classification, jitter, and cancellation.

**Why:** Retries can duplicate side effects, amplify outages, and extend latency beyond the caller's deadline.

**Prefer:** Retry only classified transient failures; establish idempotency/deduplication, one retry owner, attempt/deadline limits, backoff, and observability.

## `general.execution.string-built` — String-built executable input (`BLOCK`)

**Avoid:** Concatenating untrusted values into SQL, shell commands, expressions, templates, paths, or dynamic code.

**Why:** Data crosses into executable syntax and can alter the intended operation.

**Prefer:** Bind parameters, typed APIs, allowlisted identifiers, structured command arguments, and canonical path checks. Never use escaping as the sole boundary when a structured API exists.

## `general.secret.exposure` — Secret in source, output, or diagnostics (`BLOCK`)

**Avoid:** Hard-coded credentials, secret-bearing identifiers, raw tokens in exceptions/logs, or debug rendering of sensitive objects.

**Why:** Source history, telemetry, crash reports, and agent transcripts become disclosure channels.

**Prefer:** Secret stores/environment injection, redaction-aware types, allowlisted structured logging, and non-secret correlation identifiers.

## `general.state.hidden-global` — Hidden mutable global state (`WARN`)

**Avoid:** Process-wide mutable state that changes behavior without an explicit owner, synchronization rule, reset boundary, or test isolation strategy.

**Why:** Ordering, concurrency, reuse, and tests become dependent on invisible prior activity.

**Prefer:** Pass owned state, encapsulate it behind one lifecycle owner, or document and prove the narrow global invariant.

## Reporting rule

A named pattern is not automatically a finding. Report it only after identifying:

```text
trigger → prohibited behavior → failure mechanism → caller/operational consequence
```

If that chain is not established, return it as unproved or omit it.
