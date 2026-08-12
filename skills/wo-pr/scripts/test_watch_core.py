import json
import os
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from watch_core import (
    LeaseConflict,
    acquire_file_lease,
    acquire_lease,
    evaluate_snapshot,
    load_state,
    mark_action,
    new_state,
    pipeline_summary,
    record_read_error,
    record_retry,
    release_file_lease,
    save_state_atomic,
    validate_state_target,
)
from pr_watch import apply_state_updates, evaluate_and_save_state, main, make_provider, parse_args, target_identity


def snapshot(*, sha="abc", jobs=None, state="OPEN", reviews=None, complete=True):
    return {
        "provider": "github",
        "host": "github.com",
        "repository": "acme/widgets",
        "number": 42,
        "url": "https://github.com/acme/widgets/pull/42",
        "state": state,
        "merged": state == "MERGED",
        "closed": state == "CLOSED",
        "base": {"branch": "main", "sha": "base"},
        "head": {"branch": "feature", "sha": sha},
        "pipeline": {"evidence_complete": complete, "jobs": jobs or []},
        "review_items": reviews or [],
        "mergeability": "MERGEABLE",
        "review_decision": "",
        "capabilities": {},
        "errors": [],
    }


class PipelineSummaryTests(unittest.TestCase):
    def test_no_pipeline_is_not_vacuously_green(self):
        result = pipeline_summary([], evidence_complete=True)
        self.assertEqual("no_pipeline_evidence", result["state"])

    def test_explicit_no_pipeline_expectation_is_green(self):
        result = pipeline_summary([], evidence_complete=True, no_pipeline_expected=True)
        self.assertEqual("green", result["state"])

    def test_only_optional_neutral_skipped_manual_and_allowed_failure_are_non_errors(self):
        jobs = [
            {"name": "required", "status": "success", "required": True},
            {"name": "neutral", "status": "neutral", "required": False},
            {"name": "skipped", "status": "skipped", "required": False},
            {"name": "manual", "status": "manual", "required": False},
            {"name": "allowed", "status": "failure", "required": False, "allow_failure": True},
        ]
        self.assertEqual("green", pipeline_summary(jobs, evidence_complete=True)["state"])

    def test_required_manual_and_unknown_requiredness_block(self):
        required_manual = [{"name": "deploy", "status": "manual", "required": True}]
        unknown_requiredness = [{"name": "lint", "status": "neutral", "required": None}]
        self.assertEqual("pending", pipeline_summary(required_manual, evidence_complete=True)["state"])
        self.assertEqual("incomplete", pipeline_summary(unknown_requiredness, evidence_complete=True)["state"])

    def test_optional_running_or_failed_checks_do_not_block_required_pipeline(self):
        jobs = [
            {"name": "required", "status": "success", "required": True},
            {"name": "optional-running", "status": "running", "required": False},
            {"name": "optional-failed", "status": "failure", "required": False},
        ]
        self.assertEqual("green", pipeline_summary(jobs, evidence_complete=True)["state"])

    def test_required_neutral_check_is_successful_terminal_work(self):
        jobs = [{"name": "policy", "status": "neutral", "required": True}]

        self.assertEqual("green", pipeline_summary(jobs, evidence_complete=True)["state"])

    def test_required_skipped_check_requests_diagnosis_instead_of_flaky_retry(self):
        state = new_state(objective="until-merged")
        result = evaluate_snapshot(
            snapshot(jobs=[{"name": "policy", "status": "skipped", "required": True}]),
            state,
            now=10,
            authority={"retry-ci"},
        )

        self.assertEqual(["diagnose_ci_failure"], result["actions"])

    def test_required_neutral_check_can_complete_the_settle_window(self):
        state = new_state(objective="until-ready")
        current = snapshot(jobs=[{"name": "policy", "status": "neutral", "required": True}])

        first = evaluate_snapshot(current, state, now=1000, authority=set())
        threshold = evaluate_snapshot(current, state, now=1300, authority=set())
        settled = evaluate_snapshot(current, state, now=1360, authority=set())

        self.assertEqual(["ready_settling"], first["actions"])
        self.assertEqual(["ready_settling"], threshold["actions"])
        self.assertEqual(["stop_ready"], settled["actions"])


class EvaluationTests(unittest.TestCase):
    green_jobs = [{"name": "test", "status": "success", "required": True}]

    def test_until_ready_requires_a_confirmation_poll_after_five_quiet_minutes(self):
        state = new_state(objective="until-ready")
        first = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())
        self.assertFalse(first["terminal"])
        self.assertEqual(["ready_settling"], first["actions"])

        early = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1299, authority=set())
        self.assertFalse(early["terminal"])

        threshold = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1300, authority=set())
        self.assertFalse(threshold["terminal"])

        settled = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1360, authority=set())
        self.assertTrue(settled["terminal"])
        self.assertEqual("pipeline_ready", settled["reason"])

    def test_green_pipeline_does_not_settle_while_provider_readiness_is_blocked(self):
        cases = [
            ("draft", {"draft": True}, "draft_item"),
            ("conflict", {"mergeability": "CONFLICTING"}, "mergeability_blocker"),
            ("unknown mergeability", {"mergeability": "UNKNOWN"}, "incomplete_provider_evidence"),
            ("GitLab mergeability pending", {"mergeability": "checking"}, "incomplete_provider_evidence"),
            ("required review", {"review_decision": "REVIEW_REQUIRED"}, "review_requirement_blocker"),
            ("changes requested", {"review_decision": "CHANGES_REQUESTED"}, "review_requirement_blocker"),
            (
                "capability gap",
                {"capabilities": {"approval_state": False}},
                "incomplete_provider_evidence",
            ),
            ("provider error", {"errors": ["approval state unavailable"]}, "incomplete_provider_evidence"),
        ]

        for label, changes, reason in cases:
            with self.subTest(label=label):
                state = new_state(objective="until-ready")
                current = snapshot(jobs=self.green_jobs)
                current.update(changes)

                first = evaluate_snapshot(current, state, now=1000, authority=set())
                settled = evaluate_snapshot(current, state, now=1300, authority=set())

                self.assertNotIn("stop_ready", first["actions"])
                self.assertNotIn("stop_ready", settled["actions"])
                self.assertEqual(reason, settled["reason"])
                self.assertIsNone(state["settle"]["green_since"])

    def test_cleared_provider_blocker_starts_a_new_settle_window(self):
        state = new_state(objective="until-ready")
        evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())
        blocked = snapshot(jobs=self.green_jobs)
        blocked["draft"] = True
        evaluate_snapshot(blocked, state, now=1299, authority=set())

        result = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1300, authority=set())

        self.assertFalse(result["terminal"])
        self.assertEqual(["ready_settling"], result["actions"])
        self.assertEqual(1300, state["settle"]["green_since"])

    def test_review_activity_resets_the_settle_window(self):
        state = new_state(objective="until-ready")
        evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())

        result = evaluate_snapshot(
            snapshot(jobs=self.green_jobs, reviews=[{"id": "review:7", "body": "Please fix"}]),
            state,
            now=1299,
            authority=set(),
        )

        self.assertEqual(["process_review_comment"], result["actions"])
        self.assertIsNone(state["settle"]["green_since"])

    def test_review_after_the_five_minute_threshold_cancels_confirmation(self):
        state = new_state(objective="until-ready")
        evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())
        threshold = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1300, authority=set())
        self.assertFalse(threshold["terminal"])

        review = evaluate_snapshot(
            snapshot(jobs=self.green_jobs, reviews=[{"id": "review:8", "body": "Late feedback"}]),
            state,
            now=1313,
            authority=set(),
        )
        restarted = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1360, authority=set())

        self.assertEqual(["process_review_comment"], review["actions"])
        self.assertFalse(restarted["terminal"])
        self.assertEqual(1360, state["settle"]["green_since"])

    def test_new_sha_or_job_resets_settle(self):
        state = new_state(objective="until-ready")
        evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())
        changed = snapshot(sha="def", jobs=self.green_jobs + [{"name": "lint", "status": "success", "required": True}])
        result = evaluate_snapshot(changed, state, now=1301, authority=set())
        self.assertFalse(result["terminal"])
        self.assertEqual(1301, state["settle"]["green_since"])

    def test_replaced_green_job_resets_settle(self):
        state = new_state(objective="until-ready")
        first_job = [{"id": "attempt-1", "name": "test", "status": "success", "required": True}]
        evaluate_snapshot(snapshot(jobs=first_job), state, now=1000, authority=set())

        replacement = [{"id": "attempt-2", "name": "test", "status": "success", "required": True}]
        result = evaluate_snapshot(snapshot(jobs=replacement), state, now=1300, authority=set())

        self.assertFalse(result["terminal"])
        self.assertEqual(1300, state["settle"]["green_since"])

    def test_failed_snapshot_breaks_green_settle_window(self):
        state = new_state(objective="until-ready")
        evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1000, authority=set())
        failed = [{"name": "test", "status": "failure", "required": True}]
        evaluate_snapshot(snapshot(jobs=failed), state, now=1100, authority=set())
        result = evaluate_snapshot(snapshot(jobs=self.green_jobs), state, now=1300, authority=set())
        self.assertFalse(result["terminal"])
        self.assertEqual(1300, state["settle"]["green_since"])

    def test_review_activity_has_priority_over_retry(self):
        state = new_state(objective="until-merged")
        failed = [{"name": "test", "status": "failure", "required": True, "failure_kind": "flaky"}]
        result = evaluate_snapshot(
            snapshot(jobs=failed, reviews=[{"id": "review:7", "body": "Please fix"}]),
            state,
            now=1000,
            authority={"retry-ci"},
        )
        self.assertEqual("process_review_comment", result["actions"][0])

    def test_explicitly_incomplete_review_resolution_is_a_blocker(self):
        state = new_state(objective="until-ready")
        current = snapshot(jobs=self.green_jobs)
        current["capabilities"]["review_thread_resolution"] = False
        result = evaluate_snapshot(current, state, now=1000, authority=set())
        self.assertTrue(result["terminal"])
        self.assertEqual("incomplete_review_evidence", result["reason"])

    def test_terminal_provider_state_outranks_pending_work(self):
        state = new_state(objective="until-stopped")
        result = evaluate_snapshot(snapshot(state="MERGED", reviews=[{"id": "x"}]), state, now=10, authority=set())
        self.assertTrue(result["terminal"])
        self.assertEqual(["stop_pr_closed"], result["actions"])

    def test_retry_budget_is_per_sha(self):
        state = new_state(objective="until-merged")
        for _ in range(3):
            record_retry(state, "abc")
        failed = [{"name": "test", "status": "failure", "required": True, "failure_kind": "flaky"}]
        exhausted = evaluate_snapshot(snapshot(jobs=failed), state, now=10, authority={"retry-ci"})
        self.assertTrue(exhausted["terminal"])
        self.assertEqual("retry_budget_exhausted", exhausted["reason"])
        self.assertEqual(0, state["retry_counts"].get("def", 0))

    def test_surfaced_and_claimed_actions_remain_unhandled_after_restart(self):
        state = new_state(objective="until-merged")
        mark_action(state, "review:7", "surfaced")
        first = evaluate_snapshot(snapshot(reviews=[{"id": "review:7"}]), state, now=10, authority=set())
        self.assertIn("process_review_comment", first["actions"])
        mark_action(state, "review:7", "claimed")
        second = evaluate_snapshot(snapshot(reviews=[{"id": "review:7"}]), state, now=20, authority=set())
        self.assertIn("process_review_comment", second["actions"])
        mark_action(state, "review:7", "handled")
        third = evaluate_snapshot(snapshot(reviews=[{"id": "review:7"}]), state, now=30, authority=set())
        self.assertNotIn("process_review_comment", third["actions"])

    def test_edited_handled_feedback_is_surfaced_again(self):
        state = new_state(objective="until-merged")
        first_item = {"id": "review:7", "body": "First request", "updated_at": "2026-08-12T10:00:00Z"}
        evaluate_snapshot(snapshot(reviews=[first_item]), state, now=10, authority=set())
        mark_action(state, "review:7", "handled", now=20)
        unchanged = evaluate_snapshot(snapshot(reviews=[first_item]), state, now=30, authority=set())
        self.assertNotIn("process_review_comment", unchanged["actions"])
        edited = {"id": "review:7", "body": "Different request", "updated_at": "2026-08-12T10:05:00Z"}
        changed = evaluate_snapshot(snapshot(reviews=[edited]), state, now=40, authority=set())
        self.assertIn("process_review_comment", changed["actions"])


class PersistenceAndLeaseTests(unittest.TestCase):
    def test_atomic_round_trip_and_schema_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-ready")
            save_state_atomic(path, state)
            self.assertEqual(state, load_state(path))
            path.write_text(json.dumps({"schema_version": 999}), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_state(path)

    def test_active_lease_conflicts_and_dead_same_host_recovers(self):
        state = new_state(objective="until-ready")
        host = socket.gethostname()
        acquire_lease(state, owner="one", host=host, pid=os.getpid(), now=10, process_alive=lambda _: True)
        with self.assertRaises(LeaseConflict):
            acquire_lease(state, owner="two", host=host, pid=999999, now=11, process_alive=lambda _: True)
        recovered = acquire_lease(
            state,
            owner="two",
            host=host,
            pid=os.getpid(),
            now=20,
            process_alive=lambda _: False,
        )
        self.assertEqual("recovered", recovered)

    def test_cross_host_lease_needs_explicit_takeover(self):
        state = new_state(objective="until-ready")
        acquire_lease(state, owner="one", host="other-host", pid=1, now=0)
        with self.assertRaises(LeaseConflict):
            acquire_lease(state, owner="two", host="this-host", pid=2, now=600)
        self.assertEqual("taken_over", acquire_lease(state, owner="two", host="this-host", pid=2, now=600, takeover=True))

    def test_file_lease_is_an_atomic_single_owner_claim(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "target.lease"
            self.assertEqual("acquired", acquire_file_lease(path, owner="one", pid=os.getpid()))
            with self.assertRaises(LeaseConflict):
                acquire_file_lease(path, owner="two", pid=os.getpid())
            release_file_lease(path, owner="one")
            self.assertEqual("acquired", acquire_file_lease(path, owner="two", pid=os.getpid()))

    def test_file_lease_recovers_a_dead_same_host_owner(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "target.lease"
            acquire_file_lease(path, owner="dead", pid=999999, process_alive=lambda _: True)
            result = acquire_file_lease(path, owner="new", pid=os.getpid(), process_alive=lambda _: False)
            self.assertEqual("recovered", result)

    def test_file_lease_takeover_has_no_unlink_window(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "target.lease"
            acquire_file_lease(path, owner="old", pid=os.getpid())

            with patch("watch_core.os.unlink", wraps=os.unlink) as unlink:
                result = acquire_file_lease(path, owner="new", pid=os.getpid(), takeover=True)

            self.assertEqual("taken_over", result)
            self.assertFalse(any(Path(args[0]) == path for args, _kwargs in unlink.call_args_list))
            self.assertEqual("new", json.loads(path.read_text(encoding="utf-8"))["owner"])

    def test_watcher_that_lost_file_lease_cannot_renew(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "target.lease"
            acquire_file_lease(path, owner="one", host="host-one", pid=1)
            acquire_file_lease(path, owner="two", host="host-two", pid=2, takeover=True)

            with self.assertRaises(LeaseConflict):
                acquire_file_lease(path, owner="one", host="host-one", pid=1)

            release_file_lease(path, owner="one")
            self.assertEqual("two", json.loads(path.read_text(encoding="utf-8"))["owner"])

    def test_state_only_updates_record_action_and_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            save_state_atomic(path, new_state(objective="until-merged"))
            result = apply_state_updates(path, marks=["review:7=handled"], retry_sha="abc", now=50)
            loaded = load_state(path)
            self.assertEqual("handled", loaded["actions"]["review:7"]["phase"])
            self.assertEqual(1, loaded["retry_counts"]["abc"])
            self.assertEqual(1, result["retry_count"])

    def test_recorded_failure_classification_reaches_runtime_policy(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "abc"
            save_state_atomic(path, state)
            apply_state_updates(
                path,
                marks=[],
                retry_sha=None,
                failure_classifications=[["abc", "job-1", "flaky"]],
                now=50,
            )

            _state, result = evaluate_and_save_state(
                path,
                state,
                snapshot(jobs=[{"id": "job-1", "name": "test", "status": "failure", "required": True}]),
                now=60,
                authority={"retry-ci"},
            )

            self.assertEqual(["retry_failed_checks"], result["actions"])
            self.assertEqual("flaky", result["snapshot"]["pipeline"]["jobs"][0]["failure_kind"])

    def test_recording_a_retry_consumes_failure_classifications_for_that_head(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "abc"
            save_state_atomic(path, state)
            apply_state_updates(
                path,
                marks=[],
                retry_sha=None,
                failure_classifications=[["abc", "job-1", "flaky"]],
                now=50,
            )

            apply_state_updates(
                path,
                marks=[],
                retry_sha="abc",
                failure_classifications=[],
                now=60,
            )

            self.assertNotIn("abc", load_state(path)["failure_classifications"])

    def test_partial_failure_classification_still_requests_diagnosis(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "abc"
            save_state_atomic(path, state)
            apply_state_updates(
                path,
                marks=[],
                retry_sha=None,
                failure_classifications=[["abc", "job-1", "flaky"]],
                now=50,
            )

            _state, result = evaluate_and_save_state(
                path,
                state,
                snapshot(jobs=[
                    {"id": "job-1", "name": "test", "status": "failure", "required": True},
                    {"id": "job-2", "name": "lint", "status": "failure", "required": True},
                ]),
                now=60,
                authority={"retry-ci"},
            )

            self.assertEqual(["diagnose_ci_failure"], result["actions"])

    def test_recorded_classification_drives_branch_and_blocker_actions(self):
        cases = [
            ("branch", ["fix_branch_failure"], "branch_failure", False),
            ("infrastructure", ["user_help_required"], "infrastructure_failure", True),
            ("ambiguous", ["user_help_required"], "ambiguous_ci_failure", True),
        ]
        for kind, actions, reason, terminal in cases:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "state.json"
                state = new_state(objective="until-merged")
                state["current_head"] = "abc"
                save_state_atomic(path, state)
                apply_state_updates(
                    path,
                    marks=[],
                    retry_sha=None,
                    failure_classifications=[["abc", "job-1", kind]],
                    now=50,
                )

                _state, result = evaluate_and_save_state(
                    path,
                    state,
                    snapshot(jobs=[
                        {"id": "job-1", "name": "test", "status": "failure", "required": True}
                    ]),
                    now=60,
                    authority={"retry-ci"},
                )

                self.assertEqual(actions, result["actions"])
                self.assertEqual(reason, result["reason"])
                self.assertEqual(terminal, result["terminal"])

    def test_mixed_branch_and_flaky_classifications_select_the_branch_fix_first(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "abc"
            save_state_atomic(path, state)
            apply_state_updates(
                path,
                marks=[],
                retry_sha=None,
                failure_classifications=[
                    ["abc", "job-1", "branch"],
                    ["abc", "job-2", "flaky"],
                ],
                now=50,
            )

            _state, result = evaluate_and_save_state(
                path,
                state,
                snapshot(jobs=[
                    {"id": "job-1", "name": "test", "status": "failure", "required": True},
                    {"id": "job-2", "name": "lint", "status": "failure", "required": True},
                ]),
                now=60,
                authority={"retry-ci", "fix-commit-push"},
            )

            self.assertEqual(["fix_branch_failure"], result["actions"])

    def test_optional_failed_job_does_not_require_failure_classification(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "abc"
            save_state_atomic(path, state)
            apply_state_updates(
                path,
                marks=[],
                retry_sha=None,
                failure_classifications=[["abc", "required-job", "flaky"]],
                now=50,
            )

            _state, result = evaluate_and_save_state(
                path,
                state,
                snapshot(jobs=[
                    {
                        "id": "required-job", "name": "test", "status": "failure",
                        "required": True, "allow_failure": False,
                    },
                    {
                        "id": "optional-job", "name": "preview", "status": "failure",
                        "required": False, "allow_failure": False,
                    },
                ]),
                now=60,
                authority={"retry-ci"},
            )

            self.assertEqual(["retry_failed_checks"], result["actions"])

    def test_gitlab_can_be_merged_fallback_allows_settlement(self):
        state = new_state(objective="until-ready")
        current = snapshot(jobs=[{"name": "test", "status": "success", "required": True}])
        current["provider"] = "gitlab"
        current["mergeability"] = "can_be_merged"

        result = evaluate_snapshot(current, state, now=1000, authority=set())

        self.assertEqual(["ready_settling"], result["actions"])

    def test_failure_classification_rejects_a_stale_head(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            state = new_state(objective="until-merged")
            state["current_head"] = "new-head"
            save_state_atomic(path, state)

            with self.assertRaisesRegex(ValueError, "does not match current head"):
                apply_state_updates(
                    path,
                    marks=[],
                    retry_sha=None,
                    failure_classifications=[["old-head", "job-1", "flaky"]],
                    now=50,
                )

    def test_watcher_save_reloads_a_state_only_update(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            save_state_atomic(path, new_state(objective="until-merged"))
            stale_watcher_state = load_state(path)
            apply_state_updates(path, marks=["review:7=handled"], retry_sha=None, now=50)

            evaluate_and_save_state(
                path,
                stale_watcher_state,
                snapshot(jobs=[{"name": "test", "status": "success", "required": True}]),
                now=60,
                authority=set(),
            )

            self.assertEqual("handled", load_state(path)["actions"]["review:7"]["phase"])

    def test_watcher_reload_records_only_current_invocation_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            prior = new_state(objective="until-merged")
            prior["authority_observed"] = ["fix-commit-push"]
            prior["lease_state"] = "old"
            save_state_atomic(path, prior)

            state, _result = evaluate_and_save_state(
                path,
                prior,
                snapshot(jobs=[{"name": "test", "status": "success", "required": True}]),
                now=60,
                authority={"observe"},
                lease_state="acquired",
            )

            self.assertEqual(["observe"], state["authority_observed"])
            self.assertEqual("acquired", state["lease_state"])

    def test_successful_fetch_clears_persisted_read_errors_under_the_update_lock(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "state.json"
            persisted = new_state(objective="until-merged")
            record_read_error(persisted, "first", now=10)
            record_read_error(persisted, "second", now=20)
            save_state_atomic(path, persisted)
            stale_watcher_state = load_state(path)
            stale_watcher_state["read_errors"] = {"consecutive": 0, "last": None}

            evaluate_and_save_state(
                path,
                stale_watcher_state,
                snapshot(jobs=[{"name": "test", "status": "success", "required": True}]),
                now=30,
                authority=set(),
            )

            self.assertEqual(
                {"consecutive": 0, "last": None},
                load_state(path)["read_errors"],
            )

    def test_loaded_state_rejects_a_different_canonical_target(self):
        state = new_state(objective="until-ready")
        state["target"] = {
            "provider": "github", "host": "github.com", "repository": "acme/other",
            "number": 7, "url": "https://github.com/acme/other/pull/7",
        }
        with self.assertRaises(ValueError):
            validate_state_target(state, snapshot())


class TargetIdentityTests(unittest.TestCase):
    def test_github_url_resolves_enterprise_host_and_repository(self):
        identity = target_identity("https://github.acme.test/payments/api/pull/42", provider="auto")
        self.assertEqual("github", identity["provider"])
        self.assertEqual("github.acme.test", identity["host"])
        self.assertEqual("payments/api", identity["repository"])

    def test_gitlab_url_resolves_self_managed_host_and_nested_project(self):
        identity = target_identity("https://gitlab.acme.test/group/subgroup/api/-/merge_requests/9", provider="auto")
        self.assertEqual("gitlab", identity["provider"])
        self.assertEqual("gitlab.acme.test", identity["host"])
        self.assertEqual("group/subgroup/api", identity["repository"])

    def test_gitlab_trusted_host_flag_reaches_the_provider(self):
        args = parse_args([
            "--provider", "gitlab",
            "--pr", "https://gitlab.acme.test/group/api/-/merge_requests/9",
            "--trusted-gitlab-host", "gitlab.acme.test",
            "--once",
        ])

        provider = make_provider(args)

        self.assertEqual({"gitlab.com", "gitlab.acme.test"}, provider.trusted_hosts)


class WatchLoopLeaseTests(unittest.TestCase):
    def test_takeover_is_used_once_and_file_ownership_is_renewed(self):
        current = snapshot(jobs=[{"name": "test", "status": "pending", "required": True}])

        class Provider:
            def fetch(self, _target):
                return current

        file_takeovers = []
        embedded_takeovers = []

        def acquire(_path, **kwargs):
            file_takeovers.append(kwargs["takeover"])
            return "taken_over" if len(file_takeovers) == 1 else "renewed"

        def evaluate(_path, state, _snapshot, **kwargs):
            embedded_takeovers.append(kwargs["takeover"])
            state["lease_state"] = "taken_over"
            state["lease"] = {"owner": "test-owner"}
            return state, {"terminal": False, "next_poll_seconds": 0}

        with tempfile.TemporaryDirectory() as directory, patch(
            "pr_watch.make_provider", return_value=Provider()
        ), patch("pr_watch.acquire_file_lease", side_effect=acquire), patch(
            "pr_watch.evaluate_and_save_state", side_effect=evaluate
        ), patch("pr_watch.release_file_lease"), patch("pr_watch.emit"):
            result = main([
                "--provider", "github",
                "--pr", "42",
                "--repo", "acme/widgets",
                "--state-file", str(Path(directory) / "state.json"),
                "--watch",
                "--takeover",
                "--max-snapshots", "2",
            ])

        self.assertEqual(0, result)
        self.assertEqual([True, False], file_takeovers)
        self.assertEqual([True, False], embedded_takeovers)

    def test_watcher_stops_when_it_loses_file_ownership_before_the_second_poll(self):
        current = snapshot(jobs=[{"name": "test", "status": "pending", "required": True}])

        class Provider:
            def fetch(self, _target):
                return current

        file_takeovers = []
        evaluations = []

        def acquire(_path, **kwargs):
            file_takeovers.append(kwargs["takeover"])
            if len(file_takeovers) == 2:
                raise LeaseConflict("lease replaced by another watcher")
            return "taken_over"

        def evaluate(_path, state, _snapshot, **kwargs):
            evaluations.append(kwargs["takeover"])
            state["lease"] = {"owner": "test-owner"}
            return state, {"terminal": False, "next_poll_seconds": 0}

        with tempfile.TemporaryDirectory() as directory, patch(
            "pr_watch.make_provider", return_value=Provider()
        ), patch("pr_watch.acquire_file_lease", side_effect=acquire), patch(
            "pr_watch.evaluate_and_save_state", side_effect=evaluate
        ), patch("pr_watch.release_file_lease"), patch("pr_watch.emit"):
            result = main([
                "--provider", "github",
                "--pr", "42",
                "--repo", "acme/widgets",
                "--state-file", str(Path(directory) / "state.json"),
                "--watch",
                "--takeover",
                "--max-snapshots", "2",
            ])

        self.assertEqual(3, result)
        self.assertEqual([True, False], file_takeovers)
        self.assertEqual([True], evaluations)


if __name__ == "__main__":
    unittest.main()
