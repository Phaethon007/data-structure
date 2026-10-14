print("Masukkan daftar nomor ID:")
data = [int(x) for x in input().split()]

data.sort(reverse=True)

print("Daftar nomor ID setelah diurutkan:", data)

cari = int(input("Masukkan nomor ID yang dicari: "))

awal = 0
akhir = len(data) - 1
ditemukan = False

while awal <= akhir:
    tengah = (awal + akhir) // 2

    if data[tengah] == cari:
        print("Nomor ID ditemukan pada index", tengah)
        ditemukan = True
        break
    elif data[tengah] < cari:
        akhir = tengah - 1
    else:
        awal = tengah + 1

if not ditemukan:
    print("Nomor ID tidak ditemukan")