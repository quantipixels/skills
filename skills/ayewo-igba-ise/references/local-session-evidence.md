# Local coding-agent session evidence

Use when a session/corpus postmortem depends on persisted local Codex or Claude Code history.

The bundled read-only adapter inventories and normalizes structural evidence so Àyẹ̀wò can select the smallest relevant sample. It may discover current session roots; preserve proved root relationships and unresolved ancestry; emit host/session/root/project/version/time/event/tool counts, parse gaps and conservative skill-reference line locators; and filter by explicit host, project, session/root/ancestor or time range.

It must never emit raw prompts, responses, source, tool arguments/results, credentials or pasted content. Structural counts are locators, not proof of retries, waste, selection, loading, usefulness or failure cause. A fork/subagent/unresolved child is not an independent root without evidence.

Read a known transcript directly when it suffices. Use the adapter for inventory/relationship normalization and consult its current --help for invocation and options. Project/session/time filters apply after parsing. The repeatable --skill option focuses emitted reference signals; it does not filter sessions. Omitting time bounds means no cutoff. Explicit --codex-root, --claude-root or --skills-root can supply already located stores.

Default roots follow current host conventions: CODEX_HOME or ~/.codex for Codex session storage, and CLAUDE_CONFIG_DIR or ~/.claude/projects for Claude Code. history.jsonl is not treated as a full Codex transcript. Durable indexes, when useful, belong under .qp/ayewo-igba-ise/<stable-subject>/session-evidence.json.

## Evidence semantics

Activity records structurally identified call/result counts, explicit error flags, consecutive same-tool calls and result byte sizes by observed name. These may under-report schema variants and never establish efficiency or waste.

Skill references distinguish explicit user invocation from user mentions, structured fields and SKILL.md paths. Only explicit invocation is high-confidence invocation evidence; none proves eligibility, loading, availability or value.

Codex parent metadata is followed only through indexed records; absent parents leave root identity unresolved. A Claude subagent path may prove its root relationship, subject to version-sensitive schema.

Use the index to select root sessions, then inspect only evidence needed to reconstruct contract, owner selection, correction/rework, proof, recovery or tool/environment friction. Semantic classifications remain in [agent session](agent-session.md) and [corpus analysis](corpus-analysis.md).

## Provenance and drift

The current Codex basis is openai/codex commit 773f0b081de689b0d54f2809e7b17bfdb4c9f341 for session paths and metadata. The Claude basis is its official Manage sessions documentation, which declares transcript entries internal and version-sensitive. The parser reports invalid/unreadable records rather than inferring absence. Refresh this guidance when host paths/schema change or a real corpus exposes gaps.

Do not add hooks, receipts or background telemetry by default; use native records first.
