import pandas as pd

path = 'C:/Users/Naufal/OneDrive/Desktop/Web-Scraping/PI/Survei_Medsos.csv'

try:
    df = pd.read_csv(path)
    print("✅ File CSV berhasil dibaca!")
    print("Nama kolom:")
    print(df.columns.tolist())
    print("\nContoh 5 baris pertama data:")
    print(df.head())
except FileNotFoundError:
    print(f"❌ File tidak ditemukan di path: {path}")
except Exception as e:
    print(f"❌ Terjadi error saat baca file: {e}")
