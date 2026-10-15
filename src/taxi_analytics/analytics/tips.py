import numpy as np
def tip_summary(df):
    fare, tip = df["fare"], df["tip"]
    pct = np.divide((tip/fare*100).to_numpy(dtype=float, na_value=np.nan),
        np.ones(len(df)), out=np.full(len(df), np.nan),
        where=fare.to_numpy(dtype=float, na_value=np.nan)>0)
    work = df.assign(tip_percent_of_fare=pct)
    return work.groupby("payment", dropna=False).agg(
        trip_records=("tip","size"), known_tip_records=("tip","count"),
        mean_tip=("tip","mean"), median_tip=("tip","median"),
        mean_tip_percent_of_fare=("tip_percent_of_fare","mean")
    ).reset_index().sort_values("trip_records", ascending=False).round(2)
