def fibo(n):
    if (n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)

sayi=int(input("Sayı gir:"))
print(fibo(sayi))