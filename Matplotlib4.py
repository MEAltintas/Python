import matplotlib.pyplot as plt
x6=np.arange(-10,10,0.1)
y6_1=x6**2
y6_2=-x6**2
plt.plot(x6,y6_1,'r*')   # r=red yıldız koyar ,rd yazarsak baklava dilimi koyar.
# color='pink',marker='d',markersize=3,linewidth=8,markerfacecolor='none' açıklama altta
# yazarakta rengini pembe ve şeklini baklava dilimi baklava diliminin boyutunu 3 kalınlığı 8 içinide boş yapar.
plt.plot(x6,y6_2,'b-.')  # b=blue bir çizgi bir nokta koyar, bo-yapsak daire ve çizgi koyar
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.legend(['x^2 eğrisi','-x^2 eğrisi'])
plt.xlim(-5,5)
plt.ylim(-30,30)
plt.title('Grafik')
plt.show()