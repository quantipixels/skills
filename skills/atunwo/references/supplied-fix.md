# Judging a supplied fix

Use when an open pull request or exact commit is offered as the repair for a symptom. The verdict is whether it really fixes the symptom.

Pin its baseline and patched revisions. Use the same discriminating path, inputs, dependencies, configuration, data basis and permitted environment for both, and reset mutable state between runs. Establish that the baseline shows the broken state, then check on the patched candidate both that the broken state is gone and that the expected behavior is present.

Return:

- `fixed`: the baseline shows the symptom, the patch does not, and the expected behavior is present, with the bounded before/after evidence;
- `insufficient fix`: both revisions show the symptom;
- `inconclusive`: either half cannot be observed under comparable conditions.

For a verify-only request, make no edits to the repair, offer no competing patch and publish nothing. The verdict is evidence about the pinned artifact; it does not authorize correction. Use existing project isolation without overwriting unrelated work, and keep runtime effects inside the authorized test boundary. Record the hypothesis, the predicted discriminator, the observation and any condition or coverage limit.

When the symptom's cause is not known well enough to say what a real fix must change, get the cause established first (return that need to the caller), then judge the fix against it. After a reduced reproduction guides the comparison, replay the original scenario whenever reduction removed integration conditions.
