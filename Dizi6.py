uzunluk=int(input("Dizinin boyutunu giriniz: "))
dizi=[]
for i in range(uzunluk):
    elemanlar=int(input(f"Dizi [{i}]: " ))
    dizi.append(elemanlar)
print("Dizideki elemanlar")
for i in dizi:
    print(i)
sayac=0
for i in range(0,len(dizi)):
    for j in range(2,dizi[i]):
        if(dizi[i]%j==0):
            sayac+=1
    if(sayac==0):
        print("Asal sayılar: ",dizi[i])
    else:
        print("Asal olmayan sayılar: ",dizi[i])
        sayac=0