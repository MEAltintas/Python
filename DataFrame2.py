import pandas as pd
maasSozlugu={"Departman":["Yazılım","Yazılım","Hukuk","Hukuk","Pazarlama","Pazarlama"],
            "Çalışan İsmi":["Ahmet","Mehmet","Ayşe","Fatma","Gül","Çiçek"],
            "Maaş":[100,150,200,300,400,500]
            }
maasDtf=pd.DataFrame(maasSozlugu)
print(maasDtf)
grup=maasDtf.groupby("Departman")
print(grup.count())
print(grup.min())
print(grup.max())
print(grup.describe())