# SITAS Development Progress Log 

## Project

**Project Title:** Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  
**Unit:** COIT13236 Cyber Security Project  
**Project Context:** Sunhaven Care Workforce IAM  
**Development Stage:** Working prototype with two implemented scenarios  
**Document status:** Verified against the current project files and evidence ZIP

\---

## 1\. Purpose of This Document

This document records the actual SITAS work completed so far and separates completed work from planned work.

The information below was checked against the current `sunhaven-sitas-threat-simulator` project files, source code, scenario files, screenshots and Git repository state.

The project is being developed as a standalone individual technical contribution. It models fictional identity-related attack paths and simulated security controls without performing operational Microsoft Entra administration, Joiner-Mover-Leaver automation, manager access reviews, workforce compliance checking, security-event monitoring or access remediation.

\---

## 2\. Current Project Structure

The current project contains the following main areas:

```text
sunhaven-sitas-threat-simulator/
├── config/
│   ├── controls.json
│   ├── environment.json
│   └── risk-model.json
├── docs/
│   ├── diagrams/
│   │   └── architecture-diagram.png
│   ├── project-plan.md
│   ├── requirements.md
│   └── test-plan.md
├── evidence/
│   ├── 07-scenario-01-mfa-off-open.png
│   ├── 08-scenario-01-mfa-on-blocked.png
│   ├── 09-scenario-02-session-off-open.png
│   ├── 10-scenario-02-session-on-blocked.png
│   ├── evidence-after-mfa.png
│   ├── evidence-first-attack-path.png
│   ├── evidence-risk-before-mfa.png
│   └── first\_VS Code\_structure.png
├── reports/
├── scenarios/
│   ├── scenario-01-stolen-nurse-credential.json
│   └── scenario-02-shared-session.json
├── src/
│   ├── control\_engine.py
│   ├── graph\_engine.py
│   ├── model\_loader.py
│   ├── pathfinder.py
│   ├── risk\_engine.py
│   └── sitas.py
├── tests/
├── .gitignore
├── README.md
└── First progress.txt
```

The `reports/` and `tests/` folders currently exist but do not yet contain the planned reporting or automated test implementation.

\---

## 3\. Planning and Documentation Completed

The following planning documents currently exist:

* `docs/project-plan.md`
* `docs/requirements.md`
* `docs/test-plan.md`

### 3.1 Project Plan

The project plan currently documents:

* the fictional Sunhaven Care context;
* the identity-related security problem;
* the proposed standalone Python simulator;
* the main project objective;
* specific objectives;
* individual contribution boundary;
* in-scope and out-of-scope work;
* planned technologies.

### 3.2 Requirements

The requirements document currently defines functional requirements for:

* loading fictional JSON environment data;
* validating required environment sections;
* representing objects as graph nodes;
* representing relationships as directed graph edges;
* choosing start and target nodes;
* discovering attack paths;
* using Breadth-First Search;
* avoiding endless graph processing;
* calculating risk;
* classifying severity;
* supporting simulated controls;
* comparing security exposure;
* displaying understandable results.

The document also defines non-functional requirements covering synthetic data, offline use, repeatable results, explainability, modular code, safe input handling, secret protection, understandable implementation and independence from other team members' runtime systems.

### 3.3 Test Plan

The test plan currently contains 15 planned test cases.

These tests are documented but **have not yet been implemented as an automated pytest suite**.

The `tests/` folder is currently empty.

\---

## 4\. Architecture Design

A PNG architecture diagram currently exists at:

```text
docs/diagrams/architecture-diagram.png
```

The diagram shows the following flow:

```text
Fictional Sunhaven Environment
        ↓
JSON Configuration
        ↓
Model Loader
        ↓
Attack Graph
        ↓
BFS Pathfinder
        ↓
Risk Calculator
        ↓
Security Control Simulation
        ↓
Before / After Comparison
        ↓
Security Findings
```

This accurately represents the intended SITAS processing flow.

### Current Diagram Limitation

The current ZIP contains the PNG architecture image, but it does **not** contain an editable `.drawio` source file.

An editable Draw.io version should therefore be added later if required for final design evidence.

\---

## 5\. Configuration Files

### 5.1 `config/environment.json`

This file currently contains the fictional nodes and directed relationships required for Scenario 1 and Scenario 2.

Current fictional nodes include:

* External Attacker;
* Stolen Nurse Password;
* Nurse Identity;
* Shared Nurse Workstation;
* Unauthorised Person;
* Unattended Shared Workstation;
* Active Nurse Session;
* Sunhaven Care Portal;
* Fictional Resident Records.

The environment currently supports the following two paths.

### Scenario 1 path

```text
External Attacker
→ Stolen Nurse Password
→ Nurse Identity
→ Shared Nurse Workstation
→ Sunhaven Care Portal
→ Fictional Resident Records
```

### Scenario 2 path

```text
Unauthorised Person
→ Unattended Shared Workstation
→ Active Nurse Session
→ Sunhaven Care Portal
→ Fictional Resident Records
```

### 5.2 `config/controls.json`

The current control file contains:

* `CTRL-MFA` – Multi-Factor Authentication;
* `CTRL-RBAC` – Role-Based Access Control;
* `CTRL-SESSION` – Session Timeout.

In the current uploaded project state:

```text
CTRL-MFA     = false
CTRL-RBAC    = false
CTRL-SESSION = true
```

This current state reflects the final Scenario 2 blocked test. The values can be changed between `true` and `false` to demonstrate different simulated security states.

### 5.3 `config/risk-model.json`

The file currently exists but is **empty**.

The current working program does **not** load risk settings from `risk-model.json`.

Risk calculation and severity classification are currently implemented directly in:

```text
src/risk\_engine.py
```

Therefore, `risk-model.json` should be treated as a planned configuration file rather than a completed risk configuration.

\---

## 6\. Python Modules Implemented

### 6.1 `src/model\_loader.py`

This module is implemented and currently provides:

* `load\_environment(file\_path)`
* `load\_json\_file(file\_path)`

`load\_environment()` checks that the environment contains both:

* `nodes`
* `relationships`

It also handles:

* file-not-found errors;
* invalid JSON errors;
* missing required environment sections.

`load\_json\_file()` is used for general JSON files such as controls and scenario definitions.

### 6.2 `src/graph\_engine.py`

This module currently provides:

* `build\_graph(environment)`
* `get\_node\_names(environment)`

`build\_graph()` converts the JSON relationships into a simple directed adjacency-list graph.

`get\_node\_names()` maps internal node IDs to readable names for terminal output.

### 6.3 `src/pathfinder.py`

This module implements:

```text
find\_path\_bfs(graph, start, target)
```

The function uses Breadth-First Search with a queue.

A `visited` set prevents the same node from being repeatedly expanded, reducing the risk of endless processing when graph cycles exist.

The current function returns the first path it finds between the selected start and target nodes.

### 6.4 `src/risk\_engine.py`

This module currently implements:

```python
calculate\_risk(likelihood, impact)
classify\_risk(score)
```

The risk calculation is:

```text
Risk Score = Likelihood × Impact
```

The current severity logic is:

```text
1–4   = Low
5–9   = Medium
10–16 = High
17+   = Critical
```

The two implemented scenarios currently use likelihood and impact values on a 1–5 scale.

The code currently does not validate that input values remain within 1–5. Input validation can be added later.

### 6.5 `src/control\_engine.py`

The current control engine implements:

* `get\_control\_enabled()`
* `check\_mfa\_control()`
* `check\_session\_timeout\_control()`
* `assess\_control()`

Two controls currently have working simulation rules:

```text
CTRL-MFA
CTRL-SESSION
```

`CTRL-RBAC` exists in `controls.json`, but its simulation rule has **not yet been implemented**.

### 6.6 `src/sitas.py`

The main program currently:

1. loads the fictional environment;
2. loads the current controls;
3. loads a scenario JSON file;
4. displays the scenario;
5. builds the attack graph;
6. runs BFS;
7. displays the discovered path;
8. calculates risk;
9. classifies severity;
10. assesses the scenario's related control;
11. displays OPEN or BLOCKED status.

Scenario 1 runs by default:

```powershell
python src/sitas.py
```

Scenario 2 can be selected using:

```powershell
python src/sitas.py scenarios/scenario-02-shared-session.json
```

\---

## 7\. Scenario 1 – Stolen Nurse Credential

Scenario file:

```text
scenarios/scenario-01-stolen-nurse-credential.json
```

### Scenario Definition

```text
Scenario ID:   SITAS-S01
Scenario Name: Stolen Nurse Credential
Start Node:    external\_attacker
Target Node:   resident\_records
Likelihood:    4
Impact:        5
Control:       CTRL-MFA
```

### Discovered Attack Path

```text
External Attacker
↓
Stolen Nurse Password
↓
Nurse Identity
↓
Shared Nurse Workstation
↓
Sunhaven Care Portal
↓
Fictional Resident Records
```

### Risk Result

```text
Likelihood: 4/5
Impact:     5/5
Risk Score: 20/25
Severity:   Critical
```

### MFA Disabled Result

A genuine earlier screenshot exists showing the MFA-disabled path as OPEN:

```text
evidence/evidence-risk-before-mfa.png
```

Observed result:

```text
Attack Path Status: OPEN
Reason: MFA does not block this path.
```

### MFA Enabled Result

The current evidence includes a successful MFA-enabled blocked result:

```text
evidence/08-scenario-01-mfa-on-blocked.png
```

Observed result:

```text
Control: CTRL-MFA
Status: BLOCKED
Reason: MFA blocks password-only authentication.

Final Attack Path Status: BLOCKED
```

### Evidence Naming Issue Found

The file:

```text
evidence/07-scenario-01-mfa-off-open.png
```

is incorrectly named.

Its actual screenshot content shows an MFA **BLOCKED** result rather than an OPEN result.

It should not be used as evidence of the MFA-off state unless it is replaced with a correct screenshot.

For accurate documentation, use:

```text
evidence/evidence-risk-before-mfa.png
```

for the existing MFA OFF / OPEN evidence, and:

```text
evidence/08-scenario-01-mfa-on-blocked.png
```

for MFA ON / BLOCKED evidence.

\---

## 8\. Scenario 2 – Shared Workstation Session Misuse

Scenario file:

```text
scenarios/scenario-02-shared-session.json
```

### Scenario Definition

```text
Scenario ID:   SITAS-S02
Scenario Name: Shared Workstation Session Misuse
Start Node:    unauthorised\_person
Target Node:   resident\_records
Likelihood:    3
Impact:        5
Control:       CTRL-SESSION
```

### Discovered Attack Path

```text
Unauthorised Person
↓
Unattended Shared Workstation
↓
Active Nurse Session
↓
Sunhaven Care Portal
↓
Fictional Resident Records
```

### Risk Result

```text
Likelihood: 3/5
Impact:     5/5
Risk Score: 15/25
Severity:   High
```

### Session Timeout Disabled Result

Evidence:

```text
evidence/09-scenario-02-session-off-open.png
```

Observed result:

```text
Control: CTRL-SESSION
Status: OPEN
Reason: Session timeout does not block this path.

Final Attack Path Status: OPEN
```

### Session Timeout Enabled Result

Evidence:

```text
evidence/10-scenario-02-session-on-blocked.png
```

Observed result:

```text
Control: CTRL-SESSION
Status: BLOCKED
Reason: Session timeout prevents reuse of the stale active session.

Final Attack Path Status: BLOCKED
```

Both Scenario 2 screenshots match their filenames and expected results.

\---

## 9\. Manual Verification of Current Program State

The current project was checked by executing both scenarios using the uploaded files.

### Current Scenario 1 result

With the current `controls.json` state:

```text
CTRL-MFA = false
```

Scenario 1 currently returns:

```text
Control: CTRL-MFA
Status: OPEN
Final Attack Path Status: OPEN
```

### Current Scenario 2 result

With the current `controls.json` state:

```text
CTRL-SESSION = true
```

Scenario 2 currently returns:

```text
Control: CTRL-SESSION
Status: BLOCKED
Final Attack Path Status: BLOCKED
```

These results are consistent with the current source code and current controls configuration.

\---

## 10\. Development Problem Encountered

A Python import error occurred during development:

```text
ImportError: cannot import name 'assess\_control' from 'control\_engine'
```

### Cause

The updated `sitas.py` expected:

```python
from control\_engine import assess\_control
```

but the local `control\_engine.py` still contained an earlier version that did not include `assess\_control()`.

### Resolution

`control\_engine.py` was updated to include the new `assess\_control()` function and saved.

After the files were synchronised, Scenario 1 executed successfully and displayed:

```text
Control: CTRL-MFA
Status: BLOCKED
Final Attack Path Status: BLOCKED
```

This was a genuine development issue and is useful reflection evidence because it shows a dependency problem between Python modules and the process used to correct it.

\---

## 11\. Git Repository Status

The uploaded project contains a Git repository.

The current Git history contains two commits:

```text
9a35470 Add initial SITAS threat simulator implementation
13ec6bb Initial commit
```

However, the most recent scenario, documentation, evidence and source-code changes in the uploaded project are currently **not committed**.

The working tree contains modified and untracked files.

Therefore, the current documentation should not claim that Scenario 1 and Scenario 2 work have already been committed to GitHub.

A new meaningful commit should be made after the current files are reviewed and cleaned.

\---

## 12\. README Status

`README.md` currently exists, but it is still minimal.

It currently contains the SITAS title and a short sentence describing the simulator.

A more complete README is still planned and should later include:

* project purpose;
* features;
* setup;
* commands;
* scenario examples;
* controls;
* architecture;
* testing;
* output/report information;
* limitations;
* synthetic-data statement.

The README should therefore be described as **started**, not complete.

\---

## 13\. Current Evidence Status

The current project contains genuine screenshots for:

* initial VS Code/project structure;
* first working attack path;
* risk result before MFA;
* MFA blocked output;
* Scenario 2 Session Timeout OFF / OPEN;
* Scenario 2 Session Timeout ON / BLOCKED.

The following evidence issue should be corrected:

```text
07-scenario-01-mfa-off-open.png
```

does not match its filename because the screenshot actually shows a BLOCKED MFA result.

Recommended action:

* keep `evidence-risk-before-mfa.png` as the current Scenario 1 OFF/OPEN evidence; or
* capture a new Scenario 1 OFF/OPEN screenshot and give it the intended `07-scenario-01-mfa-off-open.png` filename.

\---

## 14\. Current Progress Summary

|Area|Verified Status|
|-|-|
|Project folder structure|Completed|
|Project plan|Completed initial version|
|Requirements|Completed initial version|
|Test plan|Completed as planned tests|
|Architecture PNG|Completed|
|Editable Draw.io source|Not present in current ZIP|
|Environment JSON|Working for Scenarios 1 and 2|
|Controls JSON|Working|
|Risk model JSON|File exists but currently empty|
|Graph engine|Working|
|BFS pathfinder|Working|
|Risk engine|Working|
|Scenario 1 JSON|Working|
|MFA simulation|Working|
|Scenario 1 OFF evidence|Exists under `evidence-risk-before-mfa.png`|
|Scenario 1 ON evidence|Working and correctly captured|
|Scenario 2 JSON|Working|
|Session Timeout simulation|Working|
|Scenario 2 OFF evidence|Correct|
|Scenario 2 ON evidence|Correct|
|RBAC simulation|Not implemented|
|Account Disablement|Not implemented|
|Scenario 3|Not implemented|
|Automated pytest tests|Not implemented|
|JSON result export|Not implemented|
|CSV result export|Not implemented|
|HTML report|Not implemented|
|Complete README|Not completed|
|Current work committed to Git|Not yet|
|Final documentation|In progress|

\---

## 15\. Work From This Point

Development will continue from the current working two-scenario prototype.

### A. Correct Current Evidence and Configuration

Before adding new functionality:

* correct or replace the incorrectly named Scenario 1 OFF screenshot;
* decide on a normal default state for `controls.json`;
* populate or remove the currently empty `risk-model.json`;
* add the editable Draw.io source if available;
* update the README;
* commit the verified Scenario 1 and Scenario 2 work.

### B. Scenario 3 – Former Worker Identity Misuse

Add a fictional path such as:

```text
Former Worker
↓
Former Worker Identity
↓
Sunhaven Care Portal
↓
Fictional Resident Records
```

Add a simulated Account Disablement control and compare:

```text
Control OFF → OPEN
Control ON  → BLOCKED
```

### C. RBAC Scenario

Add a separate scenario that demonstrates excessive or inappropriate privilege and simulate RBAC as the control.

### D. Additional Scenarios

Add further independent threat scenarios such as:

* agency credential compromise;
* privileged administrator compromise;
* additional credential/session misuse scenarios where useful.

### E. Automated Testing

Implement pytest tests for:

* environment loading;
* invalid JSON;
* graph nodes and relationships;
* BFS path discovery;
* unreachable targets;
* graph cycles;
* risk calculations;
* severity classification;
* MFA;
* Session Timeout;
* Account Disablement;
* RBAC;
* scenario execution.

### F. Reporting

Add:

```text
JSON output
CSV output
HTML threat assessment report
```

The HTML report should be a generated assessment report, not a security-monitoring dashboard.

### G. Documentation and Evidence

Continue with:

* additional Draw.io diagrams;
* screenshots;
* requirements/test traceability;
* Git commits;
* test logs;
* technical documentation;
* demonstration preparation.

\---

## 16\. Reflection on Work Completed

The project has moved from planning into a working technical prototype.

The current implementation demonstrates how JSON configuration, modular Python files, a directed graph and Breadth-First Search can be combined to model identity-related cybersecurity attack paths.

Scenario 1 demonstrates a password-based attack path and a simulated MFA control. Scenario 2 demonstrates misuse of an active session on an unattended shared workstation and a simulated Session Timeout control.

The risk engine provides a simple and explainable likelihood × impact calculation. This is suitable for the current prototype because it allows risk results to be demonstrated clearly without introducing unnecessary mathematical complexity.

A practical issue occurred when `sitas.py` was updated before `control\_engine.py`, resulting in an import error for `assess\_control`. Updating and saving the dependent module resolved the problem. This provided useful experience with Python module dependencies and debugging.

The current implementation is still an early-to-intermediate prototype rather than a finished capstone system. The main remaining technical work is to add more scenarios and controls, automate testing, generate reports and improve final documentation and evidence.

\---

## 17\. Verified Current Status

The verified project currently has:

```text
2 working attack scenarios
2 working simulated security controls
1 directed graph environment
1 BFS pathfinder
1 risk-scoring engine
scenario selection through the command line
manual before/after evidence for MFA and Session Timeout
initial planning, requirements and test documentation
an architecture PNG
a working Git repository
```

The next development work will extend this base rather than restart the project.

