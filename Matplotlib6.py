import matplotlib.pyplot as plt
import numpy as np

veri=[100,333,23,980,57]
isim=['Aksaray','Kırıkkale','Burdur','İstanbul','Ankara']
plt.barh(isim,veri,color=[0.6,0.7,0.9])
plt.show()