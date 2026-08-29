# Bundled script boundary

Read only after capability placement still leaves executable code as the smallest credible surface. A script is not justified merely because it is short, useful, tested, or deterministic.

## Runtime script gates

Keep or add an internal skill script only when the applicable gates hold:

1. **Natural owner** — guidance, the capable agent, project/provider/framework tooling, or a focused mature library cannot carry the result as well.
2. **Owned result** — the skill genuinely owns the mechanical result rather than using code to imitate another owner.
3. **Demonstrated need** — recurrence, correctness, race/atomicity, portability, machine-consumer, or transformation evidence warrants packaging.
4. **Deterministic seam** — the operation has a bounded mechanical contract such as `given X, produce Y` or `publish Y iff identity X still holds`.
5. **Judgment stays outside** — routing, recommendation, architecture, acceptance, authorization, and recovery choice remain with the semantic owner/agent.
6. **Leverage** — packaging materially improves correctness/reuse over an ordinary visible/native operation.
7. **State discipline** — persistent state, locks, retries, schemas, or daemons exist only for the observed need.
8. **Truth boundary** — repository/provider/runtime truth remains authoritative; the script does not maintain a parallel semantic model.
9. **Consumer** — a real machine/human boundary uses the exact result the script emits.
10. **Proof** — deterministic tests can falsify the retained seam.

Before finalizing, strip every responsibility that the agent/native/project/tool owner can safely perform. Prefer pure transforms and exact mutation kernels over workflow-shaped CLIs.

Examples of seams that can justify code: lock-held compare-and-swap publication, exact compiler/validator transformations, or another externally consumed deterministic artifact. Provider normalization for model consumption, ordinary Git/filesystem orchestration, search/filter wrappers, and lifecycle checklists normally do not.

## Human-facing entrypoints

Evaluate a public install/bootstrap/uninstall/helper wrapper separately. It may be justified by invocation leverage even when native tools own its internals. Keep it transparent, conservative, portable enough for its advertised use, free of parallel semantic state, and small enough to audit as an entrypoint rather than an engine.

## Disposition

For internal runtime code return `KEEP | SHRINK | REPLACE_WITH_GUIDANCE | REPLACE_WITH_NATIVE | REPLACE_WITH_LIBRARY | MOVE_TO_OWNER | PROMOTE_TO_ENGINE | REMOVE | NEEDS_EVIDENCE`.

For public convenience wrappers return `KEEP ENTRYPOINT | SHRINK ENTRYPOINT | REPLACE_WITH_COMMAND | REMOVE | NEEDS_EVIDENCE`.

For `KEEP`/`SHRINK`, name the exact deterministic seam and what moved back to natural owners.
