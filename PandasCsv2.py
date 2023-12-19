import pandas as pd
movies_df=pd.read_csv('IMDB-Movie-Data.csv',index_col='Title') # title bölümünü index yaptık
print(movies_df.columns)
print(df1.head())
print(df1.tail(7))