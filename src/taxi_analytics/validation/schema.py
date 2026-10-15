import pandas as pd

REQUIRED_COLUMNS = {"pickup","dropoff","passengers","distance","fare","tip","tolls","total",
                    "color","payment","pickup_borough","pickup_zone","dropoff_borough","dropoff_zone"}
def validate_schema(df: pd.DataFrame) -> list[str]:
    missing = sorted(REQUIRED_COLUMNS.difference(df.columns))
    return [f"Missing required columns: {missing}"] if missing else []
def assert_schema(df: pd.DataFrame):
    errors = validate_schema(df)
    if errors:
        raise ValueError("; ".join(errors))
