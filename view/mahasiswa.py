class ViewMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        print("\n=== Daftar Mahasiswa ===")
        for mhs in data_mahasiswa:
            print(mhs)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\n=== Detail Mahasiswa ===")
            print(f"NIM      : {mahasiswa.nim}")
            print(f"Nama     : {mahasiswa.nama}")
            print(f"Jurusan  : {mahasiswa.jurusan}")
            print(f"Angkatan : {mahasiswa.angkatan}")
        else:
            print("Data tidak ditemukan.")
