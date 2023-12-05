def kabarcik(dizi):
    sayac=0
    for indis in range(len(dizi)-1):
        if(dizi[indis]>dizi[indis+1]):
            dizi[indis],dizi[indis+1]=dizi[indis+1],dizi[indis]
            sayac+=1
    if(sayac==0):
        return dizi
    else:
        return kabarcik(dizi)

liste=[3,5,7,1,2,9]
print(kabarcik(liste))