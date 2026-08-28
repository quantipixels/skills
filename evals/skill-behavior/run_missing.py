#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

from run_evals import DATA, SYSTEM, load_bundle

URL = "http://127.0.0.1:8080/v1/chat/completions"

# The first sweep produced complete new responses but three old-package calls
# exceeded the 600 s transport timeout. These reductions preserve the branch
# that the scenario exercises while dropping unrelated reference volume.
PATH_OVERRIDES = {
    "amoye-blank-slate": [
        "SKILL.md",
        "references/quick-reference.md",
    ],
    "eto-existing-system": [
        "SKILL.md",
        "references/token-architecture.md",
        "references/component-specs.md",
        "references/states-and-variants.md",
        "templates/design-tokens-starter.json",
    ],
    "asa-existing-mantine": [
        "SKILL.md",
        "references/ui-component-libraries.md",
        "references/shadcn-accessibility.md",
    ],
}


def call_model(messages: list[dict], max_tokens: int, seed: int):
    body = json.dumps(
        {
            "model": "qwen2.5-3b-instruct-q4_k_m",
            "messages": messages,
            "temperature": 0.1,
            "top_p": 0.9,
            "max_tokens": max_tokens,
            "seed": seed,
            "stream": False,
        }
    ).encode()
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    start = time.time()
    with urllib.request.urlopen(req, timeout=1200) as response:
        payload = json.load(response)
    return (
        payload["choices"][0]["message"]["content"].strip(),
        payload.get("usage", {}),
        time.time() - start,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=sorted(PATH_OVERRIDES))
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    idx, original = next((i, c) for i, c in enumerate(DATA["cases"]) if c["id"] == args.case)
    case = dict(original)
    case["paths"] = PATH_OVERRIDES[args.case]

    out = Path(args.out)
    (out / "inputs" / case["id"]).mkdir(parents=True, exist_ok=True)
    (out / "responses").mkdir(parents=True, exist_ok=True)

    ref = DATA["base"]
    bundle, files = load_bundle(ref, case)
    user = f"""<skill-package>
{bundle}
</skill-package>

<exact-environment-evidence>
{case['fixture']}
</exact-environment-evidence>

<user-request>
{case['prompt']}
</user-request>"""
    input_path = out / "inputs" / case["id"] / "old.txt"
    input_path.write_text("SYSTEM\n" + SYSTEM + "\n\nUSER\n" + user, encoding="utf-8")

    record = {
        "case_id": case["id"],
        "skill": case["skill"],
        "group": case["group"],
        "title": case["title"],
        "variant": "old",
        "ref": ref,
        "seed": 41000 + idx,
        "model": "Qwen2.5-3B-Instruct-GGUF Q4_K_M",
        "package_files": files,
        "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
        "evaluation": case["evaluation"],
        "prompt": case["prompt"],
        "fixture": case["fixture"],
        "rerun_reason": "original full-package call exceeded 600 s timeout",
        "rerun_package_policy": "relevant branch-preserving reduction",
    }

    try:
        text, usage, elapsed = call_model(
            [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
            int(case.get("max_tokens", 600)),
            41000 + idx,
        )
        response_path = out / "responses" / f"{case['id']}--old.txt"
        response_path.write_text(text, encoding="utf-8")
        record.update(
            {
                "status": "ok",
                "response": text,
                "response_sha256": hashlib.sha256(text.encode()).hexdigest(),
                "usage": usage,
                "elapsed_seconds": round(elapsed, 3),
            }
        )
        failures = 0
        print(f"{case['id']} old OK {elapsed:.1f}s", flush=True)
    except Exception as exc:
        failures = 1
        record.update({"status": "error", "error": repr(exc)})
        print(f"{case['id']} old ERROR {exc!r}", file=sys.stderr, flush=True)

    (out / "results.jsonl").write_text(json.dumps(record, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = {
        "baseline": DATA["base"],
        "candidate": DATA["head"],
        "case_id": case["id"],
        "cases": 1,
        "calls": 1,
        "failures": failures,
        "model": "Qwen/Qwen2.5-3B-Instruct-GGUF:Q4_K_M",
        "runner": "llama.cpp OpenAI-compatible server",
        "temperature": 0.1,
        "evaluation_type": "actual isolated model inference; targeted timeout recovery",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "case.json").write_text(json.dumps(case, ensure_ascii=False, indent=2), encoding="utf-8")
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
