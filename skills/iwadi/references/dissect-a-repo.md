# Dissect a repository

Use when the user asks to understand a repository fully, or when a question about one repository can only be answered well from a whole picture of it. The result is a reference document the user keeps, not a chat answer.

## Where it goes

Write to the user's stated place for such documents (for example their wiki), otherwise the project's research location, otherwise wherever the project keeps working reports. One file per repository, named after it. If the user also wants an adoption or comparison judgment, write that as a separate report so the dissection stays a neutral reference.

## What it covers

- **Purpose and philosophy:** what the repository is for, who uses it, and the ideas that shape it, taken from its own instructions and design docs.
- **Layout:** the top-level parts and what each holds, including executables, config, tests and docs.
- **Every component:** for each skill, module, command or service: what it does, what triggers it, how it works in order, what it produces and where it writes, and what it calls. Cover all of them; a sample is not a dissection.
- **How the parts connect:** the main flows and chains, with a diagram (Mermaid) where it helps.
- **Configuration:** settings, defaults, how users override them, and which choices are made by people versus code.
- **Feedback loops:** how the system learns, refreshes or improves over time, if it does.
- **Testing and proof:** what is checked mechanically, what is judged by people or models, and what is not checked.
- **Strengths, weaknesses and fit:** what works well, what costs or misleads, and, when the user has a target in mind, what to take or leave.

Cite file paths for claims. Separate what the source states, what you observed by running it, and your interpretation. Note where docs and code disagree.

## How to run it

1. Inventory first: list every component from the file tree, so coverage can be checked at the end.
2. Split large repositories into areas and give each area to a delegated reader, each with the inventory slice, the outline above and the output file. Readers are read-only on the repository.
3. Write the document section by section and save after each, so a stall still leaves usable work.
4. Check coverage against the inventory: every component has a section, every section cites its source. Fix gaps before reporting.
5. Report the file path, the coverage check, and anything that could not be read or run.
