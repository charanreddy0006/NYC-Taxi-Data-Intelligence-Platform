import seaborn as sns
df=sns.load_dataset("taxis")
print(df.groupby("payment",dropna=False).agg(records=("fare","size"),valid_fares=("fare","count"),
 mean_fare=("fare","mean"),median_fare=("fare","median"),recorded_total=("total","sum")).sort_values("records",ascending=False).round(2))
