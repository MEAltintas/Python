def tam(sayi1,sayi2):
    if(sayi1%sayi2==0):
        return True
    else:
        return False
n1=int(input("Birinci sayıyı gir: "))
n2=int(input("İkinci sayıyı gir: "))
if(tam(n1,n2)==True):
    print("Bölünür")
else:
    print("Bölünmez")