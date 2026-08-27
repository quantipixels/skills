# Elixir supervision, Tasks, and failure semantics

Use when the candidate starts supervised children, Tasks, retries, or background work.

<a id="ex-sup-strategy"></a>
## `ex-sup-strategy` — Choose restart strategy from failure meaning

Select one-for-one/rest-for-one/etc. and child restart policy from dependency and failure semantics. Supervision should expose recovery structure, not hide persistent invalid state.

<a id="ex-sup-restart-storm"></a>
## `ex-sup-restart-storm` — Prevent restart/retry storms

Persistent external or configuration failures can cause repeated crashes. Bound retries/backoff or fail the owning subsystem explicitly rather than looping indefinitely.

<a id="ex-sup-task-owner"></a>
## `ex-sup-task-owner` — Own important Tasks

Await/yield/cancel or supervise work whose result/failure matters. Detached `spawn`/Task work is suitable only when loss is genuinely acceptable and bounded.

<a id="ex-sup-task-supervisor"></a>
## `ex-sup-task-supervisor` — Use Task.Supervisor for dynamic owned concurrency

A Task supervisor gives lifecycle/failure ownership but does not remove the need to bound concurrency, timeouts, result handling, or downstream resources.

<a id="ex-sup-timeout"></a>
## `ex-sup-timeout` — Timeouts do not cancel arbitrary external effects

Know whether the timed-out operation is actually terminated, still running, or has already produced irreversible effects. Design compensation/idempotency at the owning boundary.

## Sources

- Supervisor: <https://hexdocs.pm/elixir/Supervisor.html>
- Task: <https://hexdocs.pm/elixir/Task.html>
- DynamicSupervisor: <https://hexdocs.pm/elixir/DynamicSupervisor.html>
