import numpy as np
x=np.array([[8.5,12,14],[9,11,20],[7,15,18]],float)
print("column means",x.mean(axis=0)); print("row means",x.mean(axis=1))
print("percentiles",np.percentile(x,[25,50,75])); print("std",x.std())
print("correlation\\n",np.corrcoef(x,rowvar=False))
