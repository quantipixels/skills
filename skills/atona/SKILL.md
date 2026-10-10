---
name: atona
description: Atọ́nà. Produces one plan for building a settled need, with risks, premortem, rollout readiness, coordinated delivery and closure, and tracks the initiative's progress. Use when work spans steps, needs an order and risks, or needs coordinated delivery.
---

# Atọ́nà

**Output:** one current plan (working record, kind: plan) and the initiative's progress: what is built and proven, what remains, any decision waiting on the user. Update the existing plan rather than starting another.

**Needs:** a settled need: a spec, a clear brief, or a request whose purpose, user and success are known. If it is too thin, or the wanted result is something other than a plan, return to the caller and say what is missing. Missing or partly retrieved requirements are readiness gaps; a source summary does not confirm a requirement.

## Method

**Workflow** (`asoju`): before planning in a large or unfamiliar source (repository, long thread, many docs), have a reader write a record and plan from it.

Own the plan and the initiative's progress: keep one plan, record each returned result against it, and say what is ready next. When the plan needs the work cut into tickets, ask the caller for them and use the result; do not keep a second split. A plan, ticket set or handoff is an intermediate result when the user requested a build.

Read [initiative progression](references/initiative.md). It owns the plan (chat, issue or Markdown; a person can get an HTML page generated from it), delivery, continuity and closure, and points to the rest as needed: [premortem](references/premortem.md), [rollout readiness](references/rollout-readiness.md), [delivery tracking](references/delivery-tracking.md), [durable reconciliation](references/durable-reconciliation.md), and [managed initiative](references/managed-initiative.md) only when the workflow needs named readiness states. A planning-only request ends at the plan.

## Done

The plan states order, risks and readiness; each step the request covers is recorded as built and proven, or named as remaining with its reason.

## Return

Return the plan, what is built and proven, what remains, and any decision that waits on the user.
