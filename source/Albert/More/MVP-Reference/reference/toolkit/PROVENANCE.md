# Provenance and reuse boundary

The owner explicitly authorized copying useful DAD assets into this digital asset package and an optional working read-only connection. This is the recorded scope of this delivery. We preserve the donor's notice and do not assert a general open-source license. Broader public redistribution needs an explicit package license and treatment of adapted material; no DAD private data or catalog rows are included here.

The following two generic skill sources are copied byte-for-byte from the locally observed DAD checkout on 2026-09-08. They are reference snapshots, not installed instructions. Their original repository references and runtime commands are historical context; use the self-contained adapted team skills for execution. Raw SHA-256 binds the observed file, including any checkout changes; this is not a claim that a clean Git revision was reviewed.

| DAD relative source | Local reference copy | Observed SHA-256 |
|---|---|---|
| `assets/agent-skills/dad-learning-loop/SKILL.md` | [donors/DAD-LEARNING-LOOP.md](donors/DAD-LEARNING-LOOP.md) | `9bb9a240793e5fcee0f0c060227c2253f21a7cf95930c5db9d9162ad162dbf04` |
| `assets/agent-skills/subagent-continuous-improvement/SKILL.md` | [donors/DAD-CONTINUOUS-IMPROVEMENT.md](donors/DAD-CONTINUOUS-IMPROVEMENT.md) | `9c12ced77362473836e358dbb71419ff6e7f8ff2f1b4e471c497a5ecfdef0a5b` |
| `LICENSE_DECISION_REQUIRED.md` | [donors/LICENSE_DECISION_REQUIRED.md](donors/LICENSE_DECISION_REQUIRED.md) | `b23423f56d192eb3e1777fee018d78616a6c1cafae02ff31cd68b97415b10d50` |

## Adaptation map

- `team-learning-loop`, P02–P04 and WF02 adapt the before/during/close loop and reference-bound fixes, with explicit local handoffs.
- `team-agent-routing` and P05 adapt independent evaluation, evaluator checks, layer attribution, no-change and human adoption from the continuous-improvement source. Provider names and donor-specific commands are removed from the portable core.
- Asset cards, searchable descriptions, typed graph relationships, exact retrieval and candidate authority follow DAD's catalog/graph/MCP design. The team runtime has its own dependency closure; it does not import the DAD hub to search local assets.
- `learning.py` adds local revision and distinct-reviewer field checks. DAD's collector does not by itself enforce the entire proposed lesson lifecycle; this package does not claim otherwise. The executable contract describes the actual checks and their limits.
- Evidence and podcast skills/P01 adapt this task's Albert 3.3.1 review work. They contain no case facts or reference-podcast text.

## Implementation source fingerprints (reference, not wholesale copies)

| DAD relative reference | Observed SHA-256 |
|---|---|
| `src/digital_asset_directory/graph_engine.py` | `6edd9b98e4aa5b4b0f3ec06f4e0e036248757dfe0406a521de2474ec06da88ee` |
| `src/digital_asset_directory/models.py` | `009d09d9d56b8d43b5e43c608e9affd522177ba5b8a081a80666a51f9c80997b` |
| `src/digital_asset_directory/mcp_server.py` | `6f8d3e47c270d290f08287392e80848464df134d65885fbc22844c4f5a4517b6` |
| `src/digital_asset_directory/exceptions_lake.py` | `53e4e6dd8f68232766b1a03d373de56e6f18bdcd43b5344dfed47f1c719e9376` |
| `src/digital_asset_directory/priority_content_lessons.py` | `426aa6ab457cd1ad10f48c0f58aae23cc3b140f39492de1b0d0fd1f0ebc90602` |
| `registry/exception-learning-methodology.json` | `95978543cb7e4a3a339aa6376c03f04a4a116955cade3117134b68756cd74173` |
| `schemas/exception-event.schema.json` | `38141347ee1effb7f06b5a1049e21b2122cae598bb71da1d976ed43043644294` |
| `schemas/exception-fix-outcome.schema.json` | `b72ca4bc8622b863874a917efcc840e7e170eb377aca4c51346e8c37578a94f9` |

The architecture review covered navigation and authority; asset cards/index; graph construction, surfaces and query contracts; exception capture, collection, fixes and learning handoffs; MCP implementation/dependencies; and relevant tests. It was not an execution audit of every DAD module. Mail, transport, private stores and unrelated campaigns were intentionally excluded from copying. No donor tests, lifecycle commands or writes were run for that source review.

The optional MCP SDK and dependencies are separately licensed third-party packages installed by the recipient from `requirements.txt`; they are not vendored in this package. The installation report used for local tests is retained in task intermediates. No credentials or host-specific DAD configuration are distributed.

Additional directly adapted helper source: src/digital_asset_directory/utils.py, observed SHA-256 046db685aa9a060131fa2cd2020d8fbb0cbd182f24dcbecf9438bb41e56e3b31. toolkit.py locally ports its tokens, idf_weights and idf_weighted_cosine functions; graph_engine.build_edges supplies the normalized relation approach. The local cap is four candidates at both endpoints; no DAD import, graph database or rank/approval authority is copied.


## Release 0.2.0 additions

A01, WF04 and their skill/template adapt the copied DAD continuous-improvement design and the existing P03/P05 cores: instruction-output traceability, competing causal layers, evaluator challenge, bounded testing and owner adoption. A02/P06/WF05 are new portable candidate compositions informed by the user's original NotebookLM podcast craft and verified public product descriptions; see PODCAST-REFERENCE-NOTES.md. No private case source text, notebook custom prompt, hidden model instruction or Meta runtime/code is copied into this generic package. The current role bindings are observed test metadata, not permanent selectors.

The nineteen 0.1.0 catalog assets remain byte-identical and retain identities. Ten new assets and twenty explicit relationships produce 29 assets/39 edges; eight additional generated similarity candidates are discovery hints. Old 0.1.0 QA is historical and not used as a new prompt/tenant qualification.
