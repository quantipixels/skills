# CRAP measurements

Use for an explicit complexity-and-coverage risk question. This is advisory evidence for alaga or atunwo, not a test-quality verdict or a universal gate.

Identify the requested methods and revision. Obtain actual per-method cyclomatic complexity and automated-test coverage with tool/version, command or supplied-report origin, collection revision, exclusions and coverage granularity. Confirm that both inputs refer to the same code and methods; compiler-generated names may require source mapping. Missing methods, failed collection and stale or incompatible reports are not zero coverage.

For complexity `c` and coverage ratio `v` in `[0,1]`, calculate:

`CRAP = c² × (1 − v)³ + c`

Use a calculator or script and show the inputs. At full coverage the result equals `c`; at zero coverage it equals `c² + c`. The original description uses basis-path coverage. Label line- or branch-coverage substitutions as variants; do not silently compare unlike measures. Preserve the complexity tool's definition rather than mixing language-specific decision counts.

If either usable input is unavailable, report the missing input and the smallest collection step. Report available complexity separately if useful, but do not manufacture a CRAP score or install a collector automatically. Disclose failed tests when using their partial coverage. Resolve contradictory reports before calculation.

Rank only within the stated scope and compatible provenance. Any threshold is an explicit project policy. A high score can motivate investigation; it does not establish a defect, weak assertions or a need for more tests. Do not extract methods solely to lower the score: preserve coherent responsibilities and review the actual complexity and proof gap.

Formula and coverage definition: [original CRAP description](https://www.artima.com/weblogs/viewpost.jsp?thread=215899).
