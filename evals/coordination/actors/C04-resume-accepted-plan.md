# C04 — resume an accepted plan

**Observation:** executed outcome  
**Instruction source:** supplied candidate  
**Workspace:** a disposable copy of `evals/engineering/fixtures/migration/`

Use the supplied Alárinà candidate and installed-skill definitions available in this run.

Resume the accepted migration plan below. Steps 1 and 2 are complete and were accepted in the previous session. Continue from the first unfinished step without restarting discovery or replacing the plan unless direct evidence makes it unsafe.

When the run supplies an existing HTML plan, keep its identity and accepted decisions current in that same file. The fixture's `RESULT.md` is the execution evidence report, not a second plan.

1. [done] Inspect the v1 and v2 schema contract.
2. [done] Confirm that membership identity must come from the populated legacy join, not row order.
3. [next] Implement the migration in `migration.py`.
4. Add focused regression coverage for mapping, repeat execution, and unsupported versions.
5. Run the requested checks and record the mapping invariant, proof, and limits in `RESULT.md`.

Carry the remaining authorized work through completion. Do not publish or merge anything.
