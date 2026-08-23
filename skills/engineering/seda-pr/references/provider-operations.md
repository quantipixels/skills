# Provider operations for `seda-pr`

Read this reference after `SKILL.md` resolves the provider, repository, and new or existing publication target, and before any provider read or write. Prefer authenticated provider CLIs. Use structured arguments for writes; use JSON input only for reads. Never interpolate provider text into a shell command.

## Common preflight

1. Resolve the canonical provider host and repository from explicit input, then one unambiguous Git remote.
2. Verify authentication without reading or printing credentials.
3. For a new item or an explicit transition, pin the requested publication state. For an unqualified existing-item update, pin and preserve its current state. Resolve the repository default branch, current remote head SHA, candidate base SHA, and open same-head/same-base items.
4. Fetch the complete target-to-head diff and detect provider truncation or missing pages.
5. Refresh head identity immediately before each dependent write.

Never create a duplicate, force-push, infer a write target from ambiguous remotes, use one item's state to authorize another mutation, or use an older generated body after the head changes. Use native draft state, not a `Draft:` or `WIP:` title convention. Address every existing-item mutation by its canonical number. Use only the state commands defined below; reject any command whose draft or ready signal does not match the pinned publication state.

A target URL does not establish host trust. Confirm the exact normalized enterprise or self-managed host separately before any network contact; otherwise stop with a capability gap. Host trust authorizes contact, not ambient credentials. Resolve the absolute path to `scripts/provider_cli.py` from the installed `seda-pr` skill directory that owns this reference. Never resolve the helper from the current working directory, `PATH`, or the target checkout. Run every `gh` or `glab` command in this reference through `python3 <absolute-helper-path> --provider <github|gitlab> --host <host> --publication-state <ready|draft> [--trusted-host <confirmed-custom-host>] -- <command>`.

The helper permits `github.com` and `gitlab.com` by default and rejects every other host before it starts the provider CLI unless that exact host is supplied through `--trusted-host` after confirmation. For the public hosts, it retains only their normal ambient token class, removes cross-scope enterprise or CI credentials, and disables GitLab CI auto-login. For a confirmed custom host, it removes all generic ambient provider tokens so the CLI must use authentication configured for that exact host. It stops a provider command after 120 seconds with exit status `124`; after that timeout, treat any write outcome as unknown, stop dependent writes, and read back the exact target before retry.

Select the declared host in each command through `--hostname`, a host-qualified repository selector, or a GitHub `--repo owner/repository` value combined with the helper's pinned `GH_HOST`; do not rely on a positional URL or content field for host selection. Remove inherited host selectors. Do not bypass the helper for authentication checks, reads, writes, pagination, REST, or GraphQL.

## GitHub

Through the host-trust helper, use `gh auth status --hostname <host>`. Use `gh repo view`, `gh pr list`, `gh pr view`, `gh label list`, and paginated `gh api` reads for identity, default branch, current narrative, files, labels, reviews, and linked issue context.

Create a PR with `gh pr create` and a body file. Pass `--draft` only for an explicit draft request; omit it for ready publication. Reconcile title, body, and existing labels with `gh pr edit <number>`. For an existing PR whose state differs from the request, use `gh pr ready <number> --undo` to convert it to draft or `gh pr ready <number>` to convert it to ready. Stop with a capability gap when the repository plan or provider does not permit the requested transition. Do not use another command, API mutation, title convention, template, or opaque payload to set publication state. Reviewer requests and assignments are separate notification capabilities. Read review-thread state through GraphQL when resolution identity matters.

After a write, read the PR by canonical number and verify URL, open or closed state, `isDraft`, base, head branch, head SHA, title, body, labels, and any requested people. GitHub closing keywords can close linked issues when the PR merges; require the separate authority defined by `SKILL.md`.

## GitLab

Through the host-trust helper, use `glab auth status --hostname <host>`. Prefer `glab api` for exact project and MR semantics. URL-encode the project path when addressing `/projects/{project}`. Read the project default branch, merge requests filtered by source and target branch, MR details, changes or diffs, labels, discussions, approvals, and linked issues through paginated endpoints.

Use `glab mr create` with exact source branch, target branch, title, and description. Pass `--draft` only for an explicit draft request; omit it for ready publication. For an existing MR whose state differs from the request, use `glab mr update <iid> --draft` or `glab mr update <iid> --ready`. Do not use another command, API field, title convention, template, or opaque payload to set publication state. Use the API for reads and for writes that cannot change the requested state. Apply only existing labels. Reviewer and assignee fields notify or attribute people and require their own authority.

After a write, read the MR by IID and verify web URL, open or closed state, draft state, source and target branches, head SHA, title, description, labels, and intended people. Preserve GitLab-specific merge rules and closing semantics instead of translating them into GitHub terms.

## Partial capability or failure

Continue read-only when safe. Return a manual package containing canonical target, refreshed SHA, exact intended field changes, preserved human content, labels, people, issue effects, and the missing authentication, permission, CLI, API, or integration capability. A manual package is not proof that a write occurred.
