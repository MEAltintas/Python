import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,4*np.pi,0.1)  # 0 ile 4pi arasında 0.1 aralıklarla oluşturur
y=np.sin(x)
plt.plot(x,y)
plt.show()
