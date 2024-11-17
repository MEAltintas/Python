import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Verisetinin okunması
df = pd.read_csv("diabetes.csv")

#Verisetinde ki NaN değer kontrolü
print("\nVerilerin de NaN değerler:")
print(df.isna().sum())

# Verisetinin boyutunun kopyalanması ve rastgele NaN değer eklenmesi için gerekli değişkenlerin tanımlanması
df_missing = df.copy()
df_size = df.size
missing_rate = 0.05
num_missing = int(df_size * missing_rate)

# Rastgele NaN değer ekleme
for _ in range(num_missing):
    row_idx = np.random.randint(0, df.shape[0])
    col_idx = np.random.randint(0, df.shape[1])
    df_missing.iat[row_idx, col_idx] = np.nan

#Eklenen Nan değerlerin gösterilmesi
print("\nNaN değerlerinin eklendiği veri:")
print(df_missing.isna().sum())

# Verisetindeki sütunların gösterilmesi
print("Veri setindeki sütunlar:")
print(df.columns)

# Veriseti hakkında bilgi alınması
print("\nVeri seti hakkında bilgi:")
print(df.info())

# Verisetinde ortalama, standart sapma vb. değerlerin incelenmesi
print("\nVeri setinin istatistiksel özeti:")
print(df.describe())

#Veriler arası korelasyon ilişkisi
print("\nVeriler arası korelasyon ilişkisi:")
print(df.corr())

#Verisetinde Id adında bir sütun oluşturup Id değerlerini oraya atadık
df["Id"]=np.arange(0,df.shape[0])
df.index=df["Id"]



#Grafikler

#Yaş Dağılımının seaborn ile gösterilmesi
sns.histplot(df["Age"])
plt.title("Yaş Dağılımı")
plt.show()
plt.close()

#Yaş ve Deri İlişkisini Karşılaştırma Grafiği
age_bins = [20, 30, 40, 50, 60, 70, 80]  # Yaş aralıkları
age_labels = ['20-30', '30-40', '40-50', '50-60', '60-70', '70-80']  # Aralıklara karşılık gelen etiketler
# Age sütununu kategorilere ayırma
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
# Age ve SkinThickness ortalamalarını aralıklara göre karşılaştırma
sns.barplot(x='Age_Group', y='SkinThickness', data=df, color='brown', label='Deri Kalınlığı',errorbar=None)
sns.barplot(x='Age_Group', y='Age', data=df, color='magenta', label='Yaş Aralığı', alpha=0.6,errorbar=None)
plt.title("Yaş ve Deri Kalınlığı Karşılaştırması")
plt.xlabel("Yaş Aralığı")
plt.ylabel("Deri Kalınlığı")
plt.show()
plt.close()

#Gebelikte glikoz ve insülin değerlerinin etkisi
plt.bar(df["Pregnancies"],df["Insulin"],label="Insülin")
plt.bar(df["Pregnancies"],df["Glucose"],label="Glikoz")
plt.title("Gebelikte Glikoz ve Insülin")
plt.legend()
plt.show()
plt.close()

#Vücut Kütle İndeksine Göre Ortalama Tansiyon grafiği
df['BMI_Group'] = pd.cut(df['BMI'], bins=[0, 18.5, 25, 30, 35, 40, 45], labels=['0-18.5', '18.5-25', '25-30', '30-35', '35-40', '40-45'])

plt.figure(figsize=(12, 6))
sns.barplot(x='BMI_Group', y='BloodPressure', data=df, errorbar=None,color="blue",alpha=0.3)
plt.title('Vücut Kütle İndeksine Göre Ortalama Tansiyon')
plt.xlabel('Vücut Kütle Indeksi Aralığı')
plt.ylabel('Ortalama Tansiyon')
plt.show()
plt.close()

#Future Selection
# Korelasyon Grafiği
df.drop(["Id","BMI_Group","Age_Group"],axis=1,inplace=True)
sns.heatmap(df.corr() , annot= True)
plt.show()
plt.close()


