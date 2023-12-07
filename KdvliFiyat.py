urunfiyat=float(input("Ürünün fiyatını giriniz: "))
kdv=float(input("KDV giriniz: "))
kdv=(urunfiyat*kdv)/100
sonuc=float(urunfiyat+kdv)
print("Sonuç: ",sonuc)