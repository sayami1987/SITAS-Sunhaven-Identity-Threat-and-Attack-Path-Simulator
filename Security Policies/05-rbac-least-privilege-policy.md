# RBAC and Least Privilege Policy

## Purpose

To ensure users receive only the permissions required for their approved role.

## Policy

Sunhaven should:

- assign access according to legitimate job responsibilities;
- restrict administrative functions to authorised roles;
- avoid unnecessary privileged access;
- remove permissions that are no longer needed;
- separate normal access from restricted administrative access where practical.

## SITAS Alignment

SITAS Scenario 4 models an identity with excessive privilege.

The path includes:

```text
Care Worker Identity
→ Over-Privileged Role
→ Restricted Admin Function
→ Fictional Resident Records
```

The related control is:

```text
CTRL-RBAC
```

Automated tests confirm:

```text
RBAC OFF → OPEN
RBAC ON  → BLOCKED
```

**Verified status:** Implemented and tested as a simulation.
