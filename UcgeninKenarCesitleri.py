a=int(input("Birinci kenarı giriniz: "))
b=int(input("İkinci kenarı giriniz: "))
c=int(input("Üçüncü kenarı giriniz: "))
if(a==b and a==c):
    print("Eşkenar üçgendir")
elif(a==b or a==c):
    print("İkizkenar üçgendir")
else:
    print("Çeşitkenar üçgendir")