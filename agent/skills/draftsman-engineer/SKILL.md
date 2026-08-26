---
name: draftsman-engineer
description: Product engineering architecture assistant for product registration, local repo .draft/sdp.yaml scaffolding, code autodiscovery, and local validation.
---

# Draftsman Engineer Skill

## Role & Responsibilities

The `draftsman-engineer` agent skill is used by connected AI coding assistants (Cursor, Claude Code, GitHub Copilot, Antigravity, VS Code) in product engineering repositories.

It guides developers through:
1. **Product Registration**: Registering a product in the central `drafting-table` workspace using the `product_registration` schema contract.
2. **Local SDP Scaffolding**: Initializing `.draft/sdp.yaml` and `.github/workflows/draft-sync.yml` inside the product repository via `/draft init`.
3. **Code Autodiscovery**: Inspecting `Dockerfile`, `docker-compose.yml`, `main.tf`, `pom.xml`, `package.json`, or `requirements.txt` to infer application runtimes, ports, and datastore dependencies.
4. **Local Validation & Authoring**: Editing `.draft/sdp.yaml` and running `python3 .draft/framework/tools/validate.py` to ensure pre-commit compliance.

## Environment & Permissions

- **Execution Context**: Developer's local workstation / IDE chat session.
- **Identity Model**: Runs under the developer's local Git working copy and Git credentials.
- **Write Permissions**: Writes `.draft/sdp.yaml` to the local filesystem for normal Git commits and Pull Requests.
