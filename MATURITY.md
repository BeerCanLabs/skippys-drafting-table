# DRAFT — Engineering Maturity & Agent Compliance Guide

**Source of truth:** DRAFT Engineering Maturity Framework (dsackr / getdraft Open Source Ecosystem).
**This file is vendored and org-owned.** Do not edit inside managed blocks. Repo-specific guidance for agents belongs in `AGENTS.md`.

## How to use this file

You are an AI agent or developer writing code in this repository. Read this file before you plan a change, and check your work against §5 before you open a PR.

DRAFT Engineering Maturity defines 8 vectors and 3 cumulative levels (L1 Baseline → L2 Established → L3 Advanced). Every requirement has a stable ID of the form `4.<vector>.<level>.<seq>` — e.g. `4.3.1.2` is Observability, L1, requirement 2. **Always cite these IDs** when you flag a gap, justify a decision, or explain why you stopped.

Levels are cumulative: a repo targeting L2 must satisfy L1 and L2. Reaching L3 means satisfying all requirements across all three levels.

## 1. This repo's target level

> **Maintainers: fill this in.** If blank, assume **L1 Baseline** — mandatory for all active applications.

| Vector | Target | Notes |
|---|---|---|
| 4.1 Architecture | L1 | Registered in DRAFT catalog |
| 4.2 Environments | L1 | |
| 4.3 Observability | L1 | |
| 4.4 Testing | L1 | |
| 4.5 Code Promotion | L1 | |
| 4.6 Gating | L1 | Automated CI checks |
| 4.7 Branch Management | L1 | GitHub Flow |
| 4.8 Repository Design | L1 | |

## 2. Hard rules — never violate these

These rules keep contributions safe and high-quality. If a task cannot be completed without breaking one, **stop and report it**.

1. **Never bypass, weaken, disable, or route around a gate.** That includes scan gates (SAST/SCA/IaC/container/secrets), required checks, and test suites. Do not add suppressions, `# nosec`/`# noqa`-style ignores, allowlist entries, `--no-verify`, or `continue-on-error: true` to force a broken build green. *(4.6.1.\*, 4.6.2.\*, 4.6.3.\*)*
2. **Never commit a secret.** Any detected secret blocks promotion. Use Secret Manager or environment variables. *(4.6.1.4, 4.6.2.3)*
3. **Never push unvalidated schema changes.** Database schema changes MUST be backward-compatible and use expand-and-contract patterns decoupled from app code releases. *(4.5.3.6)*
4. **Never put real production data or credentials in lower environments or tests.** Use synthetic data and fixtures. *(4.2.1.3)*
5. **Never introduce an undocumented manual step into deploy or infrastructure.** All infrastructure changes MUST be expressed as version-controlled OpenTofu/Terraform code. *(4.5.1.6, 4.2.2.6)*
6. **Automated CI Validation:** PRs must pass automated test suites and schema validation (`validate.py`) before merging to `main`. *(4.7.2.2)*

## 3. Before you write code

- **Read `README.md` and `AGENTS.md`** for repo-specific build, test commands, and conventions.
- **Check the target level** in §1 so you scope your obligations correctly.
- **If adding a runtime service, data store, queue, or gateway**, register it in `dsackr/drafting-table` and update `.draft/sdp.yaml`. *(4.1.1.1, 4.1.1.2)*

## 4. While you write code

### Observability (4.3)
- Log to standard output/JSON or OTEL-compatible central collector. Local-file-only logging is not acceptable as the sole sink. *(4.3.1.5)*
- Log level must be configurable via environment variables without requiring a code rebuild. *(4.3.2.5)*

### Testing (4.4)
- Ship tests with every functional change. Update `KPF.md` for any touched feature. *(4.4.1.3)*
- Do not delete, skip, or `xfail` a failing test to get green. Fix the test or fix the code.

### Database and schema changes (4.5.3.6)
- Schema changes are **decoupled from application deploys** using expand-and-contract: add the new column/table → backfill → dual-write → cut over → remove old shape in a later release.

### Deploys and infrastructure (4.1, 4.2, 4.5)
- Infrastructure changes MUST be expressed in IaC (OpenTofu/Terraform). *(4.2.2.6)*
- Declare an automated rollback path for anything non-trivially revertible. *(4.5.1.4)*

### Branches and PRs (4.7)
- Default branching strategy is **GitHub Flow**: short-lived feature branch off `main`, PR, CI pass, merge. *(4.7.2.5)*
- `main` must always be shippable. Do not merge broken code. *(4.7.2.2)*

## 5. Pre-PR checklist

Run through this before opening or merging a PR:

- [ ] `KPF.md` updated if product functionality changed *(4.3.1.1)*
- [ ] Tests added or updated; no test skipped, deleted, or weakened to get green *(4.4.1.\*)*
- [ ] No secrets, credentials, tokens, or real production data in the diff *(4.6.1.4)*
- [ ] No gate suppressions, ignores, or `continue-on-error` added *(4.6.3.\*)*
- [ ] Schema changes are backward-compatible and expand-and-contract *(4.5.3.6)*
- [ ] Infrastructure/config changes expressed in IaC — no manual steps *(4.2.2.6)*
- [ ] `validate.py` passes cleanly against the workspace *(4.1.1.\*)*
- [ ] Branch and commit conventions followed *(4.7.2.\*)*
