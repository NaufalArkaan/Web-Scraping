import pandas as pd

# Ganti path jika perlu
file_path = 'C:/Users/Naufal/OneDrive/Desktop/Web-Scraping/PI/Survei_Medsos.csv'

try:
    df = pd.read_csv(file_path)
    print("✅ File berhasil dibaca.")
    print("🧾 Daftar kolom yang tersedia:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. '{col}'")
except FileNotFoundError:
    print("❌ File tidak ditemukan! Cek path dan nama file.")
except Exception as e:
    print(f"❌ Terjadi error: {e}")
