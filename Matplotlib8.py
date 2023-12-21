import matplotlib.pyplot as plt
veri3=[3,7,14,20]
plt.pie(veri3,explode=[0,0,0.3,0],autopct='%%%.2f',shadow=0.9)  
plt.legend(['3','7','14','20'])
plt.show()