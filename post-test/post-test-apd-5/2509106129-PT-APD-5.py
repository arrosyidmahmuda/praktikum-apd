# Sistem Data Alat Perkebunan
dataAkun = [["asoy", "120905", 1], ["siktir", "sana", 0]]
data_alat = []
jenisAlat = [
["Cangkul", 30000, 45000],["Sekop", 25000, 40000],["Parang", 20000, 35000],["Gunting", 15000, 25000]
]

while True:
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
    inputMenuUtama = input("Pilih (1-3): ")

    if inputMenuUtama == "1":
        print("""
\033[32m
    ____             _      __                  _ 
   / __ \___  ____ _(_)____/ /__________ ______(_)
  / /_/ / _ \/ __ `/ / ___/ __/ ___/ __ `/ ___/ / 
 / _, _/  __/ /_/ / (__  ) /_/ /  / /_/ (__  ) /  
/_/ |_|\___/\__, /_/____/\__/_/   \__,_/____/_/   
           /____/                                 
\033[37m""")
        registUsername = input("Input username : ")
        registPassword = input("Input password : ")
        registRole = 0
        dataAkun.append([registUsername, registPassword, registRole])
        print("Berhasil register!\n")

    elif inputMenuUtama == "2":
        print("""
\033[32m
    __                _     
   / /   ____  ____ _(_)___ 
  / /   / __ \/ __ `/ / __ \\
 / /___/ /_/ / /_/ / / / / /
/_____/\____/\__, /_/_/ /_/ 
            /____/          
\033[37m""")
        inputUsername = input("Username anda : ")
        inputPassword = input("Password anda : ")

        login_berhasil = False

        for akun in dataAkun:
            username, password, role = akun
            if inputUsername == username and inputPassword == password:
                login_berhasil = True

                # ==== ADMIN ====
                if role == 1:
                    print("\nLogin sebagai ADMIN\n")
                    while True:
                        print("""
\033[32m
===== DATA ALAT PERKEBUNAN =====
--------------------------------
1. TAMBAH DATA ALAT
2. TAMPILKAN DATA
3. UBAH DATA
4. HAPUS DATA
5. LOGOUT
================================
\033[37m""")
                        pilih = input("Pilih (1-5): ")

                        if pilih == "1":
                            print("== TAMBAH DATA ALAT ==")
                            nama = input("Namanya: ")
                            print("Pilih jenis alat: ")
                            for i in range(len(jenisAlat)):
                                print(f"{i+1}. {jenisAlat[i][0]} (Modal: {jenisAlat[i][1]}, Harga jual: {jenisAlat[i][2]})")

                            pilihJenis = input("Pilih nomor jenis alat: ")

                            if pilihJenis.isdigit() and 1 <= int(pilihJenis) <= len(jenisAlat):
                                tipe_alat = int(pilihJenis) - 1
                                namaJenis, modal, harga = jenisAlat[tipe_alat]
                                laba = harga - modal
                                data_alat.append([nama, namaJenis, modal, harga, laba])
                                print(f"Berhasil menambah data alat: {data_alat[-1]}\n")
                            else:
                                print("Input salah!\n")

                        elif pilih == "2":
                            print("\n== DATA ALAT TERDAFTAR ==")
                            if len(data_alat) == 0:
                                print("Belum ada data alat.\n")
                            else:
                                totalLaba = 0
                                for i in range(len(data_alat)):
                                    nama, jenis, modal, harga, laba = data_alat[i]
                                    print(f"""
\033[32m
-------------------------------
Alat ke-{i+1}
Nama  : {nama}
Jenis : {jenis}
Modal : Rp{modal}
Harga : Rp{harga}
Laba  : Rp{laba}
-------------------------------\033[37m""")
                                    totalLaba += laba
                                print(f"|Total data: {len(data_alat)} | Total Laba: Rp{totalLaba}\n")

                        elif pilih == "3":
                            print("== UBAH DATA ALAT ==")
                            if len(data_alat) == 0:
                                print("Belum ada data untuk diubah.\n")
                                continue

                            for i in range(len(data_alat)):
                                print(f"{i+1}. {data_alat[i][0]} - {data_alat[i][1]}")

                            ubah = input("Pilih alat yang ingin diubah (nomor): ")
                            if ubah.isdigit() and 1 <= int(ubah) <= len(data_alat):
                                ngubah = int(ubah) - 1
                                nama, jenis, modal, harga, laba = data_alat[ngubah]
                                print(f"Data sekarang: {data_alat[ngubah]}")

                                ubahNama = input("Ubah nama (Enter jika tidak): ")
                                ubahJenis = input("Ubah jenis (Cangkul/Sekop/Parang/Gunting) (Enter jika tidak): ").capitalize()

                                if ubahNama:
                                    data_alat[ngubah][0] = ubahNama

                                if ubahJenis:
                                    found = False
                                    for alat in jenisAlat:
                                        if alat[0] == ubahJenis:
                                            data_alat[ngubah][1] = ubahJenis
                                            data_alat[ngubah][2] = alat[1]
                                            data_alat[ngubah][3] = alat[2]
                                            data_alat[ngubah][4] = alat[2] - alat[1]
                                            found = True
                                            break
                                    if not found:
                                        print("Jenis tidak dikenali, perubahan jenis dibatalkan.")
                                print("Data berhasil diubah!\n")
                            else:
                                print("Input salah!\n")

                        elif pilih == "4":
                            print("== HAPUS DATA ==")
                            if len(data_alat) == 0:
                                print("Belum ada data untuk dihapus.\n")
                                continue

                            for i in range(len(data_alat)):
                                print(f"{i+1}. {data_alat[i][0]} - {data_alat[i][1]}")

                            hapus = input("Pilih data yang ingin dihapus (nomor): ")
                            if hapus.isdigit() and 1 <= int(hapus) <= len(data_alat):
                                del data_alat[int(hapus) - 1]
                                print("Data berhasil dihapus!\n")
                            else:
                                print("Input salah!\n")

                        elif pilih == "5":
                            print("Logout admin\n")
                            break
                        else:
                            print("Input salah! Hanya bisa 1-5\n")

                # ==== USER ====
                elif role == 0:
                    print("\nLogin sebagai USER\n")
                    while True:
                        print("""
\033[32m
===== MENU PENGGUNA =====
--------------------------
1. LIHAT JENIS ALAT
2. LIHAT DATA TERSEDIA
3. LOGOUT
==========================
\033[37m""")
                        pilih = input("Pilih (1-3): ")

                        if pilih == "1":
                            print("\n== JENIS ALAT PERKEBUNAN ==")
                            for alat in jenisAlat:
                                print(f" {alat[0]} | Harga Jual: Rp{alat[2]} ")
                            print("")

                        elif pilih == "2":
                            if len(data_alat) == 0:
                                print("Belum ada data alat yang tersedia.\n")
                            else:
                                for alat in data_alat:
                                    print(f"{alat[0]} - {alat[1]} (Harga: Rp{alat[3]})")
                                print("")
                        elif pilih == "3":
                            print("Logout user\n")
                            break
                        else:
                            print("Input salah! Hanya bisa 1-3\n")

                break

        if not login_berhasil:
            print("Username atau password salah!\n")

    elif inputMenuUtama == "3":
        print("Program berhenti. Terima kasih ")
        break

    else:
        print("Input salah! Hanya bisa 1-3\n")
