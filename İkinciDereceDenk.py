a=int(input("A değeri: "))
b=int(input("B değeri: "))
c=int(input("C değeri: "))
delta=b**2-4*a*c
if (delta<0):
    print("Reel kök yoktur.")
elif (delta==0):
    x=-b/(2*a)
    print("Denklemin kökü: ",x)
else:
    x1=(-b+(delta**1/2))/(2*a)
    x2 = (-b - (delta ** 1 / 2)) / (2 * a)
    print("Birinci Kök:",x1,"İkinci Kök:",x2,sep="\n")