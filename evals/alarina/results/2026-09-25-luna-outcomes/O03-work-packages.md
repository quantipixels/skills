# Work packages

Dependency-ordered set; no external prerequisites. The supplied HTTP middleware and queue serializer with contract tests are sufficient context for these bounded packages. These are draft delivery packages derived from the accepted change, not published tickets.

## WP-1: Accept or generate a request ID at the HTTP boundary

**What it delivers:** Each incoming request has a request ID: preserve the optional request ID header when present, and generate an ID when it is absent. Existing clients that omit the header continue to work.

**Context:** The existing HTTP middleware is the entry point. Existing clients must remain compatible.

**Acceptance and proof:** Contract tests show that a supplied header value becomes the request ID; a request without the header receives a generated ID; both request forms proceed through the existing request path.

**Depends on:** None
**Boundary:** Does not define a new header name or ID format; use the accepted interface and existing project convention.
**State:** Open

## WP-2: Propagate the request ID into asynchronous job metadata

**What it delivers:** Jobs created from requests carry that request's ID in their metadata, including IDs generated for requests without a header.

**Context:** The queue serializer is the existing job metadata boundary.

**Acceptance and proof:** Serializer contract tests prove a request ID survives serialization into job metadata for both supplied and generated IDs. Existing serialized clients or payloads remain consumable where required by current compatibility behavior.

**Depends on:** WP-1
**Boundary:** No external ticket publication or release work.
**State:** Open

## WP-3: Include the request ID in structured logs

**What it delivers:** Structured log records for the request and its asynchronous job include the same request ID.

**Context:** Use the ID established at the HTTP boundary and carried in job metadata.

**Acceptance and proof:** Log-boundary checks verify the same ID appears in structured request and job records for both supplied and generated IDs; existing clients remain supported.

**Depends on:** WP-2
**Boundary:** No logging backend migration or release work.
**State:** Open

**Startable frontier:** WP-1

**Validation:** Dependencies are acyclic and reflect the flow from request identification to job propagation to job logging. Each package has an observable outcome and a proof seam. The header name, ID format, and exact log event set were not supplied, so the packages leave those details to established project conventions rather than inventing requirements.
