# Agent experience

Use when Codex or Claude Code setup may need a persistent provider-native agent definition because native/per-spawn controls are insufficient for a recurring capability. `pepeye` owns coordination and normally shapes workers dynamically from their assignments.

## Start from native capability

Inspect the selected host, version, scope, current native agents/subagent controls, model/effort/permission/isolation behavior, existing user/repository agent definitions, and relevant configuration from the installed host and current official documentation.

Do not begin by inventing a reusable agent fleet. First determine whether the required worker can be expressed adequately through:

1. a native/general host agent;
2. task-specific assignment instructions/context;
3. current per-spawn model/effort/tool/permission/isolation controls; or
4. an existing user-owned definition/configuration.

If those are sufficient, recommend no new definition.

## Admit a persistent definition only when it earns a file

A package-managed agent definition is justified only when all are true:

- the needed behavior/runtime constraint is recurring and stable rather than task-specific;
- the active host cannot express it adequately through normal per-spawn controls, assignment instructions, or existing configuration;
- no suitable native/user-owned definition already provides it; and
- persisting the definition materially improves reliability, enforcement, reuse, or cost.

Examples that may qualify depending on the host include a stable tool/permission envelope, required isolation mode, provider-specific environment/configuration, or an intentionally persistent model/effort pin.

Exploration, analysis, writing, implementation, verification, research, and review do **not** by themselves justify reusable definitions. Task-specific behavior belongs in the assignment.

Semantic skills are separate. Do not preload or hardcode skill identities or workflow stages into agent definitions.

## Inspect existing definitions before proposing change

Current locations are useful conventions, not contracts:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/agents/` (default `~/.codex/agents/`) | `<repo>/.codex/agents/` |
| Claude Code | `~/.claude/agents/` | `<repo>/.claude/agents/` |

Follow the installed host when its supported location/schema differs.

Existing user definitions remain user-owned. When one already provides the needed persistent constraint, reuse it. If a material difference creates a real choice, offer only reasonable options such as **keep existing**, **replace with the shown package-managed definition**, **add a separate non-conflicting definition**, or **leave unchanged**. Never merge package text into an existing user definition.

## Run setup autonomously

Use the environment and existing configuration as evidence. Do not begin with a Host → Scope → Model → Agent questionnaire when those facts can be discovered.

Form the smallest sensible recommendation yourself. If there is no material conflict, show one compact proposal and ask for final confirmation. If existing state creates several materially different valid outcomes, show the audit and choices together, obtain the user's selection, then continue.

Preserve the root/main model and startup defaults unless the user explicitly asked to change them. Agent-experience setup may report a material limitation caused by current root configuration, but root-model tuning is a separate setup request.

If auditing the user's **global instruction file** could improve the setup, ask permission once before reading it. Declining that audit does not block agent-definition setup.

## Build definitions directly from the active host

When a definition passes the admission gate, construct the smallest provider-native definition from the active host's current schema and capability. Do not route the work through a provider-neutral role/posture catalogue or generic renderer merely to normalize different hosts.

Include only persistent configuration that earned its place. Keep task-specific outcomes, evidence, acceptance criteria, semantic skills, and workflow position in the assignment.

Treat model/effort/permission fields according to actual provider precedence. Omit persistent model/effort pins unless the user intentionally chose them or current host semantics make them clearly necessary. Do not describe a definition-level value as dynamically overridable when the provider gives it stronger precedence.

## Preview and apply

Show a compact proposal containing:

- host + scope;
- native/existing capabilities being reused;
- the concrete persistent limitation a new/replacement definition solves;
- exact provider-native definition/configuration to add or replace;
- any intentional model/effort pin;
- requested permission/isolation behavior and the actual host mechanism providing it;
- exact files changed;
- backup location; and
- any host capability limitation.

Then ask one final mutation confirmation equivalent to:

```text
Apply these agent-experience changes? [y/N]
```

A blank answer means **No**. If the proposal materially changes after preview, show the changed proposal and confirm again.

Do not enable Code Mode, agent teams, scheduling, join/wait policy, retries, or another orchestration feature merely to install a definition. Those remain harness capabilities Pepeye may use when already available and useful.

## Ownership, update, and rollback

When the host format permits a harmless comment/metadata marker, package-managed definitions may carry `qp-skills-agent-definition: v1` as ownership evidence. The marker is not permission to overwrite arbitrary user changes.

Before replacing/removing a package-managed definition or other affected config, save a byte-for-byte backup under the host's own configuration area. Use unique names and never overwrite earlier backups. Refresh every destination immediately before writing; reconcile any material concurrent change before mutation.

If a marked definition has materially diverged from the generated/proposed content, treat it as customized and present the difference rather than overwriting it automatically.

## Verify and return

Read changed definitions/config back and confirm:

- the persistent limitation identified in the proposal is actually addressed;
- no unnecessary role/posture fleet or duplicate native capability was introduced;
- no semantic skill or task-specific workflow instruction was hardcoded;
- intentional provider pins match the accepted preview;
- requested permission/isolation behavior is enforced only to the degree the host actually supports;
- unrelated host configuration/definitions are unchanged; and
- any package ownership marker appears only on package-managed definitions.

Return the host/scope, capabilities reused, definition/configuration added/replaced/skipped, actual runtime configuration when material, changed files, verification, backup/rollback path, and residual host limitations.
