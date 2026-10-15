from time import perf_counter
import pandas as pd, seaborn as sns
df=pd.concat([sns.load_dataset("taxis")]*20,ignore_index=True)
start=perf_counter(); df["calculated"]=df.fare+df.tip; elapsed=perf_counter()-start
print(f"Vectorized operation on {len(df):,} rows: {elapsed:.6f}s")
print("Memory bytes:",df.memory_usage(deep=True).sum(),"Benchmark depends on hardware and input.")
