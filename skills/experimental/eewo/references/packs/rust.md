# Rust starter guard pack

These are high-confidence seeds, not a complete Rust style guide. Load only when applicable.

## `rust.async.sync-lock-across-await`

- Kind: prohibition
- Applies: async Rust using `std::sync` or `parking_lot` lock guards.
- Invariant: an async task must not hold a non-async-aware lock guard across a suspension point.
- Do not: carry such a guard across `.await`.
- Failure mechanism: the lock is not designed for suspension across async scheduling and can block progress or contribute to deadlock.
- Safe paths: end the guard's lexical scope before `.await`; use an async-aware mutex only when state genuinely must remain locked across suspension.
- Enforcement: `clippy::await_holding_lock` plus semantic review for equivalent/custom guard types.
- Source: official Clippy `await_holding_lock` documentation.

## `rust.async.refcell-borrow-across-await`

- Kind: prohibition
- Applies: async code holding `RefCell` `Ref`/`RefMut` values.
- Invariant: dynamic borrow exclusivity must not remain outstanding across suspension.
- Do not: retain a `Ref` or `RefMut` across `.await`.
- Failure mechanism: later task progress can encounter the still-active dynamic borrow and panic.
- Safe paths: constrain the borrow to a lexical block before awaiting; redesign ownership when the value must survive suspension.
- Enforcement: `clippy::await_holding_refcell_ref` plus semantic review.
- Source: official Clippy documentation.

## `rust.error.unproved-unwrap-on-fallible-data`

- Kind: advisory
- Applies: non-test production paths consuming caller-, file-, network-, parse-, or dependency-controlled fallible values.
- Invariant: ordinary external failure remains represented as an error rather than an unexplained process panic.
- Do not: use `unwrap()`/`expect()` merely because success is assumed.
- Failure mechanism: an unproved assumption converts recoverable failure into panic.
- Safe paths: propagate with `?`, pattern-match/transform the error, or establish a local invariant and document why the panic is unreachable/intentional.
- Exceptions: tests, compile-time/initialization invariants, or explicitly fail-fast boundaries where panic is part of the contract.
- Enforcement: selectively enable Clippy `unwrap_used`/`expect_used`; do not blanket-enable every restriction lint.
- Sources: official Clippy lint/configuration documentation; community candidate inventories such as `actionbook/rust-skills` are supporting evidence only.
