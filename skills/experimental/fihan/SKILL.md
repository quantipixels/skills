---
name: fihan
description: Temporarily expose one explicit local file or directory through tailnet-only Tailscale Serve or an explicitly accepted encrypted Tailcat fallback. Use only when explicitly invoked or after explicit experimental acceptance. Exclude public/anonymous tunnels, permanent hosting, production serving, and artifact creation.
disable-model-invocation: true
---

# Fihan

Make one bounded local resource temporarily reachable through a private route and leave exact revocation/cleanup. The local source remains authoritative.

Explicit invocation authorizes only task-scoped staging, an ephemeral local listener when needed, and one narrow temporary private route using already-ready tooling. It does not authorize installation, persistent startup/configuration, saved credentials/keys, public exposure, DNS publication, broad served roots, or unrelated mutation.

## Bound the resource

Pin the exact file/directory, required companion assets, intended reader/access mode, and expiry condition. Reject a repository/home/credential directory, traversal target, unresolved symlink, or resource containing unrelated secrets. When companions are required, expose only a reviewed allowlist; stage them narrowly when the chosen transport cannot preserve that boundary directly.

## Choose the narrowest private transport

### Tailscale Serve — preferred

Use when the host is already online in a tailnet and the intended reader can access that tailnet. Prefer direct file/directory Serve when the current client/platform supports it and it preserves the accepted resource boundary; otherwise proxy a task-owned loopback service. Never use Funnel for this outcome.

Preserve unrelated Serve/Services state. Before mutation, capture only the applicable pre-state needed to prove exact rollback; when named Services are present/in scope, include their configuration because Serve status surfaces are not equivalent. Add only one non-conflicting endpoint/path and determine its exact scoped removal before mutation. Do not reset all Serve state to clean up one share.

Tailnet membership is the access boundary unless current tailnet policy proves something narrower; Serve does not add a second application login.

### Tailcat — fallback

Read [Tailcat fallback](references/tailcat.md). Use only when Tailscale Serve is unavailable/unsuitable, the reader can run a compatible Tailcat client, and the user accepts Tailcat's bearer-capability, relay-metadata, CLI-receiver, and upstream-stability limits. Tailcat forwards a port rather than serving files, so expose only a task-owned loopback service/port.

If Tailcat must be installed or changed, use `irinse`; that mutation needs its own authority. Never silently substitute a public tunnel.

## Prove the boundary

Before reporting success, prove the claims that matter:

- the exact requested resource is reachable through the returned target;
- content outside the accepted boundary is not reachable;
- the route is private and no unintended listener/public transport was enabled; and
- pre-existing transport configuration remains unchanged except for the task-owned route.

If the receiver is available, verify retrieval. Otherwise return `RECEIVER_ACTION_REQUIRED`, not `AVAILABLE`.

## Revoke cleanly

On failure or expiry, revoke remote access first, then stop/delete only task-owned local listeners, staging, and ephemeral secret material. Verify unrelated transport state matches the captured pre-state. If cleanup is incomplete, report the exact residual route/process/secret and recovery action; never claim cleanup succeeded.

Return exactly one result:

- `AVAILABLE` — the intended reader retrieved the requested resource through the private route;
- `RECEIVER_ACTION_REQUIRED` — the private route is ready but receiver-side retrieval remains; or
- `CAPABILITY_GAP` — a named transport, reader, authority, privacy, or access-mode requirement prevents the route.

Lead with the exact access target: a direct HTTPS resource URL for Tailscale Serve, or Tailcat's receiver command plus separately secured token-delivery step. Include transport, access boundary, expiry, verification, residual limitations, and cleanup/revocation. Never place a live Tailcat token in durable records, logs, screenshots, Git, or broad chat/issue channels.
