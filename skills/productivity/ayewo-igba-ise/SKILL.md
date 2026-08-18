---
name: ayewo-igba-ise
description: Analyze one coding-agent session, rollout, or bounded multi-session corpus from evidence. Use when a user asks why an agent failed, what caused friction or waste, which patterns repeat across sessions, or which durable improvements the evidence justifies.
---

# Àyẹ̀wò Ìgbà Iṣẹ́

Produce one evidence-backed retrospective of a completed, abandoned, or disputed coding-agent session or bounded corpus. Keep code review, feature delivery, and skill authoring with their owning skills.

## 1. Pin the evidence unit

Resolve whether the unit is one session or a corpus. For one session, pin its record, repository, candidate revisions, time span, and requested output. For a corpus, pin the time range, session roots, repositories, inclusion and exclusion rules, selection method, and requested output before drawing conclusions.

Create a coverage ledger for every explicit question and requested deliverable. Map each item to its evidence, intended output section, and current status: `answered`, `evidence gap`, or `deferred`. Reconcile the ledger before completion; an executive summary, project matrix, or repeated-pattern aggregate does not replace an unanswered item.

Distinguish a user task, root session, resumed or copied history, rollout file, and subagent rollout. Do not treat rollout count as task count, first-to-last span as labour time, or repeated transcript content as independent evidence. Inventory the corpus before sampling. For a large corpus, use deterministic extraction for counts and metadata, then read the smallest representative and risk-weighted sample that can answer the question. Record the population, sample, exclusions, and evidence gaps.

Read the evidence needed to reconstruct the user contract, agent actions, results, and final state. Do not treat hidden reasoning or a later summary as evidence.

Record the instructions and skill versions active during each analyzed session when its record provides them. For reported skill use, distinguish mention, read, selection, invocation, result, mutation, installation, activation, and handoff; do not infer one state from another. Treat current copies as comparison context, not proof of what the agent saw. Use pinned durable facts from repository instructions, current skills, diffs, artifacts, or verified external state to assess forward-looking improvements, but do not use later evidence to change a historical verdict. Keep repository and external state read-only unless the user separately authorizes a report artifact or correction.

A durable fact must have a pinned source, remain applicable to the current owner, and support behavior beyond the incident.

## 2. Reconstruct contracts and causal records

For one session, reconstruct its contract revisions and timeline. For a corpus, reconstruct bounded causal records for the sampled sessions; do not invent one global timeline or infer the same contract across different tasks. Include contrasting successful or uneventful records when they can disprove a claimed pattern. Do not use a later requirement to condemn an earlier compliant action.

Pin the first material divergence between the then-current user contract and agent conduct. Verify material action and completion claims against the referenced candidate or external state when available.

Call a pattern repeated only when the same material mechanism appears in at least two independent root sessions. Report its supporting records, eligible denominator when known, counterevidence, and coverage limit. Keep a single incident labeled as an incident even when it produced many subagent rollouts or repeated recovery attempts.

## 3. Explain the friction and failure chain

Identify the frictions that made correct progress harder or recovery more expensive. Distinguish agent execution error from structural friction in instructions, ownership, sequencing, evidence gates, tools, or environment. Rank only evidence-backed friction by impact, likelihood of recurrence, and leverage outside the analyzed evidence unit.

For each material failure, compare expected and actual conduct, cite the evidence and impact, and place it in the causal chain. Separate the root divergence from downstream symptoms and repeated recovery work.

Classify each cause as a missing rule, ambiguous rule, violation of a clear rule, tool or environment failure, evidence gap, or reasonable decision that only later became obsolete. Do not propose a new rule for every mistake. When a clear rule already existed, strengthen it only if the session shows that its trigger or gate was too easy to miss.

Assess correctness, decision quality, and efficiency. Report wasted or repeated work only when the evidence proves it, and explain its cause and impact. Normalize corpus counts to the pinned unit and report the numerator, denominator, and exclusions when they matter. Use counts and elapsed time only when the record supports them.

## 4. Recommend durable improvements and report

For each warranted recommendation, state its owning surface, the durable fact that makes it applicable beyond the session, the smallest behavioral change, expected benefit, risk, and required proof. Prefer clarifying, merging, moving, or removing instructions over adding another rule. Return no change when no durable structural gap exists.

Use `ko-skill` to assess any recommendation that may create or change a skill and to apply authorized changes. Route an evidenced codebase-simplification recommendation to Pare `audit` or `review`. Use broad QP Code Review when a source-code correction requires a defect verdict.

For one session, return the executive verdict, evidence boundary, timeline and causal chain, ranked frictions, effective recovery, recommendation assessment, material rejected recommendations, and residual limits.

For a corpus, return the executive verdict, population and unit definitions, inventory and sampling ledger, repeated-pattern matrix with independent supporting records and counterevidence, representative causal chains, ranked frictions, effective recoveries, recommendation assessment, rejected recommendations, and residual limits. When the corpus spans projects, include one dossier for every normalized project in the population, not only sampled or problematic projects. Each dossier must state its aliases and evidence coverage; outcomes and verified current state; user actions and decisions; effective work; failures, inefficiencies, and gaps; applicable lessons; recommendations and no-change findings; counterevidence; and limits. Classify each durable decision or lesson as implemented, still applicable, superseded, or unresolved, and name its owning project document, skill, test, or workflow when known. Link aggregate patterns to their project dossiers; do not use the aggregate to replace project-level analysis. When skill corrections are authorized, distinguish source, installed, published, and active states.
