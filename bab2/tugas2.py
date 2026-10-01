# membuat class mahasiswa
class Mahasiswa:
    def __init__(self,nama,nim,alamat,semester):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.semester = semester
        print('Objek mahasiswa telah dibuat')

    def tampilkanNama(self):
        print("Nama mahasiswa :", self.nama)

    def tampilkanNim(self):
        print("Nim mahasiswa :", self.nim)

    def tampilkanAlamat(self):
        print("Alamat mahasiswa :", self.alamat)

    def tampilkanSemester(self):
        print("Semester mahasiswa :", self.semester)

# membuat objek mahasiswa
mahasiswa1 = Mahasiswa("Muhammad Daffa' Arrazy", "1202507007", "Mojosongo", 3)

# menampilkan informasi mahasiswa
mahasiswa1.tampilkanNama()
mahasiswa1.tampilkanNim()
mahasiswa1.tampilkanAlamat()
mahasiswa1.tampilkanSemester()