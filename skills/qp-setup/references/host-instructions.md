# Host instructions and Pepeye preferences

Use for an explicitly requested instruction-file change or Pepeye configuration setup. They are separate choices: instruction files steer behavior; Pepeye JSON selects models and reasoning.

## Resolve the target

- Reuse the selected host and scope. Verify current locations and precedence from installed host/help or official documentation when needed.
- Common instruction targets are Codex `$CODEX_HOME/AGENTS.md` (default `~/.codex/AGENTS.md`) and repository `AGENTS.md`; Claude Code `~/.claude/CLAUDE.md` and repository `CLAUDE.md`.
- Repository setup does not authorize reading or changing global instruction files or `~/.qp/settings.json`. Continue within scope; ask for broader access only when it affects the requested result.

## Optional user instructions

- Shared instructions are not an installation prerequisite. Point users to the [README's optional user instructions](https://github.com/quantipixels/skills#optional-user-instructions) for manual copy-and-edit.
- When asked to apply them, offer relevant README lines individually, “All,” or “None”; allow custom wording. Include premise checking with `ro-wo` and the writing, diagnosis, or review choices when useful. Show the destination and exact proposed text. Reuse choices already made.
- Use `oro-fun-sigidi` for requested custom instruction text. Preserve the user's wording where it already works; do not turn simple setup into a policy audit unless requested.
- Add only accepted text. Keep model preferences in JSON and orchestration methods in Pepeye. Do not generate managed blocks or duplicate the skill catalogue.
- Existing `qp-policy` or deprecated `managed-skills` blocks are user-editable content. Consolidate or remove them only within the requested migration; preserve unrelated instructions and later user edits.

## Pepeye configuration

- Create `~/.qp/settings.json` when Pepeye hands off a missing configuration, or create/edit it when the user requests setup. Use the shipped [JSON template](../assets/settings.json) as the starting proposal. Carry forward the caller's task, host, preferences, and authority; after verification, return control so that task continues. Do not turn this handoff into a general host-instruction interview.
- Detect the active host and propose only its template section: `providers.codex` or `providers.claude`. Offer “This host (recommended)” and “Both hosts” when the choice is unresolved; reuse an explicit host choice without asking again. Copy both sections only when selected. If host detection is inconclusive, ask which host to configure.
- Merge the selected section into existing settings. Preserve unrelated root keys, the other host's settings, and customized action values; show conflicts rather than replacing them with template defaults. Adding support for another host later is a merge, not a full-file replacement. Selecting one host does not delete an existing section for the other.
- Preview the concrete template-based settings under the entrypoint's authority rules; reuse approval already provided. Resolve the active host's supported models and reasoning controls before presenting active defaults. Preserve explicit preferences and let the user accept defaults, customize, or decline; an unavailable model label is not proof of host support. Never overwrite an existing file just because this handoff expected it to be absent.
- Use `providers.codex.actions` and `providers.claude.actions`. Each maps actions to objects containing `model` and `reasoning` strings. Supported actions are `read`, `synthesis`, `code`, `plan`, `review`, `premortem`, and `exceptional`.
- Read the matching action directly; missing actions use cost-aware selection. `host-default` leaves reasoning unset. Translate `reasoning` to the host's supported effort control without changing global runtime settings.
- Initialize only accepted template settings or the user's selected preferences. Empty action maps are valid: missing choices let Pepeye select sufficient capability at reasonable cost. Keep inactive-host settings as editable preferences without claiming they were runtime-verified.
- Do not create free-form `instructions` fields at any level. When migrating existing files, preview their removal; move only guidance the user explicitly wants to retain into their chosen instruction file or task request.
- Explicit task choices override config; governing instructions and tool permissions still apply. Never interpret configuration as authority to delegate, publish, or access credentials.

- When migrating legacy `~/.qp/pepeye.json`, preserve user settings and convert host `preferences` maps to `actions`. Reconcile legacy `default`/`demanding` choices into the requested actions rather than dropping custom values. Merge into existing `~/.qp/settings.json` without overwriting unrelated keys; resolve collisions before writing. Back up both files and verify the merged result before removing the legacy file.
- The template uses documented Claude Code slugs and supported effort levels from [model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration) and [effort controls](https://code.claude.com/docs/en/model-config#adjust-effort-level). Sonnet handles collection/synthesis, Opus coding, and Fable planning/judgment; these are cost-aware starting choices, not benchmark-proven optima. Verify availability for the user's host.

## Apply and verify

- Follow the entrypoint's authority rules. Preview the exact change, reuse existing approval, refresh before writing, and reconcile material changes since preview.
- Back up existing instruction files under the host's configuration/data area; back up Pepeye JSON under `~/.qp/backups/pepeye/`. Use unique byte-for-byte backups. Inspection creates no files.
- Preserve unrelated content and settings. Invalid JSON or unsupported fields need a reported correction, not a reset. Delete a user-owned file only when its removal is explicitly requested.
- Read back the result. For instructions, check intended text and applicable precedence. For JSON, parse it and check changed preferences; report unavailable model/reasoning controls separately.
- Verify that only selected host sections were added or changed, existing custom actions and unrelated settings survived, and no unselected template section was introduced.
- Repair verification failures within accepted scope. Finish with the changed target, result, backup/recovery path, and material limitations.
