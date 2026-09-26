# Skill and command mechanics

Read after agent-writing when creating or restructuring skills or commands. Its common authority, composition and conditional-loading rules still apply. A public identity, compatibility break or retirement must be within the requested scope.

A skill is a packaging and invocation choice around a useful behavioural contract. Do not start from taxonomy. Start from the result a user or another skill needs.

## Choose a cohesive capability boundary

A command is a selectable method inside a skill. Define its user/use case, useful result, required expertise, scope, authority, accepting evidence and next consumer before choosing its size. Keep multiple responsibilities together when they serve the same outcome and need the same context and feedback. Depth is justified by difficult decisions and recurring failure modes, not a word budget.

For example, `alaga-deliver` owns implementation, testing and affected documentation because together they complete an accepted change. `akowe-audit` and `akowe-sync` remain separate because a read-only judgment and authorized reconciliation have different effects and accepting evidence. Do not split a checklist into commands or create commands for each technical layer.

Split when callers need an independently useful result, materially different authority, distinct expertise/load conditions or a separately reusable contract. Combine when repeated context transfer, copied procedure or artificial handoffs exceed the value of independent selection. Preserve useful conditional depth in references; consolidation must not erase expertise.

Choose the appropriate home:

| Need | Home |
| --- | --- |
| Discover a distinct package with its own users or runtime dependencies | Skill, only when an existing entry cannot coherently own it. |
| Select a cohesive capability with a meaningful stopping point | Command within the existing entry. |
| Apply conditional expertise, examples or a shared invariant | Reference/contract with explicit load conditions. |
| Progress through dependent results | Playbook; reuse command methods and skip resolved stages. |
| Repeat a bounded mechanical operation reliably | Shared script, only when existing tools do not suffice. |
| Supply persistent host-specific configuration | Provider adapter; keep portable semantics with the method. |

For Alárinà, add commands to `commands/` and `routes.yaml`, then regenerate the menu and provider packages. Keep one discovery entry. Shared runtime operations live in `scripts/`; supporting expertise stays in `references/`, grouped by use case rather than a command or former skill. Choose the topic that explains when the guidance helps; commands across families can consume the same reference. Keep direct conditional links at callers and update the [reference guide](../../README.md) when discovery changes. Do not add a new standalone skill, wrapper or worker type merely because an old skill used to have one.

Keep shared meaning with one authoritative owner. A caller states the required result and consumes its evidence instead of copying the callee's procedure. Direct links cover known dependencies; leave the entrypoint's discovery path available when the task exposes an uncovered obligation. A command's reference list is not an exclusive allowlist of useful expertise. Retain consequential authority and stop conditions at the local branch where the agent chooses an action. When moving or retiring an owner, reconcile routes, consumers, resource paths and published package content together.

For a useful command-to-command dependency, link the exact method with the question, participants and result the caller needs. Reuse adequate evidence and preserve the caller's authority. Adapt the assignment before changing the reusable method. Keep task-specific application directions with the caller; when several callers need the same adaptation, give it one conditional reference, such as the [agent-respondent perspective](../../productivity/inquiry/agent-respondent.md). It supplies that adaptation and links the original method instead of copying it or creating a new mode. Avoid mutual handoffs for the same prerequisite and speculative links between every command.

## Decide whether a separate skill earns a public identity

A separate skill should have:

- an independently useful result or steering contract;
- a realistic trigger that should select it directly;
- nearest exclusions that keep adjacent owners distinct; and
- a reason the behaviour cannot live more coherently in an existing skill or instruction surface.

Different subject matter, a long file, or the ability to write guidance does not by itself justify another public skill.

## Invocation is part of the design

Choose whether the model must be able to reach the skill autonomously.

- **Model-reachable** spends always-loaded routing context but lets agents/other skills discover it.
- **Human-invoked** spends less model context but makes the human remember the skill.

Use the host/package's current invocation controls rather than copying volatile provider syntax here. Keep model-reachable descriptions discriminative enough to fire on real branches and reject adjacent ones.

A compatibility alias should not compete with its replacement. Narrow its description to explicit legacy-name use and keep the method at one owner.

## Do not confuse a skill with an agent definition

A skill owns a reusable semantic result/method. An assignment specifies what a delegated worker must accomplish now, including its context, authority, evidence, independence, completion boundary, and any useful runtime constraints. A provider-native **agent definition** is an optional reusable host artifact only when a persistent behavior/runtime delta cannot be expressed adequately through the assignment or native host controls. A workflow owns progression between results.

Good:

- use a native/general worker with a fresh read-only assignment for independent judgment; [atunwo](../../../commands/atunwo.md) remains the semantic code-review method when that method is useful;
- shape a generic worker for a README, architecture document, prompt, or handoff instead of creating a permanent writer agent type;
- add a provider-native definition when a recurring tool, permission, isolation, or persistent model constraint genuinely requires one on that host.

Bad:

- create an `alaga-agent` definition that duplicates Alága's method;
- hardcode [atunwo](../../../commands/atunwo.md) into every reviewer-like definition;
- maintain explorer/writer/reviewer/posture catalogues only to classify work before spawning it;
- create a new skill merely because a provider benefits from a named worker.

Before creating another public skill or agent definition, ask whether the missing behavior can live more coherently in the assignment or an existing native host control.

Use the provider's supported interface for installing, configuring, migrating, or verifying provider-native agent declarations. This skill owns their instruction text; the provider/host owns readiness and mutation.

## Treat the description as a pointer

The description decides whether the skill becomes reachable. State the owned result and genuinely distinct trigger branches, plus the nearest meaningful exclusions. Do not summarize the procedure or pad one branch with synonyms.

Good:

> Review a fixed code candidate or codebase snapshot for independent engineering judgment. Use for change, codebase, or parity review.

Bad:

> Review, inspect, examine, check, assess, analyze, evaluate, or look over code for quality.

If two skills attract the same realistic request, resolve the ownership/result distinction before adding more trigger vocabulary.

## Routers encode topology, not inventory

A router earns its place by encoding useful route shapes or adjacent-owner distinctions that individual descriptions do not.

Good:

- Installed definitions provide the dynamic inventory; the router preserves common paths and owner boundaries.

Bad:

- Replace route topology with description matching because “the model can discover the skills”.
- Rebuild a second exhaustive catalogue inside the router.

When simplifying a router, identify which topology is being retained, replaced, or deliberately retired.

## Review a skill portfolio when asked

For an explicitly requested portfolio review, compare public identities, owned results, routing collisions, compatibility aliases, cumulative always-loaded context, and representative end-to-end task paths. Structural counts and lexical overlap are leads, not quality or redundancy verdicts.

Look actively for no-ops, caches, sediment, copied callee procedure, competing outcomes, and compatibility surfaces that no longer earn public routing load.

## Support lifecycle decisions with evidence

When deciding whether to promote, narrow, fold, replace, or remove a skill, use real-use evidence where available: eligible opportunities, correct/incorrect selections, missed triggers, incremental value/cost, boundary failures, counterevidence, and coverage limits.

Do not infer usage or value from repository shape, raw invocation count, or one successful example. A proved structural defect can justify a change; missing historical evidence remains a gap, not a permanent veto.

## Verify the boundary that changed

Validate selection when routing changed, loading when disclosure changed, authority when action semantics changed, and behaviour when instructions changed materially. Package syntax checks prove structure only.

For material refactors, use the evolution audit from `instruction-economics`: retain, strengthen, relocate, replace, or retire. The goal is a better current skill, not preservation of its history.
