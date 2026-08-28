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
SELECTED_IDS = [
    "amoye-blank-slate",
    "eto-existing-system",
    "amose-term-conflict",
    "pare-test-cleanup",
    "root-cause-timeout",
    "html-simple-report",
]


def call_model(messages: list[dict], max_tokens: int, seed: int) -> tuple[str, dict, float]:
    body = json.dumps({
        "model": "qwen2.5-3b-instruct-q4_k_m",
        "messages": messages,
        "temperature": 0.1,
        "top_p": 0.9,
        "max_tokens": max_tokens,
        "seed": seed,
        "stream": False,
    }).encode()
    request = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    started = time.time()
    with urllib.request.urlopen(request, timeout=900) as response:
        payload = json.load(response)
    return payload["choices"][0]["message"]["content"].strip(), payload.get("usage", {}), time.time() - started


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--case-position", type=int, required=True)
    args = parser.parse_args()

    out = Path(args.out)
    (out / "inputs").mkdir(parents=True, exist_ok=True)
    (out / "responses").mkdir(parents=True, exist_ok=True)

    chosen = [(idx, case) for idx, case in enumerate(DATA["cases"]) if case["id"] in SELECTED_IDS]
    base_idx, case = chosen[args.case_position]
    results: list[dict] = []
    failures = 0
    order = ["old", "new"] if base_idx % 2 == 0 else ["new", "old"]

    for variant in order:
        ref = DATA["base"] if variant == "old" else DATA["head"]
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
        case_dir = out / "inputs" / case["id"]
        case_dir.mkdir(parents=True, exist_ok=True)
        input_path = case_dir / f"{variant}.txt"
        input_path.write_text("SYSTEM\n" + SYSTEM + "\n\nUSER\n" + user, encoding="utf-8")
        seed = 41000 + base_idx
        record = {
            "case_id": case["id"], "skill": case["skill"], "group": case["group"], "title": case["title"],
            "variant": variant, "ref": ref, "seed": seed, "model": "Qwen2.5-3B-Instruct-GGUF Q4_K_M",
            "package_files": files, "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
            "evaluation": case["evaluation"], "prompt": case["prompt"], "fixture": case["fixture"],
            "base_case_index": base_idx,
        }
        try:
            text, usage, elapsed = call_model(
                [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                min(int(case.get("max_tokens", 650)), 700), seed,
            )
            response_path = out / "responses" / f"{case['id']}--{variant}.txt"
            response_path.write_text(text, encoding="utf-8")
            record.update({"status": "ok", "response": text,
                           "response_sha256": hashlib.sha256(text.encode()).hexdigest(),
                           "usage": usage, "elapsed_seconds": round(elapsed, 3)})
            print(f"{case['id']} {variant} OK {elapsed:.1f}s", flush=True)
        except Exception as exc:
            failures += 1
            record.update({"status": "error", "error": repr(exc)})
            print(f"{case['id']} {variant} ERROR {exc!r}", file=sys.stderr, flush=True)
        results.append(record)
        (out / "results.jsonl").write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in results) + "\n", encoding="utf-8"
        )

    manifest = {
        "baseline": DATA["base"], "candidate": DATA["head"], "cases": 1,
        "case_id": case["id"], "case_position": args.case_position,
        "calls": len(results), "failures": failures,
        "model": "Qwen/Qwen2.5-3B-Instruct-GGUF:Q4_K_M",
        "runner": "llama.cpp OpenAI-compatible server",
        "temperature": 0.1,
        "evaluation_type": "actual isolated missing-case retry",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
