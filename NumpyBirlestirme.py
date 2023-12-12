import numpy as np
f1=np.array([[1,2,3],[4,5,6]])
print(f1)
f2=np.array([[7,8,9]])
print('F2 shape:',f2.shape)
print(f2)

f3=np.concatenate((f1,f2),axis=0)
print(f3)