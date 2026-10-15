import numpy as np
x=np.array([2.,4,5,7,100]); z=(x-x.mean())/x.std()
q1,q3=np.percentile(x,[25,75]); iqr=q3-q1; mask=(x<q1-1.5*iqr)|(x>q3+1.5*iqr)
print("z",np.round(z,2),"IQR flags",x[mask])
print("safe divide",np.divide([2.,4,5],[2.,0,5],out=np.full(3,np.nan),where=np.array([2.,0,5])!=0))
