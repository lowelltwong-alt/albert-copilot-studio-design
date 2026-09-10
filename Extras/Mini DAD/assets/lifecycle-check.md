# Evidence lifecycle check

Each catalog asset has a source/provenance list, review state, and an evidence
expiry date. The runtime marks expired evidence as stale and reports the state;
it does not refresh sources or demote an asset automatically. `requires` edges
are checked as a directed acyclic graph so a runtime dependency cycle is
rejected during catalog load.

Revalidate a stale asset before a human decides whether to retain, revise, or
retire it.
