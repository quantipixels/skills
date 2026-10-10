---
name: ibeere
description: Interviews the user to produce settled choices when several consequential decisions depend on each other. Use when purpose, beneficiaries, success or trade-offs are unsettled, branch into dependent decisions, or the user asks to be interviewed.
---

# Ìbéèrè

**Output:** an interview result: the confirmed decisions, and what is still open.

**Needs:** several consequential, dependent choices the user owns. A single understood choice, a complete brief or settled constraints are context, not interview targets. If the inputs are missing, or the request is not this job, return to the caller and say what is missing.

## Method

An articulated mechanism is not an established desire. Clarify the need, beneficiary, observable success and consequential trade-offs only where they remain unsettled. Do not manufacture alternatives or re-interview settled choices.

Map only the unsettled choices as a **decision tree**: each decision branches into the decisions that depend on it. Work in **rounds**. The **frontier** is every decision whose prerequisites are settled. Ask the whole answerable frontier in one round, then wait. Never ask a question whose answer depends on another open question in the same round, including "if you choose..." questions or options tucked into a summary. Recompute the frontier from confirmed answers before the next round; answers can create, remove, merge, split or reframe branches. Question cards and the rubric for close alternatives are in [interview format](references/interview-format.md).

- Finding facts is your job, never the user's. Resolve bounded facts directly; ask the independent frontier questions while a fact is being found. For substantive research, return the need to the caller. If third-party input controls part of the frontier, name it and continue with the rest. Drafting a message is not sending, and a reply is not approval.
- When the user cannot judge abstract alternatives, make the choice concrete with a small example and resume from their reaction. Keep proposed interpretations tentative until confirmed.
- Do not silently turn a recommendation, generated option or grade into a confirmed decision. The user owns each decision.
- Keep questions in the conversation. For a plan or proposed direction, reuse the plan that exists. Use a visual comparison (ask `fihanmi`) only when it clearly helps resolve the choices, and keep it current.
- Before declaring the frontier empty, challenge the tree for consequential assumptions, missing branches, contradictory decisions and dependencies never made explicit.

## Done

No unresolved material branch remains, any view in use is current, and the user's answers confirm the affected decisions. Ask for a consolidated confirmation only when a material interpretation or conflict remains. An answer that never came stays pending; never infer it from silence.

## Return

Return one state to the caller, which resumes at its first unresolved point:

- `complete`: confirmed decisions, material assumptions and evidence, alternatives or criteria that constrained a choice, deferrals with re-entry conditions, and the first unresolved action.
- `needs_decision`: only the questions answerable now. Dependent branches stay pending; the caller relays this frontier as is.
- `blocked`: the missing input, evidence or go-ahead, and what would unblock it.
- `failed`: what was attempted and the decisive failure.

Report newly found domain, factual or technical gaps. This skill produces no spec, plan or build.
