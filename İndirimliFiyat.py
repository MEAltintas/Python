fiyat=int(input("Ürünün fiyatı: "))
indirim=int(input("Yüzdelik İndirim: "))
def urun(f1,i1):
    ucret=f1-((f1*i1)/100)
    return ucret
print(urun(fiyat,indirim))