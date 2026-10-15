import seaborn as sns
df=sns.load_dataset("taxis")
print(df[["distance","fare","tip","total"]].head())
print(df.loc[df.distance.gt(5),["distance","fare","total"]].head())
print(df.sort_values("fare",ascending=False)[["distance","fare"]].head())
df["fare_plus_tip"]=df["fare"]+df["tip"]; print(df[["fare","tip","fare_plus_tip"]].head())
