import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

numpyDizisi=np.linspace(0,10,20)
print(numpyDizisi)

numpyDizisi2=numpyDizisi**3
print(numpyDizisi2)

plt.subplot(1,2,1)
plt.plot(numpyDizisi,numpyDizisi2,"r*-")
plt.subplot(1,2,2)
plt.plot(numpyDizisi2,numpyDizisi,"g--")
plt.show()