import pandas as pd

def build_quality_report(df: pd.DataFrame, enriched=None) -> pd.DataFrame:
    rows = []
    def add(check, count, severity, description):
        rows.append({"check": check, "flagged_count": int(count), "severity": severity, "description": description})
    add("duplicate_full_rows", df.duplicated().sum(), "warning", "Exact duplicate rows; investigate before removal.")
    for col in df.columns:
        if df[col].isna().any():
            add(f"missing:{col}", df[col].isna().sum(), "info", f"Missing values in {col}.")
    if {"pickup","dropoff"}.issubset(df.columns):
        pickup, dropoff = pd.to_datetime(df["pickup"], errors="coerce"), pd.to_datetime(df["dropoff"], errors="coerce")
        duration = (dropoff-pickup).dt.total_seconds()/60
        add("invalid_pickup_timestamp", pickup.isna().sum(), "warning", "Pickup missing or unparsable.")
        add("invalid_dropoff_timestamp", dropoff.isna().sum(), "warning", "Drop-off missing or unparsable.")
        add("negative_duration", duration.lt(0).sum(), "warning", "Drop-off precedes pickup.")
        add("duration_over_6_hours", duration.gt(360).sum(), "warning", "Duration over six hours; review.")
    for col in ["distance","fare","tip","tolls","total","passengers"]:
        if col in df:
            val = pd.to_numeric(df[col], errors="coerce")
            add(f"unparseable_or_missing:{col}", val.isna().sum(), "info", f"Missing or unparseable {col}.")
    if "distance" in df:
        add("nonpositive_distance", pd.to_numeric(df["distance"], errors="coerce").le(0).sum(), "warning", "Non-positive distance.")
    if "fare" in df:
        add("negative_fare", pd.to_numeric(df["fare"], errors="coerce").lt(0).sum(), "warning", "Negative fare.")
    if enriched is not None and "average_speed_mph" in enriched:
        add("speed_over_100_mph", enriched["average_speed_mph"].gt(100).sum(), "warning", "Derived speed above 100 mph; review.")
    return pd.DataFrame(rows, columns=["check","flagged_count","severity","description"])
