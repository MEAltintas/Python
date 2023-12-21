import matplotlib.pyplot as plt
veri2=[2,5,8,9,6,7,44,3,22,22,22,67,56,67,9,5,7,56,44,6,56]
plt.hist(veri2,bins=30,range=[1,25],color='blue',alpha=0.25)  # bins=30 kutucuğa ayırmaya çalışır(kaç girersen ona ayırır). Alpha saydamlık verir.
plt.show()