import numpy as np
fare=np.array([8.5,12,22.5,40]); tip=np.array([1.5,2,4.5,6])
print("fare + tip",fare+tip)
print("10% scenario",fare*1.10)
print("tip %",np.divide(tip,fare,out=np.full_like(tip,np.nan),where=fare!=0)*100)
counts=np.array([[10,20,30],[15,25,35],[9,18,27]])
print("broadcast difference\\n",counts-np.array([12,22,32]))
