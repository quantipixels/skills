# Engineering evaluations

Compare actual repairs with and without Alaga using the [engineering kit](engineering/README.md). It prepares fixed tasks and checks the resulting code with an independent oracle and the actor's own tests against the original defect. Model execution stays with your native agent host.

The default historical profile covers a lost-reply settlement with durable SQLite state and a small batching bug. An opt-in playbooks profile adds a project verification journey, a populated-data migration, and a runtime-profile diagnosis. These are development fixtures, not a measure of every skill or a substitute for real-project journeys. Correctness, regression detection, epistemic judgment and resource use remain separate results.

Keep generated studies and private traces in ignored `.qp/` or external evaluation storage. Package installation and CI need no model credentials or private services. Run generated code only in an appropriate evaluation environment; directory separation is not a sandbox.

Earlier evaluation structure was informed by [SureForge](vendor/sureforge/UPSTREAM.md); its attribution and license remain. Its product-specific gate model and supplied-judgment evaluator are not part of this kit.
