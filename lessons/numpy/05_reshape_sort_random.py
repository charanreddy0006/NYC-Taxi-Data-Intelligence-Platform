import numpy as np
x=np.arange(1,13)
print(x.reshape(3,4)); print("transpose\\n",x.reshape(3,4).T)
print("sort",np.sort([8,2,5,2,9])); print("unique/count",np.unique([1,1,2,3,3],return_counts=True))
print("repeatable",np.random.default_rng(42).integers(0,100,size=5))
