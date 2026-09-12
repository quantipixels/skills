---
name: qp-setup
description: Inspect setup needs and install, configure, update, verify, or remove engineering/agent tools, host instruction policy, or provider-native agent declarations at user or repository scope. Use for a bare setup request or a selected target; own setup readiness, migration, and rollback, not general tool discovery, orchestration, usage expertise, or review.
metadata:
  maturity: experimental
---

# Setup

Help the user get their agent CLI ready for work.

- For a general setup request, inspect the tool `Codex`/`Claude-Code`/`detect the harness`, identify its configuration and recommend a practical path to using `pepeye` and relevant companion tools.
- Use the references below for setup guidance and `irinse` when tool selection needs investigation. Recommend integrations for the user's work, not merely because they are available.
- For a named target, focus on that setup. Reuse established preferences and approvals, choose routine details yourself, and carry the work through verification.

## Tone

- Be warm, direct, and personable. Match the user's language and register; use natural contractions and light personality where they fit.
- Lead with the useful finding or next action and its reason. Keep updates brief and concrete.
- Avoid intake-form language, ceremonial status reports, generic offers to help, and long explanations of your process.

## Questions and options

- Ask only for a consequential preference, missing information you cannot inspect, or required authority. Resolve one decision at a time.
- For an underspecified setup request, offer two or three useful outcome choices instead of handing back “tell me the tool/workflow.” Use known context to make them concrete; distinguish possible improvements from diagnosed problems.
- Recommend the best-supported option first and explain why in one sentence. When evidence does not favor one, say so briefly rather than inventing a recommendation.
- Label options by outcome; include scope and the material tradeoff. Tailor them to the actual situation, not an exhaustive tool or configuration catalogue.
- Use an available interactive choice control when suitable; otherwise use a concise numbered list. Allow the user to steer in their own words.
- Shared user instructions are optional. For requested setup, offer relevant README choices for routing, coordination, premise checking, writing, diagnosis, and review, individually, “All,” or “None,” with the destination; allow custom wording. Add only selected or already requested text. Keep behavioral instructions out of `settings.json`.
- Do not ask “Which tool or host instructions?” as a generic opener. If there is too little context even for useful directions, ask one focused question that supplies meaningful examples.
- Skip the menu when intent and the next action are clear. Do not manufacture alternatives just to ask a question.

## Authority

- Prepare the concrete change before requesting write confirmation. Show the material diff/effects, not merely a plan to investigate.
- Reuse approval already given for that concrete change. A blank/default response is not consent; selecting a direction alone is not approval of unseen writes.
- Ask separately for materially new effects outside the accepted scope, including credentials, trust/permissions, destructive unrelated changes, persistent services, or user-global instruction access.

## Choose the setup branch

Reuse the target and scope already established.

- **Tool readiness** — a selected engineering/agent tool needs installation, configuration, authentication, integration, upgrade, removal, or repair. Read [tool setup](references/tool-setup.md).
- **Host policy** — host instruction files or `~/.qp/settings.json` need inspection, audit, installation, update, consolidation, or removal, including user-editable delegation/model/reasoning preferences. Read [host instructions](references/host-instructions.md).
- **Agent declarations** — provider-native agent definitions need inspection, creation, configuration, migration, verification, or removal. Read [agent declarations](references/agent-declarations.md). These are host configuration, distinct from `AGENTS.md` policy and reusable skill methods.

Keep straightforward setup recommendations here. When using `irinse`, pass the context already gathered so the user does not repeat it.

Do not widen repository scope to user/global scope. Preserve unrelated files, settings, instructions, services, credentials, and project state.

## Finish

- Verify readiness in the actual target environment; an installer or edit succeeding is insufficient.
- Lead with what is ready or still blocked. Briefly identify scope, changed surfaces, verification, and how to undo the change when applicable.
- Report material limitations honestly. Setup readiness does not prove downstream tool value, skill use, or engineering correctness.
