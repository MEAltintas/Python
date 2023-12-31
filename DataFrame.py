import pandas as pd
data=["İç Anadolu","Doğu Anadolu","Ege","Akdeniz"]
seri1=pd.Series(data)

data2=["Aksaray","Diyarbakır","Denizli","Antalya"]
seri2=pd.Series(data2)
birlestir=dict(Bölge=seri1,Şehir=seri2)

dtf1=pd.DataFrame(birlestir)
print(dtf1)