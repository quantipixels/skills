# Elixir and OTP guards

Elixir's official anti-pattern guides provide the primary catalogue. The rules remain context-sensitive: a named anti-pattern is a trigger for analysis, not an automatic rewrite.

## Code-related guards

### `elixir.atom.unbounded-dynamic-creation` (`BLOCK`)

**Avoid:** `String.to_atom/1` on request-, file-, dependency-, or otherwise unbounded values.

**Why:** Atoms are not garbage-collected and the finite atom table can be exhausted.

**Prefer:** Keep strings, map explicitly to a finite atom set, or use `String.to_existing_atom/1` only when existence/failure is controlled.

**Source:** [Dynamic atom creation](https://hexdocs.pm/elixir/code-anti-patterns.html#dynamic-atom-creation).

### `elixir.with.complex-else` (`WARN`)

**Avoid:** A large `with ... else` that merges several unrelated failure shapes.

**Why:** It becomes unclear which operation produced an error and overlapping patterns are easy to mishandle.

**Prefer:** Normalize errors close to each operation or use explicit `case` composition when branching is the core behavior.

**Source:** [Complex `else` clauses in `with`](https://hexdocs.pm/elixir/code-anti-patterns.html#complex-else-clauses-in-with).

### `elixir.clause.complex-extraction` (`WARN`)

**Avoid:** Extracting many body-only fields directly in several function heads alongside match/guard fields.

**Why:** Readers cannot distinguish dispatch criteria from ordinary local data.

**Prefer:** Match only what controls the clause; bind the whole value and extract body data inside.

**Source:** [Complex extractions in clauses](https://hexdocs.pm/elixir/code-anti-patterns.html#complex-extractions-in-clauses).

### `elixir.function.long-parameter-list` (`WARN`)

**Avoid:** Long positional parameter lists whose values can be confused or belong to clear groups.

**Why:** Call sites become error-prone and the function may own several responsibilities.

**Prefer:** Structs/maps for coherent data, keyword options for optional configuration, or split responsibilities. Do not apply a fixed arity threshold mechanically.

**Source:** [Long parameter list](https://hexdocs.pm/elixir/code-anti-patterns.html#long-parameter-list).

### `elixir.module.namespace-trespass` (`BLOCK`)

**Avoid:** A library defining modules under another library's namespace without the namespace owner's contract.

**Why:** The VM loads one module per name and future/current packages can collide.

**Prefer:** Prefix modules with the package namespace; keep documented protocol/Mix-task exceptions.

**Source:** [Namespace trespassing](https://hexdocs.pm/elixir/code-anti-patterns.html#namespace-trespassing).

### `elixir.map.non-assertive-required-access` (`BLOCK`)

**Avoid:** `map[:required_key]` when the key is contractually required.

**Why:** Missing data becomes `nil` and fails later, far from the boundary.

**Prefer:** `map.required_key`, `Map.fetch!`, struct access, or pattern matching; retain access syntax for genuinely optional/dynamic keys.

**Source:** [Non-assertive map access](https://hexdocs.pm/elixir/code-anti-patterns.html#non-assertive-map-access).

### `elixir.pattern.catch-all-hides-new-state` (`BLOCK`)

**Avoid:** A broad `_` branch for a closed return contract where new variants must be handled deliberately.

**Why:** Unexpected/new values are silently folded into an unrelated path.

**Prefer:** Match known variants explicitly and let unexpected values fail or return a clear error.

**Source:** [Non-assertive pattern matching](https://hexdocs.pm/elixir/code-anti-patterns.html#non-assertive-pattern-matching).

### `elixir.boolean.truthiness-for-boolean-contract` (`WARN`)

**Avoid:** `&&`, `||`, or `!` when operands are required to be booleans, especially around Erlang APIs returning atoms such as `:error`/`:undefined`.

**Why:** Non-boolean truthy values can pass a condition unexpectedly.

**Prefer:** `and`, `or`, `not` for boolean contracts; use truthiness only when it is intentional.

**Source:** [Non-assertive truthiness](https://hexdocs.pm/elixir/code-anti-patterns.html#non-assertive-truthiness).

### `elixir.struct.too-many-fields` (`WARN`)

**Avoid:** Very large flat structs, especially 32+ fields, without evidence that one cohesive value owns them.

**Why:** BEAM map representation changes and the shape often indicates mixed responsibilities.

**Prefer:** Cohesive nested structs or separate domain values; retain a large struct when measured access/serialization needs justify it.

**Source:** [Structs with 32 fields or more](https://hexdocs.pm/elixir/code-anti-patterns.html#structs-with-32-fields-or-more).

## Process and OTP guards

### `elixir.process.code-organization` (`WARN`)

**Avoid:** A GenServer/Agent/process solely to group functions with no runtime state, concurrency, shared-resource, or fault-isolation requirement.

**Why:** Calls become serialized and the process imposes runtime behavior without a runtime need.

**Prefer:** Modules/functions; introduce a process only for an owned runtime property.

**Source:** [Code organization by process](https://hexdocs.pm/elixir/process-anti-patterns.html#code-organization-by-process).

### `elixir.process.scattered-interface` (`BLOCK`)

**Avoid:** Direct `Agent`/`GenServer.call`/`cast` interactions scattered across unrelated modules.

**Why:** State format and process protocol can be mutated inconsistently and ownership becomes unclear.

**Prefer:** One public interface module that owns messages, validation, and state invariants.

**Source:** [Scattered process interfaces](https://hexdocs.pm/elixir/process-anti-patterns.html#scattered-process-interfaces).

### `elixir.process.excessive-message-copy` (`WARN`)

**Avoid:** Sending/capturing a large struct when the receiving process needs only a few fields.

**Why:** BEAM message passing copies data between process heaps and increases CPU/memory cost.

**Prefer:** Extract the minimal payload before `send`, `spawn`, `Task`, call, or cast.

**Source:** [Sending unnecessary data](https://hexdocs.pm/elixir/process-anti-patterns.html#sending-unnecessary-data).

### `elixir.process.unsupervised-long-lived` (`BLOCK`)

**Avoid:** Long-running important processes started outside a supervision tree.

**Why:** Startup order, restart policy, shutdown order, introspection, and lifecycle control become ad hoc.

**Prefer:** A child specification under the correct supervisor; short-lived deliberately linked tasks are separate.

**Source:** [Unsupervised processes](https://hexdocs.pm/elixir/process-anti-patterns.html#unsupervised-processes).

### `elixir.task.async-without-consumption` (`BLOCK`)

**Avoid:** `Task.async` without later `await`, `yield`, or `shutdown`, or when the task should not be linked to the caller.

**Why:** The task is linked and its result/failure/lifecycle is left unconsumed.

**Prefer:** Consume the task result; use supervised tasks or `Task.start` only for a deliberately different ownership contract.

**Source:** [`Task`](https://hexdocs.pm/elixir/Task.html).

### `elixir.genserver.blocking-callback` (`BLOCK`)

**Avoid:** Long blocking I/O/CPU work in a GenServer callback while the same process must serve other messages.

**Why:** One callback serializes the mailbox and creates latency/backlog for every caller.

**Prefer:** Keep callbacks short, offload owned work to tasks/workers, and return results through an explicit protocol.

**Source:** [`GenServer`](https://hexdocs.pm/elixir/GenServer.html).

### `elixir.cast.requires-acknowledgement` (`BLOCK`)

**Avoid:** `cast` for an operation whose caller needs acceptance, ordering confirmation, backpressure, or a result.

**Why:** Cast returns before the server processes the message and supplies no application-level acknowledgement.

**Prefer:** `call`, a monitored task, or an explicit async acknowledgement protocol.

**Source:** [`GenServer.cast`](https://hexdocs.pm/elixir/GenServer.html#cast/2).
