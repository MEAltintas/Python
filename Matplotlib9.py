import matplotlib.pyplot as plt
veri4=[2,5,8,9,6,7,44,3,22,22,22,67,56,67,9,5,7,56,44,6,56,444]
veri5=[3,7,14,20,188]
plt.boxplot([veri4,veri5],labels=['Original','Predicted'])
plt.show()