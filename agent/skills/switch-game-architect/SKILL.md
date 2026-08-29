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
 │ • RA: `ra-aiden-game-`   │ • RA: `ra-aiden-game-`      │ • RA: `ra-aiden-game-`        │
 │   `tier1-static.yaml`    │   `tier2-persistent.yaml`   │   `tier3-multiplayer.yaml`    │
 │ • LocalStorage state     │ • Auth & User Profiles      │ • Redis Session / WebSockets  │
 │ • Host: GitHub Pages     │ • Host: GitHub Pages + API  │ • Host: Cloud Run WebSocket   │
 │ • Storage: Browser Local │ • Storage: Cloud SQL DB     │ • Storage: Redis + Cloud SQL  │
 └──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

---

## 🛠️ Step-by-Step Execution Playbook for Switch

### Step 1: Feature Evaluation & Reference Architecture Selection
1. If the game only needs local clicks, sound effects, or single-device progress:
   -> Select **Tier 1 (Static Web Game RA)** (`ra-aiden-game-tier1-static.yaml`).
2. If the game needs logins, saved profiles, cloud sync across devices, or leaderboards:
   -> Select **Tier 2 (Persistent Web Game RA)** (`ra-aiden-game-tier2-persistent.yaml`).

---

### Step 2: Repository Scaffolding & Specific Game SDP
Whenever Switch creates a new game repo (e.g. `dsackr/aiden-cookie-clicker`):
1. **`MATURITY.md`**: Vendor the standard `MATURITY.md` file at root.
2. **`AGENTS.md`**: Add bootstrap instructions pointing to `MATURITY.md` and `KPF.md`.
3. **`KPF.md`**: Document Key Product Functionalities (e.g., `KPF-GAME-001: Clicker Loop`, `KPF-GAME-002: User Login & Save State`) mapped to unit/integration tests.
4. **`.draft/sdp.yaml`**: Generate the specific game SDP (e.g. `sdp-aiden-cookie-clicker.yaml`), setting `followsReferenceArchitecture` to the selected RA's UID.
5. **DRAFT Product Registration**: Register the product in `dsackr/drafting-table` under `catalog/engineering/product-registrations/`.

---

### Step 3: Auth & Persistent State Standard (Tier 2 Games)
For any game requiring persistent memory or user profiles, Switch MUST follow the standard:
* **Frontend Auth UI:** Lightweight auth component (Firebase Auth or JWT token login).
* **Backend API:** Fast API service running on **GCP Cloud Run** (`host-gcp-cloud-run`).
* **Secrets:** JWT secret stored in **GCP Secret Manager** (`security-service-gcp-secret-manager`).
* **Datastore:** User profiles, save slots, and leaderboards stored in **Cloud SQL Postgres** (`data-store-service-gcp-postgres`).

---

### Step 4: Automated UAT Deployment (Aiden Playtesting)
Switch MUST set up automated GitHub Actions deployment so Aiden can immediately play:
* **Tier 1 Games:** Automated `.github/workflows/deploy-pages.yml` deploying to `https://dsackr.github.io/<repo-name>/`.
* **Tier 2 Games:** GitHub Actions builds & deploys API to Cloud Run, deploys static UI to GitHub Pages, and outputs the live playable UAT link to the chat!
