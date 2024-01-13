import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x=np.linspace(-10,10,100)
y=1/(1+np.exp(-x))
plt.plot(x,y)
plt.axvline(0)
plt.axhline(0.5)

plt.show()
