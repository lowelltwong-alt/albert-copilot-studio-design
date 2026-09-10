# Data model and graph contract

The catalog is a public-metadata graph. Source repositories remain authoritative; this package stores only the selected asset text and metadata that the owner has allowed into this package.

Each asset contains: `id`, `title`, `type`, package-relative `path`, `description`, `tags`, `capabilities`, `version`, `classification`, `review_status`, `sensitivity`, `evidence_expires_on`, `sha256`, and `provenance`. `review_status=candidate` means discoverable for human evaluation, not approved guidance.

Edges contain `source`, `target`, `type`, `evidence`, and `review_status`. The current vocabulary is `contains`, `uses_asset`, `requires`, `reviewed_by`, `produces`, `related_to`, and `supports_review`. `requires` is directed and acyclic; other edge types remain typed evidence and are not authority.

Lesson candidates carry opaque caller identity and session fields, a non-content locator hash, stable `failure_key`, safe summary, category (`runtime`, `review`, `harness`, `lifecycle`, `privacy`, `quality`), state, impact, reuse scope, bounded evidence/validation/regression references, linked asset IDs, and typed links such as `sighting_of`, `evidence_for`, `improves`, `supersedes`, `contradicts`, `regresses`, or `validated_by`.

Lifecycle is evidence-based: `unexpired` or `stale`, with `review_status` and `qualification=not_established`. Expiry does not delete an item and an unexpired candidate is not automatically trusted. Human review must approve a reviewed revision, supersession, archive, or retrieval recommendation.

