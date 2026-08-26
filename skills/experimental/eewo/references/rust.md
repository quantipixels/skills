# Rust guards

Curated from the official Rust documentation, Clippy, Tokio documentation, Rust API Guidelines, and candidate corpora in `actionbook/rust-skills`, `leonardomso/rust-skills`, and `wshobson/agents`. Community rules supplied discovery leads; the guards below are deliberately narrower.

## Errors and contracts

### `rust.error.panic-on-recoverable-input` (`BLOCK`)

**Avoid:** `unwrap`, `expect`, indexing, or explicit panic on caller-, file-, network-, parse-, or dependency-controlled failure.

**Why:** A recoverable input/dependency failure becomes process or task termination.

**Prefer:** `Result`/`Option`, `?`, explicit matching, or a locally proved invariant. Tests and deliberate fail-fast startup boundaries are exceptions when panic is part of the contract.

**Sources:** [Rust API Guidelines: errors](https://rust-lang.github.io/api-guidelines/documentation.html#function-docs-include-error-panic-and-safety-considerations-c-failure), [Clippy `unwrap_used`](https://rust-lang.github.io/rust-clippy/stable/index.html#unwrap_used).

### `rust.error.discarded-must-use` (`BLOCK`)

**Avoid:** Silencing an unused `Result`, `JoinHandle`, or `#[must_use]` value without documenting why loss is safe.

**Why:** Failure or unfinished work is dropped while the surrounding path proceeds as success.

**Prefer:** Propagate, handle, join, log with context, or explicitly bind to `_` only at a documented best-effort boundary.

**Sources:** [`unused_must_use`](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-must-use), [`must_use`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-must_use-attribute).

### `rust.error.erased-library-contract` (`WARN`)

**Avoid:** Returning an opaque catch-all error from a reusable library when callers need to distinguish domain outcomes.

**Why:** Callers cannot branch, recover, or preserve the original error contract.

**Prefer:** A stable typed error for library boundaries; context-rich aggregation may remain appropriate inside applications.

**Sources:** [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/), [std `Error`](https://doc.rust-lang.org/std/error/trait.Error.html).

## Async and concurrency

### `rust.async.blocking-on-runtime-worker` (`BLOCK`)

**Avoid:** Blocking file/network APIs, `std::thread::sleep`, or long CPU work directly inside async tasks.

**Why:** Runtime worker threads stop polling unrelated futures and can stall the service.

**Prefer:** Async APIs or `spawn_blocking`/a dedicated bounded executor for blocking or CPU-heavy work.

**Sources:** [Tokio CPU-bound tasks and blocking code](https://docs.rs/tokio/latest/tokio/index.html#cpu-bound-tasks-and-blocking-code), [`spawn_blocking`](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html).

### `rust.async.sync-lock-across-await` (`BLOCK`)

**Avoid:** Holding a `std::sync`/`parking_lot` lock guard across `.await`.

**Why:** Suspension retains a non-async-aware lock and can block progress or deadlock.

**Prefer:** End the guard's lexical scope before awaiting; use an async mutex only when the protected state genuinely must span suspension.

**Source:** [Clippy `await_holding_lock`](https://rust-lang.github.io/rust-clippy/stable/index.html#await_holding_lock).

### `rust.async.refcell-borrow-across-await` (`BLOCK`)

**Avoid:** Retaining `RefCell::Ref` or `RefMut` across `.await`.

**Why:** The dynamic borrow remains active while other work may access the cell, causing runtime panic.

**Prefer:** Constrain the borrow before the suspension point or redesign ownership.

**Source:** [Clippy `await_holding_refcell_ref`](https://rust-lang.github.io/rust-clippy/stable/index.html#await_holding_refcell_ref).

### `rust.async.unbounded-spawn` (`BLOCK`)

**Avoid:** Spawning one task per untrusted/unbounded item without admission control.

**Why:** The runtime can accumulate tasks, buffers, sockets, and downstream work faster than completion.

**Prefer:** `JoinSet` plus a semaphore, buffered streams, worker pools, or bounded request admission.

**Sources:** [Tokio spawning](https://tokio.rs/tokio/tutorial/spawning), [`JoinSet`](https://docs.rs/tokio/latest/tokio/task/struct.JoinSet.html).

### `rust.async.unbounded-channel` (`BLOCK`)

**Avoid:** Unbounded channels where producers can outrun consumers under real workload.

**Why:** Queue memory grows without backpressure.

**Prefer:** Bounded channels with explicit full/closed behavior; use unbounded channels only with a proved producer bound.

**Source:** [Tokio `mpsc`](https://docs.rs/tokio/latest/tokio/sync/mpsc/).

### `rust.async.detached-critical-task` (`BLOCK`)

**Avoid:** Dropping a `JoinHandle` for work whose failure or completion matters.

**Why:** Dropping the handle detaches the task; failure becomes unobserved and lifecycle ownership is lost.

**Prefer:** Retain/join the handle, manage tasks in a `JoinSet`, or supervise them through an explicit owner.

**Source:** [Tokio `JoinHandle`](https://docs.rs/tokio/latest/tokio/task/struct.JoinHandle.html).

### `rust.async.cancel-unsafe-select` (`BLOCK`)

**Avoid:** Using a non-cancellation-safe future in a `select!` loop where losing the race drops partial progress.

**Why:** Data or protocol state can be lost when the branch is repeatedly cancelled.

**Prefer:** Use cancellation-safe operations, retain state outside the future, or restructure the protocol.

**Source:** [Tokio `select!` cancellation safety](https://docs.rs/tokio/latest/tokio/macro.select.html#cancellation-safety).

## Unsafe, memory, and numeric behavior

### `rust.unsafe.unscoped-or-unexplained` (`BLOCK`)

**Avoid:** Large `unsafe` regions or unsafe operations without the exact local safety invariant.

**Why:** Review cannot establish which operation relies on which invariant, increasing unsoundness risk.

**Prefer:** Minimize the block, document `// SAFETY:`, and expose a safe wrapper that enforces preconditions.

**Sources:** [Rust Reference: unsafe](https://doc.rust-lang.org/reference/unsafe-keyword.html), [Rustonomicon](https://doc.rust-lang.org/nomicon/).

### `rust.unsafe.unproved-send-sync` (`BLOCK`)

**Avoid:** Manual `unsafe impl Send`/`Sync` without proving every contained pointer, aliasing, thread-affinity, and mutation invariant.

**Why:** The compiler's thread-safety guarantees are bypassed and data races/UB become possible.

**Prefer:** Let auto traits derive; otherwise document and test the invariant, including with Miri/loom where applicable.

**Source:** [Rustonomicon: Send and Sync](https://doc.rust-lang.org/nomicon/send-and-sync.html).

### `rust.unsafe.invalid-uninitialized-value` (`BLOCK`)

**Avoid:** `mem::zeroed`, deprecated uninitialized techniques, or `MaybeUninit::assume_init` before every byte/value invariant is established.

**Why:** Many Rust types have invalid bit patterns; merely creating an invalid value is undefined behavior.

**Prefer:** `MaybeUninit` with a proved initialization path and minimal unsafe scope.

**Source:** [`MaybeUninit`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html).

### `rust.unsafe.static-mut-reference` (`BLOCK`)

**Avoid:** Creating references to `static mut` or treating it as ordinary global state.

**Why:** Aliasing and concurrent access violate reference rules; Rust 2024 denies static-mut references by default.

**Prefer:** Atomics, locks, `OnceLock`, or owner-controlled thread-local state.

**Source:** [Rust 2024 static-mut references](https://doc.rust-lang.org/edition-guide/rust-2024/static-mut-references.html).

### `rust.resource.forgotten-owner` (`WARN`)

**Avoid:** `mem::forget` or deliberate leaking of a resource-owning value without a bounded, explicit contract.

**Why:** Destructors are skipped and files, locks, memory, or external handles may remain retained.

**Prefer:** Normal RAII/drop, explicit ownership transfer, or a documented process-lifetime allocation.

**Source:** [`mem::forget`](https://doc.rust-lang.org/std/mem/fn.forget.html).

### `rust.numeric.lossy-as-at-boundary` (`BLOCK`)

**Avoid:** `as` casts for externally supplied or correctness-critical numeric narrowing/sign changes.

**Why:** Values can truncate, wrap, or silently change meaning.

**Prefer:** `TryFrom`/`try_into`, range checks, and an explicit overflow/error contract.

**Sources:** [`TryFrom`](https://doc.rust-lang.org/std/convert/trait.TryFrom.html), [Rust Reference casts](https://doc.rust-lang.org/reference/expressions/operator-expr.html#type-cast-expressions).

### `rust.numeric.unchecked-overflow-contract` (`BLOCK`)

**Avoid:** Depending on release-mode integer wrapping for balances, sizes, offsets, counters, or authorization limits.

**Why:** Debug and release behavior can differ and wrapped values can bypass invariants.

**Prefer:** Checked/saturating/wrapping operations chosen explicitly for the domain.

**Source:** [Rust Reference overflow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#overflow).

## Design warnings

### `rust.ownership.clone-to-escape-design` (`WARN`)

**Avoid:** Repeated large or hot-path clones added only to silence ownership errors.

**Why:** The copy can hide unclear ownership and introduce latency/memory cost.

**Prefer:** Clarify the owner, borrow slices/strings, move values, or use shared ownership only when sharing is real. Keep a clone when its cost is negligible and it materially simplifies correct code.

**Mined from:** [`actionbook/rust-skills` anti-patterns](https://github.com/actionbook/rust-skills/blob/main/skills/m15-anti-pattern/SKILL.md), [`leonardomso/rust-skills`](https://github.com/leonardomso/rust-skills).

### `rust.api.deref-as-inheritance` (`WARN`)

**Avoid:** Implementing `Deref` merely to expose another type's API or simulate inheritance.

**Why:** Method resolution and coercion become implicit and the wrapper's semantic boundary is obscured.

**Prefer:** Named delegation, `AsRef`/`Borrow`, or `Deref` only for genuine smart-pointer-like types.

**Source:** [Rust API Guidelines: smart pointers do not add inherent methods](https://rust-lang.github.io/api-guidelines/predictability.html#smart-pointers-do-not-add-inherent-methods-c-smart-ptr).
