---
name: fihan
description: Serve one explicitly invoked local file, directory, or local web resource through private Tailscale Serve or an explicitly accepted encrypted Tailcat fallback, and return the exact access target. Use only when directly invoked to make that local resource temporarily reachable through a private transport. Exclude public/anonymous tunnels, permanent hosting, production serving, and artifact creation.
disable-model-invocation: true
---

# Fihàn

Given an eligible local resource, make it temporarily reachable through the narrowest private transport available and return the exact thing the user must open or run. Do not stop at transport recommendation, readiness, or setup guidance when the resource can be served safely now.

The local resource remains authoritative.

Direct invocation authorizes:

- task-scoped staging;
- an ephemeral local listener when the selected transport needs one; and
- one narrow temporary private route using already-ready tooling.

Separate authority is required for:

- installation;
- persistent startup/configuration;
- saved credentials/keys;
- DNS publication;
- public exposure;
- broad served roots; and
- unrelated mutation.

## Resolve tooling from current official evidence

Do not hardcode an installation/setup manual or assume current CLI syntax, but retain the smallest entry surfaces needed to avoid rediscovering each selected transport from zero.

Authoritative entry points:

- Tailscale Serve: https://tailscale.com/docs/features/tailscale-serve
- Tailcat upstream: https://github.com/tailscale/tailcat

If Tailscale is already installed, `tailscale serve --help` confirms the installed interface and `tailscale serve status` is the representative read-only pre-state check. Resolve the exact route/target syntax from installed help and current Serve documentation before mutation.

If Tailcat is already installed, prefer its embedded upstream documentation via `tailcat --readme` (and `tailcat --help` when needed) before consulting a newer upstream revision. Tailcat explicitly makes no CLI/API/wire-format stability promise, so do not freeze its sender/receiver syntax here.

- If the transport tool is already installed, identify the installed version/build/provenance and use its own help/embedded documentation plus official documentation appropriate to that version. Where the official site is not versioned, reconcile current official docs with the installed CLI rather than assuming newer flags/features exist.
- If the tool is absent and setup is authorized, use the latest official installation/setup documentation and current stable release. For an upstream with no stable releases, use its latest official upstream documentation/source and treat the interface as unstable.
- Use `irinse` when installation, upgrade, authentication, or readiness itself requires material work. Fihàn still owns the serving outcome after the tool is ready.

## Bound the resource

Pin:

- exact file, directory, or already-running local web resource;
- required companion assets;
- intended reader/access mode; and
- expiry condition.

Reject:

- repository/home/credential directories;
- traversal targets;
- unresolved symlinks; or
- boundaries containing unrelated secrets.

When companions are required, expose only a reviewed allowlist; stage them narrowly when the chosen transport cannot preserve that boundary directly.

## Serve it

### Tailscale Serve — preferred

Use when Tailscale is already usable on the host and the intended reader can access its tailnet. Follow the installed-version/current official Serve documentation to choose the smallest supported target form.

Serve a file/directory directly when supported by that installed client/platform and the accepted boundary. For an existing local web resource, or when direct file serving is unavailable, expose only the required task-owned loopback service. Never use Funnel for this outcome.

Preserve unrelated Serve/Services state. Capture only enough applicable pre-state to prove scoped rollback, add one non-conflicting route/endpoint, and determine its exact scoped removal before mutation. Tailnet policy remains the access-control boundary unless current policy proves something narrower.

Do not finish until the exact HTTPS URL for the requested resource is known and verified. Return that URL, not merely the Serve mount root, status output, or setup instructions.

### Tailcat — fallback

Read [Tailcat fallback](references/tailcat.md). Use only when Tailscale Serve is unavailable/unsuitable, the reader can run a compatible Tailcat client, and the user accepts Tailcat's bearer-capability, relay-metadata, CLI-receiver, and upstream-stability limits.

Tailcat transports TCP rather than serving files, so when the supplied resource is not already a suitable local web service, start the narrow task-owned loopback service needed to expose it and forward only that port. Resolve sender/receiver syntax from the installed Tailcat documentation or latest official upstream evidence as described above.

The access target for Tailcat is the complete receiver invocation that retrieves/opens the requested resource, together with a separately secured connection token where the current CLI requires one. Do not return only a token, sender command, port number, or setup steps.

If Tailcat must be installed or changed, use `irinse`; never silently substitute a public tunnel.

## Prove the access target

Before reporting success, prove:

- the exact requested resource is reachable through the returned URL or receiver invocation;
- content outside the accepted boundary is not reachable;
- no public or unintended listener/route was enabled; and
- pre-existing transport configuration remains unchanged except for the task-owned route.

Receiver-side execution by the human is not required to call the route ready when it cannot be performed from the current environment. Fihàn succeeds when the serving route itself is live, containment is proved, and the exact usable access target has been produced. State any remaining reader prerequisite explicitly.

## Revoke cleanly

On failure or expiry:

1. Revoke remote access first.
2. Stop/delete only task-owned local listeners, staging, and ephemeral secret material.
3. Verify unrelated transport state matches the captured pre-state.

If cleanup is incomplete, report the exact residual route/process/secret and recovery action; never claim cleanup succeeded.

## Return

Return one:

- `AVAILABLE` — the private serving route is live, bounded, verified, and the exact access target is returned; or
- `CAPABILITY_GAP` — a named transport, reader, authority, privacy, or access-mode requirement prevents serving the resource.

Lead with the exact access target:

- **Tailscale Serve:** direct HTTPS URL for the supplied resource.
- **Tailcat:** complete receiver invocation plus the separately secured token-delivery requirement.

Then include:

- transport;
- access boundary;
- reader prerequisite if any;
- expiry;
- verification;
- limitations; and
- cleanup/revocation.

Never place a live Tailcat token in durable records, logs, screenshots, Git, or broad chat/issue channels.
