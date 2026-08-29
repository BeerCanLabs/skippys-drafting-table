---
name: draftsman-engineering-maturity
description: Engineering maturity standards, APEX compliance, KPF tracking, test mapping, and automated release readiness guardrails for Archie, Switch, and engineering agents.
---

# Draftsman Engineering Maturity & Compliance Skill

## Purpose
Equips engineering agents (**Archie**, **Switch**, **Draftsman**) with mandatory protocols to ensure any new or modified repository meets our personal APEX engineering maturity standards, Key Product Functionality (`KPF.md`) tracking, test coverage mandates, and DRAFT catalog registration.

---

## Mandatory Engineering Agent Protocols

### 1. New Repository Onboarding Standard
Whenever **Archie** or **Switch** bootstraps or scaffolds a new repository, the agent MUST:

1. **Instantiate Root `APEX.md`:**
   - Vendor the personal `APEX.md` template into the repo root (`APEX.md`).
   - Declare the target maturity level in §1 (Default: **L1 Baseline**).
2. **Create `AGENTS.md` Pointer:**
   - Create `AGENTS.md` as the primary agent bootstrap file pointing directly to `APEX.md` and `KPF.md`.
3. **Instantiate `KPF.md` (Key Product Functionalities):**
   - Create `KPF.md` documenting all user- or service-facing capabilities.
   - Assign stable IDs (e.g. `KPF-APP-001`), descriptions, severities (Sev1/Sev2), and mapped automated test paths.
4. **Register in DRAFT & SDP:**
   - Create `.draft/sdp.yaml` declaring the application's software deployment pattern.
   - Register the repository URL and SDP manifest in `dsackr/drafting-table` under `catalog/engineering/product-registrations/`.

---

### 2. PR Pre-Flight & Quality Checklist (§7 APEX Compliance)
Before opening a Pull Request or declaring a task complete, **Archie** and **Switch** MUST verify:

* [ ] **`KPF.md` Updated:** Any new or modified product functionality is recorded in `KPF.md` with mapped test suite references.
* [ ] **Sev1/Sev2 Test Coverage:** Every touched Sev1/Sev2 KPF has at least one passing automated test.
* [ ] **Zero Gate Suppressions:** No `# nosec`, `--no-verify`, or `continue-on-error: true` ignores added.
* [ ] **Zero Hardcoded Secrets:** API keys and credentials are lookups from Secret Manager / env vars.
* [ ] **Expand-and-Contract Migrations:** Database schema changes are backward-compatible and decoupled from code deploys.
* [ ] **100% IaC:** Infrastructure changes are expressed in OpenTofu/Terraform modules (no manual steps).
* [ ] **Schema Validation:** Executed `python3 .draft/framework/tools/validate.py --workspace .` with 0 errors.

---

### 3. RequirementGroup Enforcement

Engineering agents enforce compliance against `requirement-group-engineering-maturity.yaml` in `drafting-table`:

* `req-expand-contract-migrations` (Backward-compatible schema migrations)
* `req-zero-manual-infrastructure` (100% OpenTofu/Terraform IaC)
* `req-no-gate-suppressions` (No build/lint suppressions)
* `req-synthetic-test-data` (No production PII or credentials in test fixtures)
* `req-rollback-mechanism` (Automated zero-downtime rollback)
