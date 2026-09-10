def check_mfa_control(path, controls):
    """
    Check whether simulated MFA blocks a password-only attack path.
    """

    mfa_enabled = False

    for control in controls["controls"]:
        if control["id"] == "CTRL-MFA":
            mfa_enabled = control["enabled"]

    if mfa_enabled:
        if "nurse_password" in path and "nurse_identity" in path:
            return True, "MFA blocks password-only authentication."

    return False, "MFA does not block this path."
