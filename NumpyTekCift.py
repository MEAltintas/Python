import numpy as np
dizi=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
cift=dizi[dizi%2==0]
print(cift)
tek=dizi[dizi%2!=0]
print(tek)