# Optional maintainer checks

The Copilot MVP does not run these tools. A maintainer with Python 3.10+ can run, from this folder's parent:

```text
python -B checks/validate.py --final
python -B checks/test_negative.py
python -B checks/generate_views.py
```

Validation checks local links, exact imported instruction bytes, role lengths, RUN/placement/paste agreement, generated Mermaid source and frozen preview hashes, and the worked R01 Markdown graph's structural invariants. It does not prove truth, genuine owner permission, semantic retrieval, model correctness or tenant behavior. The graph checker is an R01 demonstration validator, not a production database engine.

Seven negative fixtures are run through the same aggregate validator in forward and reverse order, with a clean baseline before and after. Compare the complete finding set as well as the first intended guard. They cover dangling links, an unsupported truth upgrade, a grant-unit mismatch, conflict endpoints, source parents, stale edges and missing graph content. The fixture catalog binds exact inputs.

After an authorized change to a new candidate's workflow/role manifest, update its placement table and run `python -B checks/generate_views.py --write` to regenerate the Mermaid views. Review the diff. Re-render SVG/PNG using Mermaid 11.17.2, bind the new outputs and source/generator hashes in a new render receipt, then run final validation. A stale preview fails instead of silently representing the new workflow. Keep previous frozen versions and their receipts. This is explicit maintenance, not an installed watcher or automatic modification service.

The diagram rendering receipt records the renderer and dimensions. SVG files are scalable; PNG files are convenient for ordinary document/email viewers. The saved local QA receipt records what ran for this delivery.
