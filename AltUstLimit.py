altLimit=int(input("Alt limit giriniz: "))
ustLimit=int(input("Üst limit giriniz: "))
toplam=0
for i in range(altLimit,ustLimit):
    toplam+=i
print("Toplam: ",toplam)