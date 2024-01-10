import pandas as pd
import numpy as np
from numpy.random import randn

dtf=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Col1","Col2","Col3"])


print(dtf)
print(dtf["Col1"])
print(dtf[["Col1","Col2"]])
print(dtf[:])
print(dtf.loc["A"])
print(dtf.iloc[:2])
print(dtf.loc[:,"Col3"])
print(dtf.loc[:,"Col1":"Col3"])
print(dtf.loc["A","Col3"])
print(dtf.loc[["A","B"],["Col1"]])

dtf["Col4"]=pd.Series(randn(3),["A","B","C"])
print(dtf)

dtf["Col5"]=dtf["Col1"]+dtf["Col4"]
print(dtf)