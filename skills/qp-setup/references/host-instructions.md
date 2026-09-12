# Host instructions

Use when host instruction files need inspection, audit, installation, consolidation, update, or removal at user or repository scope.

Host policy is durable user/project steering that materially changes normal model/host behavior. Keep it small and editable. Do not use it to advertise installed skills, duplicate skill descriptions, or restate mechanics the current model/harness already performs reliably.

## Resolve host, scope, and authority

Use the host and scope already selected. Current common instruction surfaces are:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) | `<repo>/AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` | `<repo>/CLAUDE.md` |

Resolve current precedence/file locations and available model/reasoning controls from the installed host/help or current official documentation when they differ. Inspect higher-precedence override/nested surfaces that would shadow the selected target.

A request to configure a repository does **not** imply permission to inspect the user's global instruction file. When a global audit could materially help, ask once for permission to read it. If declined, leave it untouched and continue with the authorized scope. Explicitly requesting a global instruction audit already authorizes inspection; mutation still requires the normal final confirmation.

## Audit before proposing text

Classify relevant existing guidance as:

- useful durable policy to preserve;
- model/host-native behavior that no longer earns always-loaded context;
- duplicated skill/router advertising;
- stale or conflicting guidance;
- project-specific policy at the wrong scope; or
- a real missing preference that would materially change behavior.

No change is a valid result. Existing user wording wins when it expresses the same policy adequately.

## Recommended policy

This policy is a starting point the user can edit directly as models, costs, and preferences change. Keep the behavioral contract stable; resolve concrete model names and supported reasoning levels from the active host.

For a current Codex host exposing the GPT-6/GPT-5.6 family, start from:

```text
Use `pepeye` when delegation, parallel work, context isolation, independent judgment, or coordination of several results would materially improve the outcome. Keep small, sequential work local.

Use `alarina` when the right skill or route is genuinely unclear. Use `ro-wo` before accepting or rejecting a consequential premise.

For delegated work:
- Do not fork conversation context. Start workers fresh. When prior context matters, provide a concise handoff containing only the relevant outcome, constraints/decisions, decisive evidence with locators, exact candidate identity, unresolved questions, and requested result.
- Give each worker a bounded outcome, appropriate authority, required evidence, and a clear completion condition. The primary agent owns integration and final judgment.
- Funnel information by cost: use cheaper capability for high-volume reading, search, extraction, logs, and source collation; stronger capability for synthesis and execution; reserve the highest capability for planning, independent review, and consequential judgment. Preserve locators so decisive evidence can be reopened rather than trusted through compression alone.
- Prefer `gpt-5.6-luna` at low/medium effort for bulk reading, collection, exploration, and routine research. Use `gpt-5.6-terra` at medium for normal research synthesis and writing; deterministic prose may drop to Luna. Use `gpt-5.6-sol` at medium for coding, diagnosis, technical synthesis, architecture development, and difficult research synthesis; raise effort when complexity or risk warrants it. Use `gpt-6-astra` at medium for material planning and ordinary consequential review/judgment; use high for plan premortems and difficult/high-risk review, and xhigh only for exceptional unresolved judgment.
- Do not spend Sol/Astra context discovering which evidence matters when Luna/Terra can collate it first. A consequential reviewer/judge independently checks the decisive candidate and evidence, not every cheap collection step.
- Generation gets sufficient capability; consequential verification gets equal or greater judgment capability. Route material plans, candidates, or decisions through Astra review when their acceptance materially affects the outcome, not after every delegated action.
- Avoid duplicate work except deliberate independent review or competing hypotheses. Never run concurrent writers against the same mutable workspace.
- Surface material findings, blockers, failures, and completed results; do not repeat unchanged status.
- Escalate model, reasoning effort, evidence depth, or approach when the current worker is underpowered. Do not repeat the same failed configuration by default.
```

For another host, preserve the policy and map the model preferences to that host's **currently available** cost/capability tiers. Do not invent a cross-provider model equivalence. If the host cannot express a requested per-worker model/reasoning preference dynamically, report that limitation; use ordinary tool configuration only when the user wants a hard runtime setting.

## Propose proportionally

Show the smallest semantic diff and why it earns global/repository context. Do not replace unrelated personal policy while adding these preferences.

If the user accepts package-managed policy text, place only that accepted text inside one block:

```text
<!-- qp-policy:start -->
...
<!-- qp-policy:end -->
```

The block is user-editable. Treat later user changes as authoritative preferences, not drift to overwrite. Older `<!-- managed-skills:start -->` / `<!-- managed-skills:end -->` content is a deprecated package-managed surface; audit it and migrate/remove it only when the replacement still earns a place.

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

Read the resulting file back and confirm the intended policy is present/absent exactly once, user edits and unrelated instructions are preserved, applicable precedence points at the expected file, and no deprecated managed block remains unless deliberately retained.

Return the host, scope, audit result, changed file when any, backup path, verification, resolved model/reasoning preferences when material, and any shadowing/runtime limitation.
