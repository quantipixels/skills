# Kotlin coroutine proof

Use when coroutine scheduling or virtual time controls the behavior being proved. Discover the project's kotlinx-coroutines version and existing test setup; this reference does not require a dependency or dispatcher refactor for an ordinary suspend-function test.

With `runTest`, put participating test dispatchers on one `TestCoroutineScheduler`. Work deliberately using real `Dispatchers.IO` or `Default` does not acquire the test clock. Substitute a controllable dispatcher only when that is the intended proof; real-scheduler integration remains a different claim.

Choose the synchronization that exposes the contract:

- `join`/`await` establishes completion of a known child.
- `runCurrent` runs work due at the current virtual time.
- `advanceTimeBy(delta)` advances time but does not run tasks scheduled exactly at the resulting time; use `runCurrent` afterward when observing that boundary.
- `advanceUntilIdle` drains finite scheduled work; it can skip the intermediate state the test should observe.

Keep intentionally nonterminating work in `backgroundScope` or otherwise cancel it explicitly; finite collectors need not use that scope. When replacing Main, do so before creating dependent dispatchers and reset it reliably. Confirm scheduler sharing rather than assuming an explicit dispatcher argument is always required.

Assert the observable transition, not merely that a clock advanced. A virtual-time pass does not prove behavior across real concurrent schedules. Use `irinse` only for a material runner/setup gap.

Sources: [JetBrains coroutine testing](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/), [advanceTimeBy](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/advance-time-by.html), [Android coroutine testing](https://developer.android.com/kotlin/coroutines/test). Discovery: [skydoves runTest skill](https://github.com/skydoves/android-testing-skills/blob/7790b351f997f83d11dcbbb4f1428b8797d43849/jvm-tests/coroutines/testing-coroutines-with-runtest/SKILL.md); its universal rules and incorrect exact-time description are not adopted.
