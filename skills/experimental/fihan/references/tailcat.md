# Tailcat fallback

Load this reference only when an already-ready Tailscale Serve route is unavailable or unsuitable and the reader can use Tailcat.

## Evidence and stability boundary

The current evidence boundary is [`tailscale/tailcat` commit `88929418b1a3f3c74904a3136d6a9e87b1b5b9bb`](https://github.com/tailscale/tailcat/commit/88929418b1a3f3c74904a3136d6a9e87b1b5b9bb), verified 2026-08-29. Upstream has no releases and promises no CLI, API, wire-format, relay uptime, or throughput stability. Re-read the official [README](https://github.com/tailscale/tailcat/blob/main/README.md), current commit, and local `--help` before use.

Tailcat uses Tailscale's userspace WireGuard, NAT traversal, and DERP components without a Tailscale account, control plane, system routes, DNS changes, or root access. It does not install or operate the Tailscale client.

The public Tailcat DERP service is free, rate-limited, and best-effort. Payload traffic remains end-to-end WireGuard encrypted, but relay operators can observe connection metadata; confirm current logging and retention before use. Fihan does not provision or validate a self-operated DERP relay. Treat one as unavailable unless it is already ready, separately authorized, and independently verified.

## Readiness

Tailcat currently documents `go install` and Nix as its install paths; it publishes no prebuilt release. Use `irinse` for installation or upgrade. Prefer an exact reviewed commit over `@latest` because upstream provides no stability promise.

After setup, record binary path, Go module build provenance or Nix revision, current commit, `--help` behavior, OS, and one harmless parse/help signal. Do not treat a binary named `tailcat` as sufficient identity; an unrelated npm package uses the same name.

## Server path

Tailcat does not serve files or directories. Start and verify the loopback HTTP server first, then forward only its port:

```shell
tailcat --serve=<port> --key=new
```

Confirm the exact current flags through `tailcat --help`. Never use `--serve=all`, `--serve=exit-node`, or `--serve=no-auth-ssh` for file access.

At the pinned candidate, the `tailcat socks` receiver path creates a fresh client key and does not present a saved `client-default` key. The behavior is visible in the pinned [`clientSOCKSMode` source](https://github.com/tailscale/tailcat/blob/88929418b1a3f3c74904a3136d6a9e87b1b5b9bb/cmd/tailcat/tailcat.go). It therefore cannot connect to a server restricted with `--allow=<client-node-key>`. Do not combine the receiver command below with `--allow`.

For the current supported SOCKS retrieval path, possession of the connection token authorizes access to the exposed port. Require explicit acceptance of that bearer-capability boundary. The token is case-sensitive and derived from the server's WireGuard key. Generate a fresh ephemeral key for every ordinary share so terminating the process invalidates the token permanently.

If identity-bound client authorization is required, stop with `CAPABILITY_GAP` unless refreshed upstream evidence supplies and proves a receiver path that presents the allowlisted key. Do not invent a local bridge or silently weaken the requirement.

Do not run `tailcat genkey` for a temporary share. A saved `default` key silently changes later unflagged runs from ephemeral to persistent identity, allowing previous token recipients to reach future servers unless client keys restrict access.

## Receiver path

Tailcat does not return a browser-ready HTTPS URL. A compatible CLI receiver can retrieve one resource through the supported SOCKS command form:

```shell
tailcat socks <token> curl --fail --show-error http://server.tailcat:<port>/<path>
```

Use the receiver's current `tailcat --help` and an explicit output path when downloading a file. Tokens cannot be used directly as ordinary browser hostnames because browsers lowercase case-sensitive token text. The experimental browser demo transfers files and text but does not prove arbitrary local HTTP browsing or directory serving.

If the reader needs a normal browser link, stop with `CAPABILITY_GAP`. Another authenticated tunnel requires a separate explicit choice and authority.

## Token handling and cleanup

Treat the token as a bearer secret. If automated capture is necessary, create a permission-restricted temporary file and use `TAILCAT_ADDR_FILE` only for that controlled file. Never use its TCP target form, durable repository storage, or shared logs for an ordinary handoff. If any later step fails, stop Tailcat before deleting the token file so the capability becomes unusable first.

At completion:

1. Stop the Tailcat process and verify the token no longer connects.
2. Stop the loopback HTTP server.
3. Remove the permission-restricted token file and staging directory.
4. If a persistent key was created by separately authorized work, use the current `tailcat genkey --delete --key=<name>` behavior and verify the named key is gone.

DERP cache files contain fetched relay maps rather than server private keys. Do not delete caches merely to perform ordinary route cleanup.
