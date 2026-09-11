# Cybersecurity Risk Assessment Policy

## Purpose

To provide a consistent and understandable way to rate the risk of the threat scenarios analysed by SITAS.

## Policy

Each SITAS scenario should have:

- a likelihood value;
- an impact value;
- a calculated risk score;
- a severity classification.

The current model uses:

```text
Risk Score = Likelihood × Impact
```

Likelihood and impact use a 1–5 scale.

Severity bands are:

```text
1–4   = Low
5–9   = Medium
10–16 = High
17–25 = Critical
```

Risk ratings should be validated before they are used.

## SITAS Alignment

The model is stored in:

```text
config/risk-model.json
```

The current `risk_engine.py` reads the configured scale and severity bands and validates likelihood and impact values.

Automated risk tests cover valid scenario calculations, severity boundaries and invalid ratings.

**Verified status:** Implemented and tested.
