class Orang:
    def __init__(self, nama):
        self.nama = nama

    def katakanSalam(self):
        print("Assalamu,alaikum, " + self.nama)

org = Orang("Daffa")
org.katakanSalam()
