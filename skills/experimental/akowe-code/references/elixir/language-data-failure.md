# Elixir language, data, and failure contracts

**Research baseline:** Elixir 1.20 with OTP 27+ / compatible with OTP 29 at the 2026-08-27 cutoff. Preserve the repository/release baseline.

<a id="ex-lang-patterns"></a>
## `ex-lang-patterns` — Let data shape drive control flow

Prefer pattern-matched function clauses and guards when they make valid states/inputs explicit. Avoid deeply nested `case`/`if` trees when dispatch can be made structural.

<a id="ex-lang-results"></a>
## `ex-lang-results` — Use tagged results for expected failure

Return `{:ok, value}` / `{:error, reason}` for expected recoverable outcomes. Reserve exceptions for exceptional/invariant-breaking conditions or APIs whose owning contract is exception-based.

<a id="ex-lang-pipelines"></a>
## `ex-lang-pipelines` — Keep pipelines at one readable abstraction level

Use `|>` when the data transformation remains obvious. Introduce names or branching when a pipeline hides ownership, failure, ordering, or intermediate meaning.

<a id="ex-lang-binary-atom"></a>
## `ex-lang-binary-atom` — Distinguish strings/binaries/iodata and never grow atoms from untrusted input

Use the representation required by the boundary and avoid converting runtime-unbounded external strings into atoms.

<a id="ex-lang-enum-stream"></a>
## `ex-lang-enum-stream` — Choose eager versus lazy collection semantics deliberately

Use `Enum` for bounded eager work; use `Stream` when laziness/chunking meaningfully reduces work or memory. Do not add lazy layers to small finite collections without benefit.

## Sources

- Elixir anti-patterns: <https://hexdocs.pm/elixir/code-anti-patterns.html>
- Elixir core docs: <https://hexdocs.pm/elixir/>
