import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
import numpy as np
dtf1=pd.read_excel("bisiklet_fiyatlari.xlsx")
print(dtf1)

print(dtf1.head())

sbn.pairplot(dtf1)
plt.show()
