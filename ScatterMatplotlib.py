import matplotlib.pyplot as plt

dtf=pd.read_csv("iris.csv")

setosa1=dtf[dtf["Species"]=="Iris-setosa"]
vercicolor1=dtf[dtf.Species=="Iris-versicolor"]
virginica1=dtf[dtf["Species"]=="Iris-virginica"]
x=setosa1.SepalWidthCm
y=setosa1.SepalLengthCm
plt.scatter(x,y)
plt.scatter(vercicolor1.SepalWidthCm,vercicolor1.SepalLengthCm)
plt.scatter(virginica1.SepalWidthCm,virginica1.SepalLengthCm)
plt.show()