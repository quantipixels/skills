# Elixir processes, GenServer, and state ownership

Use when a process/GenServer/Agent is introduced or mutable state/messages cross process boundaries.

<a id="ex-proc-real-owner"></a>
## `ex-proc-real-owner` — Use a process only for real state, isolation, or lifecycle ownership

Keep pure logic outside processes. A GenServer is not a class wrapper; it should serialize a real invariant or own a lifecycle/resource boundary.

<a id="ex-proc-callbacks"></a>
## `ex-proc-callbacks` — Keep callbacks short and explicit

Avoid long blocking remote/file work inside callbacks. Long callbacks serialize unrelated messages and create mailbox/timeout cascades.

<a id="ex-proc-protocol"></a>
## `ex-proc-protocol` — Make message and call contracts explicit

Use stable message shapes and return semantics. Avoid hidden synchronous self-calls or generic catch-all messages that make state transitions opaque.

<a id="ex-proc-state"></a>
## `ex-proc-state` — Keep state minimal and invariant-oriented

Store only state the process genuinely owns; derive transient values when practical and keep state transition functions independently testable.

<a id="ex-proc-call-cast"></a>
## `ex-proc-call-cast` — Choose synchronous versus asynchronous interaction from ownership

Use `call` when the caller needs a result/backpressure and `cast` only when loss/failure visibility semantics are acceptable. Do not use casts merely to avoid waiting.

## Sources

- GenServer: <https://hexdocs.pm/elixir/GenServer.html>
- OTP design principles: <https://www.erlang.org/doc/system/design_principles.html>
