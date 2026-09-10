# Codex host options

Offer these independently at the scope chosen in `qp-setup`. Check support in the installed Codex version using its help, schema, or [official configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference). Do not apply a user-level setting as a workaround for unsupported repository scope.

## Main-session defaults

```toml
model = "gpt-6-astra"
model_reasoning_effort = "medium"
```

Offer these only when the user wants startup defaults. Confirm model availability rather than copying an account-specific alias. The live host selection remains authoritative; editing config does not change the current session or prove which model ran.

## Context Notes experiment

```toml
[features.context_management]
experimental_mode = true
```

Offer this as an experimental opt-in for notes and searchable conversation history. Verify the installed host supports this form and the account meets its current requirements. Explain the change in context handling before approval. Do not enable it automatically or copy unrelated memory settings.

If `features.context_management` already uses a boolean form, include its conversion to the supported table form in the preview. Preserve other feature settings. To undo the choice, remove a newly added key or restore its prior value using the approved diff and backup, while preserving subsequent user edits.
