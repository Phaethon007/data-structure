class Orang:
    total=0
    def __init__(self, nama):
        self.nama = nama
        Orang.total += 1

    def __del__(self):
        Orang.total -= 1

    def katakanHalo(self):
        print("Halo, nama saya", self.nama,", apa kabar?")

    @classmethod
    def total_populasi(cls):
        print ('Total Orang adalah ', cls.total)

org1 = Orang("Daffa")
org1.katakanHalo()
Orang.total_populasi()

org2 = Orang("Bayu")
org2.katakanHalo()
Orang.total_populasi()

print ('objek dihapus')
del org1
del org2
Orang.total_populasi()