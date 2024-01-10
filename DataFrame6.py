import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5)
dtf1=pd.DataFrame(data,columns=["Col1","Col2","Col3","Col4","Col5"])
print(dtf1)

print(dtf1.head())
print(dtf1.tail(3))

print(dtf1["Col1"].head())
print(dtf1.Col3.head(2))