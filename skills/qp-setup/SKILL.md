---
name: qp-setup
description: Install, configure, update, verify, or remove a selected engineering/agent tool, or inspect and manage host instruction policy at user or repository scope. Use after the target capability and scope are known; own setup mutation, verification, migration, and rollback, not tool selection, orchestration, usage expertise, or review.
metadata:
  maturity: experimental
---

# Setup

Make the selected capability ready with the least necessary user interruption. Inspect the real environment first, form the smallest sensible proposal, then ask only at a genuine authority or material-choice boundary.

An explicit request to install, configure, update, remove, or repair a named target authorizes inspection and preparation of that bounded setup. It does not authorize unseen mutation. Before the first write, show the material resulting change and obtain confirmation; a blank/default response must not apply it.

When relevant existing configuration is present, audit it instead of restarting requirements discovery. Preserve useful existing choices. If several reasonable outcomes remain, present the concrete differences and a small set of options, then continue autonomously from the user's choice. Do not turn setup into a long interview.

Ask separately only when the operation introduces a materially distinct effect the request did not already cover, such as credentials, trust/permissions, destructive unrelated state, persistent services, or inspection/mutation of user-global instructions.

## Choose the setup branch

Reuse the target and scope already established.

- **Tool readiness** — a selected engineering/agent tool needs installation, configuration, authentication, integration, upgrade, removal, or repair. Read [tool setup](references/tool-setup.md).
- **Host policy** — host instruction files need inspection, audit, installation, update, consolidation, or removal, including user-editable delegation/model/reasoning preferences. Read [host instructions](references/host-instructions.md).

If the useful tool/capability is still undecided, use `irinse`; setup should not select a tool merely because it can install one.

Do not widen repository scope to user/global scope. Preserve unrelated files, settings, instructions, services, credentials, and project state.

## Finish

Verify the resulting state from the real target environment rather than trusting an installer, edit, or command exit alone. Return the target, scope, setup action, resulting readiness/configuration state, changed surfaces, verification, rollback/recovery path, and material limitations.

Setup success proves readiness/configuration only. It does not prove that a tool is valuable for a task, that a model selected or used a skill, or that downstream engineering evidence is correct.
