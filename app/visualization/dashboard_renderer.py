import plotly.express as px
from app.visualization.chart_renderer import render_chart

def render_dashboard(df, dashboard):

    # SAFETY CHECK
    if "charts" not in dashboard:
        raise ValueError(f"Invalid dashboard format: {dashboard}")

    figures = []

    for chart in dashboard["charts"]:

        chart_type = chart["chart_type"]
        x = chart["x"]
        y = chart["y"]
        agg = chart.get("aggregation", "sum")

        if agg == "sum":
            grouped = df.groupby(x)[y].sum().reset_index()
        elif agg == "avg":
            grouped = df.groupby(x)[y].mean().reset_index()
        else:
            grouped = df.groupby(x)[y].count().reset_index()

        if chart_type == "bar":
            fig = px.bar(grouped, x=x, y=y)

        elif chart_type == "line":
            fig = px.line(grouped, x=x, y=y)

        elif chart_type == "pie":
            fig = px.pie(grouped, names=x, values=y)

        figures.append(fig)

    return figures