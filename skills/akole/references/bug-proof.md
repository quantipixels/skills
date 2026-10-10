# Proof for a bug fix

Applies to a defect with a reproducible symptom. It adds to [delivery](delivery.md) and a known cause; it does not replace them.

## Test first, when it is cheap

Capture the failure before the fix when a faithful check is quick to build: a test, a script, or a browser or API call that shows the wrong result. Prefer the most end-to-end check that stays fast and stable; use a unit check only when it is the cheapest honest way to show the same failure. Skip test-first when setup would cost more than the fix and a direct observation proves the same thing. Say that you skipped it and what you used instead.

1. Run the check and confirm it fails for the reason in the report, not because of setup, a typo or zero selected tests.
2. Make the smallest fix for the cause.
3. Run the same check and confirm it passes. Rerun the neighbours it could break.
4. Report before and after: the command, the failing output, the passing output.

A check that never failed proves nothing about the fix. Keep the check as regression protection unless retained proof already covers it.

## Cause chain

Do not fix until you can state the whole chain from trigger to symptom, each link with evidence. A gap in the chain is a guess; probe it or name it as open. If the cause is a deliberate contract, not a mistake, return that to whoever owns the decision before changing it.

If two fixes built on the same premise have failed, stop and question the premise (see `SKILL.md`).

## Evidence of done

A fix is done when the report shows the symptom before, the same step after, and the checks that could have caught a side effect. The symptom no longer appearing in one run is weaker than a check that failed before and passes now.
