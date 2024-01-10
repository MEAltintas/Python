import pandas as pd


dtf1=pd.read_csv("IMDB-Movie-Data.csv")
print(dtf1.info)
print(dtf1.columns)
print(dtf1)
print(dtf1.head())
print(dtf1.head(10))
print(dtf1.tail())
print(dtf1.tail(10))
print(dtf1["Title"])
print(dtf1["Title"].head())
print(dtf1[["Title","Rating"]].head())
print(dtf1[["Title","Rating"]].tail(7))
print(dtf1[5:][["Title","Rating"]])
print(dtf1[dtf1["Rating"] >= 8.0 ][["Title","Rating"]].head(50))
print(dtf1[(dtf1["Year"]>=2014) & (dtf1["Year"]<=2015)][["Title","Rating"]])
print(dtf1[(dtf1["Revenue (Millions)"]>100.000) | ((dtf1["Rating"]>=8 & (dtf1["Rating"]>9)))].head())
