# Shared Workstation and Session Security Policy

## Purpose

To reduce the risk of an unauthorised person reusing an authenticated session on a shared or unattended workstation.

## Policy

Users should:

- lock a workstation when leaving it unattended;
- sign out when work is complete;
- not allow another person to reuse their authenticated session.

Systems should use appropriate session timeout or automatic locking where the risk requires it.

## SITAS Alignment

SITAS Scenario 2 models an unauthorised person using an unattended workstation with an active nurse session.

The related control is:

```text
CTRL-SESSION
```

Automated tests confirm:

```text
Session Timeout OFF → OPEN
Session Timeout ON  → BLOCKED
```

**Verified status:** Implemented and tested as a simulation.
