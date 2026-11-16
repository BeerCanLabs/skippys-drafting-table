---
name: switch-game-architect
description: Standardized decision matrix, Reference Architecture blueprints, scaffolding protocols, and automated UAT deployment workflows for Switch to build games for Aiden.
---

# Switch Game Architect & Delivery Skill (for Aiden's Games)

## Purpose
Provides **Switch** (the AI Application & Gateway Engineer Agent) with a deterministic, repeatable decision matrix and scaffolding playbook for building games for **Aiden**. Switch will never "make up answers" or guess how to handle authentication, datastores, or UAT deployments.

---

## 🎮 Game Reference Architecture Decision Matrix

When Aiden asks Switch to build a game, Switch evaluates the requested features and selects the matching DRAFT **ReferenceArchitecture**:

```text
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                      GAME REFERENCE ARCHITECTURE DECISION MATRIX                       │
 ├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
 │ Tier 1: Static Web Game  │ Tier 2: Persistent Web Game │ Tier 3: Real-Time Multiplayer │
 ├──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
 │ • RA: `ra-aiden-game-`   │ • No approved RA            │ • No approved RA              │
 │   `tier1-static.yaml`    │ • Auth & user profiles      │ • Real-time multiplayer       │
 │ • LocalStorage state     │ • Needs a decision record   │ • Needs a decision record     │
 │ • Host: GitHub Pages     │   before Switch builds it   │   before Switch builds it     │
 │ • Storage: Browser Local │                             │                               │
 │ • Approved and live      │                             │                               │
 └──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

Tier 1 is the only approved, catalogued stack (GitHub Pages). Tier 2 and Tier 3 have no approved stack. Switch MUST get a decision record before building a Tier 2 or Tier 3 game, and MUST NOT invent a cloud or datastore choice in the meantime.

---

## 🛠️ Step-by-Step Execution Playbook for Switch

### Step 1: Feature Evaluation & Reference Architecture Selection
1. If the game only needs local clicks, sound effects, or single-device progress:
   -> Select **Tier 1 (Static Web Game RA)** (`ra-aiden-game-tier1-static.yaml`).
2. If the game needs logins, saved profiles, cloud sync across devices, or leaderboards:
   -> This is **Tier 2**. There is no approved Reference Architecture and no approved auth or datastore stack. Stop and get a decision record before building anything.
3. If the game needs real-time multiplayer:
   -> This is **Tier 3**. There is no approved Reference Architecture. Stop and get a decision record before building anything.

---

### Step 2: Repository Scaffolding & Specific Game SDP
Whenever Switch creates a new game repo (e.g. `dsackr/aiden-cookie-clicker`):
1. **`MATURITY.md`**: Vendor the standard `MATURITY.md` file at root.
2. **`AGENTS.md`**: Add bootstrap instructions pointing to `MATURITY.md` and `KPF.md`.
3. **`KPF.md`**: Document Key Product Functionalities (e.g., `KPF-GAME-001: Clicker Loop`, `KPF-GAME-002: User Login & Save State`) mapped to unit/integration tests.
4. **`.draft/sdp.yaml`**: Generate the specific game SDP (e.g. `sdp-aiden-cookie-clicker.yaml`), setting `followsReferenceArchitecture` to the selected RA's UID when an approved RA exists (Tier 1 only today).
5. **DRAFT Product Registration**: Register the product in `dsackr/drafting-table` under `catalog/engineering/product-registrations/`.
6. **Activate the game standards group**: list requirement group `01M162FHHS-XAJQ` in the drafting-table workspace under `requirements.activeRequirementGroups`, and claim it on the game SDP via `requirementGroups`.

---

### Step 3: Auth & Persistent State Standard (Tier 2 Games)
There is no approved Tier 2 stack. Switch MUST NOT pick an auth provider, secret store, API host, or datastore on its own. Get a decision record first. The requirement is cloud-neutral: standard auth with secrets in a managed secret store, and a governed persistent DataStoreService, per that decision record.

---

### Step 4: Automated UAT Deployment (Aiden Playtesting)
* **Tier 1 Games:** Switch MUST set up automated GitHub Actions deployment (`.github/workflows/deploy-pages.yml`) to `https://dsackr.github.io/<repo-name>/`, so Aiden can immediately play.
* **Tier 2 and Tier 3 Games:** There is no approved UAT stack. Switch MUST get a decision record before setting up API hosting or any path other than GitHub Pages.
