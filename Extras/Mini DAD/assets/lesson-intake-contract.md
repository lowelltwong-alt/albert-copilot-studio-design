# Explicit cross-instance lesson intake

Another AI instance can submit a privacy-safe, bounded lesson candidate only
when its caller has enabled local intake. The caller supplies an opaque instance
identifier, a one-line safe summary, category, evidence references, impact,
reuse scope, and links to local asset IDs. This package does not observe other
AI sessions, scrape their transcripts, or detect their mistakes automatically.

Identity is a stable hash of a caller-supplied non-content `failure_key`,
category, reuse scope, and linked assets. A duplicate is held for review and
never increases quality or priority; rewording has no deduplication semantics
without the same key, so semantic similarity remains a human-review question.
`needs_evidence` remains a signal; `actionable_candidate` needs at least one
safe evidence reference. A recurrence after a claimed fix returns
`reopened_verification`. A distinct reviewer can record a review only when the
separate review gate is enabled; its opaque identity is a declaration, not
authenticated proof of independence. Promotion is always human-owned.
