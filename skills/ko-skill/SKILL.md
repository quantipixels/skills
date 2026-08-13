---
name: ko-skill
description: Author or revise one portable agent skill. Focus on a narrow outcome, a clear invocation boundary, concise instructions, integrated metadata, and verified behavior.
---

# Ko Skill

Author or revise one portable skill whose process is predictable across runs. Let the target determine the output.

## 1. Set the boundary

Read repository instructions, host guidance, the target skill and resources, and relevant inventory and metadata. Establish the path, mutation authority, recurring outcome, triggers, exclusions, and invocation policy. Keep skill authoring or revision with `ko-skill` even when the target skill owns the runtime outcome. Revise that existing outcome owner instead of creating a competing skill. Create a skill only for a recurring decision, failure mode, or engineering outcome that documentation lookup does not solve.

Use the requested path. Ask one location question only when context does not identify it; use the host's personal skills directory when the user gives no preference. Choose implicit invocation only when an agent or skill must find the skill without an explicit request. Give each behavior branch one trigger.

For a behavior correction, define a realistic raw scenario that distinguishes the target contract from current behavior. Before editing, run it against the exact pre-fix candidate with a fresh producer from section 4 and record the failure or proof gap outside repository source. If current behavior passes, do not change it only to restate the contract; identify missing proof or another justified change.

**Good raw goal:**

```text
// GOOD: Neutral goal with an observable outcome
Watch PR #42 until review and CI are complete. Report only a state change or blocker.
```

**Bad raw goal:**

```text
// BAD: Leading goal that supplies the mechanism and expected behavior
Use the PR monitor skill because it must keep watching review and CI until both complete; confirm that behavior.
```

The distinction is evaluation independence: the good goal states what the user needs; the bad goal supplies what the test should discover.

## 2. Write the skill

Give the skill one narrow outcome and state the adjacent behavior it excludes. Treat user-supplied replacement wording or corrected constraints as the target contract. Preserve supplied structure and vocabulary unless host or repository requirements conflict. Reconcile conflicting owning rules and integration surfaces. Do not retain a policy the user leaves outside the skill. Identify required compatibility or integration additions and apply the remaining authoring rules only to author-owned text.

**Good contract change:**

```text
// GOOD: Requested change with its necessary repository guard
Remove default-prompt metadata and add the repository prohibition that prevents its return.
```

**Bad contract change:**

```text
// BAD: Unrequested policy expansion
Remove default-prompt metadata, then require every skill to include a usage tutorial.
```

The distinction is authority: the good change implements the request and required integration; the bad change adds unrelated policy.

For each author-owned change, identify its behavioral benefit. Retain it only when it improves invocation, agent understanding, decision or action accuracy, safety, verification, or outcome reliability. Apply this gate to instructions, descriptions, metadata, structure, examples, references, resources, and scripts. Do not add or revise content for editorial polish alone. When behaviorally stronger wording is less polished, keep the behaviorally stronger wording unless a host requirement or safety concern requires the change.

Follow the host's current schemas. Put discovery controls in the surfaces the host uses. Write a description for skill selection: front-load when to use the skill, its key use case, and its distinguishing trigger terms; state clear scope and boundaries; and exclude broad terms that do not distinguish it from adjacent skills. Describe the skill, outcome, and focus, not its stages.

**Good description:**

```text
// GOOD: Focused trigger and bounded outcome
Monitor a pull request through review and CI. Use when the user asks to monitor, watch, or babysit a PR.
```

**Bad description:**

```text
// BAD: Broad topics without a selection condition or bounded outcome
Help with pull requests, reviews, CI, GitHub, code, and developer workflows.
```

The distinction is selection precision: the good description says when to invoke the skill and what it delivers; the bad description only names related topics.

Use an example only when it passes the behavioral benefit gate. Use a good/bad pair when the contrast defines a boundary or prevents a recurring failure. Use a good-only example when one valid form is useful and invalid forms do not make one stable class. Put the example beside its owning rule, label it, and state the one distinction it demonstrates. Keep the rule authoritative; do not make the example an unannounced template or requirement.

Keep instructions required by every branch in `SKILL.md`; move substantial facts or branch guidance behind a direct pointer. Use ordered steps only when sequence matters.

When another specialist owns required work, state its required outcome, bounded starting context and status, and required result or proof. Treat supplied context as input, not proof. Keep the procedure with its owner.

Give each rule one owner based on the branches that need it. Keep its definition and caveats together, and merge repeats. Keep rationale, history, transcripts, and evidence in the owning report or reference. Run a final compression pass under the behavioral benefit gate. Use short, established terms. Add resources only when used and scripts only for repeated deterministic work.

## 3. Integrate it

Keep the name, boundary, triggers, exclusions, invocation policy, and other host-permitted metadata consistent. Use the bare skill name except where an ecosystem requires a prefix. Update packaged release metadata and any registry or catalog whose contract or inventory changes. Verify unchanged required surfaces without no-op edits. Preserve unrelated work.

For a provider-capable skill, propagate every applicable rule from the root provider-safety contract into that skill's runtime instructions. Preserve its local provider semantics unless an architecture decision changes the installation contract.

## 4. Verify it

Read every changed skill and resource. Check paths, placeholders, discovery controls, metadata, catalog, routing, and package surfaces directly. Run changed-script tests, applicable host or package checks, metadata and version checks, package dry run, and final diff check.

### Validate behavior in fresh sessions

Forward-test each material behavior change with the platform's supported subagent mechanism:

1. Pin the exact final candidate and define the intended-goal scenario plus each applicable boundary, unsafe-use, failure, or changed-state scenario. For stateful behavior, include the changed transition and a partial state that must remain open.
2. Run one producer per scenario in a fresh session with no inherited conversation turns. Load the exact candidate. Give the producer only the raw goal and minimum fixture and authority. Deny provider writes, inherited credentials, and repository mutation unless a disposable scenario authorizes them.
3. Run a separate reviewer in another fresh session. Give it the exact candidate contract, raw goal, fixture and authority record, and producer result. Withhold the expected answer, rationale, and verdict. Require `pass`, `fail`, or `insufficient evidence`, with candidate identity and supporting evidence.
4. Keep complete prompts, outputs, platform and model details, sandbox settings, and limitations outside repository source. Record only a concise proof summary in the owning plan or delivery report. Any candidate change invalidates affected proof and requires a rerun.

When the platform supports context-fork control, use its no-context setting, such as `fork_turns="none"`. Do not substitute a local CLI or isolated home directory for a platform-supported fresh subagent session. If the platform cannot provide one, report the proof gap.

Treat unexpected behavior as an ambiguous instruction or setup. Correct the smallest owning rule and rerun with fresh context.

Report the skill path, boundary, changed files, exact candidate identity, proof, direct structure and integration checks, and remaining limitations. Distinguish repository source, published, installed, and active states when they can differ. Install or publish externally only when the user requested it.
