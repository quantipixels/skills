#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, csv, hashlib, io, json, re, subprocess, sys, time, urllib.request, zlib
from pathlib import Path

PACKED_CASES = "".join(p.read_text(encoding="ascii").strip() for p in sorted(Path(__file__).parent.glob("cases.part*")))
DATA = json.loads(zlib.decompress(base64.b85decode(PACKED_CASES)).decode("utf-8"))
TOKEN_RE = re.compile(r"[A-Za-z0-9_+#.-]+")
SYSTEM = """You are executing exactly one QP agent skill in a clean isolated evaluation session.

The enclosed SKILL PACKAGE is binding for this response. Use only that package and the supplied exact environment evidence. Do not compare versions, critique the skill, mention evaluation, or claim to call tools. Return the next user-facing response that this skill should produce at this point.

Respect the skill's authority and interaction boundaries. For an interactive skill, return only the current round and wait. For a mutation-capable skill, describe the exact safe action, command, stop condition, or receipt that should occur; do not falsely claim an external mutation happened. Do not invent missing evidence. Keep the response complete enough to exercise the skill's owned result."""
URL = "http://127.0.0.1:8080/v1/chat/completions"

def git_show(ref: str, path: str) -> str | None:
    proc = subprocess.run(["git","show",f"{ref}:{path}"], text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return proc.stdout if proc.returncode == 0 else None

def skill_path(case: dict, rel: str) -> str:
    return f"skills/{case['group']}/{case['skill']}/{rel}"

def tokens(text: str) -> set[str]:
    return {x.lower() for x in TOKEN_RE.findall(text) if len(x) > 1}

def catalogue_extract(ref: str, case: dict, spec: dict) -> str:
    q=tokens(spec["query"])
    ranked=[]
    for rel in spec["paths"]:
        path=skill_path(case, rel)
        text=git_show(ref,path)
        if text is None:
            continue
        try:
            rows=list(csv.reader(io.StringIO(text)))
        except Exception:
            continue
        if not rows:
            continue
        header=rows[0]
        for index,row in enumerate(rows[1:],1):
            joined=" | ".join(row)
            rt=tokens(joined)
            overlap=len(q & rt)
            phrase=sum(1 for t in q if t in joined.lower())
            score=overlap*3+phrase
            if score:
                ranked.append((score,-index,path,header,row))
    ranked.sort(reverse=True)
    chosen=ranked[:int(spec.get("limit",8))]
    if not chosen:
        return ""
    lines=["# PRE-RETRIEVED LOCAL CATALOGUE EVIDENCE", f"Query: {spec['query']}"]
    seen=set()
    for score,_,path,header,row in chosen:
        key=(path,tuple(row))
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"\nSource: {path} | retrieval score: {score}")
        lines.append(" | ".join(header))
        lines.append(" | ".join(row))
    return "\n".join(lines)

def load_bundle(ref: str, case: dict) -> tuple[str,list[dict]]:
    pieces=[]
    manifest=[]
    for rel in case["paths"]:
        path=skill_path(case,rel)
        text=git_show(ref,path)
        if text is None:
            manifest.append({"path":path,"state":"absent"})
            continue
        manifest.append({"path":path,"state":"loaded","sha256":hashlib.sha256(text.encode()).hexdigest(),"chars":len(text)})
        pieces.append(f"\n===== FILE: {path} =====\n{text.rstrip()}\n")
    for spec in case.get("catalogues",[]):
        ext=catalogue_extract(ref,case,spec)
        if ext:
            pieces.append("\n===== ENVIRONMENT RESULT: BUNDLED SEARCH EVIDENCE =====\n"+ext+"\n")
    full="".join(pieces)
    bundle=full
    max_chars=105000
    if len(bundle)>max_chars:
        bundle=bundle[:80000]+"\n\n[PACKAGE CLIPPED FOR MODEL CONTEXT; MIDDLE OMITTED]\n\n"+bundle[-24000:]
        manifest.append({"state":"context_clip","original_chars":len(full),"delivered_chars":len(bundle)})
    return bundle,manifest

def call_model(messages: list[dict], max_tokens: int, seed: int) -> tuple[str,dict,float]:
    body=json.dumps({
        "model":"qwen2.5-3b-instruct-q4_k_m",
        "messages":messages,
        "temperature":0.1,
        "top_p":0.9,
        "max_tokens":max_tokens,
        "seed":seed,
        "stream":False
    }).encode()
    req=urllib.request.Request(URL,data=body,headers={"Content-Type":"application/json"})
    start=time.time()
    with urllib.request.urlopen(req,timeout=600) as response:
        payload=json.load(response)
    elapsed=time.time()-start
    return payload["choices"][0]["message"]["content"].strip(), payload.get("usage",{}), elapsed

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    out=Path(args.out)
    (out/"inputs").mkdir(parents=True,exist_ok=True)
    (out/"responses").mkdir(parents=True,exist_ok=True)
    results=[]
    failures=0
    for idx,case in enumerate(DATA["cases"]):
        order=["old","new"] if idx%2==0 else ["new","old"]
        for variant in order:
            ref=DATA["base"] if variant=="old" else DATA["head"]
            bundle,files=load_bundle(ref,case)
            user=f"""<skill-package>
{bundle}
</skill-package>

<exact-environment-evidence>
{case['fixture']}
</exact-environment-evidence>

<user-request>
{case['prompt']}
</user-request>"""
            case_dir=out/"inputs"/case["id"]
            case_dir.mkdir(parents=True,exist_ok=True)
            input_path=case_dir/f"{variant}.txt"
            input_path.write_text("SYSTEM\n"+SYSTEM+"\n\nUSER\n"+user,encoding="utf-8")
            record={
                "case_id":case["id"],"skill":case["skill"],"group":case["group"],"title":case["title"],
                "variant":variant,"ref":ref,"seed":41000+idx,"model":"Qwen2.5-3B-Instruct-GGUF Q4_K_M",
                "package_files":files,"input_sha256":hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "evaluation":case["evaluation"],"prompt":case["prompt"],"fixture":case["fixture"]
            }
            try:
                text,usage,elapsed=call_model(
                    [{"role":"system","content":SYSTEM},{"role":"user","content":user}],
                    int(case.get("max_tokens",600)),41000+idx
                )
                response_path=out/"responses"/f"{case['id']}--{variant}.txt"
                response_path.write_text(text,encoding="utf-8")
                record.update({"status":"ok","response":text,"response_sha256":hashlib.sha256(text.encode()).hexdigest(),"usage":usage,"elapsed_seconds":round(elapsed,3)})
                print(f"[{idx+1}/{len(DATA['cases'])}] {case['id']} {variant} OK {elapsed:.1f}s",flush=True)
            except Exception as exc:
                failures+=1
                record.update({"status":"error","error":repr(exc)})
                print(f"[{idx+1}/{len(DATA['cases'])}] {case['id']} {variant} ERROR {exc!r}",file=sys.stderr,flush=True)
            results.append(record)
            (out/"results.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in results)+"\n",encoding="utf-8")
    manifest={
        "baseline":DATA["base"],"candidate":DATA["head"],"cases":len(DATA["cases"]),
        "calls":len(results),"failures":failures,"model":"Qwen/Qwen2.5-3B-Instruct-GGUF:Q4_K_M",
        "runner":"llama.cpp OpenAI-compatible server","generation_order":"alternating old/new per case",
        "temperature":0.1,"evaluation_type":"actual isolated model inference"
    }
    (out/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    (out/"cases.json").write_text(json.dumps(DATA,ensure_ascii=False,indent=2),encoding="utf-8")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
