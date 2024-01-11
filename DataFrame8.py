import pandas as pd
import numpy as np

dtf1=pd.read_csv("IMDB-Movie-Data.csv")
print("İlk 10 kayıt:  ",dtf1.head(10))
print("Sütunları:  ",dtf1.columns)

print("Toplam kayıt sayısı:  ",dtf1.count().sum())
print("Rating ortalaması:  ",dtf1["Rating"].mean())
print("En yüksek rating:  ",dtf1["Rating"].max())
print("En yüksek rating adı:  ",dtf1[dtf1["Rating"]==dtf1["Rating"].max()]["Title"].iloc[0])
print("Title göre Rating ortalaması:  " )