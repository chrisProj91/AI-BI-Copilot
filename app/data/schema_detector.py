def detect_column_roles(df):

    roles = {
        "numeric": [],
        "categorical": [],
        "datetime": [],
        "id_like": []
    }

    for col in df.columns:

        dtype = str(df[col].dtype)

        if dtype in ["int64", "float64"]:
            roles["numeric"].append(col)

        elif "date" in col.lower():
            roles["datetime"].append(col)

        elif df[col].nunique() == len(df):
            roles["id_like"].append(col)

        else:
            roles["categorical"].append(col)

    return roles