# Elixir and OTP

Research baseline: Elixir 1.20 requires Erlang/OTP 27+ and is compatible with OTP 29 at the 2026-08-27 cutoff. Treat Elixir and OTP versions as one runtime baseline.

- Prefer pattern-matched function clauses and guards when they make valid input/state cases explicit; avoid deep nested `case`/`if` when the data shape can drive dispatch.
- Use tagged results (`{:ok, value}` / `{:error, reason}`) for expected failure contracts; reserve exceptions for exceptional or invariant-breaking conditions.
- Keep pipelines readable at one abstraction level. Do not force every operation into `|>` when intermediate names or branching make ownership/failure clearer.
- Distinguish binaries, UTF-8 strings, charlists, and iodata. Avoid atom creation from untrusted/runtime-unbounded input.
- Use `Enum` for bounded eager collections and `Stream` when laziness/backpressure over a source materially reduces work or memory.
- A process is an ownership/isolation boundary, not a class. Do not create a GenServer just to hold code or wrap pure functions.
- Keep GenServer callbacks small; own state transitions and message protocols explicitly; avoid hidden synchronous self-calls and long blocking work inside the server.
- Supervision is for restart/lifecycle strategy. Choose child restart semantics from failure meaning, and do not use supervisors to hide persistent bad state or retry storms.
- Own Tasks and async work. Await/yield/cancel or supervise them; do not spawn important detached processes with no failure/result owner.
- Bound mailboxes, concurrency, ETS growth, queues, and external work. BEAM process cheapness does not make unbounded process/channel creation safe.
- Use Registry/ETS when their shared lookup/storage semantics are actually needed; keep ownership, table type, lifecycle, and concurrency semantics explicit.
- Keep compile-time and runtime configuration separate, especially in releases. Secrets belong to runtime deployment configuration, not source.
- Use behaviours/protocols for real polymorphic contracts, not as ceremony around one implementation.
- Use current compiler/type-system diagnostics and Dialyzer/typespecs as proof where they add signal; do not treat specs as runtime validation.
- Test concurrent behavior through messages/state/results rather than sleeps; use supervised processes and deterministic synchronization.

Primary sources:

- Elixir 1.20 changelog: <https://elixir.hexdocs.pm/changelog.html>
- Elixir anti-patterns: <https://hexdocs.pm/elixir/code-anti-patterns.html>
- OTP design principles: <https://www.erlang.org/doc/system/design_principles.html>
