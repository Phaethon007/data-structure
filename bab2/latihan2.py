class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

#Menampilkan informasi persegi panjang dan menjalankan method
persegi_panjang1 = PersegiPanjang(20, 12)
print('Panjang:', persegi_panjang1.panjang)
print('Lebar:', persegi_panjang1.lebar)
print('Luas:', persegi_panjang1.luas())
print('Keliling:', persegi_panjang1.keliling())