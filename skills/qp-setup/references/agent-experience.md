# Agent experience

Use when a Codex or Claude Code setup may benefit from reusable agent definitions for a more integrated Pepeye experience. Agent definitions are optional host-native artifacts; `pepeye` owns coordination and remains usable without them.

## Keep the layers separate

The provider-neutral catalogue at [work postures](../assets/agent-experience/postures.json) names the staffing postures Pepeye may use:

- **Àṣàwárí** (`asawari`) — exploration and mapping;
- **Olùtúpalẹ̀** (`olutupale`) — bounded analysis and consequential reasoning;
- **Akọ̀wé** (`akowe`) — prose/instruction work;
- **Olùṣe** (`oluse`) — bounded execution/mutation;
- **Olùdánilójú** (`oludaniloju`) — reproduction, testing, and verification;
- **Olùwádìí** (`oluwadi`) — current external/primary-source research;
- **Olùyẹ̀wò** (`oluyewo`) — fresh independent judgment.

A work posture is not an installed agent definition. It describes how a bounded assignment should work. The host may satisfy it with native capability, an existing user definition, a QP-managed definition, or a generic subagent shaped by the assignment.

Semantic skills are separate. Do not preload or hardcode skill identities into agent definitions. An assignment may name an already-selected skill when that materially improves the work; otherwise leave ordinary skill selection to the model/host.

## Inspect before proposing anything

Resolve the selected host(s), version, scope, native agents/subagent capability, existing user/repository agent definitions, current instruction/config surfaces, and the provider's actual model/effort/permission precedence from the installed host and current official documentation. Cached provider model IDs are not authoritative.

Current definition locations are useful conventions, not contracts:

| Host | User scope | Repository scope |
| --- | --- | --- |
| Codex | `$CODEX_HOME/agents/` (default `~/.codex/agents/`) | `<repo>/.codex/agents/` |
| Claude Code | `~/.claude/agents/` | `<repo>/.claude/agents/` |

Follow the installed host when its supported location/schema differs.

Prefer execution capability in this order:

1. a suitable **native host agent/capability**;
2. a suitable **existing user agent definition**;
3. a **QP-managed agent definition** only when it adds durable value the first two do not provide;
4. a **generic native subagent** shaped by the assignment when no reusable definition earns its cost.

Do not install seven definitions merely because seven work postures exist. Do not shadow or replace a native agent just to give the posture a QP name.

Existing user definitions remain user-owned. When one overlaps the desired posture, audit it and normally keep it. If a material difference creates a real choice, offer only reasonable options such as **keep existing**, **replace with the shown QP definition**, **add a separate non-conflicting QP definition**, or **leave unchanged**. Never merge QP text into an existing user definition.

## Run setup autonomously

Use the environment and existing configuration as evidence. Do not begin with a Host → Scope → Model → Role questionnaire when those facts can be discovered.

Form the recommended smallest change yourself. If there is no material conflict, show one compact proposal and ask for final confirmation. If existing state creates several materially different valid outcomes, show the audit and choices together, obtain the user's selection, then continue.

Preserve the root/main model and its startup defaults unless the user explicitly asked to change them. Agent-experience setup may report a material limitation caused by the current root configuration, but root-model tuning is a separate setup request.

If auditing the user's **global instruction file** could improve the setup, ask permission once before reading it. Declining that audit does not block agent-definition setup.

## Keep capability provider-native

The work-posture catalogue deliberately contains no model, effort, provider model class, or sandbox field. Those are host/runtime concerns.

For each assignment, Pepeye may request lighter or stronger capability when the active host exposes a native override and the task's consequence, ambiguity, difficulty, latency, or cost warrants it. Setup should not invent one cross-provider precedence model.

When rendering an agent definition, omit `model`/`effort` by default. Add a definition-level pin only when the user intentionally chose that persistent pin or current provider semantics make it a clearly desired reusable default; include the effect in the preview. A definition-level pin must not be described as dynamically overridable when the provider gives it stronger precedence.

The catalogue's `execution_boundary` expresses intent (`read-only` or `write-capable`), not a portable sandbox guarantee. Translate it through the strongest current host mechanism available and report the effective boundary honestly.

## Preview and apply

Prepare only the selected QP-managed definitions in a temporary directory with [render-agent-definitions.py](../scripts/render-agent-definitions.py). Its temporary settings file names only definitions that setup actually intends to install; absence means **do not render/install** that posture.

Show a compact proposal containing:

- host + scope;
- native/existing capabilities being reused;
- QP definitions to add or replace, and why each earns its place;
- any intentional model/effort pin;
- requested execution boundary and the host mechanism used to approximate/enforce it;
- exact files changed;
- backup location; and
- any host capability limitation.

Then ask one final mutation confirmation equivalent to:

```text
Apply these agent-experience changes? [y/N]
```

A blank answer means **No**. If the proposal materially changes after preview, show the changed proposal and confirm again.

Do not enable Code Mode, agent teams, scheduling, join/wait policy, retries, or another orchestration feature merely to install these definitions. Those remain harness capabilities Pepeye may use when already available and useful.

## Ownership, update, and rollback

QP-managed definitions contain the marker `qp-skills-agent-definition: v1`. Treat that marker plus exact path/content as ownership evidence, not permission to overwrite arbitrary user changes.

Before replacing/removing a QP-managed definition or other affected config, save a byte-for-byte backup under the host's own configuration area. Use unique names and never overwrite earlier backups. Refresh every destination immediately before writing; reconcile any material concurrent change before mutation.

If a marked definition has materially diverged from the QP-generated content, treat it as customized and present the difference rather than overwriting it automatically.

## Verify and return

Read changed definitions/config back and confirm:

- every installed QP definition was actually selected and is discoverable by the host;
- suitable native/user capability was reused rather than duplicated where applicable;
- no semantic skill was hardcoded/preloaded;
- intentional provider pins match the accepted preview and unpinned definitions remain unpinned;
- requested execution boundaries are enforced only to the degree the host actually supports;
- unrelated host configuration/definitions are unchanged; and
- the QP ownership marker is present only on QP-managed definitions.

Return the host/scope, capabilities reused, definitions added/replaced/skipped, actual model/effort configuration when material, changed files, verification, backup/rollback path, and residual host limitations.
