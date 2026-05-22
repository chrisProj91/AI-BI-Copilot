import json

from app.data.loader import load_csv
from app.data.schema_detector import detect_column_roles
from app.data.metric_engine import compute_metrics

from app.ai.dashboard_planner import generate_dashboard_plan
from app.visualization.dashboard_renderer import render_dashboard


# -----------------------------
# SAFE JSON PARSER
# -----------------------------
def safe_json_load(text):
    try:
        return json.loads(text)
    except Exception as e:
        raise ValueError(f"Invalid JSON from AI:\n{text}") from e


# -----------------------------
# SCHEMA GUARANTEE (IMPORTANT)
# -----------------------------
def ensure_dashboard_schema(dashboard, roles):
    """
    Ensures AI output always has valid structure.
    """

    if not isinstance(dashboard, dict):
        dashboard = {}

    if "charts" not in dashboard or not isinstance(dashboard["charts"], list):
        dashboard["charts"] = []

    if len(dashboard["charts"]) == 0:
        # AUTO FALLBACK CHART (prevents crash)
        fallback_x = roles["categorical"][0] if roles["categorical"] else None
        fallback_y = roles["numeric"][0] if roles["numeric"] else None

        if fallback_x and fallback_y:
            dashboard["charts"].append({
                "chart_type": "bar",
                "x": fallback_x,
                "y": fallback_y,
                "aggregation": "sum",
                "title": "Auto Generated Fallback Chart"
            })

    return dashboard


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def run_pipeline(file_path):

    print("\n[1] Loading dataset...")
    df = load_csv(file_path)

    print("[2] Detecting schema...")
    roles = detect_column_roles(df)

    print("[3] Computing metrics...")
    metrics = compute_metrics(df, roles)

    print("[4] Generating AI dashboard plan...")
    dashboard_json = generate_dashboard_plan(df, roles)

    # SAFE PARSE
    dashboard = safe_json_load(dashboard_json)

    # ENSURE STRUCTURE
    dashboard = ensure_dashboard_schema(dashboard, roles)

    print("[5] Rendering dashboard...")
    figures = render_dashboard(df, dashboard)

    print("\n=== DASHBOARD PLAN ===")
    print(json.dumps(dashboard, indent=2))

    return {
        "df": df,
        "roles": roles,
        "metrics": metrics,
        "dashboard": dashboard,
        "figures": figures
    }


# -----------------------------
# LOCAL TEST
# -----------------------------
if __name__ == "__main__":

    file_path = "datasets/Sample_Superstore.csv"

    results = run_pipeline(file_path)