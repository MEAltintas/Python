import pandas as pd
mergeSozluk1={"İsim":["Gül","Çiçek","Yağmur","Bulut"],
            "Spor":["Koşu","Yüzme","Koşu","Basketbol"],
        }

mergedtf1=pd.DataFrame(mergeSozluk1)

mergeSozluk2={"İsim":["Gül","Çiçek","Yağmur","Bulut"],
            "Kalori":[200,100,50,300]
            }

mergedtf2=pd.DataFrame(mergeSozluk2)

print(mergedtf1)
print(mergedtf2)
print(pd.merge(mergedtf1,mergedtf2,on="İsim"))

