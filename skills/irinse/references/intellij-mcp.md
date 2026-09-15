# IntelliJ MCP

Official source: [JetBrains IntelliJ IDEA MCP Server](https://www.jetbrains.com/help/idea/mcp-server.html)

Use IntelliJ MCP for IDE-backed code insight, navigation, run configurations, terminal actions, and debugging when the installed IDE and coding-agent client support it.

## Operational guidance

When already ready, confirm the exposed tool surface and project-root scope before relying on it. Use IDE-backed navigation and inspections when indexes, symbol resolution, run configurations, or debugger integration can answer the engineering question more directly than text search alone.

Where exposed, use declaration/reference/implementation navigation for symbol identity and overload-sensitive questions; use an outline to select the relevant bodies rather than reading an entire large class. Inspect actual tool schemas: an IDE's graphical feature is not necessarily available through its MCP server. If semantic navigation is unavailable, use bounded source search and retain ambiguity instead of presenting name matches as resolved references.

Treat indexes and inspections as evidence that can be stale or incomplete. Constrain the exposed project and tools, and keep terminal/source mutations within the consuming workflow's authority. Record IDE/plugin versions, project identity, requested operation, index state, errors, and corroboration when they affect the result.

If the required IDE version/plugin/server, server state, client configuration, authentication, or integration is missing or needs mutation, use [tool setup](tool-setup.md) for the required readiness change.
