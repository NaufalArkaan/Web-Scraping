import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Baca data
df = pd.read_csv('C:/Users/Naufal/OneDrive/Desktop/Web-Scraping/PI/Survei_Medsos.csv')

# Ganti dengan nama kolom teks yang benar, contoh:
kolom_teks = 'Pekerjaan'  # contoh nama kolom, sesuaikan dengan hasil Step 1

# Pastikan kolom ada
if kolom_teks not in df.columns:
    raise KeyError(f"Kolom '{kolom_teks}' tidak ditemukan di dataset.")

# Ubah isi kolom ke string
df[kolom_teks] = df[kolom_teks].astype(str)

# Inisialisasi Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Hitung skor sentimen
df['Sentimen'] = df[kolom_teks].apply(lambda x: sia.polarity_scores(x)['compound'])

# Klasifikasi sentimen berdasarkan skor
def kategori_sentimen(score):
    if score > 0.05:
        return 'Positif'
    elif score < -0.05:
        return 'Negatif'
    else:
        return 'Netral'

df['Kategori_Sentimen'] = df['Sentimen'].apply(kategori_sentimen)

# Tampilkan 5 baris hasil analisis
print(df[[kolom_teks, 'Sentimen', 'Kategori_Sentimen']].head())

# Visualisasi distribusi sentimen
plt.figure(figsize=(8,5))
sns.countplot(x='Kategori_Sentimen', data=df, order=['Positif', 'Netral', 'Negatif'])
plt.title('Distribusi Kategori Sentimen')
plt.xlabel('Kategori Sentimen')
plt.ylabel('Jumlah')
plt.show()
