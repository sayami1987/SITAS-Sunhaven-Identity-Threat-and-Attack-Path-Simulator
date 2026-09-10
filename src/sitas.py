import sys

from model_loader import load_environment, load_json_file
from graph_engine import build_graph, get_node_names
from pathfinder import find_path_bfs
from risk_engine import assess_risk
from control_engine import assess_control


def main():
    print("SITAS - Sunhaven Identity Threat and Attack-Path Simulator")
    print("-" * 60)

    # Scenario 1 is used when no scenario file is supplied.
    scenario_file = (
        "scenarios/scenario-01-stolen-nurse-credential.json"
    )

    # Allow another scenario to be selected from the terminal.
    if len(sys.argv) > 1:
        scenario_file = sys.argv[1]

    # Load project configuration files.
    environment = load_environment(
        "config/environment.json"
    )

    controls = load_json_file(
        "config/controls.json"
    )

    risk_model = load_json_file(
        "config/risk-model.json"
    )

    scenario = load_json_file(
        scenario_file
    )

    # Stop if any required file could not be loaded.
    if (
        environment is None
        or controls is None
        or risk_model is None
        or scenario is None
    ):
        print("Unable to continue.")
        return

    # Display scenario information.
    print()
    print(f"Scenario ID:   {scenario['scenarioId']}")
    print(f"Scenario Name: {scenario['name']}")
    print(f"Description:   {scenario['description']}")

    # Build the attack graph.
    graph = build_graph(
        environment
    )

    node_names = get_node_names(
        environment
    )

    start_node = scenario["startNode"]
    target_node = scenario["targetNode"]

    # Find the attack path using BFS.
    path = find_path_bfs(
        graph,
        start_node,
        target_node
    )

    if not path:
        print("\nNo attack path found.")
        return

    # Display the attack path.
    print("\nAttack Path Found")
    print("-" * 30)

    for index, node_id in enumerate(path):
        print(node_names[node_id])

        if index < len(path) - 1:
            print("   ↓")

    # Read scenario risk values.
    likelihood = scenario["likelihood"]
    impact = scenario["impact"]

    # Calculate risk using risk-model.json.
    try:
        risk = assess_risk(
            likelihood,
            impact,
            risk_model
        )

    except ValueError as error:
        print(f"\nRisk Model Error: {error}")
        return

    # Display risk assessment.
    print("\nRisk Assessment")
    print("-" * 30)

    print(
        f"Likelihood: "
        f"{risk['likelihood']}/5 "
        f"({risk['likelihoodLabel']})"
    )

    print(
        f"Impact:     "
        f"{risk['impact']}/5 "
        f"({risk['impactLabel']})"
    )

    print(
        f"Risk Score: "
        f"{risk['riskScore']}/25"
    )

    print(
        f"Severity:   "
        f"{risk['severity']}"
    )

    # Security control assessment.
    print("\nSecurity Control Assessment")
    print("-" * 30)

    related_controls = scenario.get(
        "relatedControls",
        []
    )

    final_blocked = False

    if not related_controls:
        print(
            "No security controls are assigned "
            "to this scenario."
        )

    else:
        for control_id in related_controls:

            blocked, reason = assess_control(
                path,
                controls,
                control_id
            )

            print(f"Control: {control_id}")

            if blocked:
                print("Status:  BLOCKED")
                final_blocked = True
            else:
                print("Status:  OPEN")

            print(f"Reason:  {reason}")
            print()

    # Display final result.
    if final_blocked:
        print(
            "Final Attack Path Status: BLOCKED"
        )
    else:
        print(
            "Final Attack Path Status: OPEN"
        )


if __name__ == "__main__":
    main()