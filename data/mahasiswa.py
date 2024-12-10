class Mahasiswa:
    def __init__(self, nim, nama, jurusan, angkatan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def __str__(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - {self.angkatan}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus_data(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                self.data.remove(mahasiswa)
                return True
        return False

    def ubah_data(self, nim, nama=None, jurusan=None, angkatan=None):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                if nama:
                    mahasiswa.nama = nama
                if jurusan:
                    mahasiswa.jurusan = jurusan
                if angkatan:
                    mahasiswa.angkatan = angkatan
                return True
        return False

    def cari_data(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def semua_data(self):
        return self.data
