import pandas as pd, seaborn as sns
df=sns.load_dataset("taxis")
for c in ["pickup","dropoff"]: df[c]=pd.to_datetime(df[c],errors="coerce")
df["duration_minutes"]=(df.dropoff-df.pickup).dt.total_seconds()/60
df["pickup_hour"]=df.pickup.dt.hour; df["weekday"]=df.pickup.dt.day_name()
df["payment_clean"]=df.payment.astype("string").str.strip().str.title()
print(df[["pickup","dropoff","duration_minutes","pickup_hour","weekday"]].head())
