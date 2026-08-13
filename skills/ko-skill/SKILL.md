---
name: ko-skill
description: Author or revise one portable agent skill. Focus on a narrow outcome, a clear invocation boundary, concise instructions, integrated metadata, and verified behavior.
---

# Ko Skill

Author or revise one portable skill whose process is predictable across runs. Let the target determine the output.

## 1. Set the boundary

Read repository instructions, host guidance, the target skill and resources, and relevant inventory and metadata. Establish the path, mutation authority, recurring outcome, triggers, exclusions, and invocation policy. Keep skill authoring or revision with `ko-skill` even when the target skill owns the runtime outcome. Revise that existing outcome owner instead of creating a competing skill. Create a skill only for a recurring decision, failure mode, or engineering outcome that documentation lookup does not solve.

Use the requested path. Ask one location question only when context does not identify it; use the host's personal skills directory when the user gives no preference. Choose implicit invocation only when an agent or skill must find the skill without an explicit request. Give each behavior branch one trigger.

For a skill behavior correction, first define a realistic raw scenario that distinguishes the target contract from current behavior. Pin and exercise the pre-fix candidate in a fresh headless session before making the fix. Record the observed failure or evidence gap outside repository source. When current behavior passes, do not change it only to restate the contract; identify missing proof or another justified change. When no suitable runner is available, report that proof gap. Do not add a prompt eval suite or behavioral test to this repository.

Good raw evaluation: `Watch PR #42 until review and CI are complete. Report only a state change or a blocker.` Bad leading evaluation: `Use the PR monitor skill because it must keep watching review and CI until both complete; confirm that behavior.` The good input states the user's need without supplying the owner, intended answer, or rationale.

## 2. Write the skill

Give the skill one narrow outcome and state the adjacent behavior it excludes. When the user supplies replacement wording or a corrected constraint, treat it as the target contract. Preserve supplied structure and vocabulary unless a host or repository requirement conflicts. Locate and reconcile every conflicting owning rule and required integration surface. Do not preserve or introduce a policy that the user explicitly leaves outside the skill. Add only required compatibility or integration text, and identify each addition. Apply the remaining authoring rules only to author-owned text and required additions.

Apply YAGNI ("You Aren't Gonna Need It") to skill contents: add only behavior-bearing instructions and resources.

For each author-owned change, identify its behavioral benefit. Retain it only when it improves invocation, agent understanding, decision or action accuracy, safety, verification, or outcome reliability. Apply this gate to instructions, descriptions, metadata, structure, examples, references, resources, and scripts. Do not add or revise content for editorial polish alone. When behaviorally stronger wording is less polished, keep the behaviorally stronger wording unless a host requirement or safety concern requires the change.

Follow the host's current schemas. Put discovery controls in the surfaces the host uses. Write a description for skill selection: front-load when to use the skill, its key use case, and its distinguishing trigger terms; state clear scope and boundaries; and exclude broad terms that do not distinguish it from adjacent skills. Describe the skill, outcome, and focus, not its stages.

Good description: `Monitor a pull request through review and CI. Use when user ask to monitor, watch, or babysit the PR`. Bad description: `Help with pull requests, reviews, CI, GitHub, code, and developer workflows.` The bad description lists broad topics without a selection condition, bounded action, or monitoring outcome.

Use an example only when it passes the behavioral benefit gate. Use a good/bad pair when the contrast defines a boundary or prevents a recurring failure. Use a good-only example when one valid form is useful and invalid forms do not make one stable class. Put the example beside its owning rule, label it, and state the one distinction it demonstrates. Keep the rule authoritative; do not make the example an unannounced template or requirement.

Keep instructions required by every branch in `SKILL.md`; move substantial facts or branch guidance behind a direct pointer. Use ordered steps only when sequence matters and a compact directed acyclic graph only when dependencies remain unclear. Let the host own execution.

When another specialist owns required work, state its required outcome, bounded starting context and status, and required result or proof. Treat supplied context as input, not proof. Keep the procedure with its owner.

Choose the owning tier by branch reach. Give each rule one owning location, keep its definition, rules, and caveats together there, and merge repeats. Keep rationale, history, transcripts, and evidence in an owning report or reference. Run a final compression pass under the behavioral benefit gate and remove repetition. Use a familiar, established leading word only when it removes identifiable repeated explanation without changing user-supplied wording. Use short, direct instructions and established terms. Add only used resources and scripts for repeated deterministic work.

## 3. Integrate it

Keep the name, boundary, triggers, exclusions, default prompt, and invocation policy consistent across required metadata. Use the bare skill name except where an ecosystem requires a prefix. Update packaged release metadata and any registry or catalog whose contract or inventory changes. Verify unchanged required surfaces without no-op edits. Preserve unrelated work.

For a provider-capable skill, apply the root provider-safety contract to the changed behavior and keep each runtime-critical rule in the independently installed skill. Keep provider execution local. Do not replace local provider semantics with a shared runtime unless an architecture decision explicitly changes the installation contract.

## 4. Verify it

Read every changed skill and resource. Check paths, placeholders, discovery controls, metadata, catalog, routing, and package surfaces directly. Run changed-script tests, applicable host or package checks, metadata and version checks, package dry run, and final diff check.

Forward-test a material or complex skill against the exact final source candidate in a fresh headless session. Use realistic raw input that hides the intended owner, answer, and rationale. Run the intended goal plus independent fresh sessions for each applicable adjacent boundary, unsafe use, failure, and changed-state scenario. For stateful behavior, exercise the changed transition and a partial state that must remain open.

Deny provider writes, inherited credentials, and repository mutation unless a disposable scenario explicitly authorizes that effect. Have a separate independent session judge the results against the current skill contract. Keep full prompts, runner and model versions, session output, sandbox details, and limitations outside repository source. Put only a concise proof summary in the owning plan or delivery report. Affected proof becomes stale after any candidate change.

Treat unexpected behavior as an ambiguous instruction or setup. Correct the smallest owning rule and rerun with fresh context. Rerun affected proof whenever the candidate changes after a green result.

Existing deterministic script tests can remain while their owning source behavior remains, but do not add cases. Report the skill path, boundary, changed files, exact candidate identity, proof, direct structure and integration checks, and remaining limitations. Distinguish repository source, published, installed, and active states when they can differ. Install or publish externally only when the user requested it.
