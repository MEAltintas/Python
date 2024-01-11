import numpy as np
import pandas as pd
data=np.random.randint(10,100,15).reshape(5,3)
dtf1=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["Col1","Col2","Col3"])
dtf1=dtf1.reindex(["a","b","c","d","e","f","g","h"])
print(dtf1.fillna(value="Değeri Yok"))
