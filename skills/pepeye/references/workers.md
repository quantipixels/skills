# Worker controls

Read only when the installed host's delegation or continuation controls are unclear. Verify exposed tools and current official documentation; these anchors were checked on 2026-09-06. Do not enable disabled features or relax permissions to obtain a preferred topology.

## Claude Code

Use available `Agent`, `SendMessage`, status, and `TaskStop` controls. Prefer resumable general-purpose or custom workers when related follow-ups are likely; Explore/Plan workers are one-shot. Reuse the actual handle, not a new invocation with the same name. Custom definitions can set model and `effort`; confirm effective settings where observable.

Forks inherit the main prompt and conversation, so explicitly assign a worker role. Worktree isolation does not prove the worker started from the intended candidate: check its revision before edits. The coordination skill runs in the lead's context, not through `context: fork`. See [Claude subagents](https://code.claude.com/docs/en/sub-agents). Agent Teams is not required.

## Codex

Use exposed spawn, message, wait, resume, and close controls; `/agent` supports user inspection. The built-in `default` role and `.codex/agents/*.toml` configure spawned workers. Worker files can override requested model/effort settings; inspect effective values rather than assuming the request won. Omitted settings may be inherited.

A saved handle is useful only in a compatible live host/session. Check availability and cancellation before reusing it. If tools are missing, inspect the host version and `agents.enabled` policy rather than silently changing it. See [Codex subagents](https://developers.openai.com/codex/subagents).
