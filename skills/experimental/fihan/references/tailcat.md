# Tailcat fallback

Load only when Tailscale Serve is unavailable/unsuitable and the intended reader can run Tailcat.

## Evidence boundary

Current pinned evidence: [`tailscale/tailcat` `88929418b1a3f3c74904a3136d6a9e87b1b5b9bb`](https://github.com/tailscale/tailcat/commit/88929418b1a3f3c74904a3136d6a9e87b1b5b9bb), verified 2026-08-29. Upstream has no releases or stability promise for CLI/API/wire format/relay availability. Refresh official README/source/current `--help` before use when the current behavior matters.

Tailcat provides a userspace WireGuard tunnel without a Tailscale account/control plane/system routes. Its default public DERP relays are best-effort/rate-limited. Payload remains end-to-end encrypted, but relay operators can observe connection metadata; do not claim stronger metadata/logging/retention privacy than current upstream evidence proves.

Use `irinse` if Tailcat installation/upgrade is required. Prefer an exact reviewed revision over an unpinned install for this Experimental path.

## Temporary sender contract

Tailcat forwards TCP; it does not serve files/directories. Fihan therefore exposes only the exact task-owned loopback port needed by the requested resource.

For an ordinary temporary share, force a fresh server key with `--key=new`. A saved server key—especially the magic `default` key—makes the token reusable across later runs and therefore changes the authority boundary. Do not create/publish saved server keys or DNS tokens for ordinary Fihan use.

Never expose `all`, `exit-node`, or `no-auth-ssh` for this outcome. The returned connection token is a bearer capability unless server-side client allowlisting is actually in use; keep it out of Git, durable records, logs, screenshots, and broad channels.

## Receiver contract

The supported browser-independent retrieval path is Tailcat's CLI receiver over the exposed port, commonly through:

```shell
tailcat socks <token> curl --fail --show-error http://server.tailcat:<port>/<path>
```

Tailcat tokens are case-sensitive and are not normal browser hostnames; browsers lowercase hostnames. If the reader requires an ordinary browser URL, Tailcat does not satisfy the request.

### Client identity nuance

At the pinned revision, ordinary direct client modes use the saved `client-default` identity when present, but `clientSOCKSMode` constructs fresh client keys (`key.NewNode`) for its fixed server and per-token clients. Therefore the SOCKS receiver above cannot connect to a server restricted with `--allow=<client-node-key>` at this revision, despite the README's broader statement that client modes use `client-default`.

If named/identity-bound reader authorization is required, use only a refreshed compatible client path that demonstrably presents the allowlisted key; otherwise return `CAPABILITY_GAP`. Do not silently drop `--allow` or invent an unproved bridge.

## Revocation

Revoke the capability by stopping the Tailcat sender before deleting temporary token/staging material, then verify the token no longer reaches the resource. Remove any persistent key only when its creation was separately authorized; ordinary Fihan runs should not create one. DERP cache files are not server private keys and are not ordinary cleanup targets.
