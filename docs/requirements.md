# \# SITAS Requirements

# 

# \## Project

# 

# \*\*Project Title:\*\* Sunhaven Identity Threat and Attack-Path Simulator (SITAS)  

# \*\*Unit:\*\* COIT13236 Cyber Security Project

# 

# \---

# 

# \## 1. Functional Requirements

# 

# | ID | Requirement | Current Status |

# |---|---|---|

# | FR-01 | The system shall load a fictional Sunhaven environment from a JSON file. | Completed |

# | FR-02 | The system shall validate required environment data before processing. | Completed |

# | FR-03 | The system shall represent environment objects as graph nodes. | Completed |

# | FR-04 | The system shall represent relationships between objects as directed graph edges. | Completed |

# | FR-05 | The system shall allow an attacker node to be selected as the starting point. | Completed through scenario files |

# | FR-06 | The system shall allow a protected asset to be selected as the target. | Completed through scenario files |

# | FR-07 | The system shall search for attack paths between the attacker and target. | Completed |

# | FR-08 | The system shall use Breadth-First Search to identify attack paths. | Completed |

# | FR-09 | The system shall prevent graph cycles from causing infinite processing. | Completed and tested |

# | FR-10 | The system shall calculate a risk score using likelihood and impact. | Completed |

# | FR-11 | The system shall classify risk as Low, Medium, High or Critical. | Completed |

# | FR-12 | The system shall support simulated security controls. | Completed |

# | FR-13 | The system shall identify whether a security control blocks an attack path. | Completed |

# | FR-14 | The system shall compare attack exposure before and after controls. | Partially completed; manual OFF/ON comparison works, automatic comparison mode is planned |

# | FR-15 | The system shall display understandable attack-path results. | Completed |

# | FR-16 | The system shall support multiple independent threat scenarios. | Completed with six scenarios |

# | FR-17 | The system shall load risk settings from a JSON configuration file. | Completed |

# | FR-18 | The system shall validate likelihood and impact ratings before calculation. | Completed |

# | FR-19 | The system shall support automated testing of the main analysis components. | Completed with 45 passing pytest tests |

# | FR-20 | The system shall export structured JSON results. | Planned |

# | FR-21 | The system shall generate a CSV summary of scenario results. | Planned |

# | FR-22 | The system shall generate an understandable HTML security report. | Planned |

# 

# \---

# 

# \## 2. Implemented Security Controls

# 

# SITAS currently simulates six security controls:

# 

# 1\. \*\*CTRL-MFA – Multi-Factor Authentication\*\*

# 2\. \*\*CTRL-SESSION – Session Timeout\*\*

# 3\. \*\*CTRL-ACCOUNT – Account Disablement\*\*

# 4\. \*\*CTRL-RBAC – Role-Based Access Control\*\*

# 5\. \*\*CTRL-PRIVAUTH – Privileged Re-authentication\*\*

# 6\. \*\*CTRL-DEVICE – Trusted Device Restriction\*\*

# 

# These controls are simulated only. SITAS does not modify live Microsoft Entra settings.

# 

# \---

# 

# \## 3. Implemented Threat Scenarios

# 

# The current system includes six repeatable threat scenarios:

# 

# 1\. Stolen Nurse Credential

# 2\. Shared Workstation Session Misuse

# 3\. Former Worker Identity Misuse

# 4\. Excessive Privilege Abuse

# 5\. Privileged Administrator Credential Compromise

# 6\. Unmanaged Device Access

# 

# Each scenario includes:

# 

# \- a scenario ID;

# \- scenario name;

# \- description;

# \- start node;

# \- target node;

# \- likelihood;

# \- impact;

# \- related security control.

# 

# \---

# 

# \## 4. Risk Requirements

# 

# SITAS uses a configurable 5 × 5 risk model.

# 

# ```text

# Risk Score = Likelihood × Impact

# ```

# 

# \### Likelihood Scale

# 

# ```text

# 1 = Rare

# 2 = Unlikely

# 3 = Possible

# 4 = Likely

# 5 = Almost Certain

# ```

# 

# \### Impact Scale

# 

# ```text

# 1 = Insignificant

# 2 = Minor

# 3 = Moderate

# 4 = Major

# 5 = Severe

# ```

# 

# \### Severity Bands

# 

# ```text

# 1–4   = Low

# 5–9   = Medium

# 10–16 = High

# 17–25 = Critical

# ```

# 

# The risk settings are stored in:

# 

# ```text

# config/risk-model.json

# ```

# 

# \---

# 

# \## 5. Non-Functional Requirements

# 

# | ID | Requirement | Current Status |

# |---|---|---|

# | NFR-01 | All project data shall be fictional or synthetic. | Completed |

# | NFR-02 | The simulator shall operate without requiring a live Microsoft Entra environment. | Completed |

# | NFR-03 | The system shall provide repeatable results for the same input. | Completed and tested |

# | NFR-04 | Risk calculations shall be simple and explainable. | Completed |

# | NFR-05 | Python source code shall be divided into understandable modules. | Completed |

# | NFR-06 | The system shall handle invalid input without crashing unexpectedly. | Completed for current JSON/risk validation and tested |

# | NFR-07 | The project shall not store real passwords, access tokens or secrets. | Completed |

# | NFR-08 | The implementation shall be understandable enough to explain during a Bachelor of Information Technology assessment demonstration. | Completed |

# | NFR-09 | The system shall remain independent from other team members' runtime components. | Completed |

# | NFR-10 | Testing evidence shall be retained for assessment purposes. | Completed and ongoing |

# | NFR-11 | The same analysis engine shall be reusable across multiple scenarios. | Completed |

# | NFR-12 | The project shall remain safe for offline demonstration. | Completed |

# 

# \---

# 

# \## 6. Individual Contribution Boundary

# 

# SITAS is the threat-modelling and attack-path simulation component of the wider Sunhaven Care Workforce IAM project.

# 

# SITAS does \*\*not\*\*:

# 

# \- create, update or delete Microsoft Entra users;

# \- perform Joiner-Mover-Leaver automation;

# \- conduct manager access reviews;

# \- run live workforce compliance checks;

# \- monitor production security events;

# \- automatically remove access;

# \- perform real cyberattacks;

# \- use real employee or resident data.

# 

# Its role is to model identity threats, discover attack paths, calculate risk and demonstrate the effect of simulated security controls.

# 

# \---

# 

# \## 7. Current Requirement Summary

# 

# The core simulator requirements are now implemented.

# 

# The main remaining requirements are:

# 

# ```text

# FR-14  Automatic before/after comparison

# FR-20  JSON result export

# FR-21  CSV scenario summary

# FR-22  HTML security report

# ```

# 

# These remaining items are planned for the next development stage.



