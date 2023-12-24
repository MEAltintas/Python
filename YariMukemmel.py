sayi1=int(input("Bir sayı giriniz: "))
sayi2=int(input("Bir sayı daha giriniz: "))
for i in range(sayi1,sayi2):
    sayac=0
    toplam=0
    for j in range(i-1,1,-1):
        if(sayac<3):
            if(i%j==0):
                toplam+=j
                sayac+=1
    if(toplam==i):
        print(i)