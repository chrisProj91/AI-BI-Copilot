import plotly.express as px

def render_chart(df, chart):

    chart_type = chart["chart_type"]
    x = chart["x"]
    y = chart["y"]
    agg = chart["aggregation"]

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

    return fig