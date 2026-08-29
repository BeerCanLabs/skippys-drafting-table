# DRAFT Integrations: Slack & Discord Chat Assistants

DRAFT provides read-only Slack and Discord integration manifests so organizations can deploy **Draftsman AI** as an interactive architecture assistant inside their team chat tools.

## Architectural Boundary & Security Model

The Draftsman Slack and Discord assistants operate strictly in **Query & Guidance Mode**:

* **Read-Only Scope**: The bot queries pre-compiled workspace indexes (`catalog_indexes.json`, `AI_INDEX.md`) in `drafting-table` to answer questions about architecture, runtime ports, database engines, dependencies, and compliance status.
* **Zero Write Access**: The bot holds **no write access** to GitHub repositories and cannot mutate catalog files or open pull requests from chat.
* **Onboarding Guidance**: When an engineer asks how to onboard a product, the bot provides clear guidance on using `/draft init` directly inside native developer tools (IDE / local working copy).

## Included Manifests

* `slack/manifest.yaml`: Declarative Slack App Manifest for 1-click import at `api.slack.com/apps`.
* `discord/application.json`: Discord Application configuration and slash command definitions for the Discord Developer Portal.

## Deployment Setup

### Slack Setup
1. Go to [Slack API Apps](https://api.slack.com/apps) and click **Create New App** -> **From an app manifest**.
2. Select your Slack workspace and paste the contents of `framework/integrations/slack/manifest.yaml`.
3. Set `DRAFTSMAN_HOST` to your deployed Draftsman API endpoint.
4. Install the App to your workspace.

### Discord Setup
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application named **Draftsman AI**.
2. Register the slash commands defined in `framework/integrations/discord/application.json`.
3. Configure your bot interaction endpoint URL to point to your deployed Draftsman API endpoint.
