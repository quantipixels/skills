---
name: architect
description: "Design, survey or review technical boundaries, interfaces and evolution at the smallest sufficient scale. Excludes implementation and initiative management."
---

# Architect

Resolve the structural question for confirmed purpose, domain and quality drivers. Survey finds evidence-backed friction; design chooses structure; review judges a supplied candidate read-only. Sound current design can suffice. Do not require an architecture packet for a bounded question.

Inspect sources that can change the decision: consumers, contracts, state ownership, runtime constraints, dependencies and relevant history. Implementation demonstrates current behavior, not automatic intent. Resolve symbols and coverage where identity matters. [Amose](../amose/SKILL.md) owns domain meaning, [atona](../atona/SKILL.md) consequential intent and [iwadi](../iwadi/SKILL.md) substantive external evidence.

Read [module design](references/module-design.md) when caller knowledge, representation, seams or dependencies control the result. Prefer deep interfaces owning policy, lifecycle and failure detail. Repeated procedural reminders can indicate missing ownership; a forwarding wrapper is not the remedy.

For migrations, technology replacement or agent-facing products read [evolution](references/evolution.md). Compare retaining the current design against credible alternatives using actual constraints. Age, novelty and file counts do not establish improvement.

Begin a survey with the affected subsystem or bounded change history. Treat churn, cycles, fan-out and complexity as leads; substantiate caller burden, change amplification or ownership failure and seek counterevidence. Do not equal-weight an entire repository by default.

Keep domain intent, enforcement and usage explanation distinct. Prefer an existing type/API/constraint/check for a mechanical obligation when it covers the boundary at acceptable cost. Preserve semantics, compatibility and remaining judgment. A type does not freeze mutable authorization or concurrent state.

Return the smallest useful result: responsibility, interface, ownership, decisive trade-off, strongest alternative, migration/recovery implications and required evidence. Separate observations, estimates and untested hypotheses. A survey need not design a fix; design does not authorize implementation; a short spike does not prove long-term maintainability.
