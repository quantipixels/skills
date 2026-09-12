# Skill evaluations

Opt-in evaluation assets, maintained separately from installed skills. The owner explicitly requested these checked-in evals; generated runs and private traces remain in ignored `.qp/` or external temporary storage.

- [Pepeye](pepeye/README.md): three original cases, actor-input preparation, private rubrics, and evidence-aware grading. Use the native model host to execute prepared tasks.
- [SureForge kit](vendor/sureforge/UPSTREAM.md): pinned upstream eval scenarios, fixtures, abstract gate model, metrics tooling, tests, and license. Reuse its evaluation structure for other skills; its specific gate rules are not universal requirements.

Define each skill's intended behavior before adapting an oracle. Keep actor inputs separate from grader criteria, freeze candidate/input hashes, preserve failed and blocked attempts, and record actual model/host/resource measurements. Mechanical tests, simulated decisions, and live task execution are different evidence classes.

The tools make no model calls. Set and enforce a budget in the execution host before live runs; unknown costs remain unknown. No model credentials or private eval access are required for package CI.
