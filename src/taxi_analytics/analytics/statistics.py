import numpy as np
import pandas as pd

def numeric_correlation(df):
    cols = [c for c in ["passengers","distance","fare","tip","tolls","total"] if c in df]
    corr = df[cols].corr(numeric_only=True)
    corr.index.name = "feature"
    return corr.reset_index().round(3)

def iqr_outlier_report(df, columns=None, multiplier=1.5):
    rows=[]
    for col in columns or ["distance","fare","tip","total"]:
        if col not in df: continue
        x = pd.to_numeric(df[col], errors="coerce").dropna()
        if x.empty:
            rows.append({"column":col,"q1":np.nan,"q3":np.nan,"iqr":np.nan,
                         "lower_bound":np.nan,"upper_bound":np.nan,"flagged_count":0})
            continue
        q1,q3=x.quantile([.25,.75]); iqr=q3-q1
        lo,hi=q1-multiplier*iqr,q3+multiplier*iqr
        rows.append({"column":col,"q1":q1,"q3":q3,"iqr":iqr,"lower_bound":lo,
                     "upper_bound":hi,"flagged_count":int(((x<lo)|(x>hi)).sum())})
    return pd.DataFrame(rows).round(3)
