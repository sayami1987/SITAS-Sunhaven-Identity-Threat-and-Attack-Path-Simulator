# Privileged Access Security Policy

## Purpose

To protect administrator and other high-privilege access because compromise of a privileged identity can have a high impact.

## Policy

Privileged access should:

- be limited to authorised users;
- follow least privilege;
- use stronger authentication;
- require additional authentication for sensitive privileged actions where appropriate;
- be reviewed regularly;
- not rely on shared administrator credentials.

## SITAS Alignment

SITAS Scenario 5 models a compromised privileged administrator identity reaching a restricted admin console.

The related control is:

```text
CTRL-PRIVAUTH
```

Automated tests confirm:

```text
Privileged Re-authentication OFF → OPEN
Privileged Re-authentication ON  → BLOCKED
```

**Verified status:** Implemented and tested as a simulation. SITAS does not manage real privileged accounts.
