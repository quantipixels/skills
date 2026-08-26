# Elixir starter guard pack

The official Elixir anti-pattern guides already use a problem -> example -> refactoring shape that maps closely to `eewo`.

## `elixir.atom.unbounded-dynamic-creation`

- Kind: prohibition
- Applies: strings or identifiers controlled by requests, dependencies, files, or other unbounded sources.
- Invariant: external cardinality must not consume the finite VM atom table.
- Do not: call `String.to_atom/1` on uncontrolled values.
- Failure mechanism: atoms are not garbage-collected and uncontrolled creation can exhaust the atom table/memory and terminate the system.
- Safe paths: explicit string-to-known-atom mapping, keep values as strings, or `String.to_existing_atom/1` only when the finite atom set is already established and failure is handled.
- Source: official Elixir Code-related anti-patterns, “Dynamic atom creation”: <https://hexdocs.pm/elixir/code-anti-patterns.html#dynamic-atom-creation>.

## `elixir.with.complex-else`

- Kind: advisory
- Applies: `with` expressions with multiple failure shapes.
- Invariant: each failure must remain attributable to the operation that produced it.
- Do not: flatten several unrelated failure forms into one large `else` whose patterns are hard to associate with the originating clause.
- Failure mechanism: unrelated failures can overlap and the error origin becomes difficult to understand or maintain.
- Safe paths: normalize return values close to each operation in small functions, or use `case`/explicit composition when the branching itself matters.
- Source: official Elixir Code-related anti-patterns, “Complex `else` clauses in `with`”: <https://hexdocs.pm/elixir/code-anti-patterns.html#complex-else-clauses-in-with>.

## `elixir.process.code-organization`

- Kind: advisory
- Applies: `GenServer`, `Agent`, or other processes introduced only to group functions/code.
- Invariant: a process should model a runtime property such as concurrency, shared-resource access, state ownership, or fault isolation.
- Do not: introduce a process solely as an object/module boundary.
- Failure mechanism: unnecessary serialization can create a bottleneck and impose runtime behavior on callers without a runtime need.
- Safe paths: ordinary modules/functions for pure organization; add a process only when its runtime semantics are required.
- Source: official Elixir Process-related anti-patterns, “Code organization by process”: <https://hexdocs.pm/elixir/process-anti-patterns.html#code-organization-by-process>.
