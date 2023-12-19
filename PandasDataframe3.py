import pandas as pd


trafik={
    "Plaka":["68","71","67","15","34","35"],
    "Şehir":["Aksaray","Kırıkkale","Zonguldak","Burdur","İstanbul","İzmir"],
    "Alan":[318,382,367,315,218,235]
}
trf = pd.DataFrame(trafik)
trf2=trf.set_index("Plaka")
print(trf2)