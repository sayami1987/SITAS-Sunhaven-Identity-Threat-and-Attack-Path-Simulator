# SITAS Requirements

## Project

**Project Title:** Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  
**Unit:** COIT13236 Cyber Security Project

---

## 1. Purpose

This document defines the current functional and non-functional requirements for SITAS.

The requirements are based on the implemented Sunhaven threat-modelling prototype and are updated as the project develops. Detailed links between requirements, implementation files, tests and evidence are maintained separately in `requirements-traceability.md`.

---

## 2. Functional Requirements

| ID | Requirement | Current Status | Verification |
|---|---|---|---|
| FR-01 | The system shall load a fictional Sunhaven environment from a JSON file. | Completed | Model-loader tests |
| FR-02 | The system shall validate required environment data before processing. | Completed | Missing-node and missing-relationship tests |
| FR-03 | The system shall represent environment objects as graph nodes. | Completed | Graph creation tests |
| FR-04 | The system shall represent relationships between objects as directed graph edges. | Completed | Directed-relationship tests |
| FR-05 | The system shall allow the threat source/start node to be defined for each scenario. | Completed | Scenario JSON files |
| FR-06 | The system shall allow the protected target node to be defined for each scenario. | Completed | Scenario JSON files |
| FR-07 | The system shall search for an attack path between the configured start and target nodes. | Completed | BFS attack-path tests |
| FR-08 | The system shall use Breadth-First Search (BFS) for attack-path discovery. | Completed | `pathfinder.py` and BFS tests |
| FR-09 | The system shall prevent graph cycles from causing infinite processing. | Completed and tested | Graph-cycle test |
| FR-10 | The system shall calculate a risk score using likelihood and impact. | Completed | Risk-engine tests |
| FR-11 | The system shall classify risk as Low, Medium, High or Critical. | Completed | Severity-boundary tests |
| FR-12 | The system shall support simulated security controls. | Completed | Six controls implemented |
| FR-13 | The system shall determine whether a relevant simulated security control blocks an identified attack path. | Completed | Control-engine OFF/ON tests |
| FR-14 | The system shall compare attack exposure before and after a relevant security control is applied. | Partially completed | Manual OFF/ON comparison completed; automatic comparison mode is still planned |
| FR-15 | The system shall display understandable scenario, attack-path, risk and control results. | Completed | Manual scenario evidence |
| FR-16 | The system shall support multiple repeatable threat scenarios using the same analysis engine. | Completed | Six scenario files and shared `sitas.py` engine |
| FR-17 | The system shall load risk settings from a JSON configuration file. | Completed | Real risk-model loading test |
| FR-18 | The system shall validate likelihood and impact ratings before risk calculation. | Completed | Invalid likelihood, impact and non-integer tests |
| FR-19 | The system shall support automated testing of the main analysis components. | Completed | 45 passing pytest tests |
| FR-20 | The system shall export structured JSON result files. | Planned | Reporting tests to be added |
| FR-21 | The system shall generate a CSV summary of scenario results. | Planned | Reporting tests to be added |
| FR-22 | The system shall generate an understandable static HTML security report. | Planned | Reporting tests to be added |

---

## 3. Implemented Security Controls

SITAS currently simulates six security controls:

1. **CTRL-MFA – Multi-Factor Authentication**
2. **CTRL-SESSION – Session Timeout**
3. **CTRL-ACCOUNT – Account Disablement**
4. **CTRL-RBAC – Role-Based Access Control**
5. **CTRL-PRIVAUTH – Privileged Re-authentication**
6. **CTRL-DEVICE – Trusted Device Restriction**

These are simulated controls only. SITAS demonstrates their modelled effect on attack paths but does not configure or enforce them in a live Microsoft Entra environment.

---

## 4. Implemented Threat Scenarios

The current implementation contains six repeatable scenarios:

1. **SITAS-S01 – Stolen Nurse Credential**
2. **SITAS-S02 – Shared Workstation Session Misuse**
3. **SITAS-S03 – Former Worker Identity Misuse**
4. **SITAS-S04 – Excessive Privilege Abuse**
5. **SITAS-S05 – Privileged Administrator Credential Compromise**
6. **SITAS-S06 – Unmanaged Device Access**

Each scenario defines:

- scenario ID;
- scenario name;
- description;
- start node;
- target node;
- likelihood;
- impact;
- related security control.

The scenario files are stored under:

```text
scenarios/
```

---

## 5. Risk Requirements

SITAS uses a configurable 5 × 5 risk model.

```text
Risk Score = Likelihood × Impact
```

### Likelihood Scale

```text
1 = Rare
2 = Unlikely
3 = Possible
4 = Likely
5 = Almost Certain
```

### Impact Scale

```text
1 = Insignificant
2 = Minor
3 = Moderate
4 = Major
5 = Severe
```

### Severity Bands

```text
1–4   = Low
5–9   = Medium
10–16 = High
17–25 = Critical
```

The risk settings are stored in:

```text
config/risk-model.json
```

The risk model is used consistently across all implemented scenarios.

---

## 6. Non-Functional Requirements

| ID | Requirement | Current Status | Verification |
|---|---|---|---|
| NFR-01 | All scenario, identity, credential, session and resident data used by SITAS shall be fictional or synthetic. | Met | Current configuration and scenario design |
| NFR-02 | SITAS shall operate without requiring a live Microsoft Entra environment. | Met | Standalone Python/JSON architecture |
| NFR-03 | SITAS shall produce repeatable results when provided with the same input and configuration. | Met | Deterministic engines and automated tests |
| NFR-04 | Risk calculations shall be simple, transparent and explainable. | Met | Configurable 5 × 5 risk model |
| NFR-05 | Python source code shall be separated into understandable modules. | Met | Loader, graph, pathfinder, risk and control modules |
| NFR-06 | The current implementation shall handle invalid or missing JSON and invalid risk ratings without uncontrolled failure. | Met and tested | Model-loader and risk-validation tests |
| NFR-07 | The project shall not require real passwords, access tokens, API secrets or production credentials. | Met | Offline simulation design |
| NFR-08 | The implementation shall be understandable and demonstrable during the Bachelor of Information Technology capstone assessment. | Met for current design | Modular code, diagrams and evidence |
| NFR-09 | SITAS shall remain technically separate from other team members' operational IAM runtime components. | Met | Standalone project boundary |
| NFR-10 | Testing and demonstration evidence shall be retained for assessment verification. | Met and ongoing | `evidence/` folder and pytest screenshots |
| NFR-11 | The same core analysis engine shall be reusable across multiple scenarios. | Met | Six scenarios use the same modules and `sitas.py` |
| NFR-12 | SITAS shall remain safe for offline demonstration and shall not perform real cyberattacks. | Met | Synthetic local simulation |
| NFR-13 | Project documentation shall clearly distinguish simulated control behaviour from real-world operational enforcement. | Met and ongoing | README, policies and project documentation |

---

## 7. Individual Contribution Boundary

SITAS is the threat-modelling and attack-path simulation component within the wider Sunhaven Care Workforce IAM project.

SITAS focuses on:

- threat modelling;
- directed attack-graph construction;
- BFS attack-path discovery;
- risk scoring;
- security-control simulation;
- automated testing;
- security reporting.

SITAS does **not**:

- create, update or delete Microsoft Entra users;
- perform Joiner-Mover-Leaver automation;
- conduct manager access reviews;
- run live workforce compliance checks;
- monitor production security events;
- automatically remediate or remove access;
- enforce real device compliance;
- perform real cyberattacks;
- use real employee or resident information.

Its role is to model identity threats, discover attack paths, assess risk and demonstrate the expected effect of simulated security controls.

---

## 8. Current Requirement Status

The core attack-path simulator is substantially implemented.

### Completed Core Areas

```text
JSON environment loading
Environment validation
Directed graph construction
BFS attack-path discovery
Risk calculation and severity classification
Six threat scenarios
Six security-control simulations
Scenario-based command-line execution
Automated testing
45 passing tests
```

### Remaining Requirements

```text
FR-14  Automatic before/after control comparison
FR-20  JSON result export
FR-21  CSV scenario summary
FR-22  Static HTML security report
```

These remaining requirements are planned for the next development stage.

---

## 9. Verification Approach

Requirements are verified using a combination of:

- automated pytest tests;
- manual scenario execution;
- before/after security-control screenshots;
- architecture and design artefacts;
- configuration files;
- project documentation.

A separate requirements traceability matrix maps each requirement to its implementation, test case and supporting evidence.
