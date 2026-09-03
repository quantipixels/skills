# Ktor runtime mechanics

Load only when the exact candidate uses Ktor and touches a mechanism below whose semantics can change HTTP behavior, cancellation, security, resource ownership, resilience, or proof. This is not a cached Ktor manual.

The detected Ktor/Kotlin/coroutines version, server/client engine, deployment model, serialization/auth stack, and project configuration control exact APIs and defaults.

## Application, plugins, and routing form an ordered execution pipeline

- Treat plugin installation scope/order and application/route lifecycle as behavior, not decoration. Install/configure a concern at the narrowest scope that owns it and verify interactions when ordering can change authentication, serialization, errors, metrics, or response behavior.
- Make the HTTP contract explicit at the route boundary: method, status, headers, content type/negotiation, validation, and failure representation. Do not let scattered catches or framework defaults define public errors accidentally.
- Separate transport models from persistence/internal models when their compatibility, validation, serialization, or lifecycle differs.
- Authentication is not authorization. Keep protected-operation authorization at the owner of the sensitive action rather than assuming a successful pipeline authentication settles every later decision.

## Request cancellation must be proved for the actual engine/path

- Keep route work inside the request coroutine when its lifetime should end with the request; child work then participates in structured cancellation when the request context is canceled.
- Do not assume a client disconnect automatically cancels server processing on every Ktor generation/engine. Establish the project's request-lifecycle/plugin/engine behavior when abandoned work is consequential.
- Blocking or CPU-bound code may not observe cooperative coroutine cancellation promptly. Give it an appropriate execution boundary and explicit cancellation/resource policy.
- Background work that must outlive the request belongs to an application-owned worker/task boundary, not a detached launch from a handler.

## Clients and resilience need one owner

- Reuse an appropriately scoped configured `HttpClient`/engine for one lifecycle/remote contract instead of constructing and leaking clients per call. Own close/shutdown explicitly where the project does not.
- Distinguish connect/request/socket/pool/protocol/application failures according to the active engine/plugins before retrying or translating them.
- Retry only classified operations whose idempotency, caller deadline/budget, cancellation, attempt bound, and backoff are explicit. Avoid nested retry owners across Ktor, a resilience library, and caller code.
- Treat authentication refresh, redirect, retry, validation, and error plugins as an interacting client pipeline; verify ordering/exception semantics when they can change the result.

## Streaming and long-lived sessions multiply resource obligations

- Bound request bodies, multipart uploads, WebSockets/SSE sessions, frame/message sizes, channels, fan-out, buffers, and per-client work according to the actual product/deployment contract.
- A coroutine or socket is cheaper than a thread but still consumes memory, queues, descriptors/connections, and downstream capacity. Cheap concurrency is not unbounded concurrency.
- Keep cancellation, disconnect, backpressure/slow-consumer behavior, shutdown/drain, and unfinished-work semantics observable in proof for long-lived paths.

## Retrieval anchors

Use current Ktor first-party documentation for application/plugin and HTTP request lifecycle, the selected engine, client lifecycle/timeouts/plugins, WebSockets/SSE/uploads, authentication/security, and Ktor test facilities. Compose it over current Kotlin coroutine semantics rather than weakening structured concurrency or cancellation at the framework layer.

## What not to preserve locally

Do not cache plugin names/options, engine feature matrices, authentication recipes, serialization syntax, status-page DSLs, dependency coordinates, or release-specific defaults. Resolve those from the exact Ktor generation and project configuration.
