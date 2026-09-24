# HTML Artifact toolkit

Start with [HTML Artifact](../skills/html-artifact/SKILL.md). It turns supplied material into an understandable, inspectable browser document, choosing presentation for the reader's task.

The toolkit includes a Tailwind/jQuery base, optional view/filter/carousel/report controls, a conditional Mermaid renderer, branding assets and a structural verifier. Asset comments define integration contracts. Generate diagrams and charts from the actual material; no recipe catalogue or fixed page layout is required.

Four focused references cover dependency delivery, optional manifests, exact code-change views and live updates. Core source fidelity, accessibility, ephemeral state and verification guidance lives in the skill entrypoint.

Run the structural check with:

```sh
python3 skills/html-artifact/scripts/verify_artifact.py report.html --json
```

This does not execute JavaScript or prove visual quality, factual accuracy, accessibility or privacy. Exercise material browser behavior separately. Model-evaluation cases in `evals/html-artifact/` remain opt-in and are unexecuted until actually run.
