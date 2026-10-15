import numpy as np, seaborn as sns
df=sns.load_dataset("taxis"); x=df["distance"].dropna().to_numpy()
print("shape",x.shape,"ndim",x.ndim,"size",x.size,"dtype",x.dtype)
print("mean",x.mean(),"median",np.median(x),"min",x.min(),"max",x.max())
print("miles to km",np.round(x[:5]*1.60934,2))
