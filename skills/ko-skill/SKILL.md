---
name: ko-skill
description: Author or revise one portable agent skill. Focus on a narrow outcome, a clear invocation boundary, concise instructions, integrated metadata, and verified behavior.
---

# Ko Skill

Author or revise one portable skill whose process is predictable across runs. Let the target determine the output.

## 1. Set the boundary

Read repository instructions, host guidance, the target skill and resources, and relevant inventory and metadata. Establish the path, mutation authority, recurring outcome, triggers, exclusions, and invocation policy. Revise the existing outcome owner. Create a skill only for a recurring decision, failure mode, or engineering outcome that documentation lookup does not solve.

Use the requested path. Ask one location question only when context does not identify it; use the host's personal skills directory when the user gives no preference. Choose implicit invocation only when an agent or skill must find the skill without an explicit request. Give each behavior branch one trigger.

## 2. Write the skill

Give the skill one narrow outcome and state the adjacent behavior it excludes. When the user supplies replacement wording, treat it as the target contract. Preserve its structure and vocabulary unless a host or repository requirement conflicts. Add only required compatibility or integration text, and identify each addition. Apply the remaining authoring rules only to author-owned text and required additions.

Follow the host's current schemas. Put discovery controls in the surfaces the host uses. Describe the skill, outcome, and focus, not its stages. Keep instructions required by every branch in `SKILL.md`; move substantial facts or branch guidance behind a direct pointer. Use ordered steps only when sequence matters and a compact directed acyclic graph only when dependencies remain unclear. Let the host own execution.

When another specialist owns required work, state its required outcome, bounded starting context and status, and required result or proof. Treat supplied context as input, not proof. Keep the procedure with its owner.

Choose the owning tier by branch reach. Give each rule one owning location, keep its definition, rules, and caveats together there, and merge repeats. Keep rationale, history, transcripts, and evidence in an owning report or reference. Run a compression pass: retain only text that changes behavior, supplies required knowledge, or enforces safety. Use a familiar, established leading word only when it removes identifiable repeated explanation without changing user-supplied wording. Use short, direct instructions and established terms. Add only used resources and scripts for repeated deterministic work.

## 3. Integrate it

Keep the name, boundary, triggers, exclusions, default prompt, and invocation policy consistent across required metadata. Use the bare skill name except where an ecosystem requires a prefix. Update packaged release metadata and any registry or catalog whose contract or inventory changes. Verify unchanged required surfaces without no-op edits. Preserve unrelated work.

## 4. Verify it

Read every changed skill and resource. Check paths, placeholders, discovery controls, metadata, and package surfaces. Run applicable validators, changed-script tests, metadata and version checks, repository checks, package dry run, and final diff check.

Forward-test a material or complex skill against the exact final candidate with fresh context and realistic raw input that hides the intended answer and rationale. Include one credible failed-use scenario. For stateful behavior, exercise the changed transition, including a partial answer when unanswered state must remain open.

Treat unexpected behavior as an ambiguous instruction or setup. Correct the smallest owning rule and rerun with fresh context. Rerun affected proof whenever the candidate changes after a green result.

Report the skill path, boundary, changed files, exact candidate identity, proof, and remaining limitations. Distinguish repository source, published, installed, and active states when they can differ. Install or publish externally only when the user requested it.
