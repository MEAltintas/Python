class SuperKahraman():
    def __init__(self,isimInput,yasInput,meslekInput):
        print("__init__ çağırıldı!")
        self.isim=isimInput
        self.yas=yasInput
        self.meslek=meslekInput

superman=SuperKahraman("Süperman",30,"Gazeteci")
superman.isim="Clark Kent"
print(superman.isim)