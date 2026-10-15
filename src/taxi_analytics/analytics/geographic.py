def pickup_borough_summary(df):
    return df.groupby("pickup_borough", dropna=False).agg(
        trip_records=("pickup_borough","size"), unique_pickup_zones=("pickup_zone","nunique"),
        mean_fare=("fare","mean"), mean_distance=("distance","mean"),
        recorded_total_sum=("total","sum")
    ).reset_index().sort_values("trip_records", ascending=False).round(2)

def top_routes(df, limit=20):
    cols = ["pickup_borough","pickup_zone","dropoff_borough","dropoff_zone"]
    return df.groupby(cols, dropna=False).agg(
        trip_records=("distance","size"), mean_distance=("distance","mean"),
        mean_fare=("fare","mean"), mean_duration_minutes=("trip_duration_minutes","mean")
    ).reset_index().sort_values("trip_records", ascending=False).head(limit).round(2)
