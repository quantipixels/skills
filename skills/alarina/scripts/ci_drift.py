"""Read-only CI inventory and drift facts. Judgment and merge policy stay with the owner."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
from urllib.parse import quote

from project_context import ContextError, load_context, read_json


def _yaml(text: str):
    # A maintained YAML parser is an optional capability for this operation;
    # other installed utilities retain their standard-library-only runtime.
    try:
        import yaml
    except ImportError as error:
        raise ContextError("CI workflow inspection requires project-provided PyYAML; no dependency was installed") from error

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError("duplicate YAML key")
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    try:
        return yaml.load(text, Loader=UniqueLoader)
    except (yaml.YAMLError, ValueError, TypeError, RecursionError) as error:
        raise ContextError("workflow is not a supported unambiguous YAML mapping") from error


def invocation_hints(command: str, checks: list[dict]) -> dict:
    """Recognize literal commands only; a source hint never establishes execution."""
    try:
        argv = shlex.split(command)
    except ValueError:
        return {"check_ids": [], "kind": "unresolved-shell"}
    if not argv or any(x in command for x in ("\n", "&&", "||", ";", "|", "`", "$(", "${{")):
        return {"check_ids": [], "kind": "unresolved-shell"}
    known = {check["id"] for check in checks}
    if len(argv) > 2 and Path(argv[0]).name in {"python", "python3"} and Path(argv[1]).name == "alarina.py" and argv[2] == "verify":
        # Only the current project invocation can refer to this inventory.
        if argv.count("--project") != 1 or any(x.startswith("--project=") for x in argv) or argv.index("--project") + 1 >= len(argv) or argv[argv.index("--project") + 1] != ".":
            return {"check_ids": [], "kind": "other-project-or-unresolved"}
        selected = [argv[i + 1] for i, value in enumerate(argv[:-1]) if value == "--check"]
        if "--check" in argv and (argv[-1] == "--check" or not selected or any(x not in known for x in selected)):
            return {"check_ids": [], "kind": "invalid-check-selection"}
        return {"check_ids": sorted(set(selected) if selected else known), "kind": "shared-gate-invocation"}
    matched = [check["id"] for check in checks if check["argv"] == argv and check.get("cwd", ".") == "."]
    return {"check_ids": matched, "kind": "literal-command" if matched else "unmapped-command"}


def workflow_inventory(project: Path, checks: list[dict]) -> tuple[list, list]:
    directory = project / ".github/workflows"
    workflows, gaps = [], []
    if directory.is_symlink() or (directory.exists() and directory.resolve() != directory):
        raise ContextError("workflow directory cannot use symlink components")
    files = sorted(directory.glob("*.yml")) + sorted(directory.glob("*.yaml"))
    if len(files) > 100:
        raise ContextError("more than 100 workflows; choose a bounded project scope")
    for path in files:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 1024 * 1024:
            raise ContextError("workflow must be a regular file of at most 1 MiB")
        data = path.read_bytes()
        doc = _yaml(data.decode("utf-8"))
        if not isinstance(doc, dict) or not isinstance(doc.get("jobs"), dict):
            raise ContextError("workflow requires a jobs mapping")
        item = {"path": str(path.relative_to(project)), "sha256": hashlib.sha256(data).hexdigest(), "jobs": []}
        workflows.append(item)
        for identity, job in doc["jobs"].items():
            if not isinstance(identity, str) or not isinstance(job, dict):
                raise ContextError("workflow job must have a string ID and mapping body")
            record = {"id": identity, "name": job.get("name", identity), "condition": job.get("if"),
                      "runs_on": job.get("runs-on"), "matrix": job.get("strategy", {}).get("matrix") if isinstance(job.get("strategy", {}), dict) else None,
                      "uses": job.get("uses"), "steps": []}
            item["jobs"].append(record)
            if job.get("uses"):
                gaps.append({"kind": "reusable_workflow_requires_tracing", "workflow": item["path"], "job": identity, "uses": job["uses"]})
            steps = job.get("steps", [])
            if not isinstance(steps, list):
                raise ContextError("workflow steps must be a list")
            for index, step in enumerate(steps):
                if not isinstance(step, dict):
                    raise ContextError("workflow step must be a mapping")
                command = step.get("run")
                if command is not None and not isinstance(command, str):
                    raise ContextError("workflow run must be text")
                # Preserve conditions and environment declarations, not values of
                # env/secrets or complete shell bodies in the report.
                value = {"index": index, "name": step.get("name"), "condition": step.get("if"), "uses": step.get("uses")}
                if command:
                    value.update(invocation_hints(command.strip(), checks))
                    defaults = job.get("defaults", doc.get("defaults", {}))
                    default_cwd = defaults.get("run", {}).get("working-directory") if isinstance(defaults, dict) and isinstance(defaults.get("run", {}), dict) else None
                    value["working_directory"] = step.get("working-directory", default_cwd or ".")
                    if value["working_directory"] != ".":
                        value.update(check_ids=[], kind="other-working-directory")
                    value["command_sha256"] = hashlib.sha256(command.encode()).hexdigest()
                record["steps"].append(value)
    return workflows, gaps


def _api(endpoint: str) -> tuple[object | None, str | None]:
    try:
        result = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None, "unavailable"
    if result.returncode:
        return None, "not_found" if "HTTP 404" in result.stderr else "unavailable"
    if len(result.stdout) > 4 * 1024 * 1024:
        return None, "oversized"
    try:
        return json.loads(result.stdout), None
    except ValueError:
        return None, "invalid_response"


def provider_policy(repo: str, branch: str, transport=_api) -> dict:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) or any(x in {".", ".."} for x in repo.split("/")):
        raise ContextError("repository must be OWNER/NAME")
    if not branch or any(ord(c) < 32 for c in branch):
        raise ContextError("branch must be a nonempty branch name")
    prefix = f"repos/{repo}"
    branch_path = quote(branch, safe="")
    metadata, error = transport(f"{prefix}/branches/{branch_path}")
    result = {"repo": repo, "branch": branch, "state": "unknown", "required_checks": [], "gaps": []}
    if error or not isinstance(metadata, dict) or metadata.get("name") != branch:
        result["gaps"].append("branch existence/access not established")
        return result
    rules, rules_error = transport(f"{prefix}/rules/branches/{branch_path}")
    protection, protection_error = transport(f"{prefix}/branches/{branch_path}/protection")
    if rules_error or not isinstance(rules, list):
        result["gaps"].append("effective rules unavailable")
    if protection_error not in {None, "not_found"}:
        result["gaps"].append("legacy protection unavailable")
    names = set()
    if isinstance(rules, list):
        for rule in rules:
            if not isinstance(rule, dict) or not isinstance(rule.get("type"), str):
                result["gaps"].append("effective rule shape invalid")
                continue
            if isinstance(rule, dict) and rule.get("type") == "required_status_checks":
                parameters = rule.get("parameters", {})
                required = parameters.get("required_status_checks") if isinstance(parameters, dict) else None
                if not isinstance(required, list):
                    result["gaps"].append("required rule checks unavailable")
                    continue
                for item in required:
                    if isinstance(item, dict) and isinstance(item.get("context"), str):
                        names.add(item["context"])
                    else:
                        result["gaps"].append("required rule check shape invalid")
    if protection_error is None:
        if not isinstance(protection, dict):
            result["gaps"].append("legacy protection response invalid")
        else:
            required = protection.get("required_status_checks") or {}
            if isinstance(required, dict):
                contexts, checks = required.get("contexts", []), required.get("checks", [])
                if not isinstance(contexts, list) or not isinstance(checks, list):
                    result["gaps"].append("legacy required check shape invalid")
                else:
                    if any(not isinstance(x, str) for x in contexts) or any(not isinstance(x, dict) or not isinstance(x.get("context"), str) for x in checks):
                        result["gaps"].append("legacy required check entry invalid")
                    names.update(x for x in contexts if isinstance(x, str))
                    names.update(x["context"] for x in checks if isinstance(x, dict) and isinstance(x.get("context"), str))
            else:
                result["gaps"].append("legacy required checks unavailable")
    result["required_checks"] = sorted(names)
    if not result["gaps"]:
        result["state"] = "required_checks_observed" if names else "no_required_checks_observed"
    result["limits"] = ["Branch rules may have bypass actors and other merge conditions; this is not a mergeability or permission decision."]
    return result


def inspect_ci(project: Path, *, baseline: dict | None = None, repo: str | None = None,
               branch: str | None = None, transport=_api) -> dict:
    context = load_context(project)
    root = Path(context["project"]["root"])
    checks = context["config"]["checks"]
    workflows, gaps = workflow_inventory(root, checks)
    hinted = {identity for workflow in workflows for job in workflow["jobs"] for step in job["steps"] for identity in step.get("check_ids", [])}
    for check in checks:
        if check["id"] not in hinted:
            gaps.append({"kind": "local_check_without_literal_ci_match", "check": check["id"], "recommendation": "Trace wrappers/reusable workflows before adding or removing a job."})
    if bool(repo) != bool(branch):
        raise ContextError("provider inspection requires both --repo and --branch")
    policy = provider_policy(repo, branch, transport) if repo else {"state": "not_observed", "required_checks": []}
    if policy["state"] != "required_checks_observed":
        gaps.append({"kind": "provider_required_checks", "state": policy["state"]})
    static_names = {job["name"] for workflow in workflows for job in workflow["jobs"]
                    if isinstance(job["name"], str) and "${{" not in job["name"] and job["matrix"] is None}
    matches = [{"required_check": name,
                "source_match": "declared-job-name" if name in static_names else "requires-tracing"}
               for name in policy["required_checks"]]
    for match in matches:
        if match["source_match"] == "requires-tracing":
            gaps.append({"kind": "required_check_without_static_job_match", "check": match["required_check"],
                         "recommendation": "Resolve matrix names, external providers and retired jobs against current provider results."})
    current = {"checks": checks, "remote_checks": context["config"]["remote_checks"],
               "workflows": workflows, "provider": policy}
    changes = []
    if baseline is not None:
        if baseline.get("schema_version") != 1 or baseline.get("project_id") != context["project"]["id"] or not isinstance(baseline.get("inventory"), dict):
            raise ContextError("baseline must be this project's CI inspection record")
        for key, value in current.items():
            if baseline["inventory"].get(key) != value:
                changes.append(key)
    return {"schema_version": 1, "project_id": context["project"]["id"],
            "observed_at": datetime.now(timezone.utc).isoformat(), "inventory": current,
            "provider_check_matches": matches,
            "changes_since_baseline": changes, "baseline_compared": baseline is not None,
            "gaps": gaps, "status": "attention" if gaps or changes else "inspected",
            "limits": ["Literal invocation matches are source leads, not proof of execution, semantic coverage or enforced merge gates.",
                       "Conditions, matrices and reusable workflows require owner review; this tool does not evaluate GitHub expressions.",
                       "External actions, services, credentials and unregistered product obligations may add missing proof."], "writes": False}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--repo")
    parser.add_argument("--branch")
    args = parser.parse_args(argv)
    try:
        result = inspect_ci(args.project, baseline=read_json(args.baseline) if args.baseline else None,
                            repo=args.repo, branch=args.branch)
        print(json.dumps(result, indent=2, default=str))
        return 1 if result["status"] == "attention" else 0
    except (ContextError, OSError, ValueError, TypeError, RecursionError) as error:
        print(json.dumps({"status": "invalid-or-blocked", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
