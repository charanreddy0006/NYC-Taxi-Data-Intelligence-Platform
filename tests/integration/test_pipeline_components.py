import pandas as pd
from taxi_analytics.cleaning.cleaner import clean_taxi_data
from taxi_analytics.features.engineering import add_trip_features
from taxi_analytics.analytics.revenue import revenue_by_payment
from taxi_analytics.analytics.temporal import hourly_summary

def test_components_work_together():
    raw=pd.DataFrame({"pickup":["2019-03-23 12:00:00","2019-03-23 13:00:00"],
        "dropoff":["2019-03-23 12:15:00","2019-03-23 13:20:00"],"passengers":[1,2],
        "distance":[2.5,4.],"fare":[12.,18.],"tip":[2.,3.],"tolls":[0.,0.],"total":[14.8,21.8],
        "color":["yellow","green"],"payment":["card","cash"],"pickup_borough":["Manhattan","Queens"],
        "pickup_zone":["Midtown","Astoria"],"dropoff_borough":["Manhattan","Brooklyn"],
        "dropoff_zone":["Uptown","North Side"]})
    out=add_trip_features(clean_taxi_data(raw))
    assert revenue_by_payment(out)["trip_records"].sum()==2
    assert hourly_summary(out)["trip_records"].sum()==2
