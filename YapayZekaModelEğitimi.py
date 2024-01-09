import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sbn
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.callbacks import EarlyStopping

dtf1=pd.read_excel("maliciousornot.xlsx")
print(dtf1)
print(dtf1.info())
print(dtf1.describe())

sbn.countplot(x="Type",data=dtf1)
#plt.show()
plt.clf()
plt.close()

y=dtf1["Type"].values
x=dtf1.drop("Type",axis=1).values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)
scaler=MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

print(x_train.shape)

model=Sequential()
model.add(Dense(units=30,activation="relu"))
model.add(Dense(units=15,activation="relu"))
model.add(Dense(units=15,activation="relu"))
model.add(Dense(units=1,activation="sigmoid"))
model.compile(loss="binary_crossentropy",optimizer="adam")
model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1)
modelKaybi=pd.DataFrame(model.history.history)
modelKaybi.plot()

# earlystopping = overfiti olan modeli erken durdurur durdurduğu sayı epochs için ideal olandır
earlyStopping=EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25)
model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1,callbacks=[earlyStopping])
modelKaybi=pd.DataFrame(model.history.history)
modelKaybi.plot()











































































