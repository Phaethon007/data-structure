print("Masukkan daftar nomor ID:")
data = [int(x) for x in input().split()]

print("Daftar nomor ID:", data)

cari = int(input("Masukkan nomor ID yang dicari: "))

ditemukan = False

for i in range(len(data)):
    if data[i] == cari:
        print("Nomor ID ditemukan pada index", i)
        ditemukan = True
        break

if not ditemukan:
    print("Nomor ID tidak ditemukan")