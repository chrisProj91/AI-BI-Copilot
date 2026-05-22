import pandas as pd

def load_csv(file):
    for enc in ["utf-8", "latin1", "cp1252"]:
        try:
            return pd.read_csv(file, encoding=enc)
        except:
            continue

    raise Exception("Unsupported encoding")