boyut=int(input("Dizinin boyutunu giriniz: "))
dizi=[]
for i in range(boyut):
    eleman=int(input(f"Dizi [{i}]: "))
    dizi.append(eleman)
print("Dizideki elemanlar")
for i in dizi:
    print(i)