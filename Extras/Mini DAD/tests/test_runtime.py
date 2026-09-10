from __future__ import annotations

import json, os, subprocess, sys, threading, unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import runtime

def packet(**changes):
    row = {"source_instance_id":"test-instance","source_session_ref":"session-001","source_locator_hash":"sha256:" + "a" * 64,"failure_key":"runtime.missing-provenance","safe_summary":"Synthetic candidate catches missing provenance.","category":"harness","state":"actionable_candidate","impact":"medium","reuse_scope":"team_catalog","evidence_refs":["evidence://synthetic/provenance"],"linked_asset_ids":["albert:harness:adversarial-review"],"typed_links":[{"type":"uses_asset","target_id":"albert:harness:adversarial-review"}]}
    row.update(changes); return row

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.catalog = HERE / "catalog.json"; self.old = dict(os.environ)
        os.environ["ALBERT_LESSON_INTAKE_ENABLED"] = "true"; os.environ["ALBERT_LESSON_REVIEW_ENABLED"] = "true"
        class MemoryStore(runtime.LessonStore):
            def __init__(self, root): super().__init__(root); self.memory = {}
            def _rows(self, path): return list(self.memory.get(path.name, []))
            def _hold_lock(self): return os.open(os.devnull, os.O_WRONLY)
            def _append_unlocked(self, path, row): self.memory.setdefault(path.name, []).append(dict(row))
        self.store = MemoryStore(HERE)
    def tearDown(self):
        os.environ.clear(); os.environ.update(self.old)
    def test_search_content_typed_edges_and_lifecycle(self):
        catalog = runtime.Catalog.load(self.catalog)
        self.assertGreaterEqual(len(catalog.assets), 14)
        self.assertIn("albert:agent:subagent-improver", [row["id"] for row in catalog.search("subagent review")])
        self.assertIn("content", runtime.dispatch("GetAssetContent", {"asset_id":"albert:protocol:lesson-intake"}, self.catalog))
        self.assertTrue(runtime.dispatch("GetLifecycleStatus", {}, self.catalog)["all_evidence_unexpired"])
        with self.assertRaises(runtime.AssetError): runtime.dispatch("SearchAssets", {"query":"review", "extra": True}, self.catalog)

    def test_ai_front_door_inventory_is_present(self):
        front_door = (HERE / "AI_FRONT_DOOR.md").read_text(encoding="utf-8")
        for name in ("SearchAssets", "GetAsset", "GetNeighbors", "GetAssetContent", "GetLifecycleStatus", "GetRuntimeStatus", "GetLessonCandidate", "SubmitLessonCandidate"):
            self.assertIn(name, front_door)
        for endpoint in ("/mcp", "/api/tools/{tool}", "/openapi.json", "/healthz"):
            self.assertIn(endpoint, front_door)
    def test_stale_date_and_requires_cycle_are_rejected_or_reported(self):
        data = json.loads(self.catalog.read_text()); data["assets"][0]["evidence_expires_on"] = "2001-01-01"
        with patch("runtime._json", return_value=data): self.assertEqual("stale", runtime.Catalog.load(self.catalog).lifecycle(data["assets"][0]["id"])["assets"][0]["evidence_state"])
        data["edges"].append({"source":"albert:workflow:independent-review","target":"albert:harness:adversarial-review","type":"requires","evidence":"synthetic cycle","review_status":"candidate"})
        data["edges"].append({"source":"albert:protocol:asset-lifecycle","target":"albert:protocol:lesson-intake","type":"requires","evidence":"synthetic cycle","review_status":"candidate"})
        with patch("runtime._json", return_value=data):
            with self.assertRaisesRegex(runtime.AssetError, "cycle"): runtime.Catalog.load(self.catalog)
    def test_submission_dispositions_and_distinct_review(self):
        catalog = runtime.Catalog.load(self.catalog); first = self.store.submit(packet(), catalog); self.assertEqual("candidate", first["outcome"])
        duplicate = self.store.submit(packet(), catalog); self.assertEqual("duplicate", duplicate["outcome"]); self.assertFalse(duplicate["automatic_quality_change"])
        recurrence = self.store.submit(packet(recurs_after_claimed_fix_of=first["candidate_id"], evidence_refs=["evidence://synthetic/recurrence"]), catalog); self.assertEqual("reopened_verification", recurrence["outcome"]); self.assertTrue(recurrence["review_due"])
        quarantine = self.store.submit(packet(safe_summary="secret api key is bad"), catalog); self.assertEqual("quarantine", quarantine["outcome"])
        with self.assertRaises(runtime.AssetError): self.store.review({"candidate_id":first["candidate_id"],"reviewer_instance_id":"test-instance","decision":"actionable_candidate","review_note":"Synthetic review."})
        review = self.store.review({"candidate_id":first["candidate_id"],"reviewer_instance_id":"checker-instance","decision":"actionable_candidate","review_note":"Synthetic review."}); self.assertEqual("review_recorded_not_promoted", review["outcome"])
    def test_concurrent_duplicate_submission_records_one_candidate(self):
        outcomes=[]
        catalog = runtime.Catalog.load(self.catalog)
        def submit(): outcomes.append(self.store.submit(packet(), catalog)["outcome"])
        threads=[threading.Thread(target=submit) for _ in range(8)]
        [thread.start() for thread in threads]; [thread.join() for thread in threads]
        self.assertEqual(1, outcomes.count("candidate")); self.assertEqual(7, outcomes.count("duplicate"))

class StdioTests(unittest.TestCase):
    def test_initialize_list_and_call(self):
        child = subprocess.Popen([sys.executable, "-B", "mcp_stdio.py"], cwd=HERE, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            def request(identifier, method, params):
                child.stdin.write(json.dumps({"jsonrpc":"2.0","id":identifier,"method":method,"params":params}) + "\n"); child.stdin.flush(); return json.loads(child.stdout.readline())
            self.assertEqual("2025-06-18", request(1, "initialize", {"protocolVersion":"2025-06-18"})["result"]["protocolVersion"])
            tools = request(2, "tools/list", {})["result"]["tools"]; self.assertIn("SearchAssets", {tool["name"] for tool in tools})
            result = request(3, "tools/call", {"name":"SearchAssets","arguments":{"query":"subagent","limit":3}})["result"]["structuredContent"]
            self.assertTrue(result["assets"])
        finally:
            child.terminate(); child.wait(timeout=5); child.stdin.close(); child.stdout.close()

if __name__ == "__main__": unittest.main(verbosity=2)
