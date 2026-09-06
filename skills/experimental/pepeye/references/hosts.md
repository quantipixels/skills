# Select Pepeye as the main agent

Read for setup or a host capability gap. Keep orchestration in `pepeye`; host adapters only select and load it. Installation is not activation. Change only the user-approved configuration scope, preserve existing instructions, and never loosen permissions to make delegation work.

Host contracts below were checked on 2026-09-06. Recheck the linked official documentation and installed help when versions, loading, or controls differ. Package checks do not prove model-visible behavior.

## Claude Code

After installing the QP plugin, select its main-agent adapter:

```bash
claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
claude --agent qp-skills:pepeye
```

For an unmerged candidate, launch from the target project with the candidate checkout:

```bash
claude --plugin-dir /absolute/path/to/skills --agent qp-skills:pepeye
```

To make this the project's startup default, merge into `.claude/settings.json` only when requested:

```json
{
  "agent": "qp-skills:pepeye"
}
```

Claude's [main-agent selection](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly) replaces the default system prompt; `model: inherit` inherits the model, not that prompt. Project instructions still load. The adapter preloads only `pepeye`; missing or policy-disabled preloads must be detected. To keep Claude's built-in prompt, invoke `/qp-skills:pepeye <goal>` in an ordinary session instead. The routing-oriented `qp-skills:qp` agent remains a separate optional entry, not a prerequisite.

Use available `Agent`, `SendMessage`, status, and `TaskStop` controls. Reuse `general-purpose` or custom workers; Explore/Plan are one-shot. A new invocation is not a resume. Confirm IDs before messaging; stopped-by-user workers must not be restarted automatically. Model selection and custom-agent `effort` are host controls, not guarantees about the effective settings. See [subagent configuration and continuation](https://code.claude.com/docs/en/sub-agents).

Forks can inherit the main prompt and conversation; brief them explicitly as workers. Worktree isolation can start from the default branch rather than the parent's candidate, so verify the revision before assigning edits. Neither Agent Teams nor nested supervisor agents are required.

## Codex

Install the QP skills in the target project so workers can load their specialist contracts:

```bash
npx skills add quantipixels/skills --agent codex --skill '*' --copy -y
```

For an unmerged candidate, replace `quantipixels/skills` with its checkout's absolute path. A full existing QP installation is sufficient; do not reinstall merely to select a role.

The shipped [profile](../assets/codex/pepeye.config.toml) configures the primary session, not a custom worker. On **Codex 0.134.0 or later**, place it at `$CODEX_HOME/pepeye.config.toml` (`~/.codex/pepeye.config.toml` by default), preserving any existing profile. Then start:

```bash
codex --profile pepeye
```

A copied installation includes the profile at `.agents/skills/pepeye/assets/codex/pepeye.config.toml`. Before copying, inspect the effective `developer_instructions`: a profile replaces that string rather than appending to existing user instructions. Merge both instruction blocks when needed. The profile deliberately sets no model, sandbox, credentials, or tool permissions.

Current [profile loading](https://developers.openai.com/codex/config-advanced) uses separate files, not `[profiles.pepeye]` or `profile = "pepeye"` in `config.toml`. Project and CLI overrides can supersede the profile. For older versions, use `$pepeye <goal>` or verify that version's profile contract rather than assuming this layout.

For an explicitly requested startup default, merge the profile's `developer_instructions` into the trusted project's `.codex/config.toml`, or into `$CODEX_HOME/config.toml` for a user-wide default. Keep it at the top level and retain the primary-thread/worker guard. `model_instructions_file` replaces built-in instructions and is not this adapter. See [configuration reference](https://developers.openai.com/codex/config-reference). The direct `$pepeye <goal>` invocation remains available without any configuration changes.

Codex's `default` role and `.codex/agents/*.toml` configure spawned agents, not the main conversation. Worker files may override inherited model/effort settings; inspect effective values rather than assuming the requested override won. Use exposed spawn/message/wait/resume/close controls and `/agent` for inspection. If tools are absent, check version, policy, and `agents.enabled`; do not bypass a disabled capability. See [Codex subagents](https://developers.openai.com/codex/subagents).

## Verify and undo selection

Start a fresh session through the chosen adapter. Confirm the main thread loads Pepeye without a manual skill invocation. Ask a simple question, then request two independent read-only checks with a related follow-up to one worker. Verify no needless delegation for the question, early guidance, reuse of the same native handle, honest settings/status reporting, and no inherited coordinator role in workers. Redirect a goal and cancel a worker: the lead must update affected assignments without resurrecting the cancelled run. Prohibit edits/publication for this probe.

Resume or compact only where the host supports it; confirm the selected role, current candidate, and retained handles instead of inferring them from transcripts. A handle is not portable across hosts. Document unsupported controls as gaps. This probe is manual authenticated evidence, not a claim made by syntax/install CI.

To undo selection, remove only the added Claude `agent` setting or Codex instruction block, or omit `--agent`/`--profile` in a new session. Restore prior values rather than deleting other configuration. Existing sessions may retain their selected role. Uninstalling skills is a separate action.
