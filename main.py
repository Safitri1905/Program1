from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()
    
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan, angkatan = InputForm.form_input()
            mahasiswa = Mahasiswa(nim, nama, jurusan, angkatan)
            data_mahasiswa.tambah_data(mahasiswa)
            print("Data mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            if data_mahasiswa.hapus_data(nim):
                print("Data mahasiswa berhasil dihapus.")
            else:
                print("Data mahasiswa tidak ditemukan.")

        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            print("Kosongkan input untuk data yang tidak ingin diubah.")
            nama = input("Nama baru: ")
            jurusan = input("Jurusan baru: ")
            angkatan = input("Angkatan baru: ")
            if data_mahasiswa.ubah_data(nim, nama, jurusan, angkatan):
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Data mahasiswa tidak ditemukan.")

        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
            mahasiswa = data_mahasiswa.cari_data(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)

        elif pilihan == "5":
            ViewMahasiswa.tampilkan_list(data_mahasiswa.semua_data())

        elif pilihan == "6":
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
