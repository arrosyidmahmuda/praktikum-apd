# main.py
import inquirer
from barang import clear, tampilkan_semua_jenis, tampilkan_data_alat
from akun import daftar, login
from alat import tambah_data_alat, ubah_jenis
from data import data_alat

while True:
    clear()
    main = inquirer.prompt([
        inquirer.List(
            "menu",
            message="=== SISTEM DATA ALAT PERKEBUNAN ===",
            choices=["Daftar", "Login", "Keluar"]
        )
    ])["menu"]

    if main == "Daftar":
        daftar()

    elif main == "Login":
        username, role = login()
        if not username:
            continue

        # ===== ADMIN =====
        if role == 1:
            while True:
                clear()
                menu_admin = inquirer.prompt([
                    inquirer.List(
                        "menu_admin",
                        message="Menu Admin",
                        choices=[
                            "Tambah Data Alat",
                            "Lihat Data Alat",
                            "Ubah Data Alat",
                            "Hapus Data Alat",
                            "Logout"
                        ]
                    )
                ])["menu_admin"]

                if menu_admin == "Tambah Data Alat":
                    tambah_data_alat()

                elif menu_admin == "Lihat Data Alat":
                    tampilkan_data_alat()

                elif menu_admin == "Ubah Data Alat":
                    if not data_alat:
                        print("Belum ada data untuk diubah.")
                        input("Tekan Enter...")
                        continue
                    tampilkan_data_alat()
                    ub = input("Masukkan ID alat yang ingin diubah: ")
                    if ub.isdigit() and int(ub) in data_alat:
                        alat = data_alat[int(ub)]
                        print(f"Data sekarang: {alat}")
                        ubNama = input("Ubah nama (kosongkan jika tidak): ")
                        ubJenis = input("Ubah jenis (Cangkul/Sekop/Parang/Gunting): ").capitalize()
                        if ubNama:
                            alat["nama"] = ubNama
                        if ubJenis:
                            if not ubah_jenis(int(ub), ubJenis):
                                print("Jenis tidak valid!")
                            else:
                                print("Data berhasil diubah!")
                    else:
                        print("ID tidak valid!")
                    input("Tekan Enter...")

                elif menu_admin == "Hapus Data Alat":
                    if not data_alat:
                        print("Belum ada data untuk dihapus.")
                        input("Tekan Enter...")
                        continue
                    tampilkan_data_alat()
                    hapus = input("Masukkan ID alat yang ingin dihapus: ")
                    if hapus.isdigit() and int(hapus) in data_alat:
                        del data_alat[int(hapus)]
                        print("Data berhasil dihapus!\n")
                    else:
                        print("ID salah!\n")
                    input("Tekan Enter...")

                elif menu_admin == "Logout":
                    break

        # ===== USER =====
        else:
            while True:
                clear()
                menu_user = inquirer.prompt([
                    inquirer.List(
                        "menu_user",
                        message=f"Selamat datang {username}",
                        choices=[
                            "Lihat Jenis Alat",
                            "Lihat Data Tersedia",
                            "Logout"
                        ]
                    )
                ])["menu_user"]

                if menu_user == "Lihat Jenis Alat":
                    tampilkan_semua_jenis()
                    input("Tekan Enter...")

                elif menu_user == "Lihat Data Tersedia":
                    tampilkan_data_alat()

                elif menu_user == "Logout":
                    break

    elif main == "Keluar":
        print("Program berhenti. Terima kasih.")
        break