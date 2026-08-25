# Observer state for `wo-pr`

Read this reference after pinning the target and before starting the observer or recording an action.

The observer writes a schema-v2 checkpoint under the operating-system user-state directory. It stores only target identity, current head, handled-event receipts, retry counts, last snapshot identity, and the last readiness milestone—never credentials, logs, authority, diagnosis, or a lifecycle lease. Atomically archive a schema-v1 checkpoint and take a fresh complete provider snapshot before acting.

After a non-idempotent provider write succeeds and readback verifies it, record its receipt:

```bash
python3 scripts/pr_watch.py --state-file <path> \
  --record-receipt <head-sha> <event-id> <fingerprint> <provider-receipt>
```

If readback fails, report `PARTIAL` and do not retry without proof that the effect is absent. Record a CI retry only after the provider accepts it:

```bash
python3 scripts/pr_watch.py --state-file <path> --record-retry <head-sha> <job-id>
```
