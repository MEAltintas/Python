import pandas as pd
t1=np.array([2,4,6,8,10])
ind=['a','b','c','d','e']
t3=pd.Series(data=t1,index=ind)
t2=pd.Series(t1,dtype=np.uint8)    # pandasa numpy dtype girilebilir aynı şekilde çalışır
print(t2)
print(type(t2))
print(t3)