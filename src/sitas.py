from model_loader import load_environment, load_json_file
from graph_engine import build_graph, get_node_names
from pathfinder import find_path_bfs
from risk_engine import calculate_risk, classify_risk
from control_engine import check_mfa_control


def main():
    print("SITAS - Sunhaven Identity Threat and Attack-Path Simulator")
    print("-" * 60)

    environment = load_environment("config/environment.json")
    controls = load_json_file("config/controls.json")

    if environment is None or controls is None:
        print("Unable to continue.")
        return

    graph = build_graph(environment)
    node_names = get_node_names(environment)

    start_node = "external_attacker"
    target_node = "resident_records"

    path = find_path_bfs(graph, start_node, target_node)

    if not path:
        print("\nNo attack path found.")
        return

    print("\nAttack path found:\n")

    for index, node_id in enumerate(path):
        print(node_names[node_id])

        if index < len(path) - 1:
            print("   ↓")

    # Simple risk calculation for the first scenario.
    likelihood = 4
    impact = 5

    risk_score = calculate_risk(likelihood, impact)
    severity = classify_risk(risk_score)

    print("\nRisk Assessment")
    print("-" * 30)
    print(f"Likelihood: {likelihood}/5")
    print(f"Impact:     {impact}/5")
    print(f"Risk Score: {risk_score}/25")
    print(f"Severity:   {severity}")

    blocked, reason = check_mfa_control(path, controls)

    print("\nSecurity Control Assessment")
    print("-" * 30)

    if blocked:
        print("Attack Path Status: BLOCKED")
    else:
        print("Attack Path Status: OPEN")

    print(f"Reason: {reason}")


if __name__ == "__main__":
    main()