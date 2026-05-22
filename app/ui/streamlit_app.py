import sys
from pathlib import Path
import streamlit as st

# -----------------------------
# FIX IMPORT PATH (important)
# -----------------------------
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from app.main import run_pipeline
from app.ai.insights_generator import ask_data_question

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI BI Copilot",
    layout="wide"
)

st.title("📊 AI BI Copilot")
st.caption("Upload data → Get dashboards, KPIs, insights & AI chat")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Control Panel")

    uploaded = st.file_uploader(
        "Upload CSV dataset",
        type=["csv"]
    )

    mode = st.radio(
        "Mode",
        ["Auto Dashboard", "Explore Data", "Ask AI"]
    )

    st.divider()

    st.info("AI automatically generates KPIs, dashboards & insights from your data.")

# -----------------------------
# MAIN APP
# -----------------------------
if uploaded:

    # Save temp file
    temp_path = "temp.csv"
    with open(temp_path, "wb") as f:
        f.write(uploaded.getbuffer())

    # Run AI pipeline
    results = run_pipeline(temp_path)

    df = results["df"]
    dashboard = results["dashboard"]
    figures = results["figures"]
    metrics = results["metrics"]

    # -----------------------------
    # DASHBOARD TITLE
    # -----------------------------
    st.header(dashboard.get("dashboard_title", "AI Dashboard"))

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    st.subheader("📌 Key Metrics")

    metric_items = list(metrics.items())

    cols = st.columns(min(4, len(metric_items)))

    for i, col in enumerate(cols):
        if i < len(metric_items):
            key, value = metric_items[i]

            # format value nicely
            if isinstance(value, dict):
                value = list(value.values())[0]

            col.metric(label=key, value=str(value))

    st.divider()

    # -----------------------------
    # DASHBOARD CHARTS
    # -----------------------------
    st.subheader("📊 AI Generated Dashboard")

    for fig in figures:
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # -----------------------------
    # INSIGHTS (if available)
    # -----------------------------
    if "insights" in results:
        st.subheader("🧠 AI Insights")
        st.write(results["insights"])

    st.divider()

    # -----------------------------
    # CHAT WITH DATA (PRODUCT FEATURE)
    # -----------------------------
    if mode == "Ask AI":

        st.subheader("💬 Ask your data")

        question = st.text_input("Type your question about the dataset")

        if question:

            with st.spinner("Analyzing data..."):

                answer = ask_data_question(df, question)

            st.success(answer)

    # -----------------------------
    # EXPLORE DATA MODE
    # -----------------------------
    if mode == "Explore Data":

        st.subheader("🔍 Dataset Preview")

        st.write(df.head(50))

        st.subheader("📊 Quick Statistics")

        st.write(df.describe(include="all"))