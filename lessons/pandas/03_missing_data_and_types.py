import pandas as pd, seaborn as sns
df=sns.load_dataset("taxis"); print(df.isna().sum()); print("duplicates",df.duplicated().sum())
for c in ["pickup","dropoff"]: df[c]=pd.to_datetime(df[c],errors="coerce")
for c in ["distance","fare","tip","tolls","total","passengers"]: df[c]=pd.to_numeric(df[c],errors="coerce")
print(df.dtypes); print("Missing is not automatically equivalent to zero.")
