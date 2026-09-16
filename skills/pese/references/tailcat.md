# Tailcat fallback

Use only when Tailscale Serve is unsuitable and the intended reader can run Tailcat. Resolve the installed interface from embedded help and current official upstream documentation; Tailcat promises no stable CLI, API, wire format or public relay. Use `irinse` for authorized installation/upgrade and verify package identity.

Tailcat supplies an end-to-end encrypted userspace WireGuard tunnel, not the normal Tailscale control plane or a file server. Public relays are best-effort and can observe connection metadata. Forward only the task-owned loopback port. Use a fresh ephemeral server identity; never add saved server keys, stable DNS tokens, all-port forwarding, exit-node behavior or auth-free SSH for an ordinary share.

Treat the connection token as a bearer secret unless the exact current server/client path proves identity-bound authorization. When identity binding matters, verify that the receiver presents the allowlisted key; otherwise return `CAPABILITY_GAP` rather than removing the restriction.

Return the complete receiver invocation that reaches the exact resource path/port, plus a separate secure token-delivery requirement. Tailcat normally provides no browser-ready HTTPS URL; a browser-only requirement the current interface cannot meet is a capability gap. A token, sender command or port alone is not a target.

Revoke by stopping the sender first, then delete task-owned token/staging material and verify the target fails. Remove persistent keys only when their creation was separately authorized.
