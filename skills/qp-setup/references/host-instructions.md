# Host instructions

Use when host instruction files need inspection, audit, installation, consolidation, update, or removal at user or repository scope.

Host instructions are for durable user/project policy that materially changes normal model/host behavior. Do not use them to advertise installed skills, duplicate skill descriptions, or restate capabilities the current model/harness already performs reliably.

## Resolve host, scope, and authority

Use the host and scope already selected. Current common instruction surfaces are:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) | `<repo>/AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` | `<repo>/CLAUDE.md` |

Resolve current precedence/file locations from the installed host/help or official documentation when they differ. Inspect higher-precedence override/nested surfaces that would shadow the selected target.

A request to configure a repository does **not** imply permission to inspect the user's global instruction file. When a global audit could materially help, ask once for permission to read it. If declined, leave it untouched and continue with the authorized scope.

If the user explicitly requested a global instruction audit, that request already authorizes inspection; mutation still requires the normal final confirmation.

## Audit before proposing text

Read the selected instruction surface and classify relevant guidance as:

- useful durable policy to preserve;
- model/host-native behavior that no longer earns always-loaded context;
- duplicated skill/router advertising;
- stale or conflicting guidance;
- project-specific policy at the wrong scope; or
- a real missing preference that would materially change behavior.

No new instruction is a valid result. There is **no canonical package global instruction block** to install by default.

When agent-experience setup requested this audit, evaluate only instruction changes that materially improve that setup or the user's durable cross-project policy. Do not turn the audit into a general rewrite of unrelated personal instructions.

## Propose proportionally

If the current file is already adequate, say so and make no change.

When a change is useful, show the smallest semantic diff and why it earns global/repository context. Existing user wording wins when it expresses the same policy adequately.

If the user accepts package-managed policy text, place only that accepted text inside one block:

```text
<!-- qp-policy:start -->
...
<!-- qp-policy:end -->
```

Preserve all surrounding instructions. Do not adopt unrelated user text into the managed block merely because it overlaps.

Older `<!-- managed-skills:start -->` / `<!-- managed-skills:end -->` content is a deprecated package-managed surface. Audit it rather than silently carrying it forward. Offer removal or migration only when the resulting policy still earns a place, and obtain confirmation before changing it.

## Apply safely

Before changing an existing instruction file, save a byte-for-byte backup in the host's own configuration/data area:

- Codex user → `$CODEX_HOME/backups/skill-setup/`;
- Codex repository → `<repo>/.codex/backups/skill-setup/`;
- Claude Code user → `~/.claude/backups/skill-setup/`;
- Claude Code repository → `<repo>/.claude/backups/skill-setup/`.

Use a unique backup name and never overwrite an earlier backup. Dry-run/inspection creates no files.

Refresh the target immediately before writing. If it changed after preview in a way that affects the proposal, reconcile and show the revised material diff before applying it.

For removal, remove only package-managed blocks the evidence shows the package owns. Preserve surrounding content and later user edits. If removal leaves a file that setup created and the file is otherwise empty, deleting that empty file is part of the accepted removal.

## Verify

Read the resulting file back and confirm the intended managed policy is present/absent exactly once, unrelated instructions are preserved, applicable precedence points at the expected file, and no deprecated managed block remains unless deliberately retained.

Return the host, scope, audit result, changed file when any, backup path, verification, and any shadowing/unsupported-host limitation.
