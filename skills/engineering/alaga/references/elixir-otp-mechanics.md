# Elixir and OTP mechanics

Load only when the exact Elixir/OTP candidate touches process ownership, supervision/failure, concurrency/resource, or runtime-configuration semantics that can change correctness or operations. This is not an Elixir style guide or OTP catalogue.

The repository's actual Elixir/Erlang/OTP versions, release topology, libraries, and deployment configuration control version-sensitive behavior.

## A process is an ownership and isolation boundary, not a class

- Create a process when something needs independent state, mailbox, failure/lifecycle, scheduling, or resource ownership. Keep pure computation as functions rather than wrapping it in a GenServer for architectural appearance.
- Make message protocols and state transitions explicit. A mailbox is an asynchronous queue with resource consequences, not a free method-call abstraction.
- Keep GenServer callbacks bounded; long blocking work stalls that process's mailbox and every caller depending on it. Move independently owned work to Tasks/workers or another appropriate boundary.
- Choose synchronous calls, asynchronous casts/messages, links, and monitors from the delivery/failure contract rather than convenience. Avoid synchronous self-calls and hidden cycles that cannot make progress.

## Supervision encodes expected failure meaning

- Select supervision strategy and child restart semantics from which failures should affect siblings and whether restarting can restore a valid state. A supervisor cannot repair persistent invalid input/state by retrying forever.
- Bound restart intensity and retry loops; repeated fast failure is an operational condition, not resilience.
- Own Tasks and async work. Await/yield/shutdown/cancel or supervise them according to whether the result/failure matters; do not detach important work with no result or lifecycle owner.
- Understand link/monitor propagation at boundaries such as Tasks and supervised children so one crash neither silently disappears nor takes down unrelated work accidentally.

## Cheap processes still need cardinality and resource bounds

- Bound spawned processes, mailbox growth, Task concurrency, queues, Registry keys, ETS tables/data, external connections, and work admitted from untrusted clients.
- Give ETS and Registry state an explicit owning process/application lifecycle. Shared lookup/storage does not eliminate mutation, access, consistency, cleanup, or restart semantics.
- Prefer pressure at admission over hoping a downstream mailbox or process heap absorbs unlimited work.

## Data, failure, and configuration should preserve semantics

- Use pattern matching/guards and tagged results for expected alternatives when they keep valid states/failure explicit; reserve exceptions/exits for the failure meanings appropriate to the owning boundary.
- Do not create atoms from unbounded external input. Distinguish binaries/UTF-8 strings/charlists/iodata where encoding or I/O semantics matter.
- Keep compile-time configuration separate from runtime/deployment configuration. Runtime secrets and environment-specific values belong in the release/runtime configuration path, not baked into compiled assumptions.
- Test concurrent behavior with messages, monitors, supervised processes, or deterministic synchronization rather than sleeps/races.

## Retrieval anchors

Use current Elixir and Erlang/OTP first-party documentation for processes, GenServer/Task/Supervisor/Registry/ETS semantics, OTP design principles, releases, and compile-vs-runtime configuration. Exact library/module APIs remain a current-source question.

## What not to preserve locally

Do not cache Mix/Hex commands, macro/style advice, supervision-tree templates, module API indexes, deployment recipes, or OTP-version tables. Keep only recurring process/failure/resource semantics whose consequences survive version changes.
