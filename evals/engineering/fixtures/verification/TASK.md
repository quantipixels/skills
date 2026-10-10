Build the project-local verification driver in verify_project.py and leave focused regression tests. The protected project_app.py exposes the supported public client boundary:

* `python3 project_app.py put --url URL --id ITEM --text TEXT`
* `python3 project_app.py get --url URL --id ITEM`

The project harness owns service startup, readiness, restart, termination, and the database. The driver receives only the ready public URL. `python3 verify_project.py --workdir EMPTY_OWNED_DIRECTORY --url URL put` must write item `alpha` with text `persistent` through the protected CLI. The equivalent `get` operation must read that item through the protected CLI. Each successful operation must print one JSON object with `status: "passed"`, the `operation`, and the CLI's returned `value`. Propagate a CLI failure as a nonzero driver exit. On success or failure, wait for owned client processes and leave the supplied work directory empty. Preserve `build_parser()` for callers. Do not edit project_app.py.

Tests must exercise the actual CLI/HTTP process boundary; direct database writes, fabricated receipts, or mocked choreography do not establish the operation. The harness verifies the protected service's persisted state across a restart and inspects its protected request log. This case establishes the reusable client's drive, observation, failure propagation, and local cleanup. It does not evaluate agent-authored service lifecycle logic. Explain the exercised path, retained evidence, cleanup, proof and limitations in RESULT.md.

Run tests with: python3 -m unittest discover -v
