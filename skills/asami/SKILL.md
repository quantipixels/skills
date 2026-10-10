---
name: asami
description: Builds and maintains the user's personal agent defaults - corrections and preferences that apply to all their work - from their instruction files and about a week of sessions, shown as a draft and written only after a yes. Use when the user asks about their defaults, "my ways", or agent setup, when a lesson about the user needs to become a default, or for an opted-in weekly run.
---

# Àṣà mi

Output: a short list of the user's own rules that every agent on every host follows (about 40 lines or 4 KB). Say less rather than more. It is a personal file, not a project record.

Needs: a user request about their defaults or setup, or a proposed lesson about the user. If neither is present, return and say what is missing.

## Method

Keep a rule only if the user stated it outright or it repeated across sessions. Leave out one-offs and guesses, anything the installed skills already say, project facts, and client names, hosts, data and secrets.

- Evidence: the existing instruction file per host (`~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, and what they import) and about the last week of sessions. Get session and memory-note evidence from `ironu`, which owns reading local host records; do not copy its method or script. Read only sessions that show corrections or repeated asks. Ask a few short questions only where evidence is unclear.
- Draft: show each rule with the moment that shows it (quote or session and date), and offer add, merge or delete; prefer merge over a near-duplicate. Write nothing without a yes to this draft; "set up my defaults" asks for the draft, it does not approve it. If the user is away, stop at the draft and save it to `~/.agents/qp-pending.md`, where unanswered proposals wait.
- Write: one source file every host reads (`~/.agents/AGENTS.md`, or the user's existing single source). Some hosts ignore `@path` imports (Codex does; Claude Code expands them), so link each host file to the source (symlink) or copy the text. Never rely on an import the host ignores. Do not overwrite a host file with other content; show the change first. Over the cap, merge, move a rule into a skill, or delete. Template: [defaults template](references/defaults-template.md).
- Settings: `~/.agents/qp.yaml` (model overrides, which records live in git, docs folder) only when the user wants such defaults; show the exact YAML first.
- Triggers: manual; a proposed lesson about the user, drafted as above; an opt-in weekly run (on SIGIDI `schedule_task` with a one-week interval, elsewhere the host scheduler) that posts a draft and changes nothing without a yes; after a skills update, propose removing rules the skills now cover.

## Done

For each host the user uses, a fresh agent (a delegated agent on each model family in use) quotes one rule without reading any file. A host that cannot quote it has not loaded it: fix the link or copy and ask again.

## Return

The draft or the written list, what each host quoted, and anything left waiting for a yes.
