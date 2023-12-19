import pandas as pd
s1=pd.Series([2,4,6,8])
s2=pd.Series(['c2','c4','c6','c8'])
s3=dict(one=s1, two=s2)
print(s3)
print(type(s3))

s4=pd.DataFrame(s3)
print(s4)
print(type(s4))