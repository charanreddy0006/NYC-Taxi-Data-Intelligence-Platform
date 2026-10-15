import json
from pathlib import Path
import pandas as pd

def profile_dataframe(df: pd.DataFrame) -> dict:
    return {
        "row_count": int(len(df)), "column_count": int(len(df.columns)),
        "columns": [{"name": str(c), "dtype": str(df[c].dtype),
                     "missing_count": int(df[c].isna().sum()),
                     "missing_percent": round(float(df[c].isna().mean()*100), 3),
                     "unique_non_null": int(df[c].nunique(dropna=True))} for c in df.columns],
        "duplicate_full_rows": int(df.duplicated().sum()),
        "memory_usage_bytes": int(df.memory_usage(deep=True).sum())
    }
def save_profile(profile: dict, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(profile, indent=2), encoding="utf-8")
