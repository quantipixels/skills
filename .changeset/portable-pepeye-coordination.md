---
"qp-skills": minor
---

Add an experimental `pepeye` skill for native subagent coordination. Keep four logical roles and worker preferences while leaving routing, planning, delivery, research, and review methods with their existing QP owners. No separate plugin, setup script, native agent files, or host configuration changes are required.

The design comparison used [astra-orchestrator](https://github.com/donvito/local-evals/blob/main/.agents/skills/astra-orchestrator/SKILL.md). This independently written skill retains selective delegation and Pepeye's existing worker defaults rather than adopting mandatory delegation or a separate tester role. The earlier runtime removal remains in effect; this adds only the portable coordination method.
