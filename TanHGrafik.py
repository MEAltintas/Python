import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plt.plot(x,y,color="r")
plt.title("Tanh Optimizasyon Grafiği")
plt.xlabel("x koordinatı")
plt.ylabel("y koordinatı")
plt.axhline(0)
plt.axvline(0)
plt.show()
