# Account Lifecycle and Termination Policy

## Purpose

To prevent former, inactive or unnecessary identities from continuing to access Sunhaven systems.

## Policy

User access should follow a lifecycle:

```text
Create
→ Maintain
→ Change
→ Disable
→ Remove
```

When a worker leaves Sunhaven, their access should be disabled promptly. Role changes should also trigger an access review so permissions that are no longer required can be removed.

## SITAS Alignment

SITAS Scenario 3 models a former worker attempting to use an existing identity.

The related control is:

```text
CTRL-ACCOUNT
```

Automated tests confirm:

```text
Account Disablement OFF → OPEN
Account Disablement ON  → BLOCKED
```

**Verified status:** Implemented and tested as a simulation. SITAS does not disable real accounts.
