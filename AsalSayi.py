sayi=int(input("Sayı giriniz: "))
def asalMi(n):
    sayac=0
    for i in range(2,n):
        if(n%i==0):
            sayac=1
    if sayac==0:
        return True
    else: 
        return False
if asalMi(sayi)==True:
    print("Asal")
else:
    print("Asal değil")