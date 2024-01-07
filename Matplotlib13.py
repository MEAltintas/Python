import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
meyveKilo=[2,3,1,5,4,2,1]
meyveFiyat=[20,30,10,50,40,20,10]
plt.scatter(meyveKilo,meyveFiyat, color="green")
plt.xlabel("Meyvenin Kilosu")
pl.ylabel("Meyvenin Fiyatı")
plt.show()