---
name: scope-guard
description: Define or reinforce the boundaries of a coding task without implementing it. Use when the user needs explicit non-goals, protected behavior, or a clear trigger for approving scope expansion.
---

# Scope guard

Turn the requested outcome into a short, usable guard for the current task or agent. This is steering, not implementation authority or a second delivery procedure.

State the result to achieve, the behavior and areas that must remain unchanged, explicit exclusions, and evidence sufficient to show the intended change. Use the actual project and accepted decisions rather than generic quotas on files, lines, tests, or dependencies.

Challenge expansion when the proposed work changes an accepted behavior, interface, storage or compatibility boundary, permission, operational burden, or material risk/cost. New dependencies, infrastructure, abstractions, unrelated cleanup, or test frameworks need a current reason—not hypothetical future usefulness. A genuinely required expansion should expose the smallest consequential choice and its authority rather than hide behind a workaround.

Leave ordinary implementation choices and native mechanics to the executing agent. Do not require a separate approval or report for every reversible local choice already inside the guard.

Return the applicable boundaries and the event that requires reconsideration. Do not edit, commit, publish, or start delivery from a guard-only request. Use `alaga` when implementation is separately requested.
