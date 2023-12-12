import numpy as np
liste1=np.arange(2,8,0.5)
liste2=liste1.reshape((1,12))  # yeniden boyutlandırma
print(liste2)
print(liste2.shape)