import pandas as pd
ilkIndexler=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
icIndexler=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
birlestir=list(zip(ilkIndexler,icIndexler))
print(birlestir)
birlestir=pd.MultiIndex.from_tuples(birlestir)
print(birlestir)