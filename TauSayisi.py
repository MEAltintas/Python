sayi=int(input("Bir sayı giriniz: "))
sayac=0
for i in range(1,sayi+1):
    if(sayi%i==0):
        sayac+=1

if(sayi%sayac==0):
    print("Tau sayısıdır.")
else:
    print("Tau sayısı değildir.")