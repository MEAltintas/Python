from random import randint
rand=randint(1,100)
for i in range(8):
    sayi=int(input("Sayı giriniz: "))
    if(sayi>rand):
        print("Aşağı in")
    elif (sayi<rand):
        print("Yukarı çık")
    else:
        print("Doğru tahmin")
        break