# Key Product Functionalities (KPF) — Drafting Table

**Source of truth for product functionality & test mappings.**

| KPF ID | Name | Description | Severity | Mapped Tests | Status |
|---|---|---|---|---|---|
| `KPF-DFT-001` | Workspace Schema Validation | CLI and library tool (`validate.py`) to validate DRAFT catalog schemas, UIDs, and requirement groups. | Sev1 | `tests/test_validation.py` | Active |
| `KPF-DFT-002` | Framework Package Synchronization | Framework sync engine (`repo.py`, `/draft update`, `draft-framework-update.yml`) to vendor upstream releases. | Sev1 | `tests/test_repo.py`, `tests/test_draftsman.py` | Active |
| `KPF-DFT-003` | OpenTofu / IaC Composition Engine | IaC composition script (`compose_iac.py`) translating `.draft/sdp.yaml` to runnable OpenTofu code. | Sev1 | `tests/test_tooling_correctness.py` | Active |
| `KPF-DFT-004` | Agent Spec & Binding Lifecycle | Agent binding generator and specification validator for Hermes and CLI agents. | Sev2 | `tests/test_agent_mcp_tools.py`, `tests/test_cli.py` | Active |
