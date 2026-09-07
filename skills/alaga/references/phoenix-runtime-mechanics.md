# Phoenix runtime mechanics

Load only when the exact Phoenix candidate touches routing/context, Ecto data/transaction, Channel/PubSub/Presence, LiveView state/security, or background-work semantics that can change correctness, authorization, resource use, or proof. Compose this over Elixir/OTP process and supervision mechanics.

The detected Phoenix/Plug/LiveView/Ecto/Elixir/OTP/database versions and generated project conventions control exact APIs and defaults.

## HTTP pipelines and contexts should preserve ownership

- Keep router/Plug pipeline boundaries explicit for browser/API/session/authentication concerns; controller or LiveView transport code should translate HTTP/UI input and delegate durable business/data policy to the owning application/context boundary.
- A Phoenix context is useful when it owns capability, policy, data access, or domain meaning. Do not create forwarding context functions that merely rename Repo calls and add no boundary.
- Treat params, payloads, socket events, and client-side UI state as untrusted input regardless of what the rendered interface permits.

## LiveView has two security/lifecycle phases

- A LiveView starts as a regular HTTP render and later runs as a stateful server process. Authentication/session setup and authorization therefore have HTTP and connected-state boundaries; do not assume one check permanently authorizes later events.
- Re-authorize protected mutations at the operation/event boundary using current domain scope/identity. A connected socket is not proof that an arbitrary client-supplied event or identifier is allowed.
- Socket assigns are server-process state. Keep them minimal enough for the connection lifetime; derive/cache selectively and use streams or other appropriate mechanisms for large dynamic collections rather than retaining unnecessary full state.
- Async/background work tied to the view should stop or be reconciled when the LiveView exits. Work that must outlive navigation/disconnect belongs to a separately supervised/durable owner.

## Ecto transactions and data shape are local contracts

- Let transactions own one local database atomicity boundary. Remote effects require durable coordination/idempotency/compensation rather than a longer local transaction.
- Keep changeset validation, database constraints, authorization, and workflow policy distinct; one does not automatically replace the others.
- Select/preload/query only the data shape needed for the operation and prove cardinality/query behavior when association traversal can amplify work.
- Keep schema/entity representation separate from external API/UI contracts when compatibility, authorization, or lifecycle differs.

## Channels, PubSub, and Presence are distributed process mechanisms

- Bound channels/sockets/message rates and per-client process/resource cardinality. One client should not be able to create unbounded server processes or queues.
- Phoenix PubSub transports messages; it is not a durable exactly-once workflow or transactional source of truth.
- Presence is replicated/distributed liveness information rather than a single transactional authority. Design product decisions that need durable truth around the owning durable state, not momentary presence alone.
- Treat disconnect/reconnect, duplicate/out-of-order observations, slow clients, and node/process failure according to the actual Channel/PubSub/Presence contract when consequential.

## Retrieval anchors

Use current Phoenix, LiveView, Ecto and Phoenix.PubSub/Presence first-party documentation for router/Plug and context conventions, LiveView lifecycle/security/streams/async work, Ecto transactions/querying, Channel resource limits, PubSub and Presence semantics. Current Elixir/OTP process mechanics remain controlling underneath the framework.

## What not to preserve locally

Do not cache generated-auth code, router macros, LiveView API recipes, Ecto query syntax, deployment configuration, endpoint/socket options, or release-specific security defaults. Resolve those from the exact project generation and current owning sources.
