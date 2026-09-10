"""Optional Streamable-HTTP FastMCP adapter; local stdio remains dependency-free."""
from __future__ import annotations
import os
from typing import Any
from runtime import AssetError, dispatch, tool_specs

LOOPBACK = {"127.0.0.1", "localhost", "::1"}
def _network(host: str) -> None:
    if host not in LOOPBACK:
        raise RuntimeError("non-loopback hosting is disabled: this package has no request-level Entra/OAuth validator; deploy an authenticated adapter before enabling it")
def create_mcp_server(host: str = "127.0.0.1", *, include_review: bool = True) -> Any:
    _network(host)
    try: from mcp.server.fastmcp import FastMCP
    except ImportError as exc: raise RuntimeError("install requirements.txt in a project virtual environment for Streamable HTTP") from exc
    app = FastMCP("albert-digital-assets", instructions="Generic asset discovery and explicit local lesson intake; no case data or automatic promotion.", host=host, streamable_http_path="/mcp", stateless_http=True, json_response=True)
    @app.tool(name="SearchAssets")
    def search_assets(query: str, limit: int = 10) -> dict[str, Any]: return dispatch("SearchAssets", {"query": query, "limit": limit})
    @app.tool(name="GetAsset")
    def get_asset(asset_id: str) -> dict[str, Any]: return dispatch("GetAsset", {"asset_id": asset_id})
    @app.tool(name="GetNeighbors")
    def get_neighbors(asset_id: str, limit: int = 10) -> dict[str, Any]: return dispatch("GetNeighbors", {"asset_id": asset_id, "limit": limit})
    @app.tool(name="GetAssetContent")
    def get_asset_content(asset_id: str) -> dict[str, Any]: return dispatch("GetAssetContent", {"asset_id": asset_id})
    @app.tool(name="GetLifecycleStatus")
    def get_lifecycle_status(asset_id: str | None = None) -> dict[str, Any]: return dispatch("GetLifecycleStatus", {"asset_id": asset_id} if asset_id else {})
    @app.tool(name="GetRuntimeStatus")
    def get_runtime_status() -> dict[str, Any]: return dispatch("GetRuntimeStatus", {})
    @app.tool(name="GetLessonCandidate")
    def get_lesson_candidate(candidate_id: str) -> dict[str, Any]: return dispatch("GetLessonCandidate", {"candidate_id": candidate_id})
    if os.environ.get("ALBERT_LESSON_INTAKE_ENABLED") == "true":
        @app.tool(name="SubmitLessonCandidate")
        def submit_lesson_candidate(source_instance_id: str, source_session_ref: str, source_locator_hash: str, failure_key: str, safe_summary: str, category: str, state: str, impact: str, reuse_scope: str, evidence_refs: list[str], linked_asset_ids: list[str], typed_links: list[dict[str, str]], validation_refs: list[str] = [], regression_refs: list[str] = [], proposed_fix: bool = False, recurs_after_claimed_fix_of: str | None = None) -> dict[str, Any]:
            return dispatch("SubmitLessonCandidate", {"source_instance_id": source_instance_id, "source_session_ref": source_session_ref, "source_locator_hash": source_locator_hash, "failure_key": failure_key, "safe_summary": safe_summary, "category": category, "state": state, "impact": impact, "reuse_scope": reuse_scope, "evidence_refs": evidence_refs, "linked_asset_ids": linked_asset_ids, "typed_links": typed_links, "validation_refs": validation_refs, "regression_refs": regression_refs, "proposed_fix": proposed_fix, "recurs_after_claimed_fix_of": recurs_after_claimed_fix_of})
    if include_review and os.environ.get("ALBERT_LESSON_REVIEW_ENABLED") == "true" and os.environ.get("ALBERT_LESSON_INTAKE_ENABLED") == "true":
        @app.tool(name="ReviewLessonCandidate")
        def review_lesson_candidate(candidate_id: str, reviewer_instance_id: str, decision: str, review_note: str) -> dict[str, Any]: return dispatch("ReviewLessonCandidate", {"candidate_id": candidate_id, "reviewer_instance_id": reviewer_instance_id, "decision": decision, "review_note": review_note})
    return app
def main() -> None:
    host = os.environ.get("ALBERT_BIND_HOST", "127.0.0.1"); _network(host)
    try: import uvicorn
    except ImportError as exc: raise SystemExit("install requirements.txt in a project virtual environment") from exc
    uvicorn.run(create_mcp_server(host).streamable_http_app(), host=host, port=int(os.environ.get("ALBERT_BIND_PORT", "8765")))
if __name__ == "__main__": main()
