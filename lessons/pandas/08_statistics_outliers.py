import seaborn as sns
df=sns.load_dataset("taxis"); print(df.select_dtypes(include="number").corr().round(2))
for c in ["distance","fare","tip","total"]:
 x=df[c].dropna(); q1,q3=x.quantile([.25,.75]); iqr=q3-q1
 print(c,"bounds",q1-1.5*iqr,q3+1.5*iqr,"flagged",int(((x<q1-1.5*iqr)|(x>q3+1.5*iqr)).sum()))
