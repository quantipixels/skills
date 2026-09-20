# Private access and crawler controls

Read before enabling a Pèsè route. Privacy means keeping content outside unintended clients' reach, including crawlers, preview bots and scrapers. Crawler preferences supplement that boundary; they cannot enforce it.

## Enforce the audience first

Establish who may connect before exposure. Do not silently interpret one intended reader as the whole tailnet. Verify the effective network policy or existing application authorization, including the served port, path and companion assets. When the available boundary is broader or unknown, use a ready narrower mechanism within authority or return `CAPABILITY_GAP`. Do not change shared tailnet policy, authentication settings or persistent credentials without separate authority.

For Tailscale Serve, access rules still apply; HTTP paths are not automatically separate network-policy boundaries. Keep any backend loopback-only and prevent LAN/public origin bypass. Identity-based application gates must trust only verified Serve-injected identity, not arbitrary request headers; check installed support and tagged-device behavior before relying on it. Loopback limits remote bypass, not attacks by untrusted processes on the same host. Preserve unrelated Serve/Funnel state; never reuse a public endpoint for private content or switch an unrelated public service to private.

For Tailcat, follow the existing fallback reference. Encryption protects traffic but a bearer token authorizes its holder, including an automated client. Use verified client-key restrictions when the intended access requires identity binding and the actual receiver supports them. Otherwise require explicit acceptance of the bearer boundary, or stop; do not invent identity enforcement. Keep sender and receiver HTTP forwarding loopback-only.

Do not use a hidden URL, User-Agent allow/deny list, CAPTCHA, rate limit or robots file as authentication. Do not promise to distinguish a browser from automation using the same authorized identity. Unauthorized clients must be denied whether they advertise themselves as a crawler, a browser or neither.

## Apply HTTP privacy controls

For HTTP resources, require these response headers on the task-owned served scope, including non-HTML downloads and required assets:

```http
X-Robots-Tag: noindex, nofollow, nosnippet
Cache-Control: no-store
Referrer-Policy: no-referrer
```

Use the actual server's supported header mechanism. Cover applicable successful, partial, redirect and error responses; do not send private content or tokens in error bodies or external redirects. Replace conflicting cache policy only in the task-owned layer. An HTML meta tag does not protect a separately fetched PDF, image or JSON resource. Do not change authoritative resource bytes merely to inject tags.

When direct transport file serving cannot supply these controls, use a ready, narrow task-owned loopback serving layer. Keep resource allowlisting and the intended access boundary intact; do not turn a wrapper into an unrestricted proxy or expose its origin. If no permitted mechanism can meet the controls, stop rather than claiming success from private transport alone. Non-HTTP transfers do not acquire fictitious HTTP headers; access control and secret handling still apply.

For an entirely task-owned HTTP origin, serve UTF-8 `text/plain` at `/robots.txt`:

```text
User-agent: *
Disallow: /
```

Robots scope is the origin, not a mount directory. Do not overwrite another service's robots file or mount a misleading `/share/robots.txt`. On a shared origin, add a narrowly scoped rule only with authority and preserve existing rules; otherwise report the robots limitation and keep enforced access and response headers. Do not widen access to make the robots file readable.

Robots disallow can prevent a compliant crawler from seeing `noindex`; neither promises de-indexing of a previously exposed URL. Never make private content public to let a search engine read its tags. `no-store` directs compliant HTTP caches, not malicious clients, existing copies or application/service-worker storage. Revocation stops future access; it cannot recall downloads.

## Avoid secondary disclosure

Disable automatic directory listings and expose only the requested resource and reviewed companions. Do not publish sitemaps, submit URLs to indexers, or use public URL-checking, screenshot, preview or scanning services to verify a private resource. Return the target through the intended private channel; keep live tokens out of URLs, diagnostics and durable records except for the existing Tailcat receiver/token contract.

Inspect external subresources, telemetry and outbound requests when they can reveal private content or the access target. Referrer suppression is not a substitute for reviewing script behavior. Reuse self-contained assets where possible; do not add third-party dependencies or disclose content to them without authority. Report a controlling external-data dependency rather than silently sanitizing or breaking the original resource.

## Verify and revoke

Check the exact returned route, not only the local origin or a configuration declaration. Inspect effective access rules and test an allowed request and a relevant denied request when the required clients are available. For an application gate, missing or invalid authorization must return no protected bytes even with a browser-like User-Agent. Do not relax access to run a probe; name an unavailable denial test separately from policy evidence.

For HTTP, inspect actual headers for the requested resource and a representative non-HTML asset when present, robots location/scope when configured, traversal and directory-listing rejection, and absence of an unintended direct listener. Check applicable error or redirect behavior without enumerating an unrelated site. Record exact scope and limits, not a blanket claim that all bots are blocked.

Determine scoped revocation before enabling access. Use an enforceable expiry when a timed cutoff is required; otherwise state the actual lifetime and stop command without promising unattended cleanup. On failure or expiry revoke the route first, then clean task-owned resources and verify unrelated state. Previously public content, downloaded copies and third-party caches are separate recovery limits.
