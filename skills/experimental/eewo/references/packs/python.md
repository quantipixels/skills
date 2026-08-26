# Python starter guard pack

These seeds emphasize language traps that can produce incorrect behavior.

## `python.defaults.mutable-shared-state`

- Kind: prohibition
- Applies: function parameters whose default object is mutable.
- Invariant: independent calls must not accidentally share mutable call state.
- Do not: use a mutable object such as `{}` or `[]` as a default when each call is expected to receive fresh state.
- Failure mechanism: Python evaluates default values once at function definition time, so later calls reuse the mutated object.
- Safe paths: use `None`/a sentinel and create the object inside the function; retain a mutable default only when deliberate shared caching/state is explicitly part of the contract.
- Source: official Python Programming FAQ.

## `python.closure.loop-late-binding`

- Kind: prohibition
- Applies: closures/functions created in loops when each function is expected to remember that iteration's value.
- Invariant: each generated callable must capture the intended iteration value.
- Do not: close over the changing loop variable and assume definition-time capture.
- Failure mechanism: the free variable is looked up when the callable runs, so all closures can observe the loop's final/current value.
- Safe paths: bind the value as a default argument, create a factory scope, or pass the value explicitly.
- Source: official Python Programming FAQ.

## `python.exceptions.bare-catch`

- Kind: prohibition
- Applies: ordinary application exception handling.
- Invariant: handlers must not hide interrupts/system-exit signals or unrelated defects.
- Do not: use bare `except:` for routine error handling, and do not wrap substantially more code than the expected exception source requires.
- Failure mechanism: bare `except:` catches `BaseException` subclasses including `KeyboardInterrupt` and `SystemExit`; broad try blocks can misclassify defects from unrelated statements.
- Safe paths: catch the narrow expected exception, keep `try` small, use `finally` for unconditional cleanup, or re-raise after logging when a true catch-all boundary is required.
- Source: PEP 8.

## Mining note

`skills.sh` exposes useful community corpora such as `wshobson/agents` `python-anti-patterns`; use them to discover candidates, then validate language facts against Python docs/PEPs and move cheaply enforceable cases to Ruff/type-checking where possible.
