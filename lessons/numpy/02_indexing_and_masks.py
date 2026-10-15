import numpy as np
x=np.array([0.5,1.2,2.5,0.0,8.4,3.1])
print(x[0],x[-1],x[1:4],x[::2])
print("positive",x[x>0]); print("long",x[x>=3])
print(np.where(x>=3,"long","short"))
