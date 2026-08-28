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
    "apere-launch-route",
    "asa-existing-mantine",
    "banner-supplied-spec",
    "brand-blank-logo",
    "slides-board-update",
    "social-cross-platform",
    "irinse-astgrep-readiness",
    "pare-test-cleanup",
    "wo-pr-required-gap",
    "alarina-missing-owner",
    "arojinle-single",
    "ayewo-lost-work",
    "salaye-kafka",
]

FIXTURE_OVERRIDES = {
    "apere-launch-route": """The launch needs:
1. a light brand refresh,
2. landing-page UX direction,
3. a four-format social campaign,
4. an investor deck.
The same positioning, visual identity, accessibility constraints, and approval boundary must be shared.
The actual production will be delivered later by an implementation owner.
Currently available design selectors include:
- brand — durable brand identity and approved identity assets,
- amoye-ui-ux — UI/UX direction,
- social-graphics — social campaign graphics,
- slides — presentations and pitch decks,
- alaga — integrated production after routing.
""",
    "irinse-astgrep-readiness": """Bounded question: find Kotlin calls matching a structural pattern.
Tool candidate: ast-grep.
Authority: read-only inspection and command execution only.
No installation, authentication, global configuration, project-file mutation, or persistent service is authorized.
A plain text fallback search is available if ast-grep is missing or unsupported.
No command output has been supplied, so current readiness is not yet established. Return the minimum readiness procedure and the possible statuses rather than pretending the checks already ran.
""",
}


def call_model(messages: list[dict], max_tokens: int, seed: int) -> tuple[str, dict, float]:
    body = json.dumps({
        "model": "qwen2.5-7b-instruct-q4_k_m",
        "messages": messages,
        "temperature": 0.15,
        "top_p": 0.9,
        "max_tokens": max_tokens,
        "seed": seed,
        "stream": False,
    }).encode()
    request = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    started = time.time()
    with urllib.request.urlopen(request, timeout=1200) as response:
        payload = json.load(response)
    return payload["choices"][0]["message"]["content"].strip(), payload.get("usage", {}), time.time() - started


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    args = parser.parse_args()

    out = Path(args.out)
    (out / "inputs").mkdir(parents=True, exist_ok=True)
    (out / "responses").mkdir(parents=True, exist_ok=True)

    all_cases = [(idx, dict(case)) for idx, case in enumerate(DATA["cases"]) if case["id"] in SELECTED_IDS]
    selected = [(pos, idx, case) for pos, (idx, case) in enumerate(all_cases) if pos % args.shard_count == args.shard_index]
    results: list[dict] = []
    failures = 0

    for local_pos, (spot_pos, base_idx, case) in enumerate(selected):
        case["fixture"] = FIXTURE_OVERRIDES.get(case["id"], case["fixture"])
        order = ["old", "new"] if spot_pos % 2 == 0 else ["new", "old"]
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
            seed = 52000 + base_idx
            record = {
                "case_id": case["id"],
                "skill": case["skill"],
                "group": case["group"],
                "title": case["title"],
                "variant": variant,
                "ref": ref,
                "seed": seed,
                "model": "Qwen2.5-7B-Instruct-GGUF Q4_K_M",
                "package_files": files,
                "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "evaluation": case["evaluation"],
                "prompt": case["prompt"],
                "fixture": case["fixture"],
                "spotcheck_position": spot_pos,
                "base_case_index": base_idx,
            }
            try:
                text, usage, elapsed = call_model(
                    [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                    min(int(case.get("max_tokens", 700)), 850),
                    seed,
                )
                response_path = out / "responses" / f"{case['id']}--{variant}.txt"
                response_path.write_text(text, encoding="utf-8")
                record.update({
                    "status": "ok",
                    "response": text,
                    "response_sha256": hashlib.sha256(text.encode()).hexdigest(),
                    "usage": usage,
                    "elapsed_seconds": round(elapsed, 3),
                })
                print(f"[{local_pos + 1}/{len(selected)}] {case['id']} {variant} OK {elapsed:.1f}s", flush=True)
            except Exception as exc:
                failures += 1
                record.update({"status": "error", "error": repr(exc)})
                print(f"[{local_pos + 1}/{len(selected)}] {case['id']} {variant} ERROR {exc!r}", file=sys.stderr, flush=True)
            results.append(record)
            (out / "results.jsonl").write_text(
                "\n".join(json.dumps(item, ensure_ascii=False) for item in results) + "\n",
                encoding="utf-8",
            )

    manifest = {
        "baseline": DATA["base"],
        "candidate": DATA["head"],
        "cases": len(selected),
        "total_spotcheck_cases": len(all_cases),
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "calls": len(results),
        "failures": failures,
        "model": "Qwen/Qwen2.5-7B-Instruct-GGUF:Q4_K_M",
        "runner": "llama.cpp OpenAI-compatible server",
        "temperature": 0.15,
        "evaluation_type": "actual isolated stronger-model spotcheck",
        "fixture_overrides": sorted(FIXTURE_OVERRIDES),
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
