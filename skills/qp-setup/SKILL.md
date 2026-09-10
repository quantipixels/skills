---
name: qp-setup
description: Inspect, apply, update, or remove optional Codex host settings and QP instructions at user or repository scope. Use for reproducible Codex setup with preview, explicit permission, and backups. Exclude delegation, worker installation, and other hosts.
metadata:
  maturity: experimental
---

# QP Setup

Configure Codex at the user's selected scope. Use native file tools; this skill installs no worker definitions or runtime. `pepeye` owns delegation behavior and remains usable without setup.

## Select and inspect

Establish whether the user wants inspection, setup/update, or removal, and whether the target is user scope or one repository. Reuse the operation, scope, and selected options already established in the conversation; ask only for missing choices. Never turn a repository request into a global change.

| Scope | Instructions | Host options |
| --- | --- | --- |
| User | `$CODEX_HOME/AGENTS.md` | `$CODEX_HOME/config.toml` |
| Repository | `<repo>/AGENTS.md` | `<repo>/.codex/config.toml` |

Resolve `CODEX_HOME` from the active environment, defaulting to `~/.codex`. Resolve the repository from the requested path or current Git root. Check existing `AGENTS.override.md` files that may supersede the selected instructions, and applicable nested instructions. Report an override rather than silently editing a file Codex will not load. Repository config depends on Codex's trust rules; do not grant trust or change permissions during setup.

Read the selected files and relevant existing preferences. Offer the [general instructions](assets/instructions.md), the optional Pepeye binding below, and the two choices in [host options](references/host-options.md). Let the user select each independently. Do not copy personal biography, language preferences, paths, credentials, or unrelated settings from the configuring machine.

The optional Pepeye binding is: “Use `pepeye` when the user requests delegation or supervised workers materially help the task. Use specialist QP skills directly for their methods.” Confirm the skill is installed and discoverable before adding this binding. Setup does not install missing skills without authorization.

## Preview and apply

Prepare an exact diff for the selected paths and choices. Preserve existing instructions except for the selected overlap cleanup below, and preserve unrelated config, including comments and tables. Show current versus proposed settings, affected scope, and backup location. Ask explicit permission before writing; a request to run setup is not approval of unseen changes. Reuse approval only while the proposed changes remain the same.

Before changing or deleting any existing file, save a byte-for-byte backup with a unique name in `.qp-backups/` beside that file. Use a private directory and owner-only backup files where supported; never overwrite a previous backup. Resolve symlink targets and include them in the preview; refuse an unexpected symlink or non-file destination. Complete and verify all required backups before the first edit. Stop if a backup fails. Dry-run/inspection creates no files.

Manage selected QP instructions inside one block delimited by `<!-- qp-setup:start -->` and `<!-- qp-setup:end -->`. Reject missing, reversed, or duplicate markers. With no existing block, append it; preserve surrounding user text except for explicitly requested overlap cleanup. By default, if equivalent instructions already exist outside the block, report them and offer only missing guidance; do not duplicate or adopt the user's text. If an existing managed block was customized, show those differences and obtain approval before replacing it. Reapplying unchanged content is a no-op.

When the user asks to replace or clean up overlapping guidance and install the shipped instructions, prepare one consolidated diff: copy the selected general instructions from `assets/instructions.md` verbatim into the managed block, include the exact optional Pepeye binding above if selected, and remove the equivalent guidance outside the block. Preserve personal instructions and additional rules that the shipped text does not cover, including unique clauses in otherwise overlapping paragraphs. Show any customized binding conditions that the shipped binding would replace. Do not rewrite the shipped text or treat equivalent existing guidance as completion of this request. The diff approval covers both installation and the shown removals; no separate cleanup approval is needed. Plain inspection or setup without a cleanup request retains the default preservation behavior.

Merge only approved TOML keys into their existing tables. Never append duplicate tables or replace the file with a sample. Refresh each destination immediately before applying; if it changed since the preview, reconcile and obtain approval for the revised diff. Write atomically where supported, preserve file permissions, parse the resulting TOML, and verify the final diff matches the approved changes.

## Remove or undo

Inspect the same scope, preview cleanup, ask permission, and back up affected files first. Remove only the managed instruction block. Leave surrounding content intact; delete an instruction file only when removal leaves it empty and the user approved deletion.

For host options, compare the setup backup or approved diff with the current file. Revert only established setup changes or values explicitly selected by the user. Preserve later edits; never restore an entire old config over them. If ownership is unclear, ask what to retain. Keep backups for recovery. Removing this configuration does not uninstall QP Skills or `pepeye`.

## Finish

Report the selected scope, changed files, applied options, backup paths, and any skipped or unsupported choices. Ask the user to start a new Codex session to load the instructions and settings. File validation does not prove skill selection, model availability, or experiment activation.
