def calculate_risk(likelihood, impact):
    """
    Calculate risk using likelihood multiplied by impact.
    """
    return likelihood * impact


def classify_risk(score):
    """
    Convert the numerical risk score into a severity level.
    """
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Medium"
    elif score <= 16:
        return "High"
    else:
        return "Critical"
