sayi=int(input("Tahmin edilecek sayıyı giriniz: "))
sayac=0
for i in range(3):
    tahmin=int(input("Tahmin ettiğiniz sayıyı giriniz: "))
    if(sayi==tahmin):
        print(i+1,". Tahminde bildiniz")
        sayac=1
if (sayac==0):
    print("Doğru tahmin yapamadınız")