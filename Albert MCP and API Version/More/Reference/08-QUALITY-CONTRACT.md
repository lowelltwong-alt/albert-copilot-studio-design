# Quality contract

## Normative vocabulary and new transport schemas

The complete accompanying `06-contracts.schema.json` is the normative record vocabulary and is copied as a whole record contract, not replaced by prompt text. Its definitions are: Binding, Error, Anchor, Claim, Case, Source, Exhibit, Chunk, Witness, Tactic, GraphQuery, GraphResult, Artifact, Finding, Evaluation, Revision, Job, Layout, HumanDecision, DataMovementApproval, WitnessViewGrant, ExecutionAssignment, CaseCandidateGrant, GraphNode, GraphEdge, Assertion, Conflict, Inference, Gap, QualityPolicy, QualityDecision, JobCommand, JobAttempt, JobTransition, DependencyInvalidation, PanelAssignment, PanelRating, StudyCustody, and GoldQualification.

JSON Schema validates shape; the service validates cross-record authority, uniqueness, state transitions, signatures, current dependencies, and derived scores. Transport request schemas are separate from those records. Proposed requests are `StartJobRequest`, `CancelJobRequest`, `LookupOperationRequest`, `ReadGraphRequest`, `ReadArtifactRequest`, `SaveCandidateRequest`, `RequestEvaluationRequest`, and `RecordHumanDecisionRequest`. They all contain the common operation envelope. `StartJobRequest` has no caller-supplied job ID. Generic `complete` is not a public command; callback, reconciliation, leases, and transition commands are internal service operations.

## Writer and checker separation

Every writer and checker has a signed execution assignment bound to the case, series, artifact kind/audience, exact grant and evidence-bundle digest, prompt/runtime/model identity, capability allowlist, start/end time, and issuer attestation. SaveCandidate has explicit `source_review_proposal`, `case_profile_proposal`, `witness_settings_proposal`, `witness_packet`, and `podcast_script` kinds. P01/P02/P03 use their CaseCandidateGrant before a witness view exists; P04/P05 require a WitnessViewGrant for packet/script work. RequestEvaluation enqueues a service-assigned P06 worker with controlled evaluator context; it is not an unrestricted in-chat self-evaluation route. No child may write sources, reviews, grants, rubrics, quality decisions, jobs, or exports.

Independence is a service predicate: writer and checker require distinct authorized principals/assignments and controlled separate runtime context lineage. Record model identity for each; a different model is an optional comparison strategy, not sufficient proof or a universal requirement. A renamed child or nominally separate prompt does not establish independence. The evaluator receives controlled, restricted evidence and cannot inherit uncontrolled writer conversation state.

## Packet and script cycles

Packet and script are distinct series for each case/witness/artifact kind. Each begins with immutable A0 and E0. Every qualifying series requires at least two service-counted material cycles, normally A1/E1 and A2/E2, and permits at most five revision attempts. A counted cycle has a unique `(series_id, attempt)`, distinct frozen artifact and input digests, an independent evaluation, a diff binding, explicit targeted finding resolution, no critical regression, and service-derived flags showing input/artifact/outcome change. Timestamps, model claims, a no-op text edit, or a repeated evaluation cannot count.

At attempt six, or after five valid attempts without convergence, the outcome is terminal `unresolved_not_parity`. A stale policy/rubric/grant/dependency ends the affected series; a current artifact starts or continues only a compatible frozen series. A rubric revision starts a new evaluation series and is never substituted mid-series.

Podcast-script quality uses the existing eight required dimensions: examination readiness; conflicts, impeachment, and rehabilitation; role fidelity and truthful answer discipline; timeline, exhibit, and source retrieval; unseen transfer and active recall; witness-specific realism; spoken naturalness and read-aloud readiness; and navigation, concision, and non-repetition. The required artifact mean and each script dimension floor are 4.25, serious findings maximum is zero, and controls must pass. Scores are derived from individual ratings without pre-rounded pass comparisons.

Packet quality has the same immutable-baseline, independent-evaluation, two-cycle, serious-finding, controls, and cross-artifact requirements. Its category membership map is unresolved. Packet work may be built and evaluated diagnostically, but no packet QualityDecision may be marked `review_ready_pending_human` or convergence-qualified until the owner pins a category map and the service can validate it.

## Cross-artifact gate

The consistency checker receives exact packet and script bindings, their witness-view grants, the relevant quality decisions, and current dependency snapshot. It produces an immutable hard-gate result. It checks duplicate/missing chapters, outside-role facts, incompatible timelines, inconsistent labels, and cited/source binding consistency. A finding marks the affected artifact for rework and requires that artifact's next full evaluation plus another consistency run. H05 approval requires a passing current result bound to both exact hashes.

## Quality acceptance cases

`QL-01` proves two material packet cycles are required; `QL-02` proves two material script cycles and all eight script dimensions; `QL-03` proves a no-op revision cannot count; `QL-04` proves self-evaluation fails; `QL-05` proves a critical regression blocks convergence; `QL-06` proves unresolved packet categories block qualification; `QL-07` proves a post-script packet change invalidates the script pair; and `QL-08` proves H05 cannot approve hashes different from the cross-artifact result.
