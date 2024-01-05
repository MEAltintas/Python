import pandas as pd
yarismaSonucu=pd.Series([10,5,1],["Ayşe","Fatma","Hayriye"])
print(yarismaSonucu)

yarismaSonucu2=pd.Series([20,10,8],["Ayşe","Fatma","Hayriye"])
print(yarismaSonucu2)

sonuc=yarismaSonucu+yarismaSonucu2
print(sonuc)

