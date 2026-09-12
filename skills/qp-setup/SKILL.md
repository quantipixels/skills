---
name: qp-setup
description: Install, configure, update, verify, or remove a selected engineering or agent tool, or manage shared agent instructions at user or repository scope. Use after the target capability and scope are known; own setup mutation, verification, and rollback, not tool selection, usage expertise, orchestration, or review.
metadata:
  maturity: experimental
---

# Setup

Make one selected capability ready at the requested scope, or safely manage the shipped agent instruction block for a supported host.

Delegate substantial analysis, research, and expert work to subagents when it materially helps.

An explicit request to install, configure, update, remove, or repair a named target authorizes the bounded setup mutation at the requested scope. Ask only when a material target, scope, or setup choice is missing, or when the operation introduces a separately consequential effect such as credentials, trust/permissions, persistent services, destructive unrelated state, or another external write not already implied by the request.

## Choose the setup branch

Reuse the target and scope already established.

- **Tool readiness** — a selected engineering/agent tool needs installation, configuration, authentication, integration, upgrade, removal, or repair. Read [tool setup](references/tool-setup.md).
- **Host instructions** — the shipped instruction block needs inspection, installation, update, or removal for a supported agent host. Read [host instructions](references/host-instructions.md).

If the useful tool/capability is still undecided, use `irinse`; this skill should not select a tool merely because it can install one.

Do not widen repository scope to user/global scope. Preserve unrelated files, settings, instructions, services, credentials, and project state.

## Finish

Verify the resulting state from the real target environment rather than trusting an installer, edit, or command exit alone. Return the target, scope, setup action, resulting readiness/configuration state, changed surfaces, verification, rollback/recovery path, and material limitations.

Setup success proves readiness/configuration only. It does not prove that a tool is valuable for a task, that a model selected or used a skill, or that downstream engineering evidence is correct.
