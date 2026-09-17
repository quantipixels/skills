# Domain values: applicable seam and negative control

Use the Java fixture pair at `../fixtures/domain-values/` to distinguish reuse of an
applicable external-value converter from copying it into an incompatible internal boundary.
This is part of the existing opt-in engineering evaluation surface, not another model runner.

For each case, freeze a disposable actor directory with `WireValues.java` plus the chosen
`positive/` or `negative/` files. Give the actor only that case's `TASK.md` and its frozen
Alága treatment. Keep the other case, acceptance probes and reference patches private.
Run each case with the same host/model/effort/budget against baseline and candidate guidance.
Disclose assignment-only isolation when native filesystem isolation is unavailable.

The evaluator's `test_domain_values.py` owns executable probes and known-good/known-bad
controls. Its mechanics checks compile and execute Java; they do not execute a model.
Use `probe(workspace, case)` against each returned candidate and independently inspect the
diff and trace for analog discovery, unnecessary machinery and unrequested changes.
The positive oracle adds an alias through the existing seam before reading it, so an ad-hoc
switch that happens to recognize the initial tokens cannot satisfy compatibility. The
negative oracle rejects uppercase/alias/unknown/whitespace values accepted by the tolerant
external converter. Neither oracle inspects instruction prose or matches implementation names.

Record the source revision and hashes of task, fixture, oracle and guidance; files actually
loaded; acceptance, wrong actions, omissions and rework; and available usage measurements.
Do not infer model benefit from passing mechanical controls. JDK absence is a blocked
prerequisite, and compile/setup errors are errors rather than expected behavioral rejection.
