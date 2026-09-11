---
name: qp-setup
description: Install, configure, update, verify, or remove a selected engineering or agent tool, and manage optional QP/Codex host configuration at user or repository scope. Use when a capability is missing or not ready, or when the user asks to set up QP/Codex behavior; own setup state and rollback, not tool selection, usage expertise, delegation, or review.
metadata:
  maturity: experimental
---

# QP Setup

Make one selected capability ready at the requested scope. Own setup mutation, verification, and rollback. Do not own whether a companion tool is the right tool for an engineering question or how its evidence should be interpreted; use `irinse` for that.

## Select the setup target

Reuse the target, scope, and choices already established in the conversation. Ask only when a material setup choice is missing.

Choose one branch:

- **Tool readiness** — a named engineering/agent tool needs installation, configuration, authentication, integration, upgrade, removal, or readiness repair. Read [tool setup](references/tool-setup.md).
- **Codex/QP host configuration** — optional QP instructions or Codex host settings need inspection, application, update, or removal at user or repository scope. Read [Codex host configuration](references/codex-host.md).

If the request is “which tool should I use?” or the useful capability is still undecided, use `irinse`; setup should not select a tool merely because it can install one. Conversely, once the tool is selected, `qp-setup` may resolve current official installation/configuration details without sending setup mechanics back to Irinṣẹ.

Do not turn a repository-scoped request into a global change. Installation, persistent services, downloads, credential changes, trust changes, provider writes, and destructive removal require the authority appropriate to their actual effects.

Keep rollback material with the setup target it belongs to. For host configuration, backups stay inside that host's own user- or repository-scoped data/config directory rather than generic QP state elsewhere.

## Finish

Verify the resulting state from the real target environment rather than trusting an installer, edit, or command exit alone. Return the selected target, scope, setup action, resulting readiness/configuration state, changed files or system surfaces, verification, rollback/recovery path, and material limitations.

Setup success proves readiness only. It does not prove that the tool is valuable for a task, that a model selected or used a skill, or that downstream engineering evidence is correct.
