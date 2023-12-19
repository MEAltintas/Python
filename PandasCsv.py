import pandas as pd

df1=pd.read_csv('googleplaystore.csv')
print(df1.shape)
print(df1.dtypes)
print(type(df1))
print(df1.columns)