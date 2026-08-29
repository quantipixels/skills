# Tailcat fallback

Load only when Tailscale Serve is unavailable/unsuitable and the intended reader can run Tailcat.

## Resolve the actual Tailcat interface

Tailcat has no stability promise for its CLI, API, wire format, or public relay service. Do not treat this reference as a versioned command manual.

If Tailcat is installed, identify its build/version provenance and use the binary's official embedded README/help together with the matching official `tailscale/tailcat` source/docs when that revision can be resolved. Installed behavior outranks examples from a newer upstream revision.

If Tailcat is absent and installation is authorized, use the latest official `tailscale/tailcat` README/source for installation and serving/receiver syntax. Because upstream currently has no stable releases, latest official mainline documentation is the setup source of truth; refresh it at execution time rather than pinning an old setup recipe here.

Use `irinse` when installation or upgrade is required. An unrelated executable/package named `tailcat` is not sufficient identity.

## Security and stability boundary

Tailcat provides a userspace WireGuard tunnel without the normal Tailscale control plane/system routing. Public Tailcat DERP relays are best-effort and may be rate-limited or changed. Payload is encrypted end-to-end, while relay operators can observe connection metadata; report only privacy guarantees supported by current official evidence.

Tailcat forwards TCP rather than serving files/directories. Fihan therefore exposes only the task-owned loopback port needed for the requested resource.

For an ordinary temporary share, use a fresh ephemeral server identity according to the current installed/upstream interface. Do not create or reuse saved server keys, stable DNS tokens, `all`-port forwarding, exit-node behavior, or auth-free SSH for this outcome. A reusable server identity changes a one-run access capability into durable authority.

Treat the returned connection token as a bearer secret unless current verified server/client configuration proves identity-bound authorization. Keep live tokens out of Git, durable records, logs, screenshots, and broad channels.

## Return the usable receiver target

Derive the receiver syntax from the actual installed Tailcat documentation or latest official upstream documentation. The result handed to the user must be a complete receiver invocation that addresses the requested resource through the exposed port/path, not merely the connection token or sender invocation.

Tailcat does not normally produce a browser-ready HTTPS URL. If the user requires a normal browser link and the current official Tailcat interface cannot provide one, return `CAPABILITY_GAP` rather than presenting the token as a URL.

Tokens are case-sensitive; do not assume a browser can use a token hostname unless current official evidence explicitly proves that access mode.

## Client identity

Do not hardcode assumptions about which client modes reuse saved client identities. When identity-bound access matters, verify the installed/current implementation and prove that the exact receiver path presents the allowlisted client key before enabling server-side allowlisting.

If the chosen receiver path cannot present the required identity, return `CAPABILITY_GAP`; do not silently remove the restriction or invent an unproved bridge.

## Revocation

Revoke the capability by stopping the Tailcat sender before deleting temporary token/staging material, then verify the returned access target no longer reaches the resource. Remove persistent keys only when their creation was separately authorized; ordinary Fihan runs should not create them. Relay-map caches are not server private keys and are not ordinary cleanup targets.
