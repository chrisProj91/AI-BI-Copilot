def compute_metrics(df, roles):

    metrics = {}

    for col in roles["numeric"]:

        metrics[col] = {
            "sum": float(df[col].sum()),
            "avg": float(df[col].mean()),
            "max": float(df[col].max()),
            "min": float(df[col].min())
        }

    return metrics