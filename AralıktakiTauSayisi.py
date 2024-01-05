alt=int(input("Alt limit giriniz: "))
ust=int(input("Üst limit giriniz: "))

for i in range(alt,ust+1):
    sayac = 0
    for j in range(1,i+1):
        if(i%j==0):
            sayac+=1
    if(i%sayac==0):
        print(i)