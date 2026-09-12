# Host instructions

Use for an explicitly requested instruction-file change.

## Resolve the target

- Reuse the selected host and scope. Verify current locations and precedence from installed host/help or official documentation when needed.
- Common instruction targets are Codex `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) and repository `AGENTS.md`; Claude Code `~/.claude/CLAUDE.md` and repository `CLAUDE.md`.
- Repository setup does not authorize reading or changing global instruction files. Continue within scope; ask for broader access only when it affects the requested result.

## Optional user instructions

- Shared instructions are not an installation prerequisite. Point users to the [README's optional user instructions](https://github.com/quantipixels/skills#optional-user-instructions) for manual copy-and-edit.
- When asked to apply them, offer relevant README lines individually, “All,” or “None”; allow custom wording. Include premise checking with `ro-wo` and the writing, diagnosis, or review choices when useful. Show the destination and exact proposed text. Reuse choices already made.
- Use `oro-fun-sigidi` for requested custom instruction text. Preserve the user's wording where it already works; do not turn simple setup into a policy audit unless requested.
- Add only accepted text. Do not generate managed blocks or duplicate the skill catalogue.
- Existing `qp-policy` or deprecated `managed-skills` blocks are user-editable content. Consolidate or remove them only within the requested migration; preserve unrelated instructions and later user edits.

## Apply and verify

- Follow the entrypoint's authority rules. Preview the exact change, reuse existing approval, refresh before writing, and reconcile material changes since preview.
- Back up existing instruction files under the host's configuration/data area. Use unique byte-for-byte backups. Inspection creates no files.
- Preserve unrelated content. Delete a user-owned file only when its removal is explicitly requested.
- Read back the result and check intended text and applicable precedence.
- Repair verification failures within accepted scope. Finish with the changed target, result, backup/recovery path, and material limitations.
