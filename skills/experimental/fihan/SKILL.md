---
name: fihan
description: Temporarily expose one explicit local file or directory through an existing tailnet-only route or an explicitly accepted encrypted Tailcat bearer-token route. Prefer an already-ready Tailscale Serve path; when Tailscale is unavailable, use Tailcat only after confirming the receiver can use Tailcat and accepting its capability-token and stability limits. Use only when explicitly invoked or after explicit experimental acceptance. Exclude public or anonymous tunnels, permanent hosting, production serving, and artifact creation.
disable-model-invocation: true
---

# Fihan

Make one bounded local resource reachable through a tailnet-only or explicitly accepted encrypted bearer-token route, then leave an exact cleanup path. The local source remains authoritative. The workflow does not intentionally create a durable hosted copy or transfer publication or hosting ownership, but relay operators can observe connection metadata and current logging or retention must be confirmed before use.

## 1. Pin the access boundary

Record the exact file or directory, required companion assets, intended reader, viewing method, duration, host availability, and authority for downloads, tool setup, background processes, network listeners, Tailscale configuration, and cleanup.

Before starting any listener or background process, state its executable/tool identity, local and network scope, expected lifetime, state effects, and exact rollback. Obtain approval unless the user already authorized that exact temporary process and scope. A request to view or share a file does not authorize a global installation, persistent startup item, public route, or unrelated configuration change.

Reject a broad repository, home directory, credential directory, unresolved symlink, traversal path, or target that contains unrelated or secret material. When linked assets are necessary, build a permission-restricted temporary staging directory containing only the reviewed allowlist. Do not widen the served root merely to make links resolve.

Use an existing project server only when it exposes no broader content than the accepted boundary. Otherwise start a standard local HTTP server against the staging directory, bind it to `127.0.0.1`, choose one unused port, retain its process identity, and verify the target locally before adding a remote transport.

## 2. Choose the private transport

Check readiness rather than command presence alone.

### Already-ready Tailscale

Use Tailscale Serve when the host is online in a tailnet and the intended reader can join that tailnet. Inspect the existing Serve configuration before any change and preserve unrelated routes. Capture both human-readable and JSON Serve status. When named Services are supported or present, also capture the complete `get-config --all` state in a permission-restricted temporary file. Treat legacy handlers and named Services as separate configuration surfaces; status alone is not complete preservation evidence.

Proxy only the loopback port under a distinct path. This works across Tailscale's macOS variants without depending on direct file-serving support. Never use Funnel for this outcome. Do not claim owner-only access unless the current tailnet policy proves it; Serve adds no second application login.

Before starting a background route, state its device-level persistence and exact path-specific cleanup, then obtain approval. Record every flag used to add the path and confirm the current CLI's path-specific `off` form with those same flags before mutation. If a complete applicable pre-state cannot be captured, the mount path conflicts, or exact cleanup is uncertain, stop with `CAPABILITY_GAP`.

Verify the returned tailnet URL, a requested file, and one unrelated path that must fail. Re-read every applicable status/configuration surface and compare it with the pre-state; only the authorized path may differ.

Retain the exact verified URL that resolves to the requested resource. Do not substitute the Serve mount root, a staging-directory root, or an intermediate landing page unless that URL is itself the requested resource.

### Tailscale unavailable or unsuitable

Read [Tailcat fallback](references/tailcat.md). Tailcat is eligible only when the reader can run a compatible Tailcat client and accepts that the result is a CLI retrieval path rather than an ordinary browser URL.

If Tailcat is missing, use `irinse` for exact tool readiness or installation. Installation, downloads, global state, persistent keys, and credential or client-key creation require their own approval. Do not silently replace Tailcat with a public tunnel.

Return `CAPABILITY_GAP` when the reader requires a browser-only URL, cannot run Tailcat, or rejects its token, relay-metadata, or stability boundary.

## 3. Start the narrow route

Keep the local HTTP server loopback-only for both transports. Expose only its exact port.

For Tailscale, mount a unique Serve path and preserve every existing handler. For Tailcat, use a fresh ephemeral key for the run. At the pinned Tailcat candidate, the supported `socks` receiver path does not present a stable client key, so ordinary retrieval uses the connection token as the sole access capability. Require explicit acceptance of that boundary. If identity-bound client authorization is required, stop unless current upstream evidence supplies a verified compatible receiver path.

Treat the connection token as a password: keep it out of Git, durable records, command histories where avoidable, logs, screenshots, and broad chat or issue channels.

Do not add persistent startup configuration unless the user separately authorizes persistence. Do not publish DNS records, create saved Tailcat keys, or reuse a previous token for an ordinary temporary share.

## 4. Prove access and containment

Before returning `AVAILABLE`, verify all applicable claims:

- the exact local target and required assets load from the loopback server;
- the selected transport process or Serve handler is active;
- the requested remote path returns the expected content identity;
- the exact access URL or receiver command addresses the requested resource rather than only its containing route;
- an unrelated path outside the allowlist is unavailable;
- no public transport or unintended listener was enabled;
- existing Tailscale handlers remain intact; and
- the receiver successfully retrieves the target, when the receiver is present.

When the host-side route is ready but receiver verification is pending, return `RECEIVER_ACTION_REQUIRED`, not `AVAILABLE`.

## 5. Fail closed

If setup, approval, transport launch, containment proof, receiver verification, or handoff fails after local state was created, unwind the task-owned changes in reverse order before returning a non-ready result:

1. Remove only the added remote handler or stop the Tailcat process.
2. Stop the task-owned loopback server.
3. Delete the task-owned token file and temporary staging directory.
4. Re-read the applicable Tailscale configuration surfaces and verify the pre-existing state remains intact.

If rollback is incomplete, return `CAPABILITY_GAP` with the exact live residual state and immediate recovery action. Do not hide the residual listener, route, token, or file and do not claim cleanup succeeded.

## 6. Handoff and cleanup

Return exactly one result:

- `AVAILABLE` — the intended reader retrieved the target through the private route;
- `RECEIVER_ACTION_REQUIRED` — the bounded route is ready and the reader must complete the supplied Tailcat or tailnet step; or
- `CAPABILITY_GAP` — a named tool, receiver, authority, privacy, or browser-access requirement prevents the secure route.

Include target identity, transport, access boundary, reader requirement, URL or receiver command, host/process state, verification, expiry condition, limitations, and exact cleanup actions. Never include a live Tailcat token in a durable record.

Lead the handoff with the exact access target. For Tailscale Serve, return a clickable HTTPS URL that opens the requested resource directly. For Tailcat, return the exact receiver command and the separately secured token-delivery step because Tailcat cannot provide a browser link. Do not return `AVAILABLE` without the access target the reader must open or run.

When access is no longer needed, remove only the added handler, stop the transport and loopback processes, delete the temporary staging directory and token file, and verify unrelated services remain healthy. Do not reset all Tailscale Serve state when a path-specific removal is available.
