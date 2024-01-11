import matplotlib.pyplot as plt
hareket=["Penaltı","Kaleye atılan şut","Serbest vuruş"]
sayi=[12,35,7]
plt.pie(sayi,labels=hareket,colors=["r","b","g"],shadow=True,startangle=90,explode=(0.1,0,0),autopct="%1.1f%%")
plt.show()
