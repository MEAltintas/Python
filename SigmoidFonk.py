import numpy as np
n=int(input("Bir değer giriniz: "))
sigmoid=(1/(1+(np.exp(-n))))
print("Sigmoid Fonkisyonu: ",sigmoid)
