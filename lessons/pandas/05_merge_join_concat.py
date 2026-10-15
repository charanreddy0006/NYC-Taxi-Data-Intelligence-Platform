import pandas as pd
a=pd.DataFrame({"zone_id":[1,2,3],"trips":[10,20,30]})
b=pd.DataFrame({"zone_id":[1,2,3],"zone_label":["A","B","C"]})
print(a.merge(b,on="zone_id",validate="one_to_one"))
print(pd.concat([a.iloc[:2],a.iloc[2:]],ignore_index=True))
print("Illustrative lookup only; do not invent lookup values in the real analysis.")
