import pandas as pd
import matplotlib.pyplot as plt

movies_df=pd.read_csv('IMDB-Movie-Data.csv')

print(movies_df.describe())
print(movies_df.head(5))
movies_df.plot(kind='scatter',x="Rating",y='Revenue (Millions)')
plt.show()