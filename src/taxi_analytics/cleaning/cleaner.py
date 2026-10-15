import pandas as pd

TEXT_COLUMNS = ["color","payment","pickup_borough","pickup_zone","dropoff_borough","dropoff_zone"]
NUMERIC_COLUMNS = ["passengers","distance","fare","tip","tolls","total"]
def clean_taxi_data(raw: pd.DataFrame) -> pd.DataFrame:
    df = raw.copy()
    for col in ["pickup","dropoff"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in TEXT_COLUMNS:
        df[col] = df[col].astype("string").str.strip().str.replace(r"\\s+", " ", regex=True)
    df["source_row_id"] = range(1, len(df)+1)
    df["is_duplicate_row"] = df.duplicated(subset=list(raw.columns), keep=False)
    return df
