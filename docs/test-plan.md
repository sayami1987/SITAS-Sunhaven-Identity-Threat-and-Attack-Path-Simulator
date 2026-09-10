# SITAS Test Plan

## Purpose

The purpose of testing is to confirm that the SITAS prototype correctly loads
the fictional environment, builds an attack graph, identifies attack paths,
calculates risk and applies simulated security controls.

## Planned Tests

| Test ID | Test | Expected Result |
|---|---|---|
| SITAS-T01 | Load valid environment JSON | Environment loads successfully |
| SITAS-T02 | Load invalid JSON | Clear error is displayed |
| SITAS-T03 | Create graph nodes | Expected nodes are created |
| SITAS-T04 | Create graph relationships | Expected edges are created |
| SITAS-T05 | Find valid attack path | Path is returned |
| SITAS-T06 | Search unreachable target | No path is returned |
| SITAS-T07 | Graph contains a cycle | Program does not loop forever |
| SITAS-T08 | Calculate risk score | Correct likelihood × impact result |
| SITAS-T09 | Classify Low risk | Correct severity returned |
| SITAS-T10 | Classify Critical risk | Correct severity returned |
| SITAS-T11 | Apply simulated MFA | Password-only path is blocked/reduced |
| SITAS-T12 | Apply simulated RBAC | Unauthorised privilege path is blocked |
| SITAS-T13 | Apply session timeout | Stale-session path is blocked |
| SITAS-T14 | Compare before/after results | Difference is calculated correctly |
| SITAS-T15 | Execute complete prototype | Program completes without error |

## Evidence

Testing evidence will include:

- terminal output;
- screenshots;
- test result logs;
- GitHub commits;
- generated prototype results.
