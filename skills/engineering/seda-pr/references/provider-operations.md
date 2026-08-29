# Provider operations for `seda-pr`

Read this reference after `SKILL.md` resolves the provider, normalized host, repository, and new or existing publication target, and before any provider read or write. Prefer authenticated provider CLIs. Use structured arguments for writes and body files for multiline text. Never interpolate provider text into a shell command.

## Common preflight

1. Resolve the canonical provider host and repository from explicit input, then one unambiguous Git remote.
2. Confirm an enterprise, dedicated, or self-managed host separately before any network contact. A target URL identifies a host; it does not establish trust.
3. Verify authentication without reading or printing credentials. Scope every provider command to the exact host and repository. Remove inherited repository selectors and cross-host or CI credentials that could redirect or broaden the operation.
4. For a new item or explicit transition, pin the requested publication state. For an unqualified existing-item update, pin and preserve its current state.
5. Resolve the default branch, current remote head SHA, candidate base SHA, and open same-head and same-base items. Fetch the complete target-to-head diff and detect truncation or missing pages.
6. Refresh canonical item and head identity immediately before every write.

Custom-host rules establish trust, credential isolation, and command routing. They do not prove compatibility with a target server version, tier, policy, permission set, or API surface. Verify every read and write capability required for this publication on the exact host; otherwise return a capability gap before mutation.

Never create a duplicate, force-push, infer a write target from ambiguous remotes, use one item's state to authorize another mutation, or use an older generated body after the head changes. Address every existing-item mutation by its canonical number. Use native draft state, not a `Draft:` or `WIP:` title convention.

Use only the canonical command families below. The skill constructs them directly; no custom runtime reparses commands that the skill itself controls.

## GitHub

Set `GH_HOST` to the confirmed host, remove inherited `GH_REPO`, and pass an explicit `--repo`. On `github.com`, remove enterprise-token variables. On a confirmed custom host, remove generic GitHub token variables and require `gh` authentication configured for that host. Use `gh auth status --hostname <host>` without printing tokens.

Use `gh repo view`, `gh pr list`, `gh pr view`, `gh pr checks`, `gh label list`, and paginated `gh api` reads for identity, default branch, narrative, files, labels, reviews, and linked issue context.

Create with `gh pr create --repo <repo> --base <base> --head <head> --title <title> --body-file <file>`. Pass `--draft` only for an explicit draft request. Update narrative with `gh pr edit <number> --repo <repo> --title <title> --body-file <file>`. Reconcile publication state only with `gh pr ready <number> --repo <repo>` or `gh pr ready <number> --repo <repo> --undo`.

After a write, read the PR by canonical number and verify URL, open or closed state, `isDraft`, base, head branch, head SHA, title, body, labels, and any explicitly authorized people. GitHub closing keywords can close linked issues when the PR merges; require the separate authority defined by `SKILL.md`.

## GitLab

Remove inherited `GITLAB_HOST`, then set `GITLAB_HOST` to the confirmed host inline for every high-level `glab mr` command. Set `GLAB_ENABLE_CI_AUTOLOGIN=false` and remove `CI_JOB_TOKEN`. On a confirmed custom host, remove other generic GitLab token variables and require `glab` authentication configured for that host. Use `glab auth status --hostname <host>` without printing tokens. Pass the canonical full project URL to `--repo` because `glab mr create` and `glab mr update` do not expose `--hostname`; use `glab api --hostname <host>` for structured reads, mutations not safely covered by the high-level command, and readback.

Prefer paginated `glab api` reads for exact project and MR semantics. URL-encode the project path when addressing `/projects/{project}`. Read the default branch, merge requests filtered by source and target branch, MR details, changes or diffs, labels, discussions, approvals, and linked issues.

Create with `GITLAB_HOST=<host> glab mr create --repo https://<host>/<project> --source-branch <head> --target-branch <base> --title <title> --description-file <file>`. Pass `--draft` only for an explicit draft request. Update narrative with `GITLAB_HOST=<host> glab mr update <iid> --repo https://<host>/<project> --title <title> --description-file <file>`. Reconcile publication state only with the same inline host and canonical full-URL repository plus `glab mr update <iid> --draft` or `--ready`.

After a write, read the MR by IID and verify web URL, open or closed state, draft state, source and target branches, head SHA, title, description, labels, and explicitly authorized people. Preserve GitLab-specific merge rules and closing semantics instead of translating them into GitHub terms.

## Unknown or partial writes

Apply a bounded timeout through the host when provider commands can hang. After a timeout or ambiguous response, treat the write outcome as unknown, stop dependent writes, and read back the exact target before any retry. Continue read-only when safe. A manual package is not proof that a write occurred.
