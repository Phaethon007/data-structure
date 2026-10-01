class Kucing:
    def __init__(self, usia, warna_bulu):
        self.usia = usia
        self.warna_bulu = warna_bulu
        print('Objek kucing telah dibuat')

    def meong(self):
        print('Meooong...')

    def umur(self):
        print('Umur kucing adalah %s tahun' % self.usia)


# Membuat objek kucing
kucing1 = Kucing(2, 'Putih')
kucing2 = Kucing(3, 'Hitam')
kucing3 = Kucing(1, 'Oren')

# Menampilkan informasi kucing 1
print('\nKucing 1')
print('Warna bulu:', kucing1.warna_bulu)
kucing1.meong()
kucing1.umur()

# Menampilkan informasi kucing 2
print('\nKucing 2')
print('Warna bulu:', kucing2.warna_bulu)
kucing2.meong()
kucing2.umur()

# Menampilkan informasi kucing 3
print('\nKucing 3')
print('Warna bulu:', kucing3.warna_bulu)
kucing3.meong()
kucing3.umur()