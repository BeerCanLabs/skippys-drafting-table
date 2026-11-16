# Workspace-local tools and docs

This folder belongs to BeerCanLabs. It holds material that used to be mixed into the
upstream framework copy when this repo was a fork of DRAFT. It was moved here
during the conversion to the standard DRAFT workspace layout (vendored framework at
`.draft/framework/`, pinned by `.draft/framework.lock`) so that nothing was lost.
None of it was sent upstream.

Do **not** put anything here under `.draft/framework/`. That directory is replaced
wholesale on every framework update.

| Path | What it is | Where it came from |
|---|---|---|
| `tools/build_deployment_plan.py` | Resolves a SoftwareDeploymentPattern to its deployable IaC modules and lists reference-only or stub services. Standalone; needs only PyYAML. Run `python local/tools/build_deployment_plan.py --workspace . --sdp catalog/engineering/software-deployment-patterns/<file>.yaml`. Pass `--sdp` explicitly: the auto-discovery walks the whole tree, including `.draft/framework/examples/`. | `framework/tools/build_deployment_plan.py` (local addition) |
| `docs/rfc-vector-database-indexing.md` | RFC for embedded vector search over the catalog. | `framework/docs/proposals/` (local addition) |
| `docs/roadmap-local-additions.md` | The local "Vector Database Indexing" roadmap section. | Root `ROADMAP.md` (local addition to an upstream file) |
| `docs/MATURITY.md`, `docs/KPF.md` | Engineering-maturity guide and the Key Product Functionality table the fork's `AGENTS.md` pointed agents to. | Repo root (local additions) |
| `skills/switch-game-architect/` | Switch's game-architecture decision matrix and scaffolding playbook for Aiden's games. | `agent/skills/` (local addition) |
| `skills/draftsman-engineering-maturity/` | Engineering-maturity / KPF guardrail skill for engineering agents. | `agent/skills/` (local addition) |
| `patches/generate_browser-default-workspace.diff` | The fork's one-line change that made `generate_browser.py` default to the repo root, not `examples/`. **Not needed any more:** upstream already defaults to the workspace root when it runs from `.draft/framework/`. Kept for the record. | `framework/tools/generate_browser.py` |
| `patches/framework-template-draft-framework-update.diff`, `patches/active-workflow-draft-framework-update.diff` | The fork's edits to the framework-update workflow: Sunday schedule, a `repository_dispatch` trigger, and syncing the root `agent/` directory. | `framework/templates/github/` and `.github/workflows/` |

## Local deviations in `.github/workflows/draft-framework-update.yml`

The workflow is upstream's `framework/templates/github/draft-framework-update.yml` from
the pinned tag, plus these local changes (keep them when re-syncing from the upstream template):

1. Runs on Sunday at 09:17 UTC (upstream runs Monday). Carried over from the fork.
2. Also runs on `repository_dispatch` type `upstream_draftsman_updated`. Carried over from the fork.
3. Vendors `framework/skills/` into `.draft/framework/skills/`. The upstream workflow
   copy list leaves out `skills` (upstream `draft_table/repo.py` includes it), so without
   this change a refresh would silently drop the Draftsman skills.
4. Re-runs `setup_ide.py` and `validate_skills.py --workspace .` after a refresh, and
   commits `.claude/` and `AGENTS.md`, so the projected skills stay current.
5. `vendored_text()` protects existing `.draft/framework` paths with the
   `__DRAFT_VENDOR_FRAMEWORK_ROOT__` placeholder before rewriting `framework/...`
   paths and restores them afterwards. This is the same guard as upstream
   `draft_table/repo.py` `vendored_framework_text()`. Without it the workflow
   corrupts `.draft/framework/...` references in vendored Markdown into
   `.draft/...`, so the result no longer matches a `vendor_framework()` copy.
6. Every `steps.refresh.outputs.*` value used inside a `run:` script is passed
   through `env:` and read as a quoted shell variable, never interpolated with
   `${{ }}` directly into the script (prevents script injection). `if:`
   expressions still use the outputs directly.
7. `latest_target_ref()` returns only the newest `vX.Y.Z` release tag on automatic
   runs (schedule or `repository_dispatch` without `target_ref`). Upstream also
   switched to untagged `main` when main declared a newer version; that fallback
   is removed, and if no release tag exists the run stops with a message. A manual
   `workflow_dispatch` `target_ref` naming `main`, a branch, a tag, or a commit is
   still honoured.

The fork's step that synced a root `agent/` directory was dropped. `agent/` has been
retired, and the Draftsman now ships as upstream skills under `.draft/framework/skills/`.

The workflow opens its update PR with `GITHUB_TOKEN`. That only works when the
repository setting "Allow GitHub Actions to create and approve pull requests" is on.
That setting is currently off and was left unchanged.

## Retired with the conversion (still in git history)

- `agent/`: the SM-draftsman agent package (spec, Hermes bindings, MCP server, and the
  upstream `draftsman*` skills). The local skills above were kept.
- Root copies of upstream framework files: `framework/`, `templates/`, `examples/`,
  `providers/`, `draft_table/`, `tests/`, `upstream/`, `pyproject.toml`, `uv.lock`,
  `install-draft-table.sh`, `draft-framework.yaml`, the logos, `AI_INDEX.md`,
  `CHANGELOG.md`, `HISTORY.md`, `RELEASE.md`, `ROADMAP.md`, `VERSIONING.md`,
  `security.md`, the framework repo's issue and PR templates, and its release,
  tagging, and CI workflows.
- `docs/CNAME` (upstream's `draftstandard.ai` domain; Pages here has no custom domain) and
  `docs/assets/draft-indexes.json` (a framework-repo artifact the workspace browser
  does not read).
- `.claude/worktrees/agent-a699b6c2`: a stray submodule entry with no `.gitmodules` URL.
