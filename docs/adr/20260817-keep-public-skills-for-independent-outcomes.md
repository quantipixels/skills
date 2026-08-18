# Keep public skills for independent outcomes

Status: Partially superseded by [Let Pare own simplification and cleanup](20260818-pare-owns-simplification-and-cleanup.md). QP Code Review no longer owns the independently useful maintainability-only outcome.

QP will keep a workflow as a user-reachable skill only when it owns an independently useful outcome and completion boundary. A method or specialist branch used within an existing owner will remain available as a conditional reference under that owner instead of adding another public route.

This retires `tdd`, `simplify`, and `skill-portfolio-audit` as standalone skills. Alaga owns test-first delivery and loads the TDD contract only when production behavior changes or the user explicitly requests test-first work. QP Code Review owns maintainability-only and broad review and loads the maintainability contract only for those modes. Ko Skill owns read-only portfolio audits and loads their state and capability checks only for that mode. Alarina names the selected mode after it selects one of these owners. `ro-wo` and specialists with distinct authority, artifact, lifecycle, or acceptance boundaries remain independent.

Keeping every method independently installable was rejected because it increased routing and release surface while the primary owner already required the method. Copying each method into its owner's main instructions was also rejected because it would increase default context. Conditional references preserve focused context at the cost of broader owner descriptions and removal of three public identifiers.

Ko Skill's later authority modes were superseded by [one shared single-skill workflow](20260818-unify-ko-skill-workflow.md); bounded portfolio audit remains a conditional read-only reference.
