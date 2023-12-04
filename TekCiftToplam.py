ctoplam=0
ttoplam=0
for i in range(1,11):
    if (i%2==0):
        ctoplam=ctoplam+i
    else:
        ttoplam=ttoplam+i
print("Çift sayı toplamı:",ctoplam,"Tek sayı toplamı:", ttoplam, sep="\n")