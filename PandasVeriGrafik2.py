import pandas as pd
import matplotlib.pyplot as plt
a1=pd.read_csv('iris.csv',header=None)  # bu excelin başlığı(headeri yok)
print(a1.head(5))
a2=pd.read_csv('iris.csv')  # bu şekilde yazılınca başlık olmasada başlığa girilen başlık gibi algılanır
print(a2.head(5))