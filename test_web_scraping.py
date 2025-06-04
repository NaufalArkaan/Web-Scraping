import requests
from bs4 import BeautifulSoup
import csv

# 1. Tentukan URL target
url = 'https://example.com'

# 2. Ambil konten halaman
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Ekstrak data (contoh: semua tag <h1>)
h1_tags = soup.find_all('h1')

# 4. Simpan hasil ke CSV
with open('out_scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['No', 'Isi H1 Tag'])
    for idx, tag in enumerate(h1_tags, 1):
        writer.writerow([idx, tag.get_text(strip=True)])

print("Data berhasil diekstrak dan disimpan ke out_scraped_data.csv")
