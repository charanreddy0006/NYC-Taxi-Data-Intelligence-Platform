import pandas as pd, seaborn as sns
df=sns.load_dataset("taxis")
print(pd.crosstab(df.pickup_borough,df.payment,margins=True))
print(pd.pivot_table(df,index="pickup_borough",columns="color",values="fare",aggfunc="mean"))
df["payment_mean_fare"]=df.groupby("payment").fare.transform("mean")
print(df[["payment","fare","payment_mean_fare"]].head())
print(df[["distance","fare","tip","total"]].melt(var_name="metric",value_name="value").head())
