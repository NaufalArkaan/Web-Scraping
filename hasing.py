# Membuat struktur data hash menggunakan dictionary
data_mahasiswa = {
    "A001": "Budi Santoso",
    "A002": "Arkan Pratama",
    "A003": "Citra Dewi",
    "A004": "Dewi Lestari",
    "A005": "Eko Saputra"
}

# Fungsi pencarian menggunakan hashing
def cari_mahasiswa(nim):
    if nim in data_mahasiswa:
        return f"Data ditemukan: {nim} - {data_mahasiswa[nim]}"
    else:
        return "Data tidak ditemukan"

# Contoh pencarian
print(cari_mahasiswa("A003"))  # Output: Data ditemukan: A003 - Citra Dewi
print(cari_mahasiswa("A007"))  # Output: Data tidak ditemukan
