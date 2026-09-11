# SITAS Security Policies

## Purpose

This folder contains the security policies that are relevant to the **Sunhaven Identity Threat and Attack-Path Simulator (SITAS)**.

The policies are written for the fictional Sunhaven Care capstone environment. They are project-specific policies informed by common cybersecurity principles and the SANS cybersecurity policy library.

## Verified Policy Alignment

The current SITAS project was checked against the uploaded project folder before this policy set was prepared.

The following points were verified from the current project files:

- six threat scenario JSON files are present;
- six security controls are defined in `config/controls.json`;
- all six controls have simulation rules in `src/control_engine.py`;
- the environment is explicitly described as fictional;
- the protected target is named `Fictional Resident Records`;
- SITAS uses a local directed graph and BFS pathfinder;
- the risk model is stored in `config/risk-model.json`;
- the complete automated test suite runs successfully with **45 passing tests**;
- no Microsoft Entra, Microsoft Graph, Azure, HTTP, network or external API integration is present in the current `src/` code.

Therefore, SITAS is **aligned with the policy principles that are within the simulator's scope**.

It is important not to describe SITAS as operationally enforcing these policies in a real organisation. SITAS simulates the security effect of controls. For example, it models how MFA or account disablement changes an attack path, but it does not configure MFA or disable a real Microsoft Entra account.

---

## Policies in This Folder

| No. | Policy | SITAS Connection | Verified Status |
|---|---|---|---|
| 01 | Identity and Access Management Policy | Overall identity/access model | Aligned in simulator |
| 02 | Multi-Factor Authentication Policy | Scenario 1 / `CTRL-MFA` | Implemented and tested |
| 03 | Account Lifecycle and Termination Policy | Scenario 3 / `CTRL-ACCOUNT` | Implemented and tested |
| 04 | Shared Workstation and Session Security Policy | Scenario 2 / `CTRL-SESSION` | Implemented and tested |
| 05 | RBAC and Least Privilege Policy | Scenario 4 / `CTRL-RBAC` | Implemented and tested |
| 06 | Privileged Access Security Policy | Scenario 5 / `CTRL-PRIVAUTH` | Implemented and tested |
| 07 | Trusted Device and Remote Access Policy | Scenario 6 / `CTRL-DEVICE` | Implemented and tested |
| 08 | Secure Testing and Synthetic Data Policy | Fictional/offline environment and pytest | Followed by current project |
| 09 | Cybersecurity Risk Assessment Policy | 5×5 risk model | Implemented and tested |

---

## How the Policies Connect to SITAS

```text
Sunhaven Security Problem
        ↓
Security Policy
        ↓
Expected Security Control
        ↓
SITAS Threat Scenario
        ↓
Attack Path
        ↓
Risk Assessment
        ↓
Control Simulation
        ↓
OPEN or BLOCKED Result
        ↓
Testing Evidence
```

The policies define the expected security position. SITAS provides a technical simulation that demonstrates why those controls matter.

---

## Important Scope Statement

SITAS does not:

- create or modify real user accounts;
- configure Microsoft Entra;
- make Microsoft Graph calls;
- perform Joiner-Mover-Leaver automation;
- carry out live access reviews;
- monitor real security events;
- enforce device compliance on real endpoints;
- perform real cyberattacks;
- use real employee or resident information.

For that reason, statements in this folder use wording such as **"aligned", "simulated", "implemented in SITAS"** and **"tested"**, rather than claiming real-world organisational enforcement.

---

## Evidence Used for Verification

The current project contains:

```text
scenarios/scenario-01-stolen-nurse-credential.json
scenarios/scenario-02-shared-session.json
scenarios/scenario-03-former-worker.json
scenarios/scenario-04-excessive-privilege.json
scenarios/scenario-05-privileged-admin.json
scenarios/scenario-06-unmanaged-device.json
```

The control configuration contains:

```text
CTRL-MFA
CTRL-RBAC
CTRL-SESSION
CTRL-ACCOUNT
CTRL-PRIVAUTH
CTRL-DEVICE
```

Automated testing currently covers the risk engine, graph/BFS engine, control engine and model/configuration loading.

Verified test result:

```text
45 passed
```

---

## Policy References

These Sunhaven policies are original project adaptations. They are not copies of SANS templates.

Useful external reference material:

- SANS Cybersecurity / Information Security Policies and Standards  
  https://www.sans.org/information-security-policy
- SANS Access Management Policy  
  https://www.sans.org/information-security-policy/access-management-policy
- SANS Identity Management Policy  
  https://www.sans.org/information-security-policy/identity-management-policy
- SANS Privileged Account Management Policy  
  https://www.sans.org/information-security-policy/privileged-account-management-policy
- SANS Internal Network Access Management Policy  
  https://www.sans.org/information-security-policy/internal-network-access-management-policy
- SANS Safeguard Validation Management Policy  
  https://www.sans.org/information-security-policy/safeguard-validation-management-policy

