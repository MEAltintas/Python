import pandas as pd
sozluk={
    "Meyve":["Elma","Portakal","Muz","Mandalina"],
    "Sebze":["Salatalık","Patlıcan","Biber","Kabak"],
    "Fiyat":[10,7,8,16]
}
dtf2=pd.DataFrame(sozluk)
print(dtf2)

dtf2.info()

print(dtf2.columns)

print(dtf2.describe())

dtf2=dtf2.set_index("Fiyat")
print(dtf2)