# Module design

Use when module, interface, seam, adapter or dependency shape controls the architecture. Optimize leverage for callers and locality for maintainers, not abstraction count or folder shape.

## Deepen around owned knowledge

Apply information hiding: a deep module offers a small stable interface while owning substantial policy, state, lifecycle, failures and integration detail. Depth is reduced caller knowledge, not an implementation/interface line ratio or fewer public methods. Apply DRY to duplicated knowledge and YAGNI to speculative variation.

Use the deletion test. A layer is shallow when removing it loses no required responsibility and moves no complexity or policy. Keep a small module or single-adapter seam when it owns a real trust, authorization, protocol, compatibility, lifecycle, migration or operational boundary. Directory conventions may expose or enforce boundaries; they do not create depth.

Place seams only where isolation or variation has a real owner. Two production/test adapters are sufficient evidence, not a requirement. Keep internal seams private. Apply Liskov substitution to adapters and test doubles: preserve caller preconditions, guarantees, errors and effects; a matching signature does not establish fidelity.

Callers and durable behavioral tests should normally use the same external interface. Use command/query separation to distinguish observation and mutation while preserving atomic read-modify-write and useful command results. Internal tests may protect stable private invariants without widening the interface. Remove old tests only when a new proof owner fully subsumes their material failure signal.

Classify dependencies only when it changes the seam or proof:

- in-process decisions may use a functional core inside the same deep module; pure-core proof does not establish the shell;
- a faithful local substitute may remain behind a private seam;
- an owned remote process may warrant a narrow transport/lifecycle boundary; and
- a true external dependency warrants isolation of its trust, failure, compatibility and translation contract.

No category mechanically requires a port or public interface.

## Represent and defend invariants

Use the language's native parse-don't-validate idiom when a representation can retain an established invariant and remove repeated checks or invalid combinations. Preserve lifecycle and wire compatibility. Parsing does not freeze mutable permissions, balances or concurrent state, and untrusted input still needs boundary validation.

At a security-sensitive effect, challenge omitted or conflicting configuration, unsafe defaults, invalid limits/enums and swapped same-type arguments. Prefer fail-closed enforcement at the owning boundary. Documentation is not enforcement; in review these are hypotheses under `atunwo`, not automatic findings.

## Compare genuinely open designs

When consequential uncertainty leaves several credible shapes, use bounded set-based design: compare caller usage, hidden responsibilities, failure semantics, depth/locality, migration/reversibility, compatibility and proof burden; eliminate alternatives with discriminating evidence. A settled design needs no reopening, fixed candidate count, agent tournament or arbitrary adapter quota. Use `adanwo` only when an empirical experiment must decide.

For a material candidate, show a compact sketch with: responsibility and owner; caller interface/example; hidden policy, state and failures; dependencies/adapters; critical invariants and proof boundary; migration trade-off/strongest alternative; and unresolved gaps. Omit fields that do not affect the question.
