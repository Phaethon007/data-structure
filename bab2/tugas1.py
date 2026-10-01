# Membuat kelas Hewan
class Hewan:
    def __init__(self, nama, jumlahKaki, makanan,tipe):
        self.nama = nama
        self.jumlahKaki = jumlahKaki
        self.makanan = makanan
        self.tipe = tipe

    def tampilkanInfo(self):
        print("Nama Hewan:", self.nama)
        print("Jumlah Kaki:", self.jumlahKaki)
        print("Makanan:", self.makanan)
        print("Tipe:", self.tipe)

# Membuat objek hewan
hewan1 = Hewan("Harimau", 4, "daging", "karnivora")
hewan2 = Hewan("kerbau", 4, "rumput", "herbivora")
# Menampilkan informasi hewan
hewan1.tampilkanInfo()
print()
hewan2.tampilkanInfo()
