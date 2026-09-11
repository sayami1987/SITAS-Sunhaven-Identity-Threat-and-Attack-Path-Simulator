# Trusted Device and Remote Access Policy

## Purpose

To reduce the risk of valid or stolen credentials being used from unmanaged or untrusted devices.

## Policy

Sensitive access should consider the security state of the device as well as the identity of the user.

Where appropriate, Sunhaven should require trusted or managed devices for higher-risk access.

Devices used for sensitive access should use reasonable protections such as supported software, security updates and device locking.

## SITAS Alignment

SITAS Scenario 6 models a stolen care-worker credential being used to create an unmanaged device session.

The related control is:

```text
CTRL-DEVICE
```

The intended path uses a dedicated `Remote Care Worker Identity` and an `Unmanaged Device Session`.

Automated tests confirm:

```text
Trusted Device Restriction OFF → OPEN
Trusted Device Restriction ON  → BLOCKED
```

A regression test also verifies the real Scenario 6 BFS path.

**Verified status:** Implemented and tested as a simulation. SITAS does not enforce compliance on real devices.
