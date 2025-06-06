def binary_search(data, target):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Contoh data (harus terurut)
data_sorted = [12, 23, 34, 45, 56, 78, 90]
target = 78

# Pencarian
result = binary_search(data_sorted, target)
print(f"Hasil Binary Search: Data {target} ditemukan di indeks {result}" if result != -1 else "Data tidak ditemukan")
