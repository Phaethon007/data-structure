class Mobil:
    def __init__(self,warna,tipe):
        self.warna = warna
        self.tipe = tipe
        print('Objek mobil telah dibuat')

    def maju(self):
        print('mobil bergerak maju')

    def mundur(self):
        print('mobil bergerak mundur')

    def melaju(self, speed):
        print('Melaju dengan kecepatan %s km/jam' % speed)

# membuat 3 objek baru
mobil1 = Mobil('silver','sedan')
mobil2 = Mobil('putih','SUV')
mobil3 = Mobil('hitam','sport')

# menampilkan atribut dan menjalankan method
print ('\nMobil 1')
print('Warna:',mobil1.warna)
print('Tipe:',mobil1.tipe)
mobil1.maju()
mobil1.melaju(100)

print('\nMobil 2')
print('Warna:',mobil2.warna)
print('Tipe:',mobil2.tipe)
mobil2.mundur()
mobil2.melaju(80)

print('\nMobil 3')
print('Warna:',mobil3.warna)
print('Tipe:',mobil3.tipe)
mobil3.maju()
mobil3.melaju(150)
