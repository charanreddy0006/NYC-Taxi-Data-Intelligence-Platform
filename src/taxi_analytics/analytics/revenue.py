import pandas as pd

def revenue_by_payment(df):
    return df.groupby("payment", dropna=False).agg(
        trip_records=("fare","size"), valid_fares=("fare","count"),
        recorded_fare_sum=("fare","sum"), mean_fare=("fare","mean"),
        median_fare=("fare","median"), recorded_total_sum=("total","sum")
    ).reset_index().sort_values("trip_records", ascending=False).round(2)

def fare_distance_summary(df):
    work = df.loc[df["distance"].gt(0) & df["fare"].notna()].copy()
    bins = [0,1,3,5,10,20,float("inf")]
    labels = ["(0,1]","(1,3]","(3,5]","(5,10]","(10,20]","20+"]
    work["distance_band"] = pd.cut(work["distance"], bins=bins, labels=labels)
    return work.groupby("distance_band", observed=False).agg(
        trip_records=("fare","size"), mean_fare=("fare","mean"),
        median_fare=("fare","median"), mean_distance=("distance","mean")
    ).reset_index().round(2)
