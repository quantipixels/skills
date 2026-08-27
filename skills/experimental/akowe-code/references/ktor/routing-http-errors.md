# Ktor routing, HTTP contracts, and errors

Use when the candidate changes routes, content negotiation, request/response models, validation, or failure mapping.

<a id="ktor-http-route-contract"></a>
## `ktor-http-route-contract` — Make routing and HTTP semantics explicit

Keep route matching non-ambiguous and treat method, path, status, headers, content type, versioning, and error shape as part of the caller contract.

<a id="ktor-http-transport-model"></a>
## `ktor-http-transport-model` — Separate transport models when lifecycles differ

Do not expose persistence/internal types directly when wire compatibility, validation, redaction, or lifecycle differs. Map at the boundary that owns the public contract.

<a id="ktor-http-validation"></a>
## `ktor-http-validation` — Validate untrusted input before domain work

Parse, size-check, and validate external input at the HTTP boundary, then hand precise values inward. Domain invariants remain with the domain owner.

<a id="ktor-http-errors"></a>
## `ktor-http-errors` — Centralize stable error translation

Use one owned `StatusPages`/error mapping contract for shared failures. Avoid scattered catches that produce inconsistent status/body/log behavior or leak internal exceptions.

<a id="ktor-http-content"></a>
## `ktor-http-content` — Keep serialization and negotiation deliberate

Configure serializers/content negotiation once for the owned API boundary and test absent/null/default/polymorphic behavior when Kotlin model semantics affect the wire contract.

## Sources

- Ktor routing: <https://ktor.io/docs/server-routing.html>
- StatusPages: <https://ktor.io/docs/server-status-pages.html>
- Content negotiation: <https://ktor.io/docs/server-serialization.html>
