# Secure Testing and Synthetic Data Policy

## Purpose

To ensure SITAS development and demonstration can be performed without exposing real people, credentials or production systems.

## Policy

SITAS testing should:

- use fictional or synthetic identities;
- use fictional credentials and resident information;
- avoid real passwords and access tokens;
- avoid real cyberattacks;
- remain separate from live identity infrastructure;
- use repeatable automated tests;
- retain appropriate project evidence.

## SITAS Alignment

The current environment file explicitly identifies itself as:

```text
Sunhaven Care Test Environment
Fictional environment for the SITAS cybersecurity simulator
```

The protected target is:

```text
Fictional Resident Records
```

The current `src/` code contains no Microsoft Entra, Microsoft Graph, Azure, HTTP or other network/API integration.

The full automated test suite was independently rerun against the uploaded project and produced:

```text
45 passed
```

**Verified status:** Followed by the current SITAS implementation.
