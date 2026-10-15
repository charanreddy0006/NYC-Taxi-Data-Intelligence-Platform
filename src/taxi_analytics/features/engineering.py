import numpy as np
import pandas as pd

def add_trip_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    pickup = pd.to_datetime(out["pickup"], errors="coerce")
    dropoff = pd.to_datetime(out["dropoff"], errors="coerce")
    out["trip_duration_minutes"] = (dropoff-pickup).dt.total_seconds()/60
    out["pickup_hour"] = pickup.dt.hour.astype("Int64")
    out["pickup_weekday"] = pickup.dt.day_name().astype("string")
    out["pickup_date"] = pickup.dt.date
    out["is_weekend"] = pickup.dt.dayofweek.isin([5,6]).astype("boolean")
    distance = pd.to_numeric(out["distance"], errors="coerce")
    fare = pd.to_numeric(out["fare"], errors="coerce")
    tip = pd.to_numeric(out["tip"], errors="coerce")
    duration_hours = out["trip_duration_minutes"]/60
    out["average_speed_mph"] = np.divide(
        distance.to_numpy(dtype=float, na_value=np.nan),
        duration_hours.to_numpy(dtype=float, na_value=np.nan),
        out=np.full(len(out), np.nan),
        where=duration_hours.to_numpy(dtype=float, na_value=np.nan)>0)
    out["tip_percent_of_fare"] = np.divide(
        (tip/fare*100).to_numpy(dtype=float, na_value=np.nan),
        np.ones(len(out)), out=np.full(len(out), np.nan),
        where=fare.to_numpy(dtype=float, na_value=np.nan)>0)
    tolls = pd.to_numeric(out["tolls"], errors="coerce").fillna(0)
    total = pd.to_numeric(out["total"], errors="coerce")
    out["total_minus_fare_tip_tolls"] = total - (
        fare.fillna(0) + tip.fillna(0) + tolls)
    out["duration_flag"] = np.select(
        [out["trip_duration_minutes"].isna(), out["trip_duration_minutes"].lt(0),
         out["trip_duration_minutes"].gt(360)],
        ["invalid_timestamp", "negative_duration", "over_6_hours"], default="review_range")
    out["distance_flag"] = np.select([distance.isna(), distance.le(0)],
        ["missing_distance", "nonpositive_distance"], default="positive_distance")
    out["speed_flag"] = np.select([out["average_speed_mph"].isna(), out["average_speed_mph"].gt(100)],
        ["not_calculable", "over_100_mph_review"], default="review_range")
    return out
