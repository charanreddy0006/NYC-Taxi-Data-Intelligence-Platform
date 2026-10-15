from datetime import datetime, timezone
import logging
from taxi_analytics.config import load_config, resolve_path
from taxi_analytics.logging_config import configure_logging
from taxi_analytics.ingestion.loader import load_taxi_dataset
from taxi_analytics.profiling.profiler import profile_dataframe, save_profile
from taxi_analytics.validation.schema import assert_schema
from taxi_analytics.validation.quality_checks import build_quality_report
from taxi_analytics.cleaning.cleaner import clean_taxi_data
from taxi_analytics.features.engineering import add_trip_features
from taxi_analytics.analytics.revenue import revenue_by_payment, fare_distance_summary
from taxi_analytics.analytics.temporal import hourly_summary, weekday_summary
from taxi_analytics.analytics.geographic import pickup_borough_summary, top_routes
from taxi_analytics.analytics.tips import tip_summary
from taxi_analytics.analytics.statistics import numeric_correlation, iqr_outlier_report
from taxi_analytics.reporting.tables import write_csv_reports, write_json
from taxi_analytics.reporting.charts import generate_charts

log=logging.getLogger(__name__)

def _load(config_path=None):
    cfg=load_config(config_path)
    raw_dir=resolve_path(cfg["paths"]["raw_dir"])
    reports=resolve_path(cfg["paths"]["reports_dir"])
    logs=resolve_path(cfg["paths"]["logs_dir"])
    configure_logging(logs)
    raw=load_taxi_dataset(raw_dir/cfg["dataset"]["filename"])
    assert_schema(raw)
    return cfg,raw,reports

def execute_pipeline(config_path=None, generate_charts_flag=None, refresh=False):
    cfg,raw,reports_dir=_load(config_path)
    if refresh:
        raw_dir=resolve_path(cfg["paths"]["raw_dir"])
        raw=load_taxi_dataset(raw_dir/cfg["dataset"]["filename"], refresh=True)
        assert_schema(raw)
    profile=profile_dataframe(raw)
    save_profile(profile,reports_dir/"data_profile.json")
    enriched=add_trip_features(clean_taxi_data(raw))
    quality=build_quality_report(raw,enriched)
    reports={
        "data_quality_report":quality,
        "revenue_by_payment":revenue_by_payment(enriched),
        "fare_distance_summary":fare_distance_summary(enriched),
        "hourly_trip_summary":hourly_summary(enriched),
        "weekday_summary":weekday_summary(enriched),
        "pickup_borough_summary":pickup_borough_summary(enriched),
        "top_routes":top_routes(enriched,int(cfg.get("reporting",{}).get("top_routes_limit",20))),
        "tip_summary":tip_summary(enriched),
        "numeric_correlations":numeric_correlation(enriched),
        "iqr_outlier_summary":iqr_outlier_report(enriched),
    }
    reports_dir.mkdir(parents=True,exist_ok=True)
    enriched.to_csv(reports_dir/"trip_features.csv",index=False)
    write_csv_reports(reports,reports_dir)
    make_charts=cfg.get("reporting",{}).get("generate_charts",True)
    if generate_charts_flag is not None: make_charts=generate_charts_flag
    charts=generate_charts(enriched,reports_dir/"figures") if make_charts else []
    summary={"project":cfg["project"]["name"],"completed_at_utc":datetime.now(timezone.utc).isoformat(),
        "source":"Seaborn taxis dataset","raw_rows":len(raw),"raw_columns":len(raw.columns),
        "missing_cells":int(raw.isna().sum().sum()),"duplicate_full_rows":int(raw.duplicated().sum()),
        "cleaning_policy":"Conservative type parsing and text normalization; rows retained and flagged.",
        "reports":[f"{n}.csv" for n in reports],"charts":charts}
    write_json(summary,reports_dir/"run_summary.json")
    log.info("Pipeline complete. Outputs: %s",reports_dir)
    return {"profile":profile,"enriched":enriched,"reports":reports,"summary":summary}

def run_profile(config_path=None):
    cfg,raw,reports=_load(config_path)
    profile=profile_dataframe(raw); save_profile(profile,reports/"data_profile.json")
    print(f"Profile saved: {reports/'data_profile.json'}")
    return profile

def run_validation(config_path=None):
    cfg,raw,reports=_load(config_path)
    result=build_quality_report(raw); reports.mkdir(parents=True,exist_ok=True)
    result.to_csv(reports/"data_quality_report.csv",index=False)
    print(result.to_string(index=False)); return result
