import os

#Variabel Global
dataAkun = {
    "asoy": {"password": "120905", "role": 1},
    "siktir": {"password": "sana", "role": 0}
}
id_alat = 0
data_alat = {}
jenisAlat = {
    1: {"nama": "Cangkul", "modal": 30000, "harga": 45000},
    2: {"nama": "Sekop", "modal": 25000, "harga": 40000},
    3: {"nama": "Parang", "modal": 20000, "harga": 35000},
    4: {"nama": "Gunting", "modal": 15000, "harga": 25000}
}
#Fungsi tanpa Parameter
def hitung_total_laba():
    """Fungsi tanpa parameter: hitung total laba"""
    total = 0
    for i in data_alat:
        total += data_alat[i]["laba"]
    return total

def tampilkan_semua_jenis():
    """Fungsi tanpa parameter: tampilkan semua jenis alat"""
    for j in jenisAlat:
        print(f"{j}. {jenisAlat[j]['nama']} (Modal: {jenisAlat[j]['modal']}, Harga: {jenisAlat[j]['harga']})")

#Fungsi dgn Parameter
def hitung_laba(modal, harga):
    """Fungsi dengan parameter: menghitung laba"""
    try:
        return harga - modal
    except TypeError:
        print("Terjadi kesalahan pada perhitungan laba.")
        return 0

def ubah_jenis(alat_id, jenisBaru):
    """Fungsi dengan parameter: ubah jenis alat"""
    if alat_id in data_alat:
        for j in jenisAlat:
            if jenisAlat[j]["nama"] == jenisBaru:
                data_alat[alat_id]["jenis"] = jenisBaru
                data_alat[alat_id]["modal"] = jenisAlat[j]["modal"]
                data_alat[alat_id]["harga"] = jenisAlat[j]["harga"]
                data_alat[alat_id]["laba"] = hitung_laba(jenisAlat[j]["modal"], jenisAlat[j]["harga"])
                return True
    return False

def tambah_data_alat():
    """Prosedur menambah data alat"""
    global id_alat
    try:
        nama = input("Namanya: ")
        tampilkan_semua_jenis()
        pilihJenis = input("Nomor jenis: ")

        if pilihJenis.isdigit() and int(pilihJenis) in jenisAlat:
            id_alat += 1
            j = int(pilihJenis)
            modal = jenisAlat[j]["modal"]
            harga = jenisAlat[j]["harga"]
            laba = hitung_laba(modal, harga)
            data_alat[id_alat] = {
                "nama": nama,
                "jenis": jenisAlat[j]["nama"],
                "modal": modal,
                "harga": harga,
                "laba": laba
            }
            print("Data berhasil ditambahkan!\n")
        else:
            print("Input salah!\n")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    input("Tekan Enter...")

def tampilkan_data_alat():
    """Prosedur menampilkan data alat"""
    if len(data_alat) == 0:
        print("Belum ada data alat.\n")
    else:
        total = 0
        for i in data_alat:
            alat = data_alat[i]
            print(f"""
-------------------------------
ID: {i}
Nama  : {alat['nama']}
Jenis : {alat['jenis']}
Modal : Rp{alat['modal']}
Harga : Rp{alat['harga']}
Laba  : Rp{alat['laba']}
-------------------------------""")
            total += alat["laba"]
        print(f"Total Laba: Rp{total}\n")
    input("Tekan Enter...")

#Program Utama
while True:
    os.system("cls")
    print("""
\033[32m
    ____  _       __     __      __          __           
   / __ \(_)___ _/ /__  / /___ _/ /___  ____/ /__  _____  
  / /_/ / / __ `/ / _ \/ / __ `/ / __ \/ __  / _ \/ ___/  
 / ____/ / /_/ / /  __/ / /_/ / / /_/ / /_/ /  __/ /      
/_/   /_/\__, /_/\___/_/\__,_/_/\____/\__,_/\___/_/       
        /____/                                             
\033[37m
-----------------------------------
-   SISTEM DATA ALAT PERKEBUNAN   -
-----------------------------------
- 1. DAFTAR                       -
- 2. LOGIN                        -
- 3. KELUAR                       -
-----------------------------------
""")
    menu = input("Pilih (1-3): ")

    if menu == "1":
        os.system("cls")
        print("\n=== DAFTAR AKUN ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in dataAkun:
            print("Username sudah terdaftar!\n")
        else:
            dataAkun[username] = {"password": password, "role": 0}
            print("Registrasi berhasil!\n")
        input("Tekan Enter...")

    elif menu == "2":
        os.system("cls")
        print("\n=== LOGIN ===")
        username = input("Username anda: ")
        password = input("Password anda: ")

        if username in dataAkun and dataAkun[username]["password"] == password:
            role = dataAkun[username]["role"]

            # ==== ADMIN ====
            if role == 1:
                while True:
                    os.system("cls")
                    print("""
\033[32m
===== MENU ADMIN =====
-----------------------
1. TAMBAH DATA ALAT
2. TAMPILKAN DATA
3. UBAH DATA
4. HAPUS DATA
5. LOGOUT
=======================
\033[37m""")
                    pilih = input("Pilih (1-5): ")

                    if pilih == "1":
                        tambah_data_alat()

                    elif pilih == "2":
                        os.system("cls")
                        print("\n== DATA ALAT TERDAFTAR ==")
                        tampilkan_data_alat()

                    elif pilih == "3":
                        os.system("cls")
                        print("== UBAH DATA ALAT ==")
                        if len(data_alat) == 0:
                            print("Belum ada data untuk diubah.\n")
                            input("Tekan Enter...")
                            continue
                        for i in data_alat:
                            print(f"{i}. {data_alat[i]['nama']} - {data_alat[i]['jenis']}")
                        ubah = input("Pilih ID alat: ")
                        if ubah.isdigit() and int(ubah) in data_alat:
                            idu = int(ubah)
                            alat = data_alat[idu]
                            print(f"Data sekarang: {alat}")
                            ubahNama = input("Ubah nama (Enter jika tidak): ")
                            ubahJenis = input("Ubah jenis (Cangkul/Sekop/Parang/Gunting) (Enter jika tidak): ").capitalize()
                            if ubahNama:
                                alat["nama"] = ubahNama
                            if ubahJenis:
                                if not ubah_jenis(idu, ubahJenis):
                                    print("Jenis tidak dikenali.")
                            print("Data berhasil diubah!\n")
                        else:
                            print("ID tidak valid!\n")
                        input("Tekan Enter...")

                    elif pilih == "4":
                        os.system("cls")
                        print("== HAPUS DATA ==")
                        if len(data_alat) == 0:
                            print("Belum ada data untuk dihapus.\n")
                        else:
                            for i in data_alat:
                                print(f"{i}. {data_alat[i]['nama']} - {data_alat[i]['jenis']}")
                            hapus = input("Masukkan ID: ")
                            if hapus.isdigit() and int(hapus) in data_alat:
                                del data_alat[int(hapus)]
                                print("Data berhasil dihapus!\n")
                            else:
                                print("ID salah!\n")
                        input("Tekan Enter...")

                    elif pilih == "5":
                        print("Logout admin\n")
                        break
                    else:
                        print("Input salah! Hanya bisa 1-5 \n")
                        input("Tekan Enter...")

            # === USER ===
            else:
                while True:
                    os.system("cls")
                    print("""
\033[32m
===== MENU PENGGUNA =====
----------------------
1. LIHAT JENIS ALAT
2. LIHAT DATA TERSEDIA
3. LOGOUT
======================
\033[37m""")
                    pilih = input("Pilih (1-3): ")

                    if pilih == "1":
                        os.system("cls")
                        print("== JENIS ALAT PERKEBUNAN ==")
                        tampilkan_semua_jenis()
                        print("")
                        input("Tekan Enter...")

                    elif pilih == "2":
                        os.system("cls")
                        if len(data_alat) == 0:
                            print("Belum ada data alat tersedia.\n")
                        else:
                            for i in data_alat:
                                alat = data_alat[i]
                                print(f"{alat['nama']} - {alat['jenis']} (Harga: Rp{alat['harga']})")
                            print("")
                        input("Tekan Enter...")

                    elif pilih == "3":
                        print("Logout user\n")
                        break
                    else:
                        print("Input salah! Hanya bisa 1-3\n")
                        input("Tekan Enter...")
        else:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter...")

    elif menu == "3":
        print("Program berhenti. Terima kasih ")
        break

    else:
        print("Input salah! Pilih 1-3\n")
        input("Tekan Enter...")
