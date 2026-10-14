data = [12, 23, 34, 45, 56, 67, 78, 89, 90]

id_cari = int(input("Masukkan nomor ID: "))

# Linear Search
ditemukan = False

for i in range(len(data)):
    if data[i] == id_cari:
        print("Linear Search: ID ditemukan pada index", i)
        ditemukan = True
        break

if not ditemukan:
    print("Linear Search: ID tidak ditemukan")


# Binary Search (urutan terbesar)
data_binary = sorted(data, reverse=True)

awal = 0
akhir = len(data_binary) - 1
ditemukan = False

while awal <= akhir:
    tengah = (awal + akhir) // 2

    if data_binary[tengah] == id_cari:
        print("Data untuk Binary Search:", data_binary)
        print("Binary Search: ID ditemukan pada index", tengah)
        ditemukan = True
        break
    elif data_binary[tengah] < id_cari:
        akhir = tengah - 1
    else:
        awal = tengah + 1

if not ditemukan:
    print("Data untuk Binary Search:", data_binary)
    print("Binary Search: ID tidak ditemukan")