import pandas as pd
opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])
toplam=opel2018+opel2019
print(toplam)