# Provider operations for `seda-pr`

Use only after `SKILL.md` resolves the provider, normalized host, repository, and publication target. Prefer an already-connected provider API/connector that can preserve the complete contract below; otherwise use the authenticated provider CLI as an operational fallback.

## Provider contract

- Bind every read/write to the exact confirmed host and repository; an enterprise/self-managed host requires separate trust confirmation before first contact.
- Verify authentication without exposing credentials and prevent ambient repository/host selectors or cross-host/CI credentials from redirecting the operation.
- Resolve default branch, current remote head, candidate base, complete target-to-head diff, and open same-head/same-base items; pagination/truncation is an evidence gap, not negative evidence.
- Pin requested publication state; preserve an existing item's state unless transition authority is explicit.
- Refresh canonical item/head immediately before every write, use structured arguments/payloads, and never interpolate provider text into shell commands.
- Read every write back by canonical item identity before dependent mutation. Custom-host trust proves routing/credential isolation, not server-version/tier/policy/API capability.

Never create a duplicate, force-push, infer a write target from ambiguous remotes, reuse a body generated for an older head, or use one item's state to authorize another mutation. Use provider-native draft state; closing keywords require the separate issue-effect authority from `SKILL.md`.

## CLI entry anchors

When CLI is the available transport, resolve exact current syntax from installed help/current provider documentation instead of maintaining a command catalogue here.

- **GitHub:** `gh auth status --hostname <host>` is the authentication entry check. Bind `gh pr`/`gh api` operations explicitly to the confirmed host/repository; use native PR create/edit/ready semantics, paginated structured reads, and body files for multiline text.
- **GitLab:** `glab auth status --hostname <host>` is the authentication entry check. Bind `glab mr`/`glab api` to the confirmed host/project, disable/clear ambient CI or generic credentials that could redirect access, use the canonical full project identity where the CLI requires it, and preserve GitLab-native draft/merge semantics.

After creation/update, verify canonical URL, open/closed and draft state, base/target, head/source and current SHA, title/body/description, labels, and every explicitly authorized people/effect field.

## Unknown or partial writes

After timeout or ambiguous response, treat the write as unknown, stop dependent writes, and read the exact target before retrying. Retry only with absence proof or verified idempotency; a manual package is not proof that a write occurred.
