# SITAS Requirements Traceability Matrix

## Project

**Project Title:** Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  
**Unit:** COIT13236 Cyber Security Project

---

## 1. Purpose

This document links SITAS requirements to their implementation, verification method and supporting evidence.

The purpose of the matrix is to show that project requirements are not only documented but can be traced to working code, configuration, tests and evidence.

The traceability flow is:

```text
Requirement
→ Implementation
→ Verification
→ Evidence
→ Status
```

---

## 2. Functional Requirements Traceability

| Requirement | Main Implementation | Verification | Supporting Evidence | Status |
|---|---|---|---|---|
| SITAS-FR-01 Load fictional environment from JSON | `src/model_loader.py`, `config/environment.json` | `test_valid_environment_loads`, `test_real_environment_file_loads` | `evidence/22-pytest-model-loader.png` | PASS |
| SITAS-FR-02 Validate required environment data | `src/model_loader.py` | `test_environment_missing_nodes_is_rejected`, `test_environment_missing_relationships_is_rejected` | `evidence/22-pytest-model-loader.png` | PASS |
| SITAS-FR-03 Represent environment objects as graph nodes | `src/graph_engine.py` | `test_graph_creates_all_nodes` | `evidence/20-pytest-graph-bfs.png` | PASS |
| SITAS-FR-04 Represent relationships as directed graph edges | `src/graph_engine.py` | `test_graph_creates_directed_relationships` | `evidence/20-pytest-graph-bfs.png` | PASS |
| SITAS-FR-05 Define a threat source/start node per scenario | `scenarios/*.json`, `src/sitas.py` | Six scenario files load successfully | `evidence/22-pytest-model-loader.png` | PASS |
| SITAS-FR-06 Define a protected target per scenario | `scenarios/*.json`, `src/sitas.py` | Six scenario files load successfully | `evidence/22-pytest-model-loader.png` | PASS |
| SITAS-FR-07 Search for an attack path | `src/pathfinder.py` | `test_bfs_finds_attack_path` | `evidence/20-pytest-graph-bfs.png` | PASS |
| SITAS-FR-08 Use BFS for path discovery | `src/pathfinder.py` | BFS path and shortest-path tests | `evidence/20-pytest-graph-bfs.png` | PASS |
| SITAS-FR-09 Prevent cycles causing infinite processing | `src/pathfinder.py` visited-node logic | `test_bfs_handles_graph_cycle` | `evidence/20-pytest-graph-bfs.png` | PASS |
| SITAS-FR-10 Calculate likelihood × impact risk | `src/risk_engine.py` | Scenario risk tests | `evidence/19-pytest-risk-engine.png` | PASS |
| SITAS-FR-11 Classify Low, Medium, High or Critical severity | `src/risk_engine.py`, `config/risk-model.json` | Risk severity boundary tests | `evidence/19-pytest-risk-engine.png` | PASS |
| SITAS-FR-12 Support simulated security controls | `src/control_engine.py`, `config/controls.json` | Control-engine test suite | `evidence/21-pytest-control-engine.png` | PASS |
| SITAS-FR-13 Determine whether control blocks attack path | `src/control_engine.py`, `src/sitas.py` | Six enabled/disabled control pairs | `evidence/21-pytest-control-engine.png`, evidence 07–18 | PASS |
| SITAS-FR-14 Compare attack exposure before and after controls | Current manual OFF/ON workflow | Manual execution of each scenario with control OFF and ON | `evidence/07-...` through `evidence/18-...` | PARTIAL |
| SITAS-FR-15 Display understandable attack-path results | `src/sitas.py`, node names from `src/graph_engine.py` | Manual scenario execution | Scenario evidence 07–18 | PASS |
| SITAS-FR-16 Support multiple scenarios through the same engine | `src/sitas.py`, `scenarios/*.json` | `test_all_six_scenario_files_load` plus manual runs | `evidence/22-pytest-model-loader.png`, scenario evidence | PASS |
| SITAS-FR-17 Load risk settings from JSON | `config/risk-model.json`, `src/model_loader.py` | `test_real_risk_model_loads` | `evidence/22-pytest-model-loader.png` | PASS |
| SITAS-FR-18 Validate likelihood and impact values | `src/risk_engine.py` | invalid likelihood, invalid impact and non-integer tests | `evidence/19-pytest-risk-engine.png` | PASS |
| SITAS-FR-19 Support automated testing | `tests/`, `pytest.ini` | Full pytest execution | `evidence/23-pytest-full-suite-45-passed.png` | PASS |
| SITAS-FR-20 Export structured JSON results | Not yet implemented | Future reporting tests | — | PLANNED |
| SITAS-FR-21 Generate CSV scenario summary | Not yet implemented | Future reporting tests | — | PLANNED |
| SITAS-FR-22 Generate static HTML security report | Not yet implemented | Future reporting tests | — | PLANNED |

---

## 3. Non-Functional Requirements Traceability

| Requirement | Implementation / Design Evidence | Verification | Status |
|---|---|---|---|
| SITAS-NFR-01 Fictional/synthetic data only | `config/environment.json`, scenario files, fictional resident target | Documentation and configuration review | PASS |
| SITAS-NFR-02 No live Microsoft Entra dependency | Standalone Python and JSON architecture | Source/design review | PASS |
| SITAS-NFR-03 Repeatable results for same input | Deterministic graph, BFS, risk and control logic | Automated test suite | PASS |
| SITAS-NFR-04 Explainable risk calculations | `risk-model.json`, `risk_engine.py` | Risk tests and documentation | PASS |
| SITAS-NFR-05 Modular Python source | Separate loader, graph, pathfinder, risk and control modules | Architecture/source review | PASS |
| SITAS-NFR-06 Safe handling of current invalid JSON/risk input | `model_loader.py`, `risk_engine.py` | Model-loader and invalid-risk tests | PASS |
| SITAS-NFR-07 No real passwords/tokens/secrets required | Offline synthetic design | Project/source review | PASS |
| SITAS-NFR-08 Understandable for capstone demonstration | Modular output, diagrams, README and evidence | Demonstration preparation / mentor demo | ONGOING |
| SITAS-NFR-09 Independent from other team runtime components | Standalone SITAS repository and offline model | Architecture/design review | PASS |
| SITAS-NFR-10 Retain testing evidence | `evidence/`, test files, screenshots | Evidence review | PASS / ONGOING |
| SITAS-NFR-11 Reuse same engine across scenarios | Shared `sitas.py` and modules | Six scenario executions | PASS |
| SITAS-NFR-12 Safe offline demonstration | No real attack or production dependency | Design/source review | PASS |
| SITAS-NFR-13 Distinguish simulation from real enforcement | README, policies, requirements and risk-analysis wording | Documentation review | PASS / ONGOING |

---

## 4. Scenario-to-Control Traceability

| Scenario | Security Problem | Related Control | Manual Evidence | Automated Verification |
|---|---|---|---|---|
| SITAS-S01 | Stolen nurse credential | CTRL-MFA | 07 / 08 | MFA OFF/ON control tests |
| SITAS-S02 | Shared active session | CTRL-SESSION | 09 / 10 | Session OFF/ON control tests |
| SITAS-S03 | Former-worker identity | CTRL-ACCOUNT | 11 / 12 | Account OFF/ON control tests |
| SITAS-S04 | Excessive privilege | CTRL-RBAC | 13 / 14 | RBAC OFF/ON control tests |
| SITAS-S05 | Privileged admin compromise | CTRL-PRIVAUTH | 15 / 16 | Privileged re-auth OFF/ON tests |
| SITAS-S06 | Unmanaged-device access | CTRL-DEVICE | 17 / 18 | Device OFF/ON tests and Scenario 6 BFS regression test |

---

## 5. Current Coverage Summary

### Fully Implemented and Verified

```text
SITAS-FR-01 to SITAS-FR-13
SITAS-FR-15 to SITAS-FR-19
Most current NFRs
```

### Partially Implemented

```text
SITAS-FR-14 – before/after comparison
```

Manual comparison is complete for all six scenarios, but automatic comparison remains to be implemented.

### Planned

```text
SITAS-FR-20 – JSON result export
SITAS-FR-21 – CSV scenario summary
SITAS-FR-22 – HTML security report
```

---

## 6. Traceability Maintenance

This matrix should be updated whenever:

- a requirement is added or changed;
- a new feature is implemented;
- a new automated test is added;
- evidence filenames change;
- reporting features are completed.

When automatic comparison and reporting are implemented, SITAS-FR-14 and SITAS-FR-20 to SITAS-FR-22 should be updated from PARTIAL/PLANNED to PASS only after the related tests and evidence have been completed.
