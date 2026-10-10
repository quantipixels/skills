# What is not proof on its own

Each of these can look like proof and still hide the failure it claims to rule out. Use it as a lead, then run the check that could actually fail.

- A passing test count for a reported bug: the suite may never reach the reported path.
- A schema diff or an empty-database test for a data change: existing rows, old writers and partial migrations are untested.
- A rollback command for an incident: it shows a way back, not that service recovered.
- A merged PR for a release: merged is not built, deployed or serving.
- A quarantined flaky test: the signal is switched off, not fixed.
- Fewer files or a newer dependency: neither shows behaviour stayed the same or improved.
- A delegate's, an earlier session's or a tool's report: check the decisive claim against current files.
