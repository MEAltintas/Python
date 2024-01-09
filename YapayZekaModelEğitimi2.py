import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

dtf1=pd.read_excel("merc.xlsx")
print(dtf1)
print(dtf1.count())
print(dtf1.isnull())
print(dtf1.isnull().sum())
sbn.displot(dtf1["price"])
#plt.show()
plt.clf()
plt.close()

sbn.scatterplot(x="mileage",y="price",data=dtf1)
#plt.show()
plt.clf()
plt.close()

doksanDokuz=dtf1.sort_values("price",ascending=False).iloc[131:]
print(doksanDokuz.describe())

sbn.displot(doksanDokuz["price"])
#plt.show()
plt.clf()
plt.close()

print(dtf1.groupby("year")["price"].mean())
print(doksanDokuz.groupby("year")["price"].mean())
print(dtf1[dtf1.year !=1970].groupby("year")["price"].mean())

dtf1=doksanDokuz
dtf1=dtf1[dtf1.year !=1970]
print(dtf1)

print(dtf1.groupby("year")["price"].mean())
dtf1=dtf1.drop("transmission",axis=1)
print(dtf1)

y=dtf1["price"].values
x=dtf1.drop("price",axis=1).values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=10)
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=Sequential()  # Sequential dan modelimizi oluşturuyoruz
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam",loss="mse")  # adam optimizasyonu birçok durumda daha iyi performans gösterir
model.fit(x=x_train,y=y_train,validation_data=(x_test,y_test),batch_size=250,epochs=300)  # validation_data= doğrulama verisini x_test ve y_test için kıyaslamayı daha kolay hale getiriyor,batch_size=verileri parça parça modele vermektir.

kayipVerisi=pd.DataFrame(model.history.history)
print(kayipVerisi.head())
print(dtf1.iloc[2])













