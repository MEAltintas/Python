import matplotlib.pyplot as plt
sehirler=['Aksaray','Kırıkkale','Burdur','Ankara']
sicaklik=[33,12,5,9]
plt.bar(sehirler,sicaklik)
plt.xlabel('Şehirler',fontsize=16)  #fontsize yazının boyutunu büyütür.
plt.ylabel('Sıcaklıklar')
plt.show()
