# Move from standalone QP skills to Alárinà

Use this guide when replacing earlier QP skill installations with the single Alárinà skill or its native plugin. Pick **one installation method per host** and keep the same project or user scope unless you intentionally want to change it. Existing sessions can retain old instructions; verify the replacement in a new or reloaded session before cleanup.

After installing Alárinà, you can ask it to perform this process with an explicit command such as `$qp-skills:alarina qp-update migrate my old QP skills to this plugin` in Codex or `/qp-skills:alarina qp-update migrate my old QP skills to this plugin` in Claude Code. Give it the target host and scope if they are not discoverable. The command inspects actual ownership before removing anything.

## 1. Find what is active

Identify the host, manager, scope and actual resolved paths. A checkout, symlink, copied skill and plugin cache have different owners. Inspect both project and user installations when applicable:

```bash
npx skills list --json
npx skills list --global --json
codex plugin list
claude plugin list
```

The retired standalone QP IDs are `adanwo`, `akowe`, `alaga`, `amose`, `architect`, `arojinle`, `atona`, `atunwo`, `ayewo-igba-ise`, `codex-orchestra`, `fihanmi`, `html-artifact`, `iwadi`, `oro`, `pese`, `qp-update`, `seda-pr`, `system-cleanup` and `yoruba-glossary`. A prior standalone `alarina` may also exist. Do not remove a same-named skill from another source, a modified local copy or an unrelated plugin merely because its name appears here. Review the manager's inventory and any local changes first.

## 2. Install and verify the replacement

For **Codex plugin** or **Claude Code plugin**, use the native manager:

```bash
codex plugin marketplace add quantipixels/skills
codex plugin add qp-skills@qp-skills

claude plugin marketplace add quantipixels/skills
claude plugin install qp-skills@qp-skills
```

Run only the pair for your host. If the QP plugin is already installed, follow its manager's update operation in [the lifecycle guide](installation-lifecycle.md) instead of creating a second registration. Verify the manager lists `qp-skills@qp-skills`, then start a new session and try `$qp-skills:alarina` in Codex or `/qp-skills:alarina` in Claude Code. The Claude package also supplies the `qp-skills:alarina` agent. A successful install is not proof that the previous conversation has reloaded the new instructions.

Older tagged packages did not declare a plugin version; a manager may describe one as `local` or `unknown`. Identify it by its registered marketplace, source and installed inventory, not a presumed `4.2.0` version string. If an update fails or is interrupted, inspect the manager's current registration and installed path before retrying its supported update command. An old Claude cache directory may remain after a successful update or uninstall; its presence does not mean the old plugin is enabled. Do not delete manager cache files by hand to decide which version is active.

If you want **a skill without a plugin**, use [Skills CLI](https://github.com/vercel-labs/skills) for the same host and scope as the old installation. For example:

```bash
npx skills add quantipixels/skills --agent codex --skill alarina
```

Use `--agent claude-code` for Claude Code and `--global` for a user-scoped installation. Verify `alarina` in `npx skills list` (or `--global`) and invoke `$alarina` in Codex or `/alarina` in Claude Code. Skills CLI does not install the native Claude agent. Do not keep both plugin and CLI copies for the same host unless you deliberately need both and can distinguish them.

## 3. Remove only retired copies you own

For an old **native QP plugin**, update the registered package. The package update retires its old skill inventory as one unit; it does not remove separately installed CLI skills. For old **Skills CLI** installations, run `npx skills remove` in the same project or user scope and select only the retired QP IDs confirmed in step 1. Without `--agent`, the named entries are removed from all Skills CLI host bindings in that scope, so verify the replacement for each affected host first. For example:

```bash
npx skills remove alaga atona iwadi
npx skills remove alaga atona iwadi --global
```

These are examples for copies you actually own and found; use your observed names and scope, and run only one scope's command for each set of copies. If another host still needs an old entry, use `--agent` to narrow the removal and verify what its shared canonical skill directory still exposes. Do not use `--all` or `--skill '*'`. If the old files came from a manual copy or symlink, identify the target and owner before removing that exact entry. Preserve modified or ambiguous files and report them as remaining migration work. Remove a prior standalone `alarina` too when the verified plugin now supplies the one you intend to use.

Replace old explicit calls such as `$alaga`, `/atona` or `$seda-pr` with the provider-qualified Alárinà entry followed by the command: `$qp-skills:alarina alaga-deliver`, `/qp-skills:alarina atona`, or `$qp-skills:alarina seda-pr`. For a Skills CLI installation, use `$alarina` or `/alarina` instead of the plugin-qualified prefix. Check your `AGENTS.md`, `CLAUDE.md`, shell functions and saved prompts for old names or paths; preserve other project instructions.

Use the old request's intended result to select its replacement. One old skill can have several new commands:

| Old skill | Alárinà command or entry |
| --- | --- |
| `adanwo` | `adanwo` |
| `akowe` | `akowe-audit` or `akowe-sync` |
| `alaga` | `alaga-intake`, `alaga-diagnose`, `alaga-recover`, `alaga-deliver`, `alaga-compare` or `alaga-verify-project` |
| `amose` | `amose`, `amose-context`, `amose-adrs` or `amose-nongoals` |
| `architect` | `architect-survey`, `architect-design`, `architect-review` or `architect-document` |
| `arojinle` | `arojinle` |
| `atona` | `atona-direction`, `seda-spec`, `seda-tickets` or `atona` |
| `atunwo` | `atunwo` |
| `ayewo-igba-ise` | `ayewo-igba-ise` for event reconstruction; `ayewo-retro` for session environment improvement; `ayewo-corpus` for cross-session or artifact-pattern evidence. The old command also routes these explicit requests. |
| `codex-orchestra` | Alárinà's coordination method; describe the delegation result and host constraints in the request |
| `fihanmi` | `fihanmi` |
| `html-artifact` | `html-artifact` |
| `iwadi` | `iwadi` for a defined research question; `sawari` for exploration or a repository dive |
| `oro` | `oro-sigidi` for agent-facing text; `oro-eniyan` for human-facing prose |
| `pese` | `pese`, only on direct user invocation |
| `qp-update` | `qp-update`, only on direct user invocation |
| `seda-pr` | `seda-pr-description`, `seda-pr` or `wo-pr` according to the requested PR result |
| `system-cleanup` | `system-cleanup` |
| `yoruba-glossary` | `yoruba-language`, `yoruba-teach` or `yoruba-glossary` |

A previous standalone `alarina` becomes the same Alárinà entrypoint with the provider's new invocation prefix. The installed [command menu](../../../SKILL.md#commands) gives the current purpose and boundary for each command.

For saved calls to the former internal `amose-learnings` command, use `amose-context` when the result is canonical domain language or reconciliation of existing knowledge. Keep an established `.learnings` destination for independently useful non-domain entries; the new command does not imply a bulk file rename.

## 4. Pin your preferred entry

These are **optional** ways to avoid typing the provider prefix. Choose the scope that matches your preference and merge into an existing file rather than overwriting it.

- **Codex project:** add `For software-project work, use the installed $qp-skills:alarina skill and load the relevant command; follow the user's narrower request.` to the project's `AGENTS.md`. For a personal preference across projects, use `~/.codex/AGENTS.md`. This selects the skill in the current agent. For a named custom agent, the Codex bundle supplies `agents/alarina.toml`; place it in the project's `.codex/agents/` or personal `~/.codex/agents/` only when that setup is requested, preserving existing customizations. Codex 0.156.1 does not auto-register it from the plugin. See [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents) and [instruction scopes](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **Claude Code project:** merge `"agent": "qp-skills:alarina"` into `.claude/settings.json` to make the plugin agent the default for that project. Use `~/.claude/settings.json` for a personal default across projects, or launch one session with `claude --agent qp-skills:alarina`. This is a real agent-mode selection; the plugin must be installed and enabled. See [Claude agent settings](https://code.claude.com/docs/en/sub-agents).
- **Claude instructions without an agent default:** put a short preference for `/qp-skills:alarina` in the existing project `CLAUDE.md` or personal `~/.claude/CLAUDE.md`. Keep existing instructions intact. See [Claude instruction scopes](https://code.claude.com/docs/en/memory).

For a terminal shortcut in Bash or Zsh, put the functions for the providers you use in your shell configuration, then set `qp` to the preferred one:

```bash
qp_codex() { codex "\$qp-skills:alarina $*"; }
qp_claude() { claude --agent qp-skills:alarina "$@"; }
qp() { qp_codex "$@"; } # Or: qp_claude "$@"
```

The Codex function starts the skill explicitly. The Claude function starts the plugin agent explicitly; omit the argument to enter an interactive session, or pass one quoted prompt such as `qp_claude "Investigate the failing build"`. The shortcut changes no global model, permission or authentication setting. Use the host's own settings or flags if you want a specific model. For plugin-free Skills CLI installs, substitute `$alarina` or `/alarina` in an explicit prompt and do not select the absent native Claude agent.

Finally, open a fresh session and confirm the chosen entry resolves to the expected installation and that retired standalone QP entries no longer appear in that host's skill inventory. If only part of the migration succeeded, keep the working old entry until its replacement is verified and report the exact remaining copy or configuration reference.
