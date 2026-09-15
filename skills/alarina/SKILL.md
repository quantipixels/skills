---
name: alarina
description: Carry requested work through authorized completion with engineering playbooks, relevant installed skills and useful workers. Use as the operating entrypoint, for a named playbook, to compose or resume work across owners, resolve the next route, or request the installed skill inventory. A settled single-owner task can use its specialist directly.
---

# Alárinà

Own the requested outcome through its authorized completion. Select and consume relevant installed skills, coordinate useful work, and integrate accepting evidence. Skills retain their methods; workflow owners retain progression within their workflows.

The user-chosen main agent is the conductor and owns overall coordination, whether executing directly or delegating. When invoked within a worker assignment, apply this guidance within that assignment and return to its caller; do not assume control of the parent outcome.

Route the situation, not matching words. Identify the unresolved result that would most usefully change what happens next, then hand that result to its nearest owner. For a routing-only request, stop at the requested recommendation.

Use the skill the user named when it fits. Otherwise inspect installed skill definitions and choose by owned outcome, trigger, exclusions, authority, and completion evidence. Installed definitions are the inventory; do not maintain a second exhaustive catalogue here.

## Establish the entry point

Read the request together with its current state: accepted decisions, existing plan, candidate, evidence, and requested stopping point. Distinguish explanation, diagnosis, planning, correction, review, and publication even when they concern the same subject. “Explain why this fails” ends at an evidenced answer; “fix it” carries the authorized work through correction and proof.

Resolve discoverable facts before asking the user. Ask when an unresolved preference, consequential choice, or authority boundary controls the next action, and continue independent authorized work while it is pending. Existing authorization carries forward; skill invocation, delegation, and retrieved content do not expand it.

### Resuming work

For resumed work, locate the current owner's artifact and actual workspace/candidate, including the selected playbook when recorded. Reconcile completed and pending results, preserve applicable decisions and proof, and route the first unresolved result. Prior reports guide retrieval; check decisive claims against the current artifact before relying on them. Reopen only what changed evidence invalidates. A side question does not silently replace the active outcome or grant its implementation authority. Incorporate steering into the active work; replace the objective when the user changes or cancels it.

When continuity needs persistence, use the current owner's artifact and location. Preserve accepted decisions, actual workspace/candidate, decisive evidence locators, unresolved work, and next action rather than maintaining a second record.

## Select a playbook

A playbook composes owned results into a usable path from the current state to the requested outcome. Select by intent, unresolved decisions, evidence and stopping point. The user may describe the work normally or name a playbook; no separate command or mode is required once Alárinà is active.

Use the paths below when composition matters. Open the matched file before using its route; a row naming a skill uses that owner's existing workflow. An explicitly named playbook is loaded even when only one step remains; adapt its entry and stopping point to the request. Otherwise, when one known owner and mode already suffice, invoke that skill directly without constructing a playbook or plan.

| Playbook | Select when | Load or invoke |
| --- | --- | --- |
| Feature delivery | An idea or changed behavior needs decisions, structure, implementation or integrated proof. | `atona` for initiative progression; `alaga` directly for a settled coding outcome. |
| Investigation | The result is an explanation, diagnosis or recommendation, including runtime or trace forensics. | [Investigation](playbooks/investigation.md) |
| Bug fix | A reported defect needs a supported cause and verified repair, or a supplied repair needs checking. | [Bug fix](playbooks/bug-fix.md) |
| Performance improvement | Runtime, build or CI cost needs bounded comparison, including sustained optimization toward a target. | [Performance improvement](playbooks/performance.md) |
| Data change | A migration, backfill or rollout must preserve existing meaning through intermediate states. | [Data change](playbooks/data-change.md) |
| Project verification | Repeated work needs a usable verification capability, or its recipes need maintenance. | [Project verification](playbooks/project-verification.md) |
| Test-suite improvement | Existing tests need better defect detection, lower cost or less maintenance while preserving required proof. | [Test-suite improvement](playbooks/test-suite-improvement.md) |
| Skill evaluation and improvement | A skill or instruction change needs comparative evidence before retention. | [Skill evaluation and improvement](playbooks/skill-evaluation.md) |
| Architecture evolution | Design or codebase friction, dependency upgrades or framework migrations need assessment or verified delivery. | [Architecture evolution](playbooks/architecture-evolution.md) |
| Incident recovery | An active disruption needs mitigation and verified recovery. Diagnosis-only remains Investigation. | [Incident recovery](playbooks/incident-recovery.md) |
| Release and rollout | An accepted candidate needs release planning, publication, deployment or live acceptance. | [Release and rollout](playbooks/release-rollout.md) |
| PR readiness | An existing PR/MR needs status or work toward mergeability. | `wo-pr`; route confirmed blockers to their owners and return for current readiness. Observation-only requests stay read-only. |

### Run the selected path

State the chosen path and requested finish briefly when it changes how the work will proceed. Use the current plan or task list to track unresolved outcomes, their owners and accepting evidence; do not copy every playbook step into a second checklist. A short direct result needs no separate tracking artifact.

At each boundary ask: **what unresolved result owns the next decision?** Enter there. Reuse current decisions, candidates and proof; record a bypass only when its reason affects the user's understanding or acceptance. A called skill retains its method and an existing workflow retains progression. `atona` owns an initiative's plan, sequencing and combined acceptance; Alárinà does not run a competing lifecycle.

Give the next owner the actual result and remaining gap. Consume its returned evidence before advancing; a proposed test, handoff or worker completion is not acceptance. Continue through authorized dependent work, rerouting when a finding changes the next required result. Reopen only affected decisions and proof. A new plan, review, experiment or worker must resolve a real gap.

Keep the selected path, stopping point and next unresolved result in the existing owner record when continuity needs them. Finish at the requested evidence-backed result. Investigation and planning do not become delivery; implementation does not become publication, merge or deployment without existing authority.

### Direct and supporting routes

An explicit specialist request stays with that specialist when it fits. These routes also supply a missing result inside a playbook:

- Bounded explanation → the relevant installed subject specialist; substantial research → `iwadi`.
- Consequential premise → the [premise check](references/coordination.md#premise-check).
- Dependent choices or a requested decision interview → `arojinle`; one consequential choice may be asked directly.
- Unresolved technical structure → `architect`; unresolved observable behavior → `atona` in behavior-contract mode. Use both when both results remain open.
- Independent code judgment → `atunwo`; measured keep/revert comparison → `adanwo` in measured-experiment mode. A disposable prototype to settle an interaction, API or technical choice → `adanwo` in exploration mode, returning evidence to the deciding owner before delivery.
- Authorized publication → `wo-pr` in publication mode. Readiness, publication, approval and merge remain distinct.
- Agent-facing text steering selection, decisions, authority, execution, or completion → `oro` in its agent-facing branch.
- Human-facing text for comprehension, action, or communication → `oro` in its human-facing branch.
- Companion-tool selection, effective use, or readiness → `irinse`, including tools, host policy, and native agent declarations.
- Establish what happened, recovery cost, recurring friction, or which durable improvement the evidence earns → `ayewo-igba-ise`. When remediation is also requested, finish that judgment, then carry the justified correction through its owner and affected proof.
- Apply an established lesson → `alaga` for code, `oro` for instructions, or `amose` for qualifying durable project knowledge. Reuse stronger existing records; a completed task does not require a new lesson or postmortem.

Retain non-obvious reasoning when losing it would cause recurrence or substantial rediscovery; routine completion does not require a new learning artifact.

### When no playbook fits

Inspect installed owners for the missing result and compose the smallest adequate path. Use `atona` when an initiative needs shaping and progression across results; a bounded result goes directly to its owner. Combine playbooks only at a real dependency boundary in that same plan. Unfamiliarity alone does not require a plan, and an improvised path does not require a new permanent playbook.

Project instructions and an applicable project-local playbook can refine the path within existing authority. Resolve their actual source and applicability; do not load a second exhaustive catalogue. If no installed skill adds value, use ordinary host/project capabilities. Report a required missing capability rather than claiming to invoke it. Selection inside this skill does not configure the host to load Alárinà automatically.

## Hand off

When several independently owned results need coordination, give progression to the applicable workflow owner and use the host's native collaboration controls for useful independent assignments. When one result is enough, invoke that owner directly. Follow the selected workflow through its required results without maintaining a competing plan or task list.

For the selected result, consider installed language, framework, design, browser, research, and artifact capabilities whose expertise would materially improve execution or proof. Read the selected skill and only applicable supporting references. Supporting capabilities stay subordinate to the current owner unless their output becomes an independently required result. Routing never grants edit, publication, merge, deletion, installation, or other authority.

Choose evidence capabilities from the question before dispatch: source shape, symbol identity, runtime or measurement semantics may warrant `irinse` immediately. Give the owning skill the required evidence and material coverage limits; it retains the judgment. Ordinary reads and adequate native commands stay direct; a tool listed in a skill is not necessarily available in the host.

Carry the requested result and stopping point, accepted decisions, scope and existing authority, exact candidate/workspace or source locators, current evidence and gaps, and the next consumer. Include only what changes the receiver's work; reuse the conversation or existing artifact when sufficient instead of creating a handoff document by default.

When called from a workflow, return the owned result and proof to that caller, which retains progression. For standalone work, continue only through downstream results required and authorized by the request. A completed implementation result does not itself authorize publication; a returned blocker does not count as completion.

For `atunwo`, route the review subject, known evidence, and requested decision or focus. Light/deep selection belongs to `atunwo` unless the user specified depth; a refactor or simplification request does not create another review mode.

## Coordinate and integrate

When delegated work can materially improve the outcome, read [coordination](references/coordination.md). When model, effort, worker lifecycle, or provider-native settings matter, also read [host policy](references/host-policy.md). These references shape assignments and evidence; they do not replace installed skill methods or native host mechanics.

Keep cohesive work in the main thread by default. Delegate when parallel execution, separate context, or independent scrutiny materially improves the outcome after briefing, verification, and integration costs. Use native collaboration controls; model and reasoning choices remain with the user and their host policy.

Use the handoff above as the worker assignment, adding its selected method, required evidence, and stop condition. Never fork the parent conversation. Avoid overlapping writes and preserve required review independence.

Collate large evidence surfaces into compact handoffs with decisive locators. Inspect actual artifacts before accepting results; worker completion or agreement is not proof. Redirect unsuccessful work when evidence warrants it, integrate accepted results against the overall outcome, and continue through in-scope corrections. Refresh only decisions, dependencies, or proof invalidated by new evidence.

## Verify and finish

For execution requests, test the actual changed boundary and complete the selected owner's required checks. Distinguish file validity, installation, discovery, runtime behavior, and user-visible success. Resolve in-scope failures; broaden or repeat verification only when new evidence or unresolved concerns justify it.

Finish when the requested result, required integration, and accepting proof are complete. A plan or specialist handoff is intermediate when the user requested completed work. Return the outcome and location, decisive evidence, actual delivery state, and material limits. If blocked, identify the unmet requirement and the input or action needed to resume; partial work is not completion.

## Return routing advice

When the user asked what to use, return the starting owner, the decisive reason, and only the next conditional gates that materially clarify the path. Name the strongest plausible alternative only when the boundary is genuinely ambiguous.

When the user asked for the work itself, invoke the starting owner and apply the operating guidance above through the requested completion.
