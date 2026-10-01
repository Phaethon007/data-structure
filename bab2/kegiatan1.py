class Mobil:
    def __init__(self):
        self.warna = 'Hitam'
        self.tipe = 'Sedan'
        print ('Objek telah dibuat')

    def maju(self):
        print('maju')

    def mundur(self):
        print('mundur')

    def melaju(self, speed):
        print('Melaju dengan kecepatan %s km/jam' % speed)

# membuat objek pertama
mobil1 = Mobil()
print (mobil1.warna)
mobil1.maju()
mobil1.melaju(100)

# membuat objek kedua
mobil2 = Mobil()
print (mobil2.tipe)
mobil2.mundur()
mobil2.melaju(150)