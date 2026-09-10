# Cross-instance learning loop

The loop is explicit and caller-driven:

```text
search reviewed/fresh assets -> record used/rejected/missing/harmful
-> observe a repeatable surprise, regression, inaccurate recommendation or reusable asset
-> send a minimal privacy-safe candidate packet
-> validate and screen -> deduplicate or record a sighting
-> categorize and link in the graph -> disposition
-> human review -> reviewed revision only after approval
```

DAD’s donor implementation supplies the evidence-first pattern: stable exception identity, quarantine for unsafe/colliding records, fixed-outcome evidence gates, and human promotion. It does not supply a general importance score or automatic cross-AI detector. This package therefore uses explicit dispositions and evidence fields rather than pretending frequency is value.

Signal rules:

* `noise`: routine progress, preference, speculation, or no observable reusable effect. It is not stored as a candidate.
* `duplicate`: same stable failure identity and no new independent evidence. It does not increase quality or corroboration.
* `needs_evidence`: plausible but missing a bounded validation, counterexample, or applicability boundary.
* `candidate`: a privacy-safe, evidenced report awaiting a human decision. Candidate content is not guidance.
* `reopened_verification`: a supposedly fixed issue reappeared. It links the recurrence and requires independent verification; it adds zero corroboration until verified.
* `quarantine`: malformed, unsafe, credential-like, private, or otherwise rejected at intake.

Repeated reports from one session are not independent evidence. A stable caller `failure_key` makes transport retries idempotent, but semantic near-duplicate review is still human work. A high impact label is a review priority, not proof. The service does not count model confidence, graph centrality, similarity, or raw frequency as truth.

The caller must report only a short safe summary, opaque references/hashes, applicability, danger if misapplied, and typed asset links. It must never send case files, source rows, credentials, raw conversations, hidden reasoning, logs or screenshots. See `assets/lesson-intake-contract.md` for the compact provider-neutral caller instruction.

