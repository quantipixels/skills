# Native architecture evidence

Use when current project/tool/dependency/runtime facts can materially change an architecture decision. Discover from the active repository instead of maintaining ecosystem command catalogues.

Start with bounded repository truth:

```bash
git ls-files -- <relevant-roots>
git grep -n '<boundary|dependency|protocol|state owner>' -- <relevant-roots>
```

Read manifests, wrappers, deployment/config files, schemas, generated clients/specs, and exact runtime/tool versions relevant to the drivers. Then ask the active project/tool for its own capabilities:

```bash
<project-wrapper-or-tool> --help
```

Use project-native dependency/task/configuration/runtime inspection when it owns the fact. Prefer the repository wrapper (for example a checked-in build wrapper) over a globally assumed command/version.

Do not embed a Gradle/Maven/Cargo/npm/dotnet/etc command matrix here. Exact commands are volatile and should be discovered from the current project/tool/owning docs.

Pin material evidence to version/config/candidate. Tool output proves observed structure/capability, not automatic architecture intent. Keep architecture judgment with Solution Architect.
