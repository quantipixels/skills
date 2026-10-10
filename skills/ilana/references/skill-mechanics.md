# Skill mechanics

Read after agent-writing when the artifact is a skill. Its common authority, composition and conditional-loading rules still apply. A public identity, compatibility break or retirement must be within the requested scope.

A skill is a packaging and invocation choice around a useful behavioural contract. Do not start from taxonomy. Start from the result a user or another skill needs.

## Decide whether a separate skill earns a public identity

A separate skill should have:

- an independently useful result or steering contract;
- a realistic trigger that should select it directly;
- nearest exclusions that keep adjacent owners distinct; and
- a reason the behaviour cannot live more coherently in an existing skill or instruction surface.

Different subject matter, a long file, or the ability to write guidance does not by itself justify another public skill.

## Classify before adding guidance

Name the result, the observed gap and what a capable agent already does without help before choosing a home. Use these classes when deciding whether a QP skill should change; they are not a runtime checklist. A remedy can span classes, but each part needs one owner.

| Class | Placement decision | Example |
| --- | --- | --- |
| 0. Agent behaviour or capability | Defer to the capable agent, native tool or existing specialist. Add guidance only for a demonstrated remaining gap. | Let the agent choose searches, split routine work or compose a local tool path. |
| 1. QP semantic behaviour | Keep a portable, non-obvious decision, permission boundary or done condition in its existing owner. | Keep diagnosis-only scope; separate a passing artifact from a finished task. |
| 2. Skill | A skill for a cohesive reusable result; a reference for a useful progression between results. | Diagnose a defect; coordinate a populated-data migration. |
| 3. Conditional reference expertise | Load specialist knowledge only at the decision that needs it. | Identity/addressability failures or stateful recovery proof. |
| 4. Deterministic helper | Write a bounded script only when existing tools do not meet the contract. | Reject an empty test receipt; clean up an owned process group. |
| 5. Evaluation or evidence | Keep the failure, comparison or acceptance case with evaluation until it supports a remedy. | Test whether a routing instruction improves finished work. |
| 6. Host, SIGIDI or project policy | Use the user/project surface, supported host configuration or SIGIDI tool for runtime choices. | Model selection, tool access, SIGIDI orchestration (`delegate_task`, `watch_pull_request`, `schedule_task`), team-required checks. |
| 7. Nowhere | Omit or retire redundant, obsolete or unsupported material after checking who reads it. | A copied spawn, polling or PR-watch recipe the host or SIGIDI already supplies. |

Class 0 hands execution to an existing capability; it does not drop the user's task or assume every model has that capability. Class 7 removes an unneeded obligation or resource. When capability is unknown, inspect or try it briefly instead of assuming guidance helps or is redundant. Capability does not supply access, domain facts, user intent or permission.

For any retained addition, name what fails without it, its owner and when it loads, the required result versus adaptable mechanics, and the evidence that would justify changing or retiring it. Keep ordinary task-specific choices in the assignment. A severe concrete failure can justify a narrow safeguard before comparative trials; label its broader benefit unproven. Revisit model-specific workarounds when the host or model changes or the failure stops occurring, without a fixed retest schedule.

## Invocation is part of the design

Choose whether the model must be able to reach the skill autonomously.

- **Model-reachable** spends always-loaded routing context but lets agents/other skills discover it.
- **Human-invoked** spends less model context but makes the human remember the skill.

Use the host/package's current invocation controls rather than copying volatile provider syntax here. Keep model-reachable descriptions discriminative enough to fire on real branches and reject adjacent ones.

A compatibility alias should not compete with its replacement. Narrow its description to explicit legacy-name use and keep the method at one owner.

## Do not confuse a skill with an agent definition

A skill owns a reusable semantic result/method. An assignment specifies what a delegated worker must accomplish now, including its context, authority, evidence, independence, completion boundary, and any useful runtime constraints. A provider-native **agent definition** is an optional reusable host artifact only when a persistent behavior/runtime delta cannot be expressed adequately through the assignment or native host controls. A workflow owns progression between results.

Good:

- use a native/general worker with a fresh read-only assignment for independent judgment;
- shape a generic worker for a README, architecture document, prompt, or handoff instead of creating a permanent writer agent type;
- add a provider-native definition when a recurring tool, permission, isolation, or persistent model constraint genuinely requires one on that host.

Bad:

- create an `akole-agent` definition that duplicates a skill's method;
- hardcode a skill name into every reviewer-like definition;
- maintain explorer/writer/reviewer/posture catalogues only to classify work before spawning it;
- create a new skill merely because a provider benefits from a named worker.

Before creating another public skill or agent definition, ask whether the missing behavior can live more coherently in the assignment or an existing native host control.

Use the provider's supported interface for installing, configuring, migrating, or verifying provider-native agent declarations. This skill owns their instruction text; the provider/host owns readiness and mutation.

## Treat the description as a pointer

The description decides whether the skill becomes reachable. State the owned result and genuinely distinct trigger branches. Name no other skill and list no exclusions: when two skills could claim a request, give the output one owner or fix the router. Do not summarize the procedure or pad one branch with synonyms.

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

For an explicitly requested portfolio review, compare public identities, owned results, routing collisions, the full instruction text (the same rule written in two skills is a collision to resolve by owner), compatibility aliases, cumulative always-loaded context, and representative end-to-end task paths. Structural counts and lexical overlap are leads, not quality or redundancy verdicts.

Look actively for no-ops, caches, sediment, copied callee procedure, competing outcomes, and compatibility surfaces that no longer earn public routing load.

## Support lifecycle decisions with evidence

When deciding whether to promote, narrow, fold, replace, or remove a skill, use real-use evidence where available: eligible opportunities, correct/incorrect selections, missed triggers, incremental value/cost, boundary failures, counterevidence, and coverage limits.

Do not infer usage or value from repository shape, raw invocation count, or one successful example. A proved structural defect can justify a change; missing historical evidence remains a gap, not a permanent veto.

## Verify the boundary that changed

Validate selection when routing changed, loading when disclosure changed, authority when action semantics changed, and behaviour when instructions changed materially. Package syntax checks prove structure only.

For material refactors, use the evolution audit in [editing agent text](editing-agent-text.md): retain, strengthen, relocate, replace, or retire. The goal is a better current skill, not preservation of its history.
