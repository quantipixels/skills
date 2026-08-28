#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_PATH = ROOT / "eval" / "scenarios.json"
OUT = ROOT / "eval-results"
API = os.environ.get("EVAL_API", "http://127.0.0.1:8080/v1/chat/completions")

SYSTEM_PREFIX = """You are executing exactly one QP agent skill in a controlled, isolated prompt evaluation.

The complete instruction package available for this run is included below. Follow it as authoritative behavior. Respond exactly as the skill would respond to the user in a real conversation.

Rules for this evaluation:
- Do not mention the evaluation, variants, commits, scoring criteria, or instruction package.
- Use only facts supplied by the user scenario and the instruction package.
- No external tools or systems are available. Do not invent tool output, file contents, provider state, user confirmation, or completed mutations.
- When the skill requires a user decision or confirmation, return the next assistant turn and wait rather than pretending the user answered.
- When the scenario asks for a plan, explanation, assessment, route, or behavior description, provide that result directly.
- Preserve the skill's authority and completion boundary.
- Be concise but complete enough to expose whether the skill's intended behavior survived.

/no_think

=== SKILL PACKAGE START ===
"""

SYSTEM_SUFFIX = "\n=== SKILL PACKAGE END ===\n"


def git_show(ref: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


def assemble_package(ref: str, group: str, skill: str, files: list[str]) -> tuple[str, list[dict[str, Any]]]:
    root = f"skills/{group}/{skill}"
    parts: list[str] = []
    manifest: list[dict[str, Any]] = []
    for rel in files:
        path = f"{root}/{rel}"
        content = git_show(ref, path)
        if content is None:
            manifest.append({"path": path, "state": "missing"})
            continue
        digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
        manifest.append({
            "path": path,
            "state": "included",
            "sha256": digest,
            "chars": len(content),
            "lines": content.count("\n") + 1,
        })
        parts.append(f"\n--- FILE: {path} ---\n{content.rstrip()}\n--- END FILE: {path} ---\n")
    if not parts:
        raise RuntimeError(f"No instruction files found for {group}/{skill} at {ref}")
    package = "".join(parts)
    return package, manifest


def post_json(payload: dict[str, Any], timeout: int = 900) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        API,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    last_error: Exception | None = None
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")
            last_error = RuntimeError(f"HTTP {exc.code}: {detail}")
            if exc.code not in {429, 500, 502, 503, 504}:
                raise last_error
        except Exception as exc:
            last_error = exc
        if attempt < 5:
            time.sleep(attempt * 3)
    raise RuntimeError(f"Request failed after retries: {last_error}")


def clean_output(text: str) -> str:
    text = text.strip()
    # Preserve the raw response separately, but remove accidental Qwen think wrappers
    # from the user-facing output.
    if "<think>" in text and "</think>" in text:
        text = text.split("</think>", 1)[1].strip()
    return text


def run_one(doc: dict[str, Any], scenario: dict[str, Any], variant: str, index: int, total: int) -> None:
    ref = doc["baseline"] if variant == "before" else doc["candidate"]
    package, files = assemble_package(
        ref,
        scenario["group"],
        scenario["skill"],
        scenario["instruction_files"],
    )
    system = SYSTEM_PREFIX + package + SYSTEM_SUFFIX
    seed = int(doc.get("seed", 42))
    payload = {
        "model": doc["model"]["name"],
        "temperature": float(doc.get("temperature", 0)),
        "seed": seed,
        "max_tokens": int(scenario.get("max_tokens", 700)),
        "chat_template_kwargs": {"enable_thinking": False},
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": scenario["prompt"]},
        ],
    }

    target = OUT / scenario["id"]
    target.mkdir(parents=True, exist_ok=True)
    request_path = target / f"{variant}-request.json"
    response_path = target / f"{variant}-response.json"
    output_path = target / f"{variant}-output.md"
    metadata_path = target / f"{variant}-metadata.json"

    request_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        f"[{index:02d}/{total}] {scenario['id']} · {variant} · "
        f"{sum(x.get('chars', 0) for x in files):,} instruction chars",
        flush=True,
    )
    started = time.monotonic()
    response = post_json(payload)
    elapsed = time.monotonic() - started
    response_path.write_text(json.dumps(response, ensure_ascii=False, indent=2), encoding="utf-8")

    message = response.get("choices", [{}])[0].get("message", {})
    raw = str(message.get("content") or "")
    output = clean_output(raw)
    output_path.write_text(output + "\n", encoding="utf-8")

    metadata = {
        "scenario_id": scenario["id"],
        "skill": scenario["skill"],
        "name": scenario["name"],
        "group": scenario["group"],
        "variant": variant,
        "ref": ref,
        "instruction_files": files,
        "instruction_chars": len(package),
        "instruction_sha256": hashlib.sha256(package.encode("utf-8")).hexdigest(),
        "prompt": scenario["prompt"],
        "criteria": scenario["criteria"],
        "elapsed_seconds": round(elapsed, 3),
        "usage": response.get("usage"),
        "finish_reason": response.get("choices", [{}])[0].get("finish_reason"),
        "raw_reasoning_content_present": bool(message.get("reasoning_content")),
        "output_chars": len(output),
        "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    OUT.mkdir(exist_ok=True)
    doc = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
    scenarios = doc["scenarios"]
    total = len(scenarios) * 2
    cursor = 0
    run_manifest: dict[str, Any] = {
        "baseline": doc["baseline"],
        "candidate": doc["candidate"],
        "model": doc["model"],
        "seed": doc.get("seed", 42),
        "temperature": doc.get("temperature", 0),
        "scenario_count": len(scenarios),
        "generation_count": total,
        "started_at_epoch": time.time(),
        "order": [],
    }

    for scenario in scenarios:
        # Alternate A/B order deterministically to reduce warm-cache/order bias.
        first = "before" if int(hashlib.sha256(scenario["id"].encode()).hexdigest(), 16) % 2 == 0 else "after"
        variants = [first, "after" if first == "before" else "before"]
        for variant in variants:
            cursor += 1
            run_manifest["order"].append({"scenario": scenario["id"], "variant": variant})
            run_one(doc, scenario, variant, cursor, total)

    run_manifest["finished_at_epoch"] = time.time()
    run_manifest["elapsed_seconds"] = round(
        run_manifest["finished_at_epoch"] - run_manifest["started_at_epoch"], 3
    )
    (OUT / "run-manifest.json").write_text(
        json.dumps(run_manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Completed {total} isolated generations in {run_manifest['elapsed_seconds']}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
