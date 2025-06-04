def linear_search(data, target):
    for i, item in enumerate(data):
        if item == target:
            return i  # Mengembalikan indeks jika ditemukan
    return -1  # Tidak ditemukan

# Contoh data
data = [12, 34, 56, 78, 90, 23, 45]
target = 78

# Pencarian
result = linear_search(data, target)
print(f"Hasil Linear Search: Data {target} ditemukan di indeks {result}" if result != -1 else "Data tidak ditemukan")
