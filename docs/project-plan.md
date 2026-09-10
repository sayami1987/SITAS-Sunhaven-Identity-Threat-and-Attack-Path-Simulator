# SITAS Project Plan

## Project Title

Sunhaven Identity Threat and Attack-Path Simulator (SITAS)

## Project Background

Sunhaven Care is a fictional care organisation used as the case study for the
cybersecurity capstone project.

The environment includes different types of workers, user identities, shared
workstations, applications and sensitive fictional resident information.

Identity-related security weaknesses may create possible paths that an attacker
could use to reach protected systems or information.

## Problem

Threats such as stolen credentials, insecure shared workstation sessions,
stale accounts and excessive privileges may allow an attacker to move through
different systems and reach protected resources.

A traditional architecture diagram shows system components, but it does not
automatically identify the possible attack paths between an attacker and a
target.

## Proposed Solution

SITAS will be developed as a standalone Python-based cybersecurity simulator.

The program will represent a fictional Sunhaven Care environment as a directed
attack graph.

It will identify possible attack paths, calculate their risk and simulate how
selected security controls may block or reduce those paths.

## Main Objective

To design and develop a standalone attack-path simulator that models
identity-related cybersecurity threats in a fictional Sunhaven Care
environment and demonstrates how security controls reduce attack exposure.

## Specific Objectives

1. Create a fictional Sunhaven security environment.
2. Represent identities, credentials, devices, applications and assets as a graph.
3. Discover attack paths automatically.
4. Calculate risk using likelihood and impact.
5. Simulate selected security controls.
6. Compare attack exposure before and after controls.
7. Test the simulator using repeatable scenarios.
8. Generate clear security findings.

## Individual Contribution

SITAS is being developed as an individual technical component.

The simulator does not perform operational identity administration.

It does not create or modify Microsoft Entra users, perform Joiner-Mover-Leaver
automation, conduct manager access reviews, perform workforce compliance
checking, monitor security events or remediate user access.

The wider Sunhaven project provides the security scenario and business context,
while SITAS performs independent threat modelling and attack-path simulation.

## In Scope

- Fictional users and identities
- Fictional credentials
- Shared workstations
- Applications
- Protected assets
- Directed graph modelling
- Attack-path discovery
- Breadth-First Search
- Risk scoring
- MFA simulation
- RBAC simulation
- Session control simulation
- Before-and-after comparison
- Automated testing

## Out of Scope

- Real employee information
- Real resident information
- Production deployment
- Live Microsoft Entra administration
- User provisioning
- Joiner-Mover-Leaver automation
- Access-review workflow
- Compliance checking
- Security-event monitoring
- Automatic remediation

## Technologies

- Python 3
- JSON
- Visual Studio Code
- Git and GitHub
- Draw.io
- pytest
