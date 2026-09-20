# PR review brief checks

Use the existing [native-host prompt check method](../README.md#simple-prompt-checks). These cases freeze the new description, evidence, recovery and presentation boundaries; they add no runner or required model dependency.

Give the actor only its selected entry from `cases.json`, the exact candidate skills and applicable references. All case data is synthetic; supplied test results are fixture evidence, not tests executed by this repository. Candidate labels are not real Git revisions and local paths are not attachments. Keep `expectations.json` separate for assessment.

Choose cases by the changed boundary. The read-only case is the nearest authority negative control; the small documentation and genuinely reversible cases check against over-processing. Add existing coordination cases when evaluating routing rather than the brief itself.

Record candidate revision or file hashes, files actually read, model/effort, fresh versus reused context, response and assessment in the existing task record. For comparison claims, run the same packet against both instruction candidates under matched conditions. A response-only exercise cannot prove provider mutations, image capture, runtime behavior or review speed; those claims require corresponding executed or observed evidence.

Initial status: cases authored; fresh native-host runs and matched before/after comparisons have not been executed. JSON/schema checks are not behavioral passes.
