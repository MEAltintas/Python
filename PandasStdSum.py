t4={'a1':10,'a2':20,'a3':30}  # sözlük
t5=pd.Series(t4)
print(t5)


print(t5.sum())
print(t5.std())
print(t5.median())
print(t5+t5)
print(t5*2)
print(t5*t5)
print(t5.values)
print(t5.index)