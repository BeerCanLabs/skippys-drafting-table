---
type: ai-index
title: "AI Framework Index"
description: "Generated index mapping all schemas, base configurations, and tools in the DRAFT framework checkout."
tags:
  - draft
  - ai_index
  - index
timestamp: 2026-06-12T21:06:02-07:00
---

# AI Framework Index

This generated file gives AI assistants a fast map of the DRAFT framework checkout.
It is intentionally framework-first: this upstream repository is a reusable template,
not a complete company architecture catalog. Organization-specific architecture content
belongs in private company DRAFT repos that vendor this framework under `.draft/framework/`.

Regenerate with:

```bash
python3 framework/tools/generate_ai_index.py
```

## Draftsman Bootstrap

When a user says "I need a draftsman", the AI should immediately assume the
Draftsman role defined in `framework/docs/draftsman.md`, then use this index,
the selected framework schemas/configurations, provider packs, and workspace YAML to guide the conversation and edits.

## Framework Entrypoints

| Path | Purpose |
|---|---|
| AGENTS.md | Canonical AI bootstrap instructions for this repository. |
| draft-framework.yaml | Machine-readable DRAFT Framework version and compatibility manifest. |
| ROADMAP.md | v1.0 readiness roadmap and canonical MVP work items. |
| VERSIONING.md | Framework semantic versioning and compatibility policy. |
| CHANGELOG.md | Required release notes for every framework release. |
| RELEASE.md | Release checklist for version, changelog, validation, and publishing steps. |
| pyproject.toml | Python packaging metadata for experimental post-v1.0 local tooling. |
| draft_table | Experimental local DRAFT Table app prototype; not required for the v1.0 repo-first workflow. |
| framework/browser | Static browser shell, CSS, JavaScript, and default theme assets copied by generate_browser.py. |
| security.md | Credential and local security boundary notes for optional local tooling. |
| framework/docs/draftsman.md | Draftsman role, intent routing, and authoring rules. |
| framework/docs/setup-mode.md | Draftsman first-run setup mode and guided interview cadence. |
| framework/docs/engineering-onboarding.md | Targeted onboarding tutorial for product engineering teams. |
| framework/docs/shared-services-onboarding.md | Targeted onboarding tutorial for platform/shared services teams. |
| framework/docs/draft-admins-onboarding.md | Targeted onboarding tutorial for workspace administrators. |
| framework/docs/company-vocabulary.md | Optional company vocabulary lists, advisory/gated validation, and proposal flow. |
| framework/docs/overview.md | Framework concepts and object family overview. |
| framework/docs/object-types.md | User-facing DRAFT object type taxonomy and deployable/non-deployable distinction. |
| framework/docs/delivery-models.md | Delivery model meanings for self-managed, PaaS, SaaS, and appliance services. |
| framework/docs/yaml-schema-reference.md | Quick map from object families to schemas. |
| framework/docs/how-to-add-objects.md | Practical object authoring workflow. |
| framework/docs/workspaces.md | Private workspace layout and source-based workflow. |
| framework/docs/requirement-groups.md | Unified requirement group authoring and validation behavior. |
| framework/docs/capabilities.md | Capability object model and implementation lookup behavior. |
| framework/docs/drafting-sessions.md | How to persist incomplete authoring work. |
| framework/tools/validate.py | Executable validation for schemas, RequirementGroups, capabilities, and references. |
| framework/tools/apply_vocabulary_proposals.py | Materializes Draftsman vocabulary_proposal files into reviewable company vocabulary entries. |
| framework/tools/repair_uids.py | Explicit repair utility that adds or replaces generated object UIDs and rewrites object references. |
| framework/tools/generate_browser.py | Static GitHub Pages browser generator. |
| framework/tools/indexes.py | Shared canonical catalog index builders for domain-capability mappings and requirement implementation evidence. |
| framework/tools/generate_indexes.py | Generates committed machine-readable catalog indexes consumed by derived browser and AI assets. |
| framework/tools/migrations/0.36.1/migrate_to_nested_catalog.py | Automated utility to migrate flat catalog directories under catalog/ to role-nested paths. |
| install-draft-table.sh | Experimental local tooling installer retained for post-v1.0 work. |

## Framework Docs

| Path | Title | Summary |
|---|---|---|
| framework/docs/COMPOSITION_ROADMAP.md | DRAFT Framework Architecture Composition Roadmap | This roadmap defines the implementation specifications for follow-on DRAFT framework capabilities. These items build... |
| framework/docs/SHARED_SERVICE_COMPOSITION_SPEC.md | Deployable Shared Services Composition Specification | DRAFT enables **Enterprise-Grade Vibe Coding** by turning static architecture specifications into composable, standar... |
| framework/docs/capabilities.md | Capabilities | A Capability is a first-class framework object that names an architecture |
| framework/docs/company-vocabulary.md | Company Vocabulary | Company vocabulary lists are optional governed lists in `.draft/workspace.yaml`. |
| framework/docs/decentralized-sdp-setup.md | Decentralized SoftwareDeploymentPatterns & Product Registration | How product engineering teams house SoftwareDeploymentPatterns in their own repos and register with drafting-table. |
| framework/docs/decision-records.md | DecisionRecords | DecisionRecords are first-class records for known risks, |
| framework/docs/delivery-models.md | Delivery Models | Delivery models explain how a deployable service is operated. |
| framework/docs/design-principles.md | Design Principles | DRAFT is opinionated. |
| framework/docs/draft-admins-onboarding.md | Draft Admins Onboarding Guide | As a Draft Admin, you own the DRAFT **platform configuration** and **governance layers** inside the repository. |
| framework/docs/drafting-sessions.md | DraftingSessions | A DraftingSession is a machine-readable record of partial architecture work. |
| framework/docs/draftsman-ai-configuration.md | Draftsman AI Guidance | DRAFT does not include a built-in AI runtime. |
| framework/docs/draftsman.md | Draftsman Instructions | The Draftsman is an AI architecture-authoring agent for DRAFT. |
| framework/docs/engineering-onboarding.md | Engineering Onboarding Guide | As an Engineering representative, you are accountable for the **engineering layer** of the architecture catalog. |
| framework/docs/exporters.md | DRAFT Exporters | DRAFT catalogs are authoritative YAML — the source of truth for architecture |
| framework/docs/how-to-add-objects.md | How To Add Objects | The fastest way to add a new object correctly is to decide what kind of thing you are modeling before you write YAML. |
| framework/docs/naming-conventions.md | Naming Conventions | When a DRAFT object type is referred to by name in prose, headings, schema |
| framework/docs/object-types.md | DRAFT Object Types | DRAFT object types are split into deployable objects and non-deployable |
| framework/docs/operations-guide.md | Draft Operations Guide | The Draft Operations Guide defines how Draft work is routed, reviewed, ticketed, triaged, assigned, and closed in a G... |
| framework/docs/overview.md | Framework Overview | This page is the high-level object map for DRAFT. |
| framework/docs/reference-architectures.md | ReferenceArchitectures | The DRAFT framework ships a set of baseline ReferenceArchitectures in |
| framework/docs/requirement-groups.md | RequirementGroups | A RequirementGroup is the unified DRAFT requirement model. |
| framework/docs/roles-and-layers.md | Roles and Layers | DRAFT recognizes three roles. |
| framework/docs/sdp-completion-interview.md | SDP Completion Interview | The SDP Completion Interview is a structured protocol for enriching an existing |
| framework/docs/security-and-compliance-controls.md | Security And Compliance RequirementGroups | DRAFT treats compliance as an explicitly activated authoring and validation layer. |
| framework/docs/setup-mode.md | Draftsman Setup Mode | Setup mode is the first-run Draftsman conversation for a company DRAFT |
| framework/docs/shared-services-onboarding.md | Shared Services Onboarding Guide | As a Shared Services representative, you are accountable for the **shared-services layer** of the architecture catalog. |
| framework/docs/software-deployment-patterns.md | SoftwareDeploymentPatterns | A SoftwareDeploymentPattern is a declaration that a specific product is intended |
| framework/docs/soul.md | Draftsman Soul | The character, voice, and interaction design of the Draftsman — who it is, how it feels, and how it speaks to the per... |
| framework/docs/standards.md | Deployable Objects | DRAFT previously used the word "Standard" for reusable deployable building |
| framework/docs/technology-components.md | TechnologyComponents | A TechnologyComponent is a discrete vendor product object. |
| framework/docs/ticketing.md | Ticketing and Issue Creation Workflow | DRAFT is a repo-first, automation-friendly framework. |
| framework/docs/user-manual.md | DRAFT User Manual | DRAFT is an AI-first, Git-native, repo-first framework for documenting governed architecture. |
| framework/docs/workspaces.md | Workspaces | For the full adoption sequence from installation through first drafting sessions, see the role-specific onboarding tu... |
| framework/docs/yaml-schema-reference.md | YAML Schema Reference | This page is the quickest way to understand how to build a valid YAML object in |

## Schemas

| Path | Scope | Required Fields |
|---|---|---|
| framework/schemas/ai-gateway.schema.yaml | ai_gateway | schemaVersion, uid, type, name, deliveryModel, catalogStatus, lifecycleStatus |
| framework/schemas/business-unit-hierarchy.schema.yaml | business_unit_hierarchy | schemaVersion, uid, type, name, businessUnit, hierarchy, catalogStatus |
| framework/schemas/capability.schema.yaml | capability | schemaVersion, uid, type, name, description, catalogStatus, definitionOwner, domain, implementations |
| framework/schemas/data-component.schema.yaml | data_component | schemaVersion, uid, type, name, repoUrl, owner, runsOn, targetEngine, dataClassification, containsPII, catalogStatus |
| framework/schemas/data-store-service.schema.yaml | data_store_service | schemaVersion, uid, type, name, deliveryModel, catalogStatus, lifecycleStatus |
| framework/schemas/decision-record.schema.yaml | decision_record | schemaVersion, uid, type, name, category, status, catalogStatus, lifecycleStatus |
| framework/schemas/deployment-target.schema.yaml | deployment_target | schemaVersion, uid, type, name, environmentTier, targetProvider, parameters, catalogStatus |
| framework/schemas/domain.schema.yaml | domain | schemaVersion, uid, type, name |
| framework/schemas/drafting-session.schema.yaml | drafting_session | schemaVersion, uid, type, name, catalogStatus, lifecycleStatus, sessionStatus, primaryObjectType, sourceArtifacts, generatedObjects, unresolvedQuestions |
| framework/schemas/environment-tier.schema.yaml | environment_tier | schemaVersion, uid, type, name, tierId, purpose, availabilityExpectation, catalogStatus |
| framework/schemas/host.schema.yaml | host | schemaVersion, uid, type, name, catalogStatus, lifecycleStatus |
| framework/schemas/network-service.schema.yaml | network_service | schemaVersion, uid, type, name, deliveryModel, catalogStatus, lifecycleStatus |
| framework/schemas/object-patch.schema.yaml | object_patch | schemaVersion, uid, type, name, target, patch, catalogStatus, lifecycleStatus |
| framework/schemas/product-component.schema.yaml | product_component | schemaVersion, uid, type, name, repoUrl, owner, classification, catalogStatus |
| framework/schemas/product-registration.schema.yaml | product_registration | schemaVersion, uid, type, name, owner, catalogStatus, repository |
| framework/schemas/reference-architecture.schema.yaml | reference_architecture | schemaVersion, uid, type, name, catalogStatus, lifecycleStatus |
| framework/schemas/relationship.schema.yaml | relationship | schemaVersion, uid, type, name, source, label, catalogStatus |
| framework/schemas/requirement-group.schema.yaml | requirement_group | schemaVersion, uid, type, name, description, catalogStatus, activation, appliesTo, requirements |
| framework/schemas/runtime-service.schema.yaml | runtime_service | schemaVersion, uid, type, name, deliveryModel, catalogStatus, lifecycleStatus |
| framework/schemas/software-deployment-pattern.schema.yaml | software_deployment_pattern | schemaVersion, uid, type, name, catalogStatus, lifecycleStatus |
| framework/schemas/system.schema.yaml | system | schemaVersion, uid, type, name, catalogStatus, lifecycleStatus |
| framework/schemas/technology-component.schema.yaml | technology_component | schemaVersion, uid, type, name, vendor, productName, productVersion, classification, catalogStatus |

## Base Configurations

These YAML files are framework-owned base configurations. Company workspaces add third-party packs under `.draft/providers/` and company behavior through their private `configurations/` folder while keeping the vendored framework copy under `.draft/framework/` refreshable.

| UID | Name | Type | Tags | Description | Path |
|---|---|---|---|---|---|
| 01KQQ4Q026-4JR6 | Access Control Model | capability |  | Authorization model that controls access to a service or data platform. | framework/configurations/capabilities/capability-access-control-model.yaml |
| 01KTWS3D6T-5TAZ | AI Gateway | capability |  | Outbound LLM/AI request traffic is routed, authenticated, rate-limited, and audited at a managed proxy layer that enf... | framework/configurations/capabilities/capability-ai-gateway.yaml |
| 01KT0XNZEY-A7GK | Analytics | capability |  | Operational and business data is processed and analyzed to produce insight through a managed analytics platform. | framework/configurations/capabilities/capability-analytics.yaml |
| 01KT0V5MCV-3A6F | API Gateway | capability |  | Inbound API traffic is routed, authenticated, rate-limited, and transformed at a managed entry point in front of back... | framework/configurations/capabilities/capability-api-gateway.yaml |
| 01KQQ4Q026-NB1W | Application Performance Monitoring | capability |  | Tracing and performance analysis of application runtimes. | framework/configurations/capabilities/capability-apm.yaml |
| 01KT0V5MCV-RZV0 | Application Runtime | capability |  | First-party application code executes on a managed runtime that provides the process, web, or worker execution enviro... | framework/configurations/capabilities/capability-application-runtime.yaml |
| 01KT0XNZEY-7HWQ | Artifact Management | capability |  | Build outputs, packages, images, and dependencies are stored, versioned, and served from a managed artifact repository. | framework/configurations/capabilities/capability-artifact-management.yaml |
| 01KQQ4Q026-MHJM | Authentication | capability |  | Identity and access authentication capability for users, services, administrators, or workloads. | framework/configurations/capabilities/capability-authentication.yaml |
| 01KT0V5MCV-ECR4 | Caching | capability |  | Frequently accessed data is stored in a fast, ephemeral tier to reduce latency and load on the system of record. | framework/configurations/capabilities/capability-caching.yaml |
| 01KT0V5MCV-HZ37 | CDN | capability |  | Static and cacheable content is distributed and served from edge locations close to consumers to reduce latency and o... | framework/configurations/capabilities/capability-cdn.yaml |
| 01KT0XNZEY-RVTG | Certificate Management | capability |  | Digital certificates are issued, distributed, renewed, and revoked through a managed certificate or PKI service. | framework/configurations/capabilities/capability-certificate-management.yaml |
| 01KT0XNZEY-Q2TF | CI/CD Pipeline | capability |  | Source code is automatically built, tested, and promoted through environments by an automated continuous integration... | framework/configurations/capabilities/capability-cicd-pipeline.yaml |
| 01KQQ4Q026-1HZP | Compute Platform | capability |  | Compute substrate or virtualized platform used to run Hosts. | framework/configurations/capabilities/capability-compute-platform.yaml |
| 01KT0XNZEY-35Y2 | Configuration Management | capability |  | System and application configuration is declared, applied, and reconciled across environments through a managed confi... | framework/configurations/capabilities/capability-configuration-management.yaml |
| 01KQQ4Q026-GW5D | Container Orchestration | capability |  | Management of containerized workload lifecycles. | framework/configurations/capabilities/capability-container-orchestration.yaml |
| 01KT0XNZEY-DENJ | Data Integration | capability |  | Data is moved, transformed, and synchronized between systems through a managed integration or ETL platform. | framework/configurations/capabilities/capability-data-integration.yaml |
| 01KT0V5MCV-VD0Y | Data Persistence | capability |  | Structured application data is durably stored, queried, and managed in a database or persistence platform. | framework/configurations/capabilities/capability-data-persistence.yaml |
| 01KQQ4Q026-7T2H | Data Resilience | capability |  | Resilience of data against loss or corruption through backup, restore, replication, and recovery capabilities. | framework/configurations/capabilities/capability-data-resilience.yaml |
| 01KT0V5MCV-GJBH | DNS | capability |  | Names are resolved to network addresses through authoritative and recursive domain name resolution. | framework/configurations/capabilities/capability-dns.yaml |
| 01KT0XNZEY-KPTW | Email Delivery | capability |  | Outbound and transactional email is accepted, routed, and delivered to recipients through a managed mail delivery ser... | framework/configurations/capabilities/capability-email-delivery.yaml |
| 01KQQ4Q026-H3B5 | Encryption At Rest | capability |  | Protection of persisted data through encryption or equivalent storage safeguards. | framework/configurations/capabilities/capability-encryption-at-rest.yaml |
| 01KT0V5MCV-924J | File Storage | capability |  | Files are durably stored and accessed through a shared file system or file storage interface. | framework/configurations/capabilities/capability-file-storage.yaml |
| 01KT0XNZEY-K1J3 | File Transfer | capability |  | Files are exchanged between systems or partners reliably and securely through a managed file transfer service. | framework/configurations/capabilities/capability-file-transfer.yaml |
| 01KQQ4Q026-98VD | Health and Welfare Monitoring | capability |  | Runtime health, uptime, metrics, and operational welfare visibility. | framework/configurations/capabilities/capability-health-welfare-monitoring.yaml |
| 01KQQ4Q026-D04B | Log Management | capability |  | Aggregation, retention, searchability, and forwarding of system or application logs. | framework/configurations/capabilities/capability-log-management.yaml |
| 01KT0V5MCV-KT72 | Messaging | capability |  | Asynchronous messages and events are accepted, queued, and delivered between producers and consumers. | framework/configurations/capabilities/capability-messaging.yaml |
| 01KTWS3D6T-T6F6 | Model Inference & Serving | capability |  | Runtimes and infrastructure for deploying, hosting, and serving machine learning and large language model weights via... | framework/configurations/capabilities/capability-model-inference.yaml |
| 01KSWVZSZ5-Q6HW | Network Connectivity | capability |  | Hosts and services can reach each other across the network fabric through approved switching and routing infrastructure. | framework/configurations/capabilities/capability-network-connectivity.yaml |
| 01KSWVZSZ5-1RTH | Network Segmentation | capability |  | Traffic between network zones is isolated and controlled by policy through VLANs, micro-segmentation, or software-def... | framework/configurations/capabilities/capability-network-segmentation.yaml |
| 01KT0V5MCV-E9TN | Object Storage | capability |  | Unstructured objects and blobs are durably stored and retrieved through an object storage interface. | framework/configurations/capabilities/capability-object-storage.yaml |
| 01KQQ4Q026-QM2X | Operating System | capability |  | Supported operating system product used to define managed Hosts. | framework/configurations/capabilities/capability-operating-system.yaml |
| 01KQQ4Q026-BH6E | Patch Management | capability |  | Patch orchestration and update application capability for managed runtime components. | framework/configurations/capabilities/capability-patch-management.yaml |
| 01KQQ4Q026-S5J6 | Performance and Load Testing | capability |  | Capabilities to simulate load and measure system behavior under stress. | framework/configurations/capabilities/capability-performance-testing.yaml |
| 01KQQ4Q026-RTWC | Quality Gates | capability |  | Promotion criteria and automated checks required for lifecycle transitions. | framework/configurations/capabilities/capability-quality-gates.yaml |
| 01KT0XNZEY-70Y6 | Reporting | capability |  | Curated metrics and datasets are presented to consumers through managed reports and dashboards. | framework/configurations/capabilities/capability-reporting.yaml |
| 01KQQ4Q026-DTJJ | Secrets Management | capability |  | Secure storage, rotation, and access mediation for secrets and authenticators. | framework/configurations/capabilities/capability-secrets-management.yaml |
| 01KQQ4Q026-JW52 | Security Monitoring | capability |  | Threat detection, intrusion detection, security event monitoring, and audit telemetry. | framework/configurations/capabilities/capability-security-monitoring.yaml |
| 01KQQ4Q026-3ZWJ | Serverless Function Runtime | capability |  | Event-driven, scale-to-zero compute runtime capability. | framework/configurations/capabilities/capability-serverless-runtime.yaml |
| 01KT0V5MCV-RM8M | Service Mesh | capability |  | Service-to-service traffic is routed, secured, and observed through a dedicated connectivity and policy layer. | framework/configurations/capabilities/capability-service-mesh.yaml |
| 01KQQ4Q026-QC9S | Test Authoring | capability |  | Tools and frameworks used to author automated tests. | framework/configurations/capabilities/capability-test-authoring.yaml |
| 01KQQ4Q026-58Q3 | Test Execution and Automation | capability |  | Runtimes and orchestration services used to execute automated tests. | framework/configurations/capabilities/capability-test-execution.yaml |
| 01KSWVZSZ5-M0FR | Traffic Management | capability |  | Application and network traffic is distributed, shaped, and controlled across services and infrastructure through app... | framework/configurations/capabilities/capability-traffic-management.yaml |
| 01KT0V5MCV-Z079 | WAF | capability |  | Inbound web traffic is inspected and filtered against application-layer threats through managed rule sets before reac... | framework/configurations/capabilities/capability-waf.yaml |
| 01KSWVZSZ5-26F1 | WAN Connectivity | capability |  | Sites, data centers, and cloud environments are interconnected reliably through approved wide area network technology. | framework/configurations/capabilities/capability-wan-connectivity.yaml |
| 01KTWS3D6T-NB0E | AI Gateway RequirementGroup | requirement_group | ai-gateway, requirement-group, definition | Structured checklist of required questions and answers used to define a complete and correct AI Gateway. | framework/configurations/requirement-groups/requirement-group-ai-gateway.yaml |
| 01KQQ4Q027-DSDD | Appliance Delivery RequirementGroup | requirement_group | appliance, requirement-group, definition | Structured requirements used when a Runtime, Data Store, or NetworkService uses appliance delivery and the underlying... | framework/configurations/requirement-groups/requirement-group-appliance-delivery.yaml |
| 01KRWRRNM7-VJ5A | DataComponent RequirementGroup | requirement_group | data-component, requirement-group, definition | Built-in checklist for first-party data artifacts deployed onto DataStoreServices. Establishes what must be known abo... | framework/configurations/requirement-groups/requirement-group-data-component.yaml |
| 01KQQ4Q027-VBF0 | DataStoreService RequirementGroup | requirement_group | service, dbms, requirement-group, definition | Additional DataStoreService checklist items extending the service behavior RequirementGroup for durable data, recover... | framework/configurations/requirement-groups/requirement-group-data-store-service.yaml |
| 01KQQ4Q027-69VY | NIST Cybersecurity Framework RequirementGroup | requirement_group | compliance, nist, starter-pack, requirement-group | Initial NIST Cybersecurity Framework (CSF) 2.0 requirement group scoped to the outcomes that can be meaningfully answ... | framework/configurations/requirement-groups/requirement-group-draft-nist-csf.yaml |
| 01KQQ4Q027-T3CA | Security and Security Compliance RequirementGroup | requirement_group | compliance, controls, baseline, requirement-group | Baseline security and compliance requirement group bundled with DRAFT. Requirements are applied to matching object ty... | framework/configurations/requirement-groups/requirement-group-draft-security-compliance.yaml |
| 01KQQ4Q027-7JN2 | SOC 2 RequirementGroup | requirement_group | compliance, soc2, starter-pack, requirement-group | Initial SOC 2 requirement group based on the AICPA Trust Services Criteria. These requirements use DRAFT applicabilit... | framework/configurations/requirement-groups/requirement-group-draft-soc2.yaml |
| 01KQQ4Q027-1GHC | TX-RAMP RequirementGroup | requirement_group | compliance, tx-ramp, starter-pack, requirement-group | Starter TX-RAMP requirement group for DRAFT. This file is intended to map TX-RAMP control expectations onto the unifi... | framework/configurations/requirement-groups/requirement-group-draft-tx-ramp.yaml |
| 01KQQ4Q027-HHA4 | DraftingSession RequirementGroup | requirement_group | drafting-session, requirement-group, intake | Structured checklist used to capture partial architecture-authoring sessions, generated outputs, and unresolved follo... | framework/configurations/requirement-groups/requirement-group-drafting-session.yaml |
| 01KSF4NHSP-8HPP | Engineering Quality RequirementGroup | requirement_group | product-component, requirement-group, engineering, quality, optional | Optional checklist for ProductComponents covering build quality, test coverage, and performance validation practices.... | framework/configurations/requirement-groups/requirement-group-engineering-quality.yaml |
| 01KSF4NHSP-HCPX | Host Compute Profile RequirementGroup | requirement_group | host, requirement-group, compute, optional | Optional checklist for Hosts covering compute type classification. Activated per workspace; does not fire automatically. | framework/configurations/requirement-groups/requirement-group-host-compute-profile.yaml |
| 01KQQ4Q027-THYN | Host RequirementGroup | requirement_group | host, requirement-group, definition | Structured checklist of required questions and answers used to define a complete and correct Host. | framework/configurations/requirement-groups/requirement-group-host.yaml |
| 01KSWVZSZ5-B146 | NetworkService RequirementGroup | requirement_group | network, requirement-group, definition | Base requirements for NetworkService objects covering network function declaration, topology definition, and protocol... | framework/configurations/requirement-groups/requirement-group-network-service.yaml |
| 01KQQ4Q027-TPWG | PaaS Delivery RequirementGroup | requirement_group | paas, requirement-group, definition | Structured requirements used when a Runtime, Data Store, or NetworkService is vendor-managed inside the organization'... | framework/configurations/requirement-groups/requirement-group-paas-delivery.yaml |
| 01KRWRRNM7-G642 | ProductComponent RequirementGroup | requirement_group | product-component, requirement-group, definition | Built-in checklist for first-party code components deployed onto RuntimeServices. Establishes what must be known abou... | framework/configurations/requirement-groups/requirement-group-product-component.yaml |
| 01KQQ4Q027-SS2K | ReferenceArchitecture RequirementGroup | requirement_group | reference-architecture, requirement-group, definition | Structured checklist of required questions and answers used to define a complete and correct ReferenceArchitecture. | framework/configurations/requirement-groups/requirement-group-reference-architecture.yaml |
| 01KQQ4Q027-K5DR | Service Behavior RequirementGroup | requirement_group | service, requirement-group, definition | Structured checklist of required questions and answers used to define complete and correct self-managed Runtime and N... | framework/configurations/requirement-groups/requirement-group-runtime-service.yaml |
| 01KQQ4Q027-FKRM | SaaS Delivery RequirementGroup | requirement_group | saas, requirement-group, definition | Structured requirements used when a Runtime, Data Store, or NetworkService is consumed as a vendor-managed external s... | framework/configurations/requirement-groups/requirement-group-saas-delivery.yaml |
| 01KT0VM061-CRN7 | Service Capability RequirementGroup | requirement_group | service, capability, requirement-group, definition | Self-declared capability requirements for shared service objects. When a RuntimeService, DataStoreService, or Network... | framework/configurations/requirement-groups/requirement-group-service-capability.yaml |
| 01KSF29JTP-SRVE | Service Engineering Practices RequirementGroup | requirement_group | service, requirement-group, engineering, optional | Optional checklist for self-managed Runtime and NetworkServices covering advanced observability and runtime patterns.... | framework/configurations/requirement-groups/requirement-group-service-engineering.yaml |
| 01KQQ4Q027-VK45 | SoftwareDeploymentPattern RequirementGroup | requirement_group | software-deployment-pattern, requirement-group, definition | Structured checklist of required questions and answers used to define a complete and correct software deployment patt... | framework/configurations/requirement-groups/requirement-group-software-deployment-pattern.yaml |
| 01KTWS3D6T-ABD1 | AI & Machine Learning | domain |  | Strategic domain covering model training, inference serving, vector storage, and AI gateway routing. Capabilities in... | framework/configurations/domains/ai-ml.yaml |
| 01KT0XNZEY-HGZZ | Analytics | domain |  | Strategic domain covering analytical processing and reporting over operational and business data. Capabilities in thi... | framework/configurations/domains/analytics.yaml |
| 01KQQ4Q027-ZTHF | Compute & Runtime | domain |  | Strategic domain covering application runtimes, serverless functions, and physical or virtual compute resources. | framework/configurations/domains/compute.yaml |
| 01KSWVZSZ5-QHKZ | Data | domain |  | Strategic domain covering data protection and resilience. Capabilities in this domain are governed by the data and st... | framework/configurations/domains/data.yaml |
| 01KSWVZSZ5-71PY | Identity & Access Management | domain |  | Strategic domain covering authentication and authorization. Capabilities in this domain are governed by the IAM team,... | framework/configurations/domains/identity.yaml |
| 01KT0XNZEY-QY0Y | Integration | domain |  | Strategic domain covering the movement of messages, files, and data between systems. Capabilities in this domain are... | framework/configurations/domains/integration.yaml |
| 01KSWVZSZ5-4WKE | Network | domain |  | Strategic domain covering network fabric infrastructure, connectivity, and segmentation. Capabilities in this domain... | framework/configurations/domains/network.yaml |
| 01KQQ4Q027-C213 | Observability & Monitoring | domain |  | Strategic domain covering logging, metrics, tracing, and health monitoring across infrastructure and application stacks. | framework/configurations/domains/observability.yaml |
| 01KSWVZSZ5-GY67 | Security | domain |  | Strategic domain covering threat detection, security event monitoring, and secure credential management. Capabilities... | framework/configurations/domains/security.yaml |
| 01KT0XNZEY-GXYR | Software Delivery | domain |  | Strategic domain covering the build, integration, packaging, and configuration pipeline that delivers software into r... | framework/configurations/domains/software-delivery.yaml |
| 01KQQ4Q027-SGHR | Testing & Quality | domain |  | Strategic domain covering all aspects of software testing, quality assurance, and release gates. | framework/configurations/domains/testing.yaml |

## Community Configurations

These YAML files are framework-provided opt-in patterns. Company workspaces may copy them into their private repositories to endorse or adapt them.

| UID | Name | Type | Tags | Description | Path |
|---|---|---|---|---|---|
| 01KTWYEE98-D3QV | AI-Enabled Application Pattern | reference_architecture | reference-architecture, ai, rag | Standard pattern for applications utilizing Artificial Intelligence and Large Language Models (LLMs). Integrates an a... | community/reference-architectures/ra-ai-enabled-application.yaml |
| 01M1637YZS-PZSH | Tier 1 Static Web Game Platform | reference_architecture | reference-architecture, game-platform, tier1-static, github-pages, uat | Reference architecture for client-side HTML5/Canvas games hosted on GitHub Pages for immediate UAT playtesting with b... | community/reference-architectures/ra-aiden-game-tier1-static.yaml |
| 01M1637YZT-QZ2Z | Tier 2 Persistent Web Game Platform | reference_architecture | reference-architecture, game-platform, tier2-persistent, cloud-run, cloud-sql, uat | Reference architecture combining a client UI on GitHub Pages, Cloud Run backend API, GCP Secret Manager Auth JWTs, an... | community/reference-architectures/ra-aiden-game-tier2-persistent.yaml |
| 01KV0REFAR-CMSV | Containerized Microservices | reference_architecture | reference-architecture, microservices, containers, starter | Starter pattern for independently deployable services running on a container orchestration platform with service-to-s... | community/reference-architectures/ra-containerized-microservices.yaml |
| GM7YJ3ZSA0-WHSN | Event-Driven Integration | reference_architecture | reference-architecture, event-driven, integration | Deployment pattern for systems coordinated through asynchronous events, queues, streams, or pub/sub topics. Use this... | community/reference-architectures/ra-event-driven-integration.yaml |
| 01KV0REFAR-EVNT | Event-Driven Architecture | reference_architecture | reference-architecture, event-driven, messaging, starter | Starter pattern for asynchronous systems coordinated by messaging, event routing, producers, consumers, and eventuall... | community/reference-architectures/ra-event-driven.yaml |
| 01KS8N4KR3-MTSA | Multi-Tenant SaaS | reference_architecture | reference-architecture, multi-tenant, saas | Deployment pattern for software-as-a-service products that serve multiple customer tenants from shared infrastructure... | community/reference-architectures/ra-multi-tenant-saas.yaml |
| 01KS8N4KR4-SVED | Serverless Event-Driven | reference_architecture | reference-architecture, serverless, event-driven | Deployment pattern for event-driven applications using serverless compute runtimes. No persistent application-tier co... | community/reference-architectures/ra-serverless-event-driven.yaml |
| 01KV0REFAR-STRG | Strangler Migration Pattern | reference_architecture | reference-architecture, migration, strangler, starter | Starter pattern for incremental legacy modernization where new services coexist with a legacy system and traffic or c... | community/reference-architectures/ra-strangler-migration.yaml |
| 01KS8N4KR2-3TWA | Three-Tier Web Application | reference_architecture | reference-architecture, three-tier, web | Standard pattern for web-facing applications with a presentation tier (network services), an application tier (runtim... | community/reference-architectures/ra-three-tier-web.yaml |
| 8Q79XMD460-MQ5A | Two-Tier Client/Data | reference_architecture | reference-architecture, two-tier, client-data | Deployment pattern for simple applications where a client or static presentation layer talks directly to a managed da... | community/reference-architectures/ra-two-tier-client-data.yaml |
| 01KV0REFAR-2TR0 | Two-Tier Client Data Application | reference_architecture | reference-architecture, two-tier, starter | Starter pattern for applications where a client or presentation layer talks directly to a managed data tier without a... | community/reference-architectures/ra-two-tier-web.yaml |

## Example Catalog Inventory

These are sample catalog objects used to validate and demonstrate the framework. Company-specific content belongs in a private company `catalog/` folder.

| UID | Name | Type | Tags | Description | Path |
|---|---|---|---|---|---|
| 01KQQ4Q025-1XDE | AWS Lambda Serverless Host | host | lambda, serverless | Serverless execution environment provided by AWS Lambda. The host is entirely AWS-managed and blackbox to the organiz... | examples/catalog/shared-services/hosts/host-serverless-lambda.yaml |
| 01KQQ4Q025-T7B7 | AWS Lambda Runtime | runtime_service | serverless, lambda | AWS Lambda serverless execution environment. Runs organization-authored function code without requiring host manageme... | examples/catalog/shared-services/runtime-services/runtime-service-aws-lambda-runtime.yaml |
| 01KQQ4Q025-MQ3F | CrowdStrike Falcon Agent | technology_component | technology-component, agent | Endpoint security agent installed locally on a host that requires communication with the CrowdStrike Falcon platform. | examples/catalog/shared-services/technology-components/technology-agent-crowdstrike-falcon.yaml |
| 01KQQ4Q025-9N4R | Amazon EC2 Standard Compute Platform | technology_component | technology-component, compute-platform | Standard Amazon EC2 virtual machine substrate used for general-purpose host patterns. | examples/catalog/shared-services/technology-components/technology-compute-amazon-ec2-standard.yaml |
| 01KSF29JTP-8YRX | HAProxy 2.9 | technology_component | technology-component, load-balancer, haproxy, openstack | Open-source TCP/HTTP load balancer and proxy server. Provides high-availability request distribution, health checking... | examples/catalog/shared-services/technology-components/technology-haproxy-29.yaml |
| 01KQQ4Q025-3HXA | Ubuntu 22.04 LTS | technology_component | technology-component, operating-system | Canonical Ubuntu Server 22.04 LTS operating system product definition for Linux host patterns. | examples/catalog/shared-services/technology-components/technology-os-canonical-ubuntu-2204.yaml |
| 01KQQ4Q025-Z042 | nginx 1.26 | technology_component | technology-component, software | nginx web server software installed locally on a managed host and used without a required vendor platform interaction. | examples/catalog/shared-services/technology-components/technology-software-nginx-126.yaml |
| 01KSF29JTP-DRHA | HAProxy Load Balancer Operational Architecture | decision_record | decision-record, openstack, load-balancer, haproxy | Documents the operational architecture decisions for the OpenStack API Load Balancer (HAProxy) — covering authenticat... | examples/catalog/governance/decision-records/dr-haproxy-lb-operational-architecture.yaml |
| 01KT1340H6-X3T5 | AWS Lambda Serverless Host — Security and Compliance decisions | decision_record | decision-record, example, compliance |  | examples/catalog/governance/decision-records/dr-host-serverless-lambda-compliance.yaml |
| 01KSE5V73Z-DRSC | OpenStack Ops Console — Secrets Injection via Platform Secret Store | decision_record | decision-record, openstack, secrets, product-component | Documents the decision to inject application secrets into the OpenStack Ops Console at deploy time via the platform s... | examples/catalog/governance/decision-records/dr-ops-console-secrets-injection.yaml |
| 01KT1340HF-1HG3 | AWS Lambda Runtime — Security and Compliance decisions | decision_record | decision-record, example, compliance |  | examples/catalog/governance/decision-records/dr-runtime-service-aws-lambda-runtime-compliance.yaml |
| 01KT11AQX1-55F1 | AWS Lambda Runtime — Deployment Topology and Qualities | decision_record | decision-record, example, deployment |  | examples/catalog/governance/decision-records/dr-runtime-service-aws-lambda-runtime-deployment.yaml |
| 01KT11AQX2-STQ4 | AWS Lambda Runtime — Resilience and Availability | decision_record | decision-record, example, resilience |  | examples/catalog/governance/decision-records/dr-runtime-service-aws-lambda-runtime-resilience.yaml |
| 01KSKWFZZX-NE4F | AWS Lambda Runtime → Amazon CloudWatch Metrics | relationship |  |  | examples/catalog/governance/relationships/relationship-aws-lambda-runtime-calls-amazon-cloudwatch-metrics.yaml |
| 01KSKWFZZX-34KP | AWS Lambda Runtime → AWS IAM | relationship |  |  | examples/catalog/governance/relationships/relationship-aws-lambda-runtime-calls-aws-iam.yaml |
| 01KSKWFZZX-JWP6 | AWS Lambda Runtime → Amazon CloudWatch Logs | relationship |  |  | examples/catalog/governance/relationships/relationship-aws-lambda-runtime-sends-events-to-amazon-cloudwatch-logs.yaml |
| 01KSKWFZZW-ZEKF | AWS Lambda Serverless Host → AWS Lambda Service | relationship |  |  | examples/catalog/governance/relationships/relationship-aws-lambda-serverless-host-calls-aws-lambda-service.yaml |

## Content Folder Counts

| Folder | YAML Count |
|---|---|
| framework/configurations/capabilities | 44 |
| framework/configurations/requirement-groups | 21 |
| framework/configurations/reference-architectures | 0 |
| framework/configurations/domains | 11 |
| community/reference-architectures | 12 |
| examples/catalog/engineering/product-components | 0 |
| examples/catalog/engineering/data-components | 0 |
| examples/catalog/engineering/software-deployment-patterns | 0 |
| examples/catalog/shared-services/hosts | 1 |
| examples/catalog/shared-services/runtime-services | 1 |
| examples/catalog/shared-services/data-store-services | 0 |
| examples/catalog/shared-services/network-services | 0 |
| examples/catalog/shared-services/technology-components | 5 |
| examples/catalog/governance/decision-records | 6 |
| examples/catalog/governance/sessions | 0 |
| examples/catalog/governance/relationships | 4 |
| examples/catalog/governance/systems | 0 |
| examples/catalog/governance/reference-architectures | 0 |

## Templates

| Path | Purpose |
|---|---|
| templates/capability.yaml.tmpl | Reusable YAML authoring template. |
| templates/data-store-service.yaml.tmpl | Reusable YAML authoring template. |
| templates/decision-record.yaml.tmpl | Reusable YAML authoring template. |
| templates/deployment-target.yaml.tmpl | Reusable YAML authoring template. |
| templates/drafting-session.yaml.tmpl | Reusable YAML authoring template. |
| templates/github/drafting-table-receiver.yml.tmpl | DRAFT Framework 1.0 — Central Receiver GitHub Action |
| templates/github/product-repo-sync.yml.tmpl | DRAFT Framework 1.0 — Product Repo Sync GitHub Action |
| templates/host.yaml.tmpl | Reusable YAML authoring template. |
| templates/network-service.yaml.tmpl | Reusable YAML authoring template. |
| templates/object-patch.yaml.tmpl | Reusable YAML authoring template. |
| templates/product-registration.yaml.tmpl | Reusable YAML authoring template. |
| templates/reference-architecture.yaml.tmpl | Reusable YAML authoring template. |
| templates/relationship.yaml.tmpl | Reusable YAML authoring template. |
| templates/requirement-group.yaml.tmpl | Reusable YAML authoring template. |
| templates/runtime-service.yaml.tmpl | Reusable YAML authoring template. |
| templates/sdp-manifest.yaml.tmpl | Reusable YAML authoring template. |
| templates/software-deployment-pattern.yaml.tmpl | Reusable YAML authoring template. |
| templates/technology-component.yaml.tmpl | Reusable YAML authoring template. |
| templates/workspace/.cursor/rules/draftsman.mdc.tmpl | Reusable YAML authoring template. |
| templates/workspace/.draft/framework.lock.tmpl | Reusable YAML authoring template. |
| templates/workspace/.draft/workspace.yaml.tmpl | Reusable YAML authoring template. |
| templates/workspace/.github/CONTRIBUTING.md.tmpl | Contributing to Company DRAFT Workspace |
| templates/workspace/.github/copilot-instructions.md.tmpl | Copilot Instructions |
| templates/workspace/.github/workflows/draft-framework-update.yml.tmpl | Reusable YAML authoring template. |
| templates/workspace/.github/workflows/draft-vocabulary-proposals.yml.tmpl | DRAFT Vocabulary Proposal PRs |
| templates/workspace/.github/workflows/generate-browser.yml.tmpl | Reusable YAML authoring template. |
| templates/workspace/.gitignore.tmpl | Reusable YAML authoring template. |
| templates/workspace/.windsurfrules.tmpl | DRAFT Draftsman |
| templates/workspace/AGENTS.md.tmpl | AI Agent Instructions |
| templates/workspace/CLAUDE.md.tmpl | Claude Instructions |
| templates/workspace/CODEOWNERS.tmpl | DRAFT Workspace — CODEOWNERS |
| templates/workspace/GEMINI.md.tmpl | Gemini Instructions |
| templates/workspace/README.md.tmpl | Company DRAFT Workspace |
| templates/workspace/configurations/object-patches/capability-ownership-compute-runtime.yaml.tmpl | Capability Ownership — Compute & Runtime Domain |
| templates/workspace/configurations/object-patches/capability-ownership-data-engineering-quality.yaml.tmpl | Capability Ownership — Data & Engineering Quality Domains |
| templates/workspace/configurations/object-patches/capability-ownership-observability.yaml.tmpl | Capability Ownership — Observability & Monitoring Domain |
| templates/workspace/configurations/object-patches/capability-ownership-security-identity.yaml.tmpl | Capability Ownership — Security & Identity Domain |
| templates/workspace/llms.txt.tmpl | Company DRAFT Workspace |

## Validation

- Validate the example workspace: `python3 framework/tools/validate.py`
- Validate a company workspace: `python3 framework/tools/validate.py --workspace /path/to/workspace`
- Validate from inside a company repo: `python3 .draft/framework/tools/validate.py --workspace .`
- Regenerate browser after YAML changes: `python3 framework/tools/generate_browser.py`
- Regenerate this index after framework or YAML changes: `python3 framework/tools/generate_ai_index.py`
