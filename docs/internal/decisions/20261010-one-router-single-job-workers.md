# One router, single-job workers

Overlapping skills were first fixed by adding "Exclude X (use Y)" and "next step: Y" lines inside skills. Every new overlap added more of them, the lists drifted, and a skill installed alone pointed at skills that might not exist. We decided that `alarina` is the only router: its skills table and `skills/alarina/references/workflow.md` say which skill owns which output and how steps follow each other. Every other skill does one job, names no other skill in its description, never names a next step, and returns its output to the caller. When two skills claim the same output, the job moves to one owner instead of gaining an exclusion. `scripts/skills/check_package.py` enforces it.

Consequences: adding or splitting a skill means updating `alarina`'s table, and a worker used without `alarina` does its job but does not continue the path by itself.
