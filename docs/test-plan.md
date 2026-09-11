# \# SITAS Test Plan

# 

# \## Project

# 

# \*\*Project Title:\*\* Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  

# \*\*Unit:\*\* COIT13236 Cyber Security Project

# 

# \---

# 

# \## 1. Purpose

# 

# The purpose of testing is to confirm that SITAS correctly:

# 

# \- loads the fictional Sunhaven environment;

# \- validates configuration data;

# \- builds the directed attack graph;

# \- discovers attack paths using BFS;

# \- handles unreachable targets and graph cycles;

# \- calculates and classifies risk;

# \- applies simulated security controls;

# \- loads all six threat scenarios;

# \- provides repeatable results.

# 

# Automated testing is implemented using `pytest`.

# 

# \---

# 

# \## 2. Current Automated Test Summary

# 

# | Test Area | Number of Passing Tests |

# |---|---:|

# | Risk Engine | 14 |

# | Graph and BFS | 9 |

# | Control Engine | 13 |

# | Model Loader and Configuration | 9 |

# | \*\*Total\*\* | \*\*45\*\* |

# 

# Current verified result:

# 

# ```text

# 45 passed

# ```

# 

# \---

# 

# \## 3. Risk Engine Tests

# 

# The risk-engine tests confirm:

# 

# \- Scenario 1 risk result;

# \- Scenario 2 risk result;

# \- Scenario 3 risk result;

# \- Low severity lower boundary;

# \- Low severity upper boundary;

# \- Medium severity lower boundary;

# \- Medium severity upper boundary;

# \- High severity lower boundary;

# \- High severity upper boundary;

# \- Critical severity lower boundary;

# \- Critical severity upper boundary;

# \- invalid likelihood is rejected;

# \- invalid impact is rejected;

# \- non-integer rating is rejected.

# 

# Expected behaviour:

# 

# ```text

# Risk Score = Likelihood × Impact

# ```

# 

# Severity:

# 

# ```text

# 1–4   = Low

# 5–9   = Medium

# 10–16 = High

# 17–25 = Critical

# ```

# 

# Evidence:

# 

# ```text

# evidence/19-pytest-risk-engine.png

# ```

# 

# \---

# 

# \## 4. Graph and BFS Tests

# 

# The graph and pathfinder tests confirm:

# 

# \- all expected graph nodes are created;

# \- directed relationships are created correctly;

# \- node IDs map to readable names;

# \- BFS finds a reachable attack path;

# \- BFS returns the shortest reachable path;

# \- BFS returns no path for an unreachable target;

# \- graph cycles do not cause endless processing;

# \- start equal to target is handled correctly;

# \- the real Scenario 6 unmanaged-device path is correct.

# 

# The Scenario 6 regression test is important because an earlier version reused a shared identity node and BFS selected a different valid path. The graph model was corrected by introducing a separate Remote Care Worker Identity.

# 

# Evidence:

# 

# ```text

# evidence/20-pytest-graph-bfs.png

# ```

# 

# \---

# 

# \## 5. Control Engine Tests

# 

# The control-engine tests confirm the enabled and disabled behaviour of all six controls.

# 

# | Control | Disabled | Enabled |

# |---|---|---|

# | Multi-Factor Authentication | OPEN | BLOCKED |

# | Session Timeout | OPEN | BLOCKED |

# | Account Disablement | OPEN | BLOCKED |

# | Role-Based Access Control | OPEN | BLOCKED |

# | Privileged Re-authentication | OPEN | BLOCKED |

# | Trusted Device Restriction | OPEN | BLOCKED |

# 

# An additional test confirms that an unknown control does not incorrectly block an attack path.

# 

# Evidence:

# 

# ```text

# evidence/21-pytest-control-engine.png

# ```

# 

# \---

# 

# \## 6. Model Loader and Configuration Tests

# 

# These tests confirm:

# 

# \- valid environment JSON loads successfully;

# \- an environment missing nodes is rejected;

# \- an environment missing relationships is rejected;

# \- invalid JSON is rejected;

# \- a missing JSON file is handled;

# \- the real `environment.json` loads;

# \- the real `controls.json` loads;

# \- the real `risk-model.json` loads;

# \- all six scenario JSON files load successfully.

# 

# Evidence:

# 

# ```text

# evidence/22-pytest-model-loader.png

# ```

# 

# \---

# 

# \## 7. Full Test Suite

# 

# The complete project test suite is run with:

# 

# ```powershell

# python -m pytest -v

# ```

# 

# Current verified result:

# 

# ```text

# 45 passed

# ```

# 

# Evidence:

# 

# ```text

# evidence/23-pytest-full-suite-45-passed.png

# ```

# 

# This confirms that all automated test categories pass together in the current project version.

# 

# \---

# 

# \## 8. Manual Scenario Verification

# 

# Automated testing is supported by manual before/after evidence.

# 

# \### Scenario 1 – MFA

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 07-scenario-01-mfa-off-open.png

# 08-scenario-01-mfa-on-blocked.png

# ```

# 

# \### Scenario 2 – Session Timeout

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 09-scenario-02-session-off-open.png

# 10-scenario-02-session-on-blocked.png

# ```

# 

# \### Scenario 3 – Account Disablement

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 11-scenario-03-account-off-open.png

# 12-scenario-03-account-on-blocked.png

# ```

# 

# \### Scenario 4 – RBAC

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 13-scenario-04-rbac-off-open.png

# 14-scenario-04-rbac-on-blocked.png

# ```

# 

# \### Scenario 5 – Privileged Re-authentication

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 15-scenario-05-privauth-off-open.png

# 16-scenario-05-privauth-on-blocked.png

# ```

# 

# \### Scenario 6 – Trusted Device Restriction

# 

# ```text

# OFF → OPEN

# ON  → BLOCKED

# ```

# 

# Evidence:

# 

# ```text

# 17-scenario-06-device-off-open.png

# 18-scenario-06-device-on-blocked.png

# ```

# 

# \---

# 

# \## 9. Requirements Traceability

# 

# | Requirement Area | Test Evidence |

# |---|---|

# | JSON loading | Model Loader tests |

# | Required environment validation | Model Loader tests |

# | Graph nodes | Graph tests |

# | Directed relationships | Graph tests |

# | BFS attack-path discovery | BFS tests |

# | Unreachable target handling | BFS tests |

# | Graph-cycle handling | BFS tests |

# | Risk calculation | Risk Engine tests |

# | Severity classification | Risk Engine tests |

# | Invalid risk input handling | Risk Engine tests |

# | Security-control behaviour | Control Engine tests |

# | Six scenario files | Model Loader tests |

# | Repeatable results | Full pytest suite |

# 

# Automatic before/after comparison and generated reporting will receive additional tests when those features are implemented.

# 

# \---

# 

# \## 10. Remaining Testing Work

# 

# The core simulator test suite is complete for the current implementation.

# 

# Additional tests will be added for the remaining planned features:

# 

# \- automatic `--compare` mode;

# \- JSON result export;

# \- CSV summary generation;

# \- HTML report generation.

# 

# These future tests will confirm that the output files contain the correct scenario, risk, control and comparison results.

# 

# \---

# 

# \## 11. Test Evidence Retention

# 

# Testing evidence is retained through:

# 

# \- terminal output;

# \- screenshots;

# \- pytest results;

# \- source test files;

# \- Git commits;

# \- GitHub history;

# \- generated results and reports.

# 

# This evidence supports verification of the individual technical contribution and makes the project behaviour repeatable.



