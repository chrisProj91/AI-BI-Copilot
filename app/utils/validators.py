def validate_dashboard(d):

    if "charts" not in d:
        return False

    for c in d["charts"]:
        required = ["chart_type", "x", "y"]
        for r in required:
            if r not in c:
                return False

    return True