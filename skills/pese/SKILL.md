---
name: pese
description: Serve one explicitly invoked local file, directory, or local web resource through private Tailscale Serve or an explicitly accepted encrypted Tailcat fallback, and return the exact access target. Use only when directly invoked to make that local resource temporarily reachable through a private transport. Exclude public/anonymous tunnels, permanent hosting, production serving, and artifact creation.
disable-model-invocation: true
---

# Pèsè

Apply least privilege to temporary private access. Direct invocation authorizes task-scoped staging, an ephemeral local listener when needed, and one narrow temporary private route with ready tooling. Installation, persistent configuration/startup, stored credentials, DNS publication, public exposure, broad roots and unrelated mutation need separate authority.

Resolve volatile syntax from the installed transport and current official Tailscale Serve or Tailcat documentation; use `irinse` for setup changes.

## Bound and serve

Pin the exact file, directory or running local web resource, companion assets, intended reader/access mode and expiry. Reject repository/home/credential roots, traversal, unresolved symlinks and boundaries containing unrelated secrets. Review companions as a narrow allowlist and stage them only when the transport cannot preserve that boundary.

Prefer Tailscale Serve when usable and the reader has tailnet access. Serve the resource directly where the installed client supports it, otherwise expose only a task-owned loopback service. Never use Funnel. Preserve unrelated Serve/Services state: capture enough pre-state for scoped rollback, add one non-conflicting route, and determine exact removal before mutation.

Use [Tailcat fallback](references/tailcat.md) only when Serve is unsuitable, the reader can run a compatible client, and the user accepts its bearer-capability, relay-metadata, CLI-receiver and stability limits. Tailcat forwards TCP, so expose only a task-owned loopback service. Never substitute a public tunnel.

## Acceptance and revocation

Success requires:

- the exact resource is reachable through the returned HTTPS URL or complete receiver invocation;
- content outside the allowlist, including resolved symlink escapes, is unreachable;
- no public or unintended listener/route is enabled; and
- pre-existing transport configuration differs only by the task-owned route.

Route readiness and receiver prerequisites are distinct. When receiver-side execution is unavailable, prove the live route and containment, return the exact usable target, and state the remaining prerequisite.

On failure or expiry, revoke remote access before stopping only task-owned listeners/staging and deleting ephemeral secrets. Verify unrelated pre-state and that the target no longer works. Report any residual route, process or secret with its recovery action.

Return `AVAILABLE` with the exact direct HTTPS resource URL for Serve, or complete Tailcat receiver invocation plus separately secured token-delivery requirement; then transport, boundary, reader prerequisite, expiry, proof, limitations and cleanup. Return `CAPABILITY_GAP` with the unmet transport, reader, authority, privacy or access requirement.

Never place a live Tailcat token in durable records, logs, screenshots, Git or broad channels.
