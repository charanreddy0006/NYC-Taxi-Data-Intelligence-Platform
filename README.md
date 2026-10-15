# NYC Taxi Data Intelligence Platform
**A production-style NumPy & pandas learning project using Seaborn's `taxis` dataset.**

This repository combines beginner-to-advanced lessons with a modular data analytics pipeline:
- Seaborn dataset ingestion with local CSV caching
- Dataset profiling and schema validation
- Conservative cleaning and auditable quality flags
- Vectorized feature engineering with NumPy/pandas
- Fare, tips, time, borough, route, correlation, and outlier analysis
- CSV reports and PNG charts
- Config files, logging, CLI, tests, notebook, and GitHub Actions

> This is a production-style learning project, not a claim of production deployment or large-scale capacity. The Seaborn dataset is a teaching sample. The first run needs internet access unless `data/raw/taxis.csv` is already present.

## Quick start (Windows / VS Code)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e ".[dev]"
taxi-analytics run
```
If PowerShell activation is blocked, use Command Prompt: `.venv\\Scripts\\activate.bat`.

Other commands:
```bash
taxi-analytics profile
taxi-analytics validate
taxi-analytics run --no-charts
pytest
```
Or run `python -m taxi_analytics.cli run` from the repository root.

## Learning lessons
```bash
python lessons/numpy/01_array_fundamentals.py
python lessons/numpy/02_indexing_and_masks.py
python lessons/numpy/03_vectorization_and_broadcasting.py
python lessons/numpy/04_aggregation_and_statistics.py
python lessons/numpy/05_reshape_sort_random.py
python lessons/numpy/06_advanced_numeric_patterns.py
python lessons/pandas/01_series_and_dataframe.py
python lessons/pandas/02_selection_filtering.py
python lessons/pandas/03_missing_data_and_types.py
python lessons/pandas/04_groupby_aggregation.py
python lessons/pandas/05_merge_join_concat.py
python lessons/pandas/06_datetime_strings.py
python lessons/pandas/07_reshape_pivot_transform.py
python lessons/pandas/08_statistics_outliers.py
python lessons/pandas/09_performance_memory.py
```

## Architecture
```text
Seaborn dataset -> local raw cache -> profile/schema validation
 -> cleaning & quality flags -> feature engineering
 -> analytical modules -> CSV reports + PNG charts + logs
```

## Output reports
The pipeline writes `reports/` files: `data_profile.json`, `data_quality_report.csv`,
`trip_features.csv`, `revenue_by_payment.csv`, `fare_distance_summary.csv`,
`hourly_trip_summary.csv`, `weekday_summary.csv`, `pickup_borough_summary.csv`,
`top_routes.csv`, `tip_summary.csv`, `numeric_correlations.csv`,
`iqr_outlier_summary.csv`, `run_summary.json`, plus figures in `reports/figures/`.

## Data quality principles
- Preserve source rows; flag suspicious observations instead of silently deleting them.
- Missing tips are not assumed to be confirmed zero tips.
- Ratios are only calculated with valid non-zero denominators.
- IQR flags are review candidates, not proof of errors.
- Correlation is not causation.
- Do not infer production-scale performance from this small sample.

## Repository structure
See `src/taxi_analytics/` for the pipeline modules, `lessons/` for the curriculum,
`notebooks/` for interactive exploration, `tests/` for automated checks, and `configs/`
for runtime settings.
