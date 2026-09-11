# Multi-Factor Authentication Policy

## Purpose

To reduce the risk that a stolen password alone can be used to reach sensitive Sunhaven resources.

## Policy

Multi-Factor Authentication should be used for higher-risk access, including sensitive applications, remote access and privileged access where appropriate.

Users should not approve unexpected authentication requests or share authentication codes.

## SITAS Alignment

SITAS Scenario 1 models a stolen nurse credential.

```text
External Attacker
→ Stolen Nurse Password
→ Nurse Identity
→ Shared Nurse Workstation
→ Sunhaven Care Portal
→ Fictional Resident Records
```

The related control is:

```text
CTRL-MFA
```

The control engine contains a working MFA simulation rule, and automated tests verify both disabled and enabled behaviour.

```text
MFA OFF → OPEN
MFA ON  → BLOCKED
```

**Verified status:** Implemented and tested as a simulation. SITAS does not configure real MFA.
