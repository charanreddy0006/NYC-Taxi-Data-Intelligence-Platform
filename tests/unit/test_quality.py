import pandas as pd
from taxi_analytics.validation.schema import validate_schema
from taxi_analytics.validation.quality_checks import build_quality_report

def test_schema_detects_missing_columns():
    errors=validate_schema(pd.DataFrame({"distance":[1]}))
    assert errors and "pickup" in errors[0]

def test_quality_flags_invalid_duration_and_values():
    df=pd.DataFrame({"pickup":["2020-01-02","2020-01-01"],"dropoff":["2020-01-01","2020-01-02"],
        "distance":[-1,0],"fare":[-2,5],"tip":[0,1],"tolls":[0,0],"total":[-2,6],"passengers":[1,2]})
    report=build_quality_report(df).set_index("check")["flagged_count"]
    assert report["negative_duration"]==1
    assert report["nonpositive_distance"]==2
    assert report["negative_fare"]==1
