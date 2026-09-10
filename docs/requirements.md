# SITAS Requirements

## Functional Requirements

### FR-01
The system shall load a fictional Sunhaven environment from a JSON file.

### FR-02
The system shall validate required environment data before processing.

### FR-03
The system shall represent environment objects as graph nodes.

### FR-04
The system shall represent relationships between objects as directed graph edges.

### FR-05
The system shall allow an attacker node to be selected as the starting point.

### FR-06
The system shall allow a protected asset to be selected as the target.

### FR-07
The system shall search for attack paths between the attacker and target.

### FR-08
The system shall use Breadth-First Search to identify attack paths.

### FR-09
The system shall prevent graph cycles from causing infinite processing.

### FR-10
The system shall calculate a risk score using likelihood and impact.

### FR-11
The system shall classify risk as Low, Medium, High or Critical.

### FR-12
The system shall support simulated security controls.

### FR-13
The system shall identify whether a security control blocks or reduces an attack path.

### FR-14
The system shall compare attack exposure before and after controls.

### FR-15
The system shall display understandable attack-path results.

## Non-Functional Requirements

### NFR-01
All project data shall be fictional or synthetic.

### NFR-02
The simulator shall operate without requiring a live Microsoft Entra environment.

### NFR-03
The system shall provide repeatable results for the same input.

### NFR-04
Risk calculations shall be simple and explainable.

### NFR-05
The Python source code shall be divided into understandable modules.

### NFR-06
The system shall handle invalid input without crashing unexpectedly.

### NFR-07
The project shall not store passwords, access tokens or other real secrets.

### NFR-08
The implementation shall be understandable enough to explain during a Bachelor
of Information Technology assessment demonstration.

### NFR-09
The system shall remain independent from other team members' runtime components.

### NFR-10
Testing evidence shall be retained for assessment purposes.
