# Phoenix Channels, PubSub, and Presence

Use when sockets/channels, PubSub, Presence, fan-out, or per-client process/resource behavior changes.

<a id="phx-chan-bounds"></a>
## `phx-chan-bounds` — Bound channels, messages, and per-client work

Treat every socket/channel/process as a resource boundary. Bound channel counts, message rate, payload size, fan-out, and expensive handlers from explicit capacity/risk assumptions.

<a id="phx-chan-protocol"></a>
## `phx-chan-protocol` — Keep channel event contracts explicit

Event names, payloads, replies, authorization, ordering/idempotency expectations, and error behavior form a public protocol. Avoid generic catch-all events that hide ownership.

<a id="phx-chan-pubsub"></a>
## `phx-chan-pubsub` — Treat PubSub as ephemeral delivery, not durable workflow state

Use durable DB/queue/outbox state for transitions that must not be lost or need replay/exact processing. PubSub is appropriate for fan-out where missed/duplicate delivery is tolerable or independently reconciled.

<a id="phx-chan-presence"></a>
## `phx-chan-presence` — Treat Presence as distributed observation

Presence is useful for online/metadata views but should not become a transactional source of truth for business invariants.

<a id="phx-chan-failure"></a>
## `phx-chan-failure` — Define disconnect/reconnect and duplicate-event behavior

Clients reconnect and networks partition. Make server operations safe under retries/rejoins where the same user action can be delivered more than once.

## Sources

- Phoenix Channels: <https://hexdocs.pm/phoenix/channels.html>
- Phoenix PubSub: <https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html>
- Phoenix Presence: <https://hexdocs.pm/phoenix/presence.html>
