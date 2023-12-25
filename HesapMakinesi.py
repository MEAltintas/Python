def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    return a / b

print("Fonksiyonlar ile Hesap Makinesi")

a = float(input("ilk sayı: "))
b = float(input("ikinci sayı: "))

print("Toplama sonucu: ", topla(a,b))
print("Çıkarma sonucu: ", cikar(a,b))
print("Çarpma sonucu: ", carp(a,b))
print("Bölme sonucu: ", bol(a,b))