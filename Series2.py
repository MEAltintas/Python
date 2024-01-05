import pandas as pd
farkli=pd.Series([20,30,40,50],["a","b","c","d"])
farkli2=pd.Series([10,5,3,1],["a","c","f","g"])
toplam=farkli+farkli2
print(toplam)