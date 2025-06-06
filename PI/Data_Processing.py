import pandas as pd

# Ubah path ini sesuai lokasi file CSV kamu
csv_path = 'C:/Users/Naufal/OneDrive/Desktop/Web-Scraping/PI/Survei_Medsos.csv'

try:
    df = pd.read_csv(csv_path)
    print("✅ File berhasil dibaca.")
    print("Kolom yang tersedia:")
    print(df.columns)
except FileNotFoundError:
    print("❌ File tidak ditemukan. Cek path-nya.")
except Exception as e:
    print(f"❌ Terjadi error lain: {e}")
