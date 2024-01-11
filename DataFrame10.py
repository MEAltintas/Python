import numpy as np
import pandas as pd
personeller={
    "Çalışan":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cen Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yaş":[30,25,45,50,23,34,42],
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Kadıköy","Tuzla","Maltepe"],
    "Maaş":[5000,3000,4000,3500,2750,6500,4500]
}

dtf1=pd.DataFrame(personeller)
print(dtf1)

print(dtf1["Maaş"].sum())
print(dtf1.groupby(["Departman","Semt"]).groups)
semtler= dtf1.groupby("Semt")
for name,group in semtler:
    print(name)
    print(group)
print(dtf1.groupby("Departman")["Yaş"].mean())
print(dtf1.groupby("Semt")["Maaş"].mean())
print(dtf1.groupby("Semt")["Çalışan"].count())
print(dtf1.groupby("Departman")["Çalışan"].count())