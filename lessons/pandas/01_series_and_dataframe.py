import seaborn as sns
df=sns.load_dataset("taxis"); print(df.head()); print(df.shape); print(df.dtypes)
df.info(); print(df.describe(include="all").T); print(df.isna().sum())
