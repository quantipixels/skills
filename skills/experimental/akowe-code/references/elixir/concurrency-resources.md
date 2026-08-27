# Elixir concurrency, resources, Registry, and ETS

Use when work/cardinality/shared lookup/storage can grow with external input or multiple processes.

<a id="ex-res-bound-concurrency"></a>
## `ex-res-bound-concurrency` — Bound process/task/message cardinality

BEAM processes are cheap, not free. Bound fan-out, Task concurrency, client/session processes, mailbox growth, queues, and external work from explicit capacity/downstream constraints.

<a id="ex-res-mailbox"></a>
## `ex-res-mailbox` — Treat mailbox growth as backpressure evidence

A process that receives faster than it handles will accumulate memory and latency. Reduce producers, batch/coalesce, partition ownership, or introduce a bounded queue/flow rather than assuming the mailbox is infinite.

<a id="ex-res-registry"></a>
## `ex-res-registry` — Use Registry for real naming/dispatch semantics

Choose unique/duplicate registry behavior and lifecycle intentionally. Do not add process registries merely to simulate global object lookup.

<a id="ex-res-ets-owner"></a>
## `ex-res-ets-owner` — Give ETS tables an explicit owner and growth policy

Choose table type/access/concurrency options from usage, keep lifecycle ownership clear, and bound or expire externally driven data.

<a id="ex-res-external"></a>
## `ex-res-external` — Own sockets/files/ports and external clients at a lifecycle boundary

Supervision/process lifetime should match resource lifetime. Ensure shutdown and failure clean up resources instead of leaving hidden owners.

## Sources

- Registry: <https://hexdocs.pm/elixir/Registry.html>
- Erlang ETS: <https://www.erlang.org/doc/apps/stdlib/ets.html>
- OTP design principles: <https://www.erlang.org/doc/system/design_principles.html>
