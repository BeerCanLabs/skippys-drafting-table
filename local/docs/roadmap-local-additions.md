# Local roadmap additions

Moved from the root `ROADMAP.md` of the pre-workspace fork. The rest of that file was an unmodified copy of the upstream DRAFT roadmap and now lives at `.draft/framework/`-era upstream: https://github.com/getdraft/draftsman/blob/main/ROADMAP.md

> Paths below refer to the old fork layout. `agent/mcp/` has been retired; `framework/tools/` is now `.draft/framework/tools/`.

## Future Enhancements: Vector Database Indexing

Research is open for integrating embedded vector search capabilities into the Draftsman MCP agent (`agent/mcp/`) and index generator (`framework/tools/generate_ai_index.py`).

Key objectives:
- Enable natural language semantic retrieval over distributed SDPs, Shared Services, and Requirement Groups.
- Maintain DRAFT's "repo-first, zero mandatory cloud infrastructure" model using embedded stores (`sqlite-vec`, `duckdb`, or local `chromadb`).
- See [RFC: Vector Database Integration for Semantic Index Searches](rfc-vector-database-indexing.md) for execution details.

