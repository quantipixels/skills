# Host instructions

Use when the shipped agent instruction block must be inspected, installed, updated, or removed at user or repository scope.

## Resolve the host and scope

Use the host and scope the user already selected. Current supported instruction surfaces are:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) | `<repo>/AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` | `<repo>/CLAUDE.md` |

When the installed host's current precedence or file locations differ, resolve them from the installed host/help or current official documentation rather than guessing. Do not change trust, permissions, or unrelated host settings as part of instruction setup.

Inspect the selected instruction file and any higher-precedence override/nested instruction surfaces that would shadow it. Report a shadowed target rather than silently editing a file the host will not load.

The canonical shipped block lives at [instructions](../assets/instructions.md). Use the whole block unless the user explicitly asks for a subset.

## Apply safely

An explicit request to install, update, or remove the instruction block authorizes that bounded change at the selected scope. Ask only when existing/customized content creates a material choice the user has not already resolved.

Before changing an existing instruction file, save a byte-for-byte backup in the host's own configuration/data area:

- Codex user scope → `$CODEX_HOME/backups/skill-setup/`;
- Codex repository scope → `<repo>/.codex/backups/skill-setup/`;
- Claude Code user scope → `~/.claude/backups/skill-setup/`;
- Claude Code repository scope → `<repo>/.claude/backups/skill-setup/`.

Use a unique backup name and never overwrite an earlier backup. Dry-run/inspection creates no files.

Manage the shipped content inside one block delimited by `<!-- managed-skills:start -->` and `<!-- managed-skills:end -->`. Preserve all surrounding instructions. If equivalent guidance already exists outside the block, do not duplicate it; keep the existing wording unless the user asked to consolidate or replace it.

For install/update, refresh the target immediately before writing, apply only the intended managed block, and preserve unrelated content byte-for-byte where practical. If the file changed after inspection in a way that affects the proposed edit, reconcile the change before writing.

For removal, remove only the managed block. Preserve surrounding content and later user edits. If removal leaves a file that this skill created and the file is otherwise empty, deleting that empty file is part of the requested removal.

## Verify

Read the resulting file back and confirm the intended block is present or absent exactly once, surrounding instructions are preserved, and the selected host/scope points at that file. A new host session may be required to load changed instructions.

Return the host, scope, changed file, backup path when applicable, installed/removed block state, verification, and any shadowing or unsupported-host limitation.
