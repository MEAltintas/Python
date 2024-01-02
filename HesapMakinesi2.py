def hesapla(a,b,islem):
    if (islem not in "+-*/"):
        return "Lütfen şu işlemlerden birini seçiniz: +-*/"
    if (islem=="+"):
        return (str(a)," + ",str(b)," = ",str(a+b))
    if (islem=="-"):
        return (str(a)," - ",str(b)," = ",str(a-b))
    if (islem=="*"):
        return (str(a)," * ",str(b)," = ",str(a*b))
    if (islem=="/"):
        return (str(a)," / ",str(b)," = ",str(a/b))

while True:
    try:
        a=int(input("İlk sayıyı giriniz: "))
        b=int(input("İkinci sayıyı giriniz: "))
        islem=input("İşleminizi seçiniz: +-*/ = ")
    except:
        print("Lütfen geçerli sayı giriniz!")
