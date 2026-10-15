import numpy as np
import pandas as pd
import pytest
from taxi_analytics.cleaning.cleaner import clean_taxi_data
from taxi_analytics.features.engineering import add_trip_features

def sample():
    return pd.DataFrame({
        "pickup":["2019-03-23 12:00:00","2019-03-23 13:00:00","2019-03-23 14:00:00"],
        "dropoff":["2019-03-23 12:15:00","2019-03-23 13:20:00","2019-03-23 13:50:00"],
        "passengers":[1,2,1],"distance":[2.5,4.0,0.0],"fare":[12.,18.,-2.],
        "tip":[2.,3.,np.nan],"tolls":[0.,0.,0.],"total":[14.8,21.8,-2.],
        "color":[" yellow ","yellow","green"],"payment":["card","card",None],
        "pickup_borough":["Manhattan","Manhattan","Queens"],"pickup_zone":["Midtown","Midtown",None],
        "dropoff_borough":["Manhattan","Brooklyn","Queens"],"dropoff_zone":["Uptown","North Side",None]
    })

def test_cleaning_preserves_rows_and_normalizes_text():
    clean=clean_taxi_data(sample())
    assert len(clean)==3
    assert clean.loc[0,"color"]=="yellow"
    assert "source_row_id" in clean

def test_features_and_safe_division():
    out=add_trip_features(clean_taxi_data(sample()))
    assert out.loc[0,"trip_duration_minutes"]==15
    assert out.loc[1,"trip_duration_minutes"]==20
    assert np.isnan(out.loc[2,"average_speed_mph"])
    assert out.loc[0,"tip_percent_of_fare"]==pytest.approx(100*2/12)
