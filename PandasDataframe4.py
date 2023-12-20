import pandas as pandas
turkce=pd.Series(["bir","iki","üç","dört","beş","altı","yedi"])
ingilizce=(["one","two","three","four","five","six","seven"])
sozluk=dict(one=turkce,two=ingilizce)
szlk=pd.DataFrame(data=ingilizce,index=turkce)
print(szlk)