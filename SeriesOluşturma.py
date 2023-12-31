import pandas as pd

data=[15,18,21,24]
index=["İç Anadolu","Doğu Anadolu","Ege","Akdeniz"]
seri1=pd.Series(data,index)
print(seri1)

sozluk={
    1:"Aksaray",
    2:"Diyarbakır",
    3:"Denizli",
    4:"Antalya"
}
seri2=pd.Series(sozluk)
print(seri2)