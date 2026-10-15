import pandas as pd

def hourly_summary(df):
    return df.groupby("pickup_hour", dropna=False).agg(
        trip_records=("pickup_hour","size"), mean_fare=("fare","mean"),
        median_distance=("distance","median"), recorded_total_sum=("total","sum")
    ).reset_index().sort_values("pickup_hour", na_position="last").round(2)

def weekday_summary(df):
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    out = df.groupby("pickup_weekday", dropna=False).agg(
        trip_records=("pickup_weekday","size"), mean_fare=("fare","mean"),
        mean_distance=("distance","mean"), recorded_total_sum=("total","sum")
    ).reset_index()
    out["_order"] = out["pickup_weekday"].map({v:i for i,v in enumerate(order)})
    return out.sort_values("_order", na_position="last").drop(columns="_order").round(2)
