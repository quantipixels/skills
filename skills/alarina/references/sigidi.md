# SIGIDI tools

Read once per thread when the `t3-code` tools are present (names may carry an `mcp__t3-code__` prefix). SIGIDI and T3 Code are the same host. Use these instead of scripts, loops or prose that rebuild them.

## Delegate

- Call `orchestrator_capabilities` once and pick providers, models and effort names from it, never from memory. If a model is refused, use the closest one from that list and say so.
- Start each child with `delegate_task` in `mode: "async"`. Its `runtimeMode` cannot be broader than yours; use `auto` or `inherit`.
- Completion wakes you. While children run, keep a fallback check-in: on Claude Code use the host's wake-up, otherwise `schedule_task` with `{"type":"interval","everyMs":2700000}` or less, and delete it when the children are done.
- To see progress, use `task_status` and read the child's thread with `t3_thread_read`. Do not message a child to ask its status. Stop one with `task_cancel`.
- Each review round is a new `delegate_task` with its own `clientRequestId`, carrying the original brief, earlier findings and your answers. Do not continue a review by sending to the child's thread.
- Answer a child's question waiting in its thread with `t3_pending_request_list`, `t3_pending_request_read` and `t3_pending_request_respond`.

## Isolate

- Child work stays in `delegate_task`. Use `t3_thread_launch` only when the user asks for a separate top-level conversation. Give it a `workspaceStrategy`: `{"type":"worktree","baseRef":"<parent branch>","branch":"<new>","startFromOrigin":false}` for stacked work, `existing_worktree` to continue one, or `root`. Retain the returned thread id; check `t3_thread_list` before retrying a launch whose response was lost.
- Before a second writer enters a worktree, check `t3_worktree_status`.

## Pull requests

- Call `link_pull_request` with the full URL the moment a PR exists or you start work on one, for every layer of a stack. Before finishing, check `list_thread_pull_requests` and link any you missed.
- To wait on CI, review or conflicts, handle what is already there, call `watch_pull_request` and end the turn. A wake is news, not a merge decision.
- Call `unwatch_pull_request` when you hand the work back so the thread returns to the user's inbox.

## Wait and repeat

- Never write a sleep or poll loop. For recurring work use `schedule_task` with `{"type":"interval","everyMs":<ms>}`, `{"type":"fixed_time","timeOfDay":"HH:MM","weekdays":[...]}`, or `{"type":"webhook"}`; report its cadence and next run, or its `webhookUrl`.

## Show and prove

- When a chart, diagram or comparison says more than prose, check one self-contained page with `html_preview`, then publish it with `html_render` before your reply (see `ojuiwe`).
- Drive web UIs with `preview_*` and simulators or devices with `device_*`; record evidence with `preview_recording_start`/`preview_recording_stop` or `device_screenshot`. Close what you open (`t3_preview_close`, `device_close`).

## Other threads and secrets

- Read past or sibling work with `t3_thread_read` and `t3_thread_search`, scoped to the current project.
- Ask for a secret with `request_secret` and pass the returned one-use `secretRef`. Never ask for a secret in chat.
