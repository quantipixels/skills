---
title: Codex does not expand @ imports in instruction files
category: integrations
tags: [codex, claude-code, agents-md, claude-md, instructions, imports, asami]
problem_type: knowledge
date: 2026-10-10
---

## Context
The user's personal defaults were kept in one file and pulled into each host's instruction file with an `@path` import (`~/.claude/CLAUDE.md` contains `@~/.agents/AGENTS.md`).

## What went wrong or was non-obvious
Claude Code expands `@path` imports; Codex reads `~/.codex/AGENTS.md` as plain text and does not. Codex agents never saw the defaults, and nothing reported it: the import line looked correct and Claude Code worked.

## Guidance
Keep one source file (`~/.agents/AGENTS.md`). For Codex, symlink `~/.codex/AGENTS.md` to it or copy the text; use `@` imports only for hosts that expand them. After any change, ask a fresh agent on each host to quote one rule from the defaults; reading the files is not proof that a host loaded them.

## Evidence
`skills/asami/SKILL.md` (the Write step and the host check).
