# Read a GitHub PR snapshot

Use within [wo-pr](../../../commands/wo-pr.md) when deterministic feedback pagination and candidate identity help establish current provider facts. This is a read-only adapter for GitHub and GitHub Enterprise using the installed authenticated `gh` CLI. Other providers keep their native tools and the shared provider contract.

```sh
python3 <alarina-directory>/scripts/pr_snapshot.py --repo OWNER/NAME --number 123
```

Use `--host <hostname>` for the actual Enterprise host. Resolve the repository and PR from the user's target or verified project remote. A snapshot request never changes the PR, replies to a comment, resolves a thread, requests review or merges.

The helper reads PR metadata, all paginated review threads and nested comments, top-level PR comments, submitted/pending reviews, and check/status contexts for the captured head. It rereads PR identity/head/base/state afterward. Changed identity produces stale evidence; a failed or partial API response, repeated cursor or incomplete page produces incomplete coverage. Empty checks mean none observed, not success or absence of required checks.

Output intentionally omits feedback bodies. Use the returned IDs and URLs to read actual feedback before interpreting or disposing of it. Deleted-author uncertainty stays visible. Latest review activity is separate from the latest decisive submitted opinion; neither alone determines review readiness or whether a requirement has been satisfied.

`complete` means the requested fact capture finished against stable PR metadata. It is **not** `PROVIDER_READY`: required checks/branch protection, mergeability, stacked ancestors, feedback meaning, independent acceptance and authority still require the owning method's judgment. Provider facts can change after capture; recheck at a consequential boundary. The helper does not maintain an action ledger, schedule polling or infer that observed feedback was handled.

The utility prints JSON and exits 0 for complete capture, 2 for invalid/incomplete capture. Missing CLI, authentication, API limits or inaccessible data are named gaps; do not broaden credentials or install software implicitly. Save a needed snapshot at the resolved record destination and keep it private when it contains private repository metadata. Raw CLI error output and credentials are not returned.
