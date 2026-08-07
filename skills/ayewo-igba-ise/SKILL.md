---
name: ayewo-igba-ise
description: Analyze one coding-agent session or rollout from evidence. Use when a user asks why an agent failed, what caused friction or waste, or which durable improvements the session justifies.
---

# Àyẹ̀wò Ìgbà Iṣẹ́

Produce one evidence-backed retrospective of a completed, abandoned, or disputed coding-agent session. Keep code review, feature delivery, and skill authoring with their owning skills.

## 1. Pin the record

Resolve the exact session, repository, candidate revisions, time span, and requested output. Read the evidence needed to reconstruct the user contract, agent actions, results, and final state. Do not treat hidden reasoning or a later summary as evidence.

Record the instructions and skill versions active during the session when the record provides them. Treat current copies as comparison context, not proof of what the agent saw. Use pinned durable facts from repository instructions, current skills, diffs, artifacts, or verified external state to assess forward-looking improvements, but do not use later evidence to change the historical verdict. Keep repository and external state read-only unless the user separately authorizes a report artifact or correction.

A durable fact must have a pinned source, remain applicable to the current owner, and support behavior beyond the incident.

## 2. Reconstruct the contract and timeline

Reconstruct the contract revisions and timeline. Do not use a later requirement to condemn an earlier compliant action.

Pin the first material divergence between the then-current user contract and agent conduct. Verify material action and completion claims against the referenced candidate or external state when available.

## 3. Explain the friction and failure chain

Identify the frictions that made correct progress harder or recovery more expensive. Distinguish agent execution error from structural friction in instructions, ownership, sequencing, evidence gates, tools, or environment. Rank only evidence-backed friction by impact, likelihood of recurrence, and leverage outside this session.

For each material failure, compare expected and actual conduct, cite the evidence and impact, and place it in the causal chain. Separate the root divergence from downstream symptoms and repeated recovery work.

Classify each cause as a missing rule, ambiguous rule, violation of a clear rule, tool or environment failure, evidence gap, or reasonable decision that only later became obsolete. Do not propose a new rule for every mistake. When a clear rule already existed, strengthen it only if the session shows that its trigger or gate was too easy to miss.

Assess correctness, decision quality, and efficiency. Report wasted or repeated work only when the record proves it, and explain its cause and impact. Use counts and elapsed time only when the record supports them.

## 4. Recommend durable improvements and report

For each warranted recommendation, state its owning surface, the durable fact that makes it applicable beyond the session, the smallest behavioral change, expected benefit, risk, and required proof. Prefer clarifying, merging, moving, or removing instructions over adding another rule. Return no change when no durable structural gap exists.

Use `ko-skill` to assess any recommendation that may create or change a skill and to apply authorized changes. For every authorized correction, use `simplify` to review the exact candidate before finalizing it.

Return the executive verdict, evidence boundary, timeline and causal chain, ranked frictions, effective recovery, recommendation assessment, material rejected recommendations, and residual limits. When skill corrections are authorized, distinguish source, installed, published, and active states.
