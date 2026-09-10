"""Local, bounded digital-asset catalog and learning-intake runtime.

The catalog is public-metadata only.  The lesson log is opt-in, local, append
only, and candidate-only; it cannot promote an asset or contact another AI.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

SCHEMA = "albert.digital-assets.v1"
MAX_QUERY = 120
MAX_RESULTS = 25
MAX_CONTENT_BYTES = 128_000
MAX_LESSON_SUMMARY = 600
ASSET_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,119}$")
SHA256 = re.compile(r"^[a-f0-9]{64}$")
TOKEN = re.compile(r"[a-z0-9][a-z0-9_-]{1,63}")
SAFE_REF = re.compile(r"^(?:evidence|test|doc|asset)://[A-Za-z0-9._:/-]{1,180}$")
INSTANCE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{2,119}$")
FAILURE_KEY = re.compile(r"^[a-z][a-z0-9_.:-]{2,119}$")
FORBIDDEN = re.compile(r"(?i)(?:\b(?:api[_ -]?key|password|secret|bearer)\b|-----BEGIN|C:\\Users\\|https?://[^\s]*(?:token|key|secret)[^\s]*)")
EDGE_TYPES = {"contains", "uses_asset", "requires", "reviewed_by", "produces", "related_to", "supports_review"}
DIRECTED_ACYCLIC = {"requires"}
LESSON_CATEGORIES = {"runtime", "review", "harness", "lifecycle", "privacy", "quality"}
LESSON_STATES = {"noise", "needs_evidence", "actionable_candidate"}
LINK_TYPES = {"sighting_of", "evidence_for", "uses_asset", "improves", "supersedes", "contradicts", "regresses", "validated_by"}
IMPACTS = {"low", "medium", "high"}
REUSE_SCOPES = {"one_workflow", "team_catalog", "human_review_required"}


class AssetError(ValueError):
    pass


def _no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AssetError("duplicate JSON key")
        result[key] = value
    return result


def _json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_no_duplicates)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AssetError("unreadable JSON") from exc


def _text(value: Any, label: str, maximum: int = MAX_QUERY) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum or "\x00" in value:
        raise AssetError(f"{label} is invalid")
    return value.strip()


def _limit(value: Any, default: int = 10) -> int:
    if value is None:
        return default
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_RESULTS:
        raise AssetError("limit must be an integer from 1 to 25")
    return value


def _tokens(value: Any) -> set[str]:
    if isinstance(value, str):
        return set(TOKEN.findall(value.casefold()))
    if isinstance(value, list):
        return {word for item in value for word in _tokens(item)}
    return set()


@dataclass(frozen=True)
class Catalog:
    root: Path
    release: str
    assets: tuple[dict[str, Any], ...]
    edges: tuple[dict[str, str], ...]

    @classmethod
    def load(cls, path: str | Path | None = None) -> "Catalog":
        path = Path(path) if path else Path(__file__).with_name("catalog.json")
        data = _json(path)
        if not isinstance(data, dict) or set(data) != {"schema", "release", "assets", "edges"} or data["schema"] != SCHEMA:
            raise AssetError("catalog schema is invalid")
        if not isinstance(data["release"], str) or not isinstance(data["assets"], list) or not isinstance(data["edges"], list):
            raise AssetError("catalog shape is invalid")
        root, ids, assets = path.parent.resolve(), set(), []
        fields = {"id", "title", "type", "path", "description", "tags", "capabilities", "version", "classification", "review_status", "sensitivity", "evidence_expires_on", "sha256", "provenance"}
        for item in data["assets"]:
            if not isinstance(item, dict) or set(item) != fields:
                raise AssetError("asset fields are invalid")
            if not ASSET_ID.fullmatch(str(item["id"])) or item["id"] in ids:
                raise AssetError("asset id is invalid or duplicate")
            if any(not isinstance(item[k], str) or not item[k].strip() for k in fields - {"tags", "capabilities", "provenance"}):
                raise AssetError("asset scalar field is invalid")
            if any(not isinstance(item[k], list) or any(not isinstance(v, str) or not v.strip() for v in item[k]) for k in {"tags", "capabilities", "provenance"}):
                raise AssetError("asset array field is invalid")
            if item["classification"] not in {"portable_core", "runtime_adapter", "workflow", "harness"} or item["review_status"] not in {"candidate", "reviewed"} or item["sensitivity"] != "public_metadata" or not SHA256.fullmatch(item["sha256"]):
                raise AssetError("asset policy field is invalid")
            try:
                date.fromisoformat(item["evidence_expires_on"])
            except ValueError as exc:
                raise AssetError("asset evidence date is invalid") from exc
            ids.add(item["id"]); assets.append(dict(item))
        edges, keys = [], set()
        for item in data["edges"]:
            if not isinstance(item, dict) or set(item) != {"source", "target", "type", "evidence", "review_status"}:
                raise AssetError("edge fields are invalid")
            if item["source"] not in ids or item["target"] not in ids or item["type"] not in EDGE_TYPES or item["review_status"] not in {"candidate", "reviewed"}:
                raise AssetError("edge is invalid")
            key = tuple(item[k] for k in ("source", "target", "type", "evidence"))
            if key in keys: raise AssetError("duplicate edge")
            keys.add(key); edges.append(dict(item))
        catalog = cls(root, data["release"], tuple(assets), tuple(edges))
        catalog._check_cycles()
        for asset in catalog.assets: catalog._read_verified(asset)
        return catalog

    def _check_cycles(self) -> None:
        for edge_type in DIRECTED_ACYCLIC:
            graph: dict[str, list[str]] = {asset["id"]: [] for asset in self.assets}
            for edge in self.edges:
                if edge["type"] == edge_type: graph[edge["source"]].append(edge["target"])
            visiting, done = set(), set()
            def visit(node: str) -> None:
                if node in visiting: raise AssetError(f"{edge_type} edge cycle")
                if node not in done:
                    visiting.add(node)
                    for child in graph[node]: visit(child)
                    visiting.remove(node); done.add(node)
            for node in graph: visit(node)

    def _read_verified(self, asset: dict[str, Any]) -> str:
        relative = Path(asset["path"])
        if relative.is_absolute() or ".." in relative.parts or not relative.parts:
            raise AssetError("asset path escapes package")
        candidate = self.root.joinpath(relative)
        try:
            if any(part.is_symlink() for part in [self.root, *[self.root.joinpath(*relative.parts[:i]) for i in range(1, len(relative.parts)+1)]]):
                raise AssetError("asset path may not use symlinks")
            resolved = candidate.resolve(strict=True); resolved.relative_to(self.root)
            raw = resolved.read_bytes()
        except (OSError, ValueError) as exc:
            raise AssetError("asset path is not a package file") from exc
        if len(raw) > MAX_CONTENT_BYTES or hashlib.sha256(raw).hexdigest() != asset["sha256"]:
            raise AssetError("asset digest is stale")
        try: return raw.decode("utf-8")
        except UnicodeDecodeError as exc: raise AssetError("asset is not UTF-8") from exc

    def asset(self, asset_id: Any) -> dict[str, Any]:
        identifier = _text(asset_id, "asset_id")
        for asset in self.assets:
            if asset["id"] == identifier: return asset
        raise AssetError("asset is unknown")

    @staticmethod
    def view(asset: dict[str, Any]) -> dict[str, Any]:
        return {k: asset[k] for k in asset if k not in {"path", "sha256"}}

    def search(self, query: Any, limit: Any = None) -> list[dict[str, Any]]:
        words, maximum = _tokens(_text(query, "query")), _limit(limit)
        rows = []
        for asset in self.assets:
            score = len(words & _tokens([asset["id"], asset["title"], asset["description"], asset["tags"], asset["capabilities"]]))
            if score: rows.append((score, asset["id"], self.view(asset)))
        return [row for _, _, row in sorted(rows, key=lambda value: (-value[0], value[1]))[:maximum]]

    def neighbors(self, asset_id: Any, limit: Any = None) -> list[dict[str, str]]:
        identifier, maximum = _text(asset_id, "asset_id"), _limit(limit)
        self.asset(identifier)
        return sorted([edge for edge in self.edges if identifier in (edge["source"], edge["target"])], key=lambda e: (e["type"], e["source"], e["target"]))[:maximum]

    def lifecycle(self, asset_id: Any = None) -> dict[str, Any]:
        assets = [self.asset(asset_id)] if asset_id is not None else list(self.assets)
        today = date.today()
        rows = [{"asset_id": asset["id"], "evidence_expires_on": asset["evidence_expires_on"], "evidence_state": "stale" if date.fromisoformat(asset["evidence_expires_on"]) < today else "unexpired", "review_status": asset["review_status"], "qualified": False} for asset in assets]
        return {"checked_on": today.isoformat(), "assets": rows, "all_evidence_unexpired": all(row["evidence_state"] == "unexpired" for row in rows), "qualification": "not_established", "promotion": "human_review_required"}


def _safe_summary(value: Any) -> str:
    text = _text(value, "safe_summary", MAX_LESSON_SUMMARY)
    if "\n" in text or FORBIDDEN.search(text): raise AssetError("safe_summary contains unsafe content")
    return text


def _candidate(payload: dict[str, Any], catalog: Catalog) -> dict[str, Any]:
    allowed = {"source_instance_id", "source_session_ref", "source_locator_hash", "failure_key", "safe_summary", "category", "state", "impact", "reuse_scope", "evidence_refs", "validation_refs", "regression_refs", "proposed_fix", "linked_asset_ids", "typed_links", "recurs_after_claimed_fix_of"}
    required = {"source_instance_id", "source_session_ref", "source_locator_hash", "failure_key", "safe_summary", "category", "state", "impact", "reuse_scope", "evidence_refs", "linked_asset_ids", "typed_links"}
    if not isinstance(payload, dict) or set(payload) - allowed or not required <= set(payload):
        raise AssetError("lesson candidate fields are invalid")
    source = _text(payload["source_instance_id"], "source_instance_id")
    if not INSTANCE_ID.fullmatch(source): raise AssetError("source_instance_id is invalid")
    session = _text(payload["source_session_ref"], "source_session_ref")
    locator = _text(payload["source_locator_hash"], "source_locator_hash")
    if not INSTANCE_ID.fullmatch(session) or not re.fullmatch(r"sha256:[a-f0-9]{64}", locator): raise AssetError("source provenance is invalid")
    failure_key = _text(payload["failure_key"], "failure_key")
    if not FAILURE_KEY.fullmatch(failure_key): raise AssetError("failure_key is invalid")
    category, state, impact, scope = payload["category"], payload["state"], payload["impact"], payload["reuse_scope"]
    if category not in LESSON_CATEGORIES or state not in LESSON_STATES or impact not in IMPACTS or scope not in REUSE_SCOPES: raise AssetError("lesson category or lifecycle is invalid")
    evidence = payload["evidence_refs"]
    validation = payload.get("validation_refs", [])
    regression = payload.get("regression_refs", [])
    links = payload["linked_asset_ids"]
    if not isinstance(evidence, list) or len(evidence) > 8 or any(not isinstance(item, str) or not SAFE_REF.fullmatch(item) for item in evidence): raise AssetError("evidence_refs are invalid")
    if state == "actionable_candidate" and not evidence: raise AssetError("actionable candidates require evidence")
    if any(not isinstance(rows, list) or len(rows) > 8 or any(not isinstance(item, str) or not SAFE_REF.fullmatch(item) for item in rows) for rows in (validation, regression)): raise AssetError("validation or regression references are invalid")
    if payload.get("proposed_fix", False) is not False and payload.get("proposed_fix") is not True: raise AssetError("proposed_fix is invalid")
    if payload.get("proposed_fix", False) and (not validation or not regression): raise AssetError("proposed fixes require validation and regression references")
    if not isinstance(links, list) or len(links) > 8 or any(not isinstance(item, str) or not ASSET_ID.fullmatch(item) for item in links): raise AssetError("linked_asset_ids are invalid")
    for link in links: catalog.asset(link)
    typed_links = payload["typed_links"]
    if not isinstance(typed_links, list) or len(typed_links) > 12: raise AssetError("typed_links are invalid")
    normalized_links = []
    for link in typed_links:
        if not isinstance(link, dict) or set(link) != {"type", "target_id"} or link["type"] not in LINK_TYPES or not isinstance(link["target_id"], str) or not ASSET_ID.fullmatch(link["target_id"]): raise AssetError("typed_links are invalid")
        normalized_links.append({"type": link["type"], "target_id": link["target_id"]})
    prior = payload.get("recurs_after_claimed_fix_of")
    if prior is not None and (not isinstance(prior, str) or not ASSET_ID.fullmatch(prior)): raise AssetError("recurrence link is invalid")
    # The caller supplies a stable non-content failure key; rephrased summaries
    # cannot bypass deduplication. Semantic equivalence is intentionally left to review.
    identity = {"failure_key": failure_key, "category": category, "reuse_scope": scope, "linked_asset_ids": sorted(links)}
    candidate_id = "albert:lesson:" + hashlib.sha256(json.dumps(identity, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:24]
    return {"candidate_id": candidate_id, "source_instance_id": source, "source_session_ref": session, "source_locator_hash": locator, "failure_key": failure_key, "safe_summary": _safe_summary(payload["safe_summary"]), "category": category, "state": state, "impact": impact, "reuse_scope": scope, "evidence_refs": sorted(evidence), "validation_refs": sorted(validation), "regression_refs": sorted(regression), "proposed_fix": bool(payload.get("proposed_fix", False)), "linked_asset_ids": sorted(links), "typed_links": sorted(normalized_links, key=lambda row: (row["type"], row["target_id"])), "recurs_after_claimed_fix_of": prior, "review_status": "pending", "promotion": "human_review_required"}


class LessonStore:
    def __init__(self, root: Path) -> None:
        self.root, self.state = root.resolve(), root.resolve() / "state"
        self.candidates, self.events, self.reviews, self.lock = self.state / "lesson-candidates.jsonl", self.state / "lesson-events.jsonl", self.state / "lesson-reviews.jsonl", self.state / ".lesson-intake.lock"

    def _rows(self, path: Path) -> list[dict[str, Any]]:
        if not path.exists(): return []
        if path.is_symlink(): raise AssetError("lesson store is unsafe")
        try: return [json.loads(line, object_pairs_hook=_no_duplicates) for line in path.read_text(encoding="utf-8").splitlines() if line]
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc: raise AssetError("lesson store is unreadable") from exc

    def _hold_lock(self) -> int:
        self.state.mkdir(exist_ok=True)
        deadline = time.monotonic() + 2
        while True:
            try: return os.open(self.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                if time.monotonic() >= deadline: raise AssetError("lesson intake is busy")
                time.sleep(.03)

    @staticmethod
    def _append_unlocked(path: Path, row: dict[str, Any]) -> None:
        with path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"); stream.flush(); os.fsync(stream.fileno())

    def _append(self, path: Path, row: dict[str, Any]) -> None:
        descriptor = self._hold_lock()
        try:
            self._append_unlocked(path, row)
        finally:
            os.close(descriptor)
            try: self.lock.unlink()
            except FileNotFoundError: pass

    def submit(self, payload: dict[str, Any], catalog: Catalog) -> dict[str, Any]:
        try: candidate = _candidate(payload, catalog)
        except AssetError:
            return {"outcome": "quarantine", "reason_code": "schema_or_privacy_rejected", "stored": False, "promotion": "human_review_required"}
        descriptor = self._hold_lock()
        try:
            existing = {row.get("candidate_id"): row for row in self._rows(self.candidates)}
            recurrence = candidate["recurs_after_claimed_fix_of"]
            if recurrence and recurrence not in existing: raise AssetError("recurrence target is unknown")
            event = {"event_id": "albert:lesson-event:" + hashlib.sha256(json.dumps(candidate, sort_keys=True).encode()).hexdigest()[:24], "candidate_id": candidate["candidate_id"], "source_instance_id": candidate["source_instance_id"], "source_session_ref": candidate["source_session_ref"], "evidence_refs": candidate["evidence_refs"], "typed_links": candidate["typed_links"], "recurs_after_claimed_fix_of": recurrence, "verification_required": bool(recurrence), "independent_context_count_increment": 0, "automatic_quality_change": False}
            if candidate["candidate_id"] in existing:
                self._append_unlocked(self.events, event)
                if recurrence:
                    return {"outcome": "reopened_verification", "candidate_id": candidate["candidate_id"], "event_recorded": True, "typed_links": event["typed_links"] + [{"type": "regresses", "target_id": recurrence}], "review_due": True, "independent_context_count_increment": 0, "promotion": "human_review_required"}
                return {"outcome": "duplicate", "candidate_id": candidate["candidate_id"], "event_recorded": True, "automatic_quality_change": False, "promotion": "human_review_required"}
            if candidate["state"] == "noise": return {"outcome": "noise", "stored": False, "promotion": "human_review_required"}
            self._append_unlocked(self.candidates, candidate)
            self._append_unlocked(self.events, event)
            outcome = "candidate" if candidate["state"] == "actionable_candidate" else "needs_evidence"
            return {"outcome": outcome, "candidate_id": candidate["candidate_id"], "state": candidate["state"], "verification_required": bool(recurrence), "promotion": "human_review_required"}
        finally:
            os.close(descriptor)
            try: self.lock.unlink()
            except FileNotFoundError: pass

    def get(self, candidate_id: Any) -> dict[str, Any]:
        identifier = _text(candidate_id, "candidate_id")
        rows = {row.get("candidate_id"): row for row in self._rows(self.candidates)}
        if identifier not in rows: raise AssetError("lesson candidate is unknown")
        reviews = [row for row in self._rows(self.reviews) if row.get("candidate_id") == identifier]
        events = [row for row in self._rows(self.events) if row.get("candidate_id") == identifier]
        return {"candidate": rows[identifier], "events": events, "reviews": reviews, "reviewer_independence": "declared opaque identities only; not authenticated", "promotion": "human_review_required"}

    def review(self, payload: dict[str, Any]) -> dict[str, Any]:
        allowed = {"candidate_id", "reviewer_instance_id", "decision", "review_note"}
        if not isinstance(payload, dict) or set(payload) != allowed: raise AssetError("review fields are invalid")
        candidate = self.get(payload["candidate_id"])["candidate"]
        reviewer = _text(payload["reviewer_instance_id"], "reviewer_instance_id")
        if not INSTANCE_ID.fullmatch(reviewer) or reviewer == candidate["source_instance_id"]: raise AssetError("reviewer must be distinct")
        if payload["decision"] not in {"needs_evidence", "actionable_candidate", "reject"}: raise AssetError("review decision is invalid")
        row = {"candidate_id": candidate["candidate_id"], "reviewer_instance_id": reviewer, "decision": payload["decision"], "review_note": _safe_summary(payload["review_note"]), "promotion": "human_review_required"}
        self._append(self.reviews, row)
        return {"outcome": "review_recorded_not_promoted", **row}


def intake_enabled() -> bool: return os.environ.get("ALBERT_LESSON_INTAKE_ENABLED") == "true"
def review_enabled() -> bool: return intake_enabled() and os.environ.get("ALBERT_LESSON_REVIEW_ENABLED") == "true"

def tool_specs() -> list[dict[str, Any]]:
    tools = [
        ("SearchAssets", {"query": "string", "limit": "integer 1..25"}), ("GetAsset", {"asset_id": "string"}),
        ("GetNeighbors", {"asset_id": "string", "limit": "integer 1..25"}), ("GetAssetContent", {"asset_id": "string"}),
        ("GetLifecycleStatus", {"asset_id": "optional string"}), ("GetRuntimeStatus", {}), ("GetLessonCandidate", {"candidate_id": "string"}),
    ]
    if intake_enabled(): tools.append(("SubmitLessonCandidate", {"source_instance_id": "opaque caller id", "source_session_ref": "opaque session id", "source_locator_hash": "sha256 value", "failure_key": "stable non-content caller key", "safe_summary": "privacy-safe single line", "category": sorted(LESSON_CATEGORIES), "state": sorted(LESSON_STATES), "impact": sorted(IMPACTS), "reuse_scope": sorted(REUSE_SCOPES), "evidence_refs": "bounded safe refs", "typed_links": sorted(LINK_TYPES), "linked_asset_ids": "catalog ids"}))
    if review_enabled(): tools.append(("ReviewLessonCandidate", {"candidate_id": "string", "reviewer_instance_id": "distinct opaque id", "decision": ["needs_evidence", "actionable_candidate", "reject"], "review_note": "privacy-safe single line"}))
    def schema(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
        properties = {key: ({"type": "integer", "minimum": 1, "maximum": 25} if key == "limit" else {"type": "array", "maxItems": 12, "items": {"type": "object"}} if key == "typed_links" else {"type": "array", "maxItems": 8, "items": {"type": "string"}} if key.endswith("_refs") or key == "linked_asset_ids" else {"type": "string", "minLength": 1, "maxLength": MAX_LESSON_SUMMARY if key in {"safe_summary", "review_note"} else MAX_QUERY}) for key in inputs}
        required = [key for key in inputs if key not in {"limit", "asset_id", "validation_refs", "regression_refs", "proposed_fix", "recurs_after_claimed_fix_of"}]
        if name == "GetLifecycleStatus": required = []
        return {"type": "object", "properties": properties, "required": required, "additionalProperties": False}
    return [{"name": name, "description": "Bounded local digital-asset operation.", "inputSchema": schema(name, inputs)} for name, inputs in tools]


def dispatch(name: str, arguments: dict[str, Any] | None = None, catalog_path: str | Path | None = None) -> dict[str, Any]:
    arguments = arguments or {}
    allowed = {"SearchAssets": {"query", "limit"}, "GetAsset": {"asset_id"}, "GetNeighbors": {"asset_id", "limit"}, "GetAssetContent": {"asset_id"}, "GetLifecycleStatus": {"asset_id"}, "GetRuntimeStatus": set(), "GetLessonCandidate": {"candidate_id"}, "SubmitLessonCandidate": {"source_instance_id", "source_session_ref", "source_locator_hash", "failure_key", "safe_summary", "category", "state", "impact", "reuse_scope", "evidence_refs", "validation_refs", "regression_refs", "proposed_fix", "linked_asset_ids", "typed_links", "recurs_after_claimed_fix_of"}, "ReviewLessonCandidate": {"candidate_id", "reviewer_instance_id", "decision", "review_note"}}
    if name not in allowed or not isinstance(arguments, dict) or set(arguments) - allowed[name]: raise AssetError("unknown or disabled tool")
    catalog = Catalog.load(catalog_path); store = LessonStore(catalog.root)
    if name == "SearchAssets": return {"assets": catalog.search(arguments.get("query"), arguments.get("limit")), "authority": "candidate_metadata_only"}
    if name == "GetAsset": return {"asset": Catalog.view(catalog.asset(arguments.get("asset_id"))), "authority": "candidate_metadata_only"}
    if name == "GetNeighbors": return {"edges": catalog.neighbors(arguments.get("asset_id"), arguments.get("limit")), "authority": "typed_candidate_edges"}
    if name == "GetAssetContent": return {"asset_id": _text(arguments.get("asset_id"), "asset_id"), "content": catalog._read_verified(catalog.asset(arguments.get("asset_id"))), "authority": "review_before_adoption"}
    if name == "GetLifecycleStatus": return catalog.lifecycle(arguments.get("asset_id"))
    if name == "GetRuntimeStatus": return {"release": catalog.release, "transport": "stdio_mcp_local", "intake_enabled": intake_enabled(), "review_enabled": review_enabled(), "cross_instance_detection": "not_implemented; caller submits explicitly", "promotion": "human_review_required"}
    if name == "GetLessonCandidate": return store.get(arguments.get("candidate_id"))
    if name == "SubmitLessonCandidate" and intake_enabled(): return store.submit(arguments, catalog)
    if name == "ReviewLessonCandidate" and review_enabled(): return store.review(arguments)
    raise AssetError("unknown or disabled tool")
