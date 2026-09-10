def get_control_enabled(controls, control_id):
    """
    Check whether a security control is enabled.
    """

    for control in controls["controls"]:
        if control["id"] == control_id:
            return control["enabled"]

    return False


def check_mfa_control(path, controls):
    """
    Check whether MFA blocks a password-based attack path.
    """

    mfa_enabled = get_control_enabled(
        controls,
        "CTRL-MFA"
    )

    if mfa_enabled:
        if "nurse_password" in path and "nurse_identity" in path:
            return True, "MFA blocks password-only authentication."

    return False, "MFA does not block this path."


def check_session_timeout_control(path, controls):
    """
    Check whether session timeout blocks reuse of an active session.
    """

    session_enabled = get_control_enabled(
        controls,
        "CTRL-SESSION"
    )

    if session_enabled:
        if "active_nurse_session" in path:
            return True, "Session timeout prevents reuse of the stale active session."

    return False, "Session timeout does not block this path."


def assess_control(path, controls, control_id):
    """
    Run the correct security control simulation.
    """

    if control_id == "CTRL-MFA":
        return check_mfa_control(
            path,
            controls
        )

    if control_id == "CTRL-SESSION":
        return check_session_timeout_control(
            path,
            controls
        )

    return False, f"No simulation rule exists for {control_id}."