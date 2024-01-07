import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

yasListesi=[10,20,30,40,50,60,70,75,85,90]
kiloListesi=[20,60,80,85,86,87,70,90,95,90]
plt.plot(yasListesi,kiloListesi,color="b",linewidth=1.5,linestyle="--",marker="o",markerfacecolor="red",markersize=4)
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.title("Kilo/Yaş")
plt.show()