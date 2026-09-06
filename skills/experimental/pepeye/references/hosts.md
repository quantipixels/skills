# Run Pepeye on Claude Code or Codex

Read for setup or a missing host capability. Pepeye directs the existing main agent; it needs no separate manager-agent definition, orchestration server, or global mode. Installing it does not activate supervision. Use the installed host's controls and permission policy, not flags copied from another host/version.

## Claude Code

Install QP through the existing plugin distribution:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

For an unmerged candidate, launch Claude from your target project with the candidate checkout instead:

```bash
claude --plugin-dir /absolute/path/to/skills
```

Then invoke in the main conversation:

```text
/qp-skills:pepeye Supervise <goal>, delegate useful work, and report the team.
```

The existing `qp-skills:qp` main-agent adapter is optional, not another prerequisite. Do not add `context: fork` to Pepeye or delegate it to a supervisor subagent. See Claude's [plugin development](https://code.claude.com/docs/en/plugins) and [skill context](https://code.claude.com/docs/en/skills) documentation.

Use `Agent` to start workers, `SendMessage` to steer/resume them, and `TaskStop` to stop runs when those controls are available. Prefer `general-purpose` or custom workers when reuse matters; the current Explore/Plan workers are one-shot. Select a supported model per invocation or worker definition; custom definitions can also set `effort`. `/tasks` exposes worker activity and available model/effort information. These controls are documented in [Claude subagents](https://code.claude.com/docs/en/sub-agents); verify the installed version's actual fields. [Agent Teams](https://code.claude.com/docs/en/agent-teams) are not required and should not be enabled merely for this skill.

## Codex

From your target project, install Pepeye, or use the existing full QP installation:

```bash
npx skills add quantipixels/skills --skill pepeye --agent codex --copy -y
```

For an unmerged candidate, replace `quantipixels/skills` with the absolute path to its checkout. Start a fresh Codex session and invoke:

```text
$pepeye Supervise <goal>, delegate useful work, and report the team.
```

Use Codex's exposed spawn, message, wait, resume, and close controls; `/agent` lets the user inspect threads. Current releases enable subagents by default. If tools are absent, check version, policy, and `[agents].enabled` before proposing configuration changes.

Set supported model/effort values per spawn when exposed. Reusable custom worker TOML files may set `model` and `model_reasoning_effort`; those definitions take precedence over spawn/default settings. Do not assume a requested override applied. See [Codex subagents and configuration](https://developers.openai.com/codex/subagents) and [skill invocation](https://developers.openai.com/codex/skills). No Codex custom-agent wrapper is needed for the coordinator.

## Check the installed path

In the chosen host, invoke Pepeye for two independent read-only checks of a small project. Ask it to check in during work, send a related follow-up to the same worker, report observed settings/status, and stop remaining runs. Prohibit edits and publication for this probe.

Confirm the main agent remains coordinator, native handles are reused, guidance reaches workers, the table matches observable activity, and no runs remain active. Record unsupported controls as limitations, not successful checks. A copied skill or accepted plugin does not prove authenticated orchestration behavior; QP's compatibility matrix keeps those claims separate.
