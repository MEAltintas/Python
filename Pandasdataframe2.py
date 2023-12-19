import pandas as pd
b1={'isim':['ali','veli','adnan'],'yas':[20,22,24],'numara':[2,4,6]}
b2=pd.DataFrame(data=b1,index=['z1','z2','z3'])
print(b2)
b2=b2.set_index('numara')
print(b2)
print(b2.values)
print(b2.columns)