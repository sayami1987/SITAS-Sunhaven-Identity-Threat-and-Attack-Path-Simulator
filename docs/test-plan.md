# SITAS Test Plan

## Project

**Project Title:** Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  
**Unit:** COIT13236 Cyber Security Project

---

## 1. Purpose

The purpose of this test plan is to confirm that SITAS correctly:

- loads the fictional Sunhaven environment;
- validates configuration data;
- builds the directed attack graph;
- discovers attack paths using Breadth-First Search (BFS);
- handles unreachable targets and graph cycles;
- calculates and classifies risk;
- applies simulated security controls;
- loads all six threat scenarios;
- produces repeatable results.

Automated testing is implemented using `pytest`.

Testing is supported by manual scenario evidence showing the effect of controls in both disabled and enabled states.

---

## 2. Test Scope

### In Scope

The current test suite covers:

- model and JSON loading;
- environment validation;
- graph construction;
- directed relationships;
- node-name mapping;
- BFS attack-path discovery;
- shortest-path behaviour;
- unreachable targets;
- graph-cycle handling;
- risk calculation;
- risk severity boundaries;
- invalid risk input;
- six security-control simulations;
- unknown-control handling;
- all six scenario files;
- repeatability of the current simulator components.

### Not Yet in Scope

The following planned features are not yet implemented and therefore are not yet part of the current automated suite:

- automatic `--compare` mode;
- JSON result export;
- CSV summary generation;
- HTML report generation.

Tests for these features will be added when the features are implemented.

---

## 3. Test Environment

The current automated test environment uses:

```text
Python 3.13.7
pytest 9.1.1
pluggy 1.6.0
Windows
```

Tests are run from the project root using:

```powershell
python -m pytest -v
```

The project uses:

```text
pytest.ini
```

to identify the `src` directory and the `tests` directory.

---

## 4. Current Automated Test Summary

| Test Area | Number of Passing Tests |
|---|---:|
| Risk Engine | 14 |
| Graph and BFS | 9 |
| Control Engine | 13 |
| Model Loader and Configuration | 9 |
| **Total** | **45** |

Current verified result:

```text
45 passed
```

---

## 5. Risk Engine Tests

The risk-engine tests confirm:

- Scenario 1 risk calculation;
- Scenario 2 risk calculation;
- Scenario 3 risk calculation;
- Low severity lower boundary;
- Low severity upper boundary;
- Medium severity lower boundary;
- Medium severity upper boundary;
- High severity lower boundary;
- High severity upper boundary;
- Critical severity lower boundary;
- Critical severity upper boundary;
- invalid likelihood is rejected;
- invalid impact is rejected;
- non-integer rating is rejected.

Expected calculation:

```text
Risk Score = Likelihood × Impact
```

Severity bands:

```text
1–4   = Low
5–9   = Medium
10–16 = High
17–25 = Critical
```

Evidence:

```text
evidence/19-pytest-risk-engine.png
```

---

## 6. Graph and BFS Tests

The graph and pathfinder tests confirm:

- all expected graph nodes are created;
- directed relationships are created correctly;
- node IDs map to readable names;
- BFS finds a reachable attack path;
- BFS returns the shortest reachable path;
- BFS returns `None` when no path exists;
- graph cycles do not cause endless processing;
- start equal to target is handled correctly;
- the real Scenario 6 unmanaged-device path is correct.

### Scenario 6 Regression Check

An earlier Scenario 6 model reused the same care-worker identity node as another scenario. This caused BFS to select a different valid shortest route.

The graph model was corrected by introducing a separate:

```text
Remote Care Worker Identity
```

A dedicated automated test now verifies the intended Scenario 6 path so the problem can be detected if the graph is changed later.

Evidence:

```text
evidence/20-pytest-graph-bfs.png
```

---

## 7. Control Engine Tests

The control-engine tests confirm the enabled and disabled behaviour of all six controls.

| Control | Disabled | Enabled |
|---|---|---|
| Multi-Factor Authentication | OPEN | BLOCKED |
| Session Timeout | OPEN | BLOCKED |
| Account Disablement | OPEN | BLOCKED |
| Role-Based Access Control | OPEN | BLOCKED |
| Privileged Re-authentication | OPEN | BLOCKED |
| Trusted Device Restriction | OPEN | BLOCKED |

An additional test confirms that an unknown control does not incorrectly block an attack path.

Evidence:

```text
evidence/21-pytest-control-engine.png
```

---

## 8. Model Loader and Configuration Tests

These tests confirm:

- valid environment JSON loads successfully;
- an environment missing `nodes` is rejected;
- an environment missing `relationships` is rejected;
- invalid JSON is rejected;
- a missing JSON file is handled;
- the real `environment.json` loads;
- the real `controls.json` loads;
- the real `risk-model.json` loads;
- all six scenario JSON files load successfully.

Evidence:

```text
evidence/22-pytest-model-loader.png
```

---

## 9. Full Test Suite

The complete project test suite is run with:

```powershell
python -m pytest -v
```

Current verified result:

```text
45 passed
```

Evidence:

```text
evidence/23-pytest-full-suite-45-passed.png
```

This confirms that the current automated test categories pass together in the current SITAS implementation.

---

## 10. Manual Scenario Verification

Automated testing is supported by manual before/after evidence.

### Scenario 1 – Multi-Factor Authentication

```text
MFA OFF → OPEN
MFA ON  → BLOCKED
```

Evidence:

```text
evidence/07-scenario-01-mfa-off-open.png
evidence/08-scenario-01-mfa-on-blocked.png
```

### Scenario 2 – Session Timeout

```text
Session Timeout OFF → OPEN
Session Timeout ON  → BLOCKED
```

Evidence:

```text
evidence/09-scenario-02-session-off-open.png
evidence/10-scenario-02-session-on-blocked.png
```

### Scenario 3 – Account Disablement

```text
Account Disablement OFF → OPEN
Account Disablement ON  → BLOCKED
```

Evidence:

```text
evidence/11-scenario-03-account-off-open.png
evidence/12-scenario-03-account-on-blocked.png
```

### Scenario 4 – Role-Based Access Control

```text
RBAC OFF → OPEN
RBAC ON  → BLOCKED
```

Evidence:

```text
evidence/13-scenario-04-rbac-off-open.png
evidence/14-scenario-04-rbac-on-blocked.png
```

### Scenario 5 – Privileged Re-authentication

```text
Privileged Re-authentication OFF → OPEN
Privileged Re-authentication ON  → BLOCKED
```

Evidence:

```text
evidence/15-scenario-05-privauth-off-open.png
evidence/16-scenario-05-privauth-on-blocked.png
```

### Scenario 6 – Trusted Device Restriction

```text
Trusted Device Restriction OFF → OPEN
Trusted Device Restriction ON  → BLOCKED
```

Evidence:

```text
evidence/17-scenario-06-device-off-open.png
evidence/18-scenario-06-device-on-blocked.png
```

---

## 11. Test Acceptance Criteria

The current simulator test stage is considered successful when:

- all automated tests complete without failure;
- valid configuration files load correctly;
- invalid or incomplete configuration is handled safely;
- BFS produces the expected route for known scenarios;
- graph cycles do not cause infinite processing;
- risk calculations match the configured 5 × 5 model;
- each implemented control behaves as expected in enabled and disabled states;
- all six scenario files are loadable;
- manual OPEN/BLOCKED evidence matches the implemented control logic.

The current implementation satisfies these criteria with:

```text
45 passed
```

---

## 12. Requirements Traceability

Detailed requirement-to-test mapping is maintained in:

```text
docs/requirements-traceability.md
```

That document links each requirement to:

```text
Requirement
→ Implementation
→ Test
→ Evidence
→ Status
```

This test plan therefore focuses on testing strategy and results rather than duplicating the full traceability matrix.

---

## 13. Remaining Testing Work

Additional tests will be added for:

- automatic before/after comparison;
- JSON result export;
- CSV scenario summary;
- HTML report generation.

After those features are implemented, the full suite will be rerun and the total test count will be updated.

---

## 14. Test Evidence Retention

Testing evidence is retained through:

- terminal output;
- screenshots;
- pytest source files;
- project configuration;
- Git commits and repository history;
- generated results and reports.

This evidence supports verification of individual technical contribution and allows the current simulator behaviour to be repeated and checked.
