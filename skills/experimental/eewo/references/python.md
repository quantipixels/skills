# Python guards

Curated from Python documentation/PEPs and candidate skills in `wshobson/agents`, including `python-anti-patterns`, error handling, resource management, type safety, resilience, and asyncio guidance.

## Language state and control flow

### `python.defaults.mutable-shared-state` (`BLOCK`)

**Avoid:** Mutable defaults such as `[]`, `{}`, or a mutable instance when each call expects fresh state.

**Why:** Defaults are evaluated once at function definition and reused across calls.

**Prefer:** `None`/a sentinel and create the value inside; retain a mutable default only for deliberate shared state.

**Source:** [Python FAQ](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects).

### `python.defaults.dynamic-value-frozen` (`BLOCK`)

**Avoid:** `datetime.now()`, random values, environment reads, or mutable configuration as defaults when call-time evaluation is intended.

**Why:** The expression runs at definition/import time, not per call.

**Prefer:** A sentinel/factory evaluated inside the function.

**Source:** [Python function definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions).

### `python.closure.loop-late-binding` (`BLOCK`)

**Avoid:** Creating closures in a loop and assuming each captures that iteration's value.

**Why:** Free variables are resolved when the callable runs, so every closure may see the final value.

**Prefer:** Bind a default argument, create a factory scope, or pass the value explicitly.

**Source:** [Python FAQ](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result).

### `python.identity.value-comparison` (`BLOCK`)

**Avoid:** `is`/`is not` for strings, numbers, enums not defined by identity, or ordinary value objects.

**Why:** Identity is an implementation/lifetime property, not value equality.

**Prefer:** `==`/`!=`; reserve identity for `None` and deliberate singleton sentinels.

**Source:** [PEP 8 programming recommendations](https://peps.python.org/pep-0008/#programming-recommendations).

### `python.assert.runtime-validation` (`BLOCK`)

**Avoid:** `assert` for user input, authorization, protocol validation, or required production invariants.

**Why:** Assertions can be removed with optimization and raise the wrong contract-level error.

**Prefer:** Explicit validation and exceptions; use `assert` for internal developer invariants only.

**Source:** [Python `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement).

### `python.finally.control-flow` (`BLOCK`)

**Avoid:** `return`, `break`, or `continue` in `finally` when it can suppress an active exception.

**Why:** The original failure disappears and the function reports a different result.

**Prefer:** Cleanup only in `finally`; decide return/control flow after the protected block.

**Source:** [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations).

## Exceptions and resources

### `python.exception.bare-or-baseexception` (`BLOCK`)

**Avoid:** Bare `except:` or routine catching of `BaseException`.

**Why:** It captures `KeyboardInterrupt`, `SystemExit`, and other process-control exceptions.

**Prefer:** Catch the narrow expected exception; reserve a catch-all for a true top-level boundary that re-raises or terminates safely.

**Source:** [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations).

### `python.exception.swallowed` (`BLOCK`)

**Avoid:** `except ...: pass`, unexplained `None`/default fallback, or logging-and-continuing after stateful work fails.

**Why:** Callers receive false success and partial state can survive.

**Prefer:** Propagate, translate with chaining (`raise ... from ...`), aggregate, or explicitly mark best-effort loss.

**Source:** [Python exceptions](https://docs.python.org/3/tutorial/errors.html).

### `python.exception.overbroad-try` (`BLOCK`)

**Avoid:** A large `try` that catches an exception type several unrelated statements can raise.

**Why:** A defect from the wrong statement is misclassified as an expected failure.

**Prefer:** Keep `try` around the exact operation; use `else` for success-only continuation.

**Source:** [PEP 8](https://peps.python.org/pep-0008/#programming-recommendations).

### `python.resource.not-context-managed` (`BLOCK`)

**Avoid:** Files, locks, sockets, DB cursors/connections, temporary resources, or transactions without a deterministic context/lifecycle owner.

**Why:** Exceptions and early returns leak resources.

**Prefer:** `with`/`async with`, `contextlib`, or explicit `try/finally`.

**Source:** [Python `with`](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement).

### `python.cleanup.del-critical` (`BLOCK`)

**Avoid:** Depending on `__del__` for critical cleanup or externally visible correctness.

**Why:** Finalization timing/order is nondeterministic and cycles/shutdown complicate execution.

**Prefer:** Context managers, explicit `close`, and `weakref.finalize` only as defensive backup.

**Source:** [Python data model `object.__del__`](https://docs.python.org/3/reference/datamodel.html#object.__del__).

## Async and concurrency

### `python.async.blocking-event-loop` (`BLOCK`)

**Avoid:** `time.sleep`, blocking requests, filesystem/database calls, or CPU-heavy work directly in an asyncio task.

**Why:** The event-loop thread cannot run other tasks.

**Prefer:** Async-native APIs, `asyncio.to_thread`, an executor, or a separate process for CPU work.

**Source:** [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code).

### `python.async.unawaited-coroutine` (`BLOCK`)

**Avoid:** Calling a coroutine and discarding the returned coroutine object.

**Why:** The body never executes and Python may only emit a warning later.

**Prefer:** `await` it or deliberately schedule it with an owned task.

**Source:** [asyncio: detecting never-awaited coroutines](https://docs.python.org/3/library/asyncio-dev.html#detect-never-awaited-coroutines).

### `python.async.unowned-task` (`BLOCK`)

**Avoid:** Fire-and-forget `create_task` without retaining a reference and observing failure/lifecycle.

**Why:** Tasks may be garbage-collected, fail silently, or outlive their request.

**Prefer:** `TaskGroup`, a supervised task set, or an explicit background-service owner.

**Sources:** [`asyncio.create_task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task), [`TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#task-groups).

### `python.async.unbounded-gather` (`BLOCK`)

**Avoid:** Creating one coroutine/task for every untrusted item without a concurrency/resource limit.

**Why:** Memory, sockets, downstream requests, and rate limits can be exhausted.

**Prefer:** A semaphore, bounded worker queue, batching, or streaming results.

**Source:** [asyncio synchronization primitives](https://docs.python.org/3/library/asyncio-sync.html).

### `python.async.sync-lock` (`BLOCK`)

**Avoid:** Holding `threading.Lock` or another blocking synchronization primitive while awaiting.

**Why:** It can block the event-loop thread or preserve a lock across suspension.

**Prefer:** `asyncio.Lock` for task coordination and keep critical sections free of unrelated awaits when possible.

**Source:** [asyncio synchronization](https://docs.python.org/3/library/asyncio-sync.html).

## Security and data correctness

### `python.deserialize.untrusted-pickle` (`BLOCK`)

**Avoid:** Loading pickle data from an untrusted or unauthenticated source.

**Why:** Pickle can execute arbitrary code during deserialization.

**Prefer:** A non-executable data format/schema; authenticate trusted pickle data if legacy use is unavoidable.

**Source:** [`pickle` warning](https://docs.python.org/3/library/pickle.html).

### `python.execution.eval-untrusted` (`BLOCK`)

**Avoid:** `eval`/`exec` on external strings, including attempts to make them safe only by restricting globals.

**Why:** Input becomes executable Python and sandboxing is not a reliable trust boundary.

**Prefer:** Parse a constrained grammar, use literal/schema parsers, or an allowlisted command model.

**Source:** [`eval`](https://docs.python.org/3/library/functions.html#eval).

### `python.subprocess.shell-untrusted` (`BLOCK`)

**Avoid:** `shell=True` or shell-composed command strings containing untrusted values.

**Why:** Metacharacters alter command structure.

**Prefer:** Argument arrays with `shell=False`; allowlist any executable/option that is itself dynamic.

**Source:** [subprocess security considerations](https://docs.python.org/3/library/subprocess.html#security-considerations).

### `python.time.naive-boundary` (`BLOCK`)

**Avoid:** Mixing naive and aware datetimes or treating a naive timestamp as an unambiguous cross-system instant.

**Why:** Local timezone/DST assumptions create incorrect ordering and expiration behavior.

**Prefer:** Aware UTC instants at system boundaries and explicit local-zone conversion.

**Source:** [`datetime` aware and naive objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects).

### `python.numeric.float-money` (`BLOCK`)

**Avoid:** Binary `float` for exact monetary/accounting calculations.

**Why:** Decimal fractions are often not exactly representable and rounding accumulates.

**Prefer:** Integer minor units or `decimal.Decimal` created from decimal strings with explicit rounding.

**Source:** [`decimal`](https://docs.python.org/3/library/decimal.html).

## Design warnings

### `python.import.wildcard` (`WARN`)

**Avoid:** `from module import *` outside the narrow module-republication use case.

**Why:** Names become implicit, collisions are hidden, and static analysis suffers.

**Prefer:** Explicit imports or a deliberate `__all__` re-export boundary.

**Source:** [PEP 8 imports](https://peps.python.org/pep-0008/#imports).

### `python.architecture.mandatory-layers` (`WARN`)

**Avoid:** Introducing repository/service/DTO layers solely because a generic skill says every Python application needs them.

**Why:** The extra indirection can relocate rather than reduce complexity.

**Prefer:** Add a boundary only when it owns a real contract, dependency, test seam, or change axis.

**Mined and deliberately narrowed from:** [`wshobson/agents` Python anti-patterns](https://github.com/wshobson/agents/blob/main/plugins/python-development/skills/python-anti-patterns/SKILL.md).
