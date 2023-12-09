sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
toplam=0
for i in range(sayi1+1,sayi2):
    toplam+=i
print(toplam)