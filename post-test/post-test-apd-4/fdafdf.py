while True:
    NIM = input("Masukkan NIM anda: ")
    if NIM.isdigit():
        break
    else:
        print("Input tidak valid, masukkan angka")

# ===============================
# MISI 1: TES KONSENTRASI
# ===============================
stamina = int(NIM[-3:])
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("\n============ MISI 1: TES KONSENTRASI ============")
print(f"Chakra terkumpul: {chakra}")
print(f"Sisa stamina: {stamina}")
if chakra >= 200:
    print("Status: Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Status: Naruto kehabisan stamina sebelum berhasil.")
print("=================================================")

# ===============================
# MISI 2: INFILTRASI
# ===============================
tinggi_menara = int(NIM[-2:])
gulungan = 0

for i in range(3, tinggi_menara+1, 3):
    gulungan += 1

print("\n========= MISI 2: INFILTRASI ==========")
print(f"Tinggi menara: {tinggi_menara} meter")
print(f"Gulungan informasi yang didapatkan: {gulungan}")
print("=======================================")

# ===============================
# MISI 3: PENYELIDIKAN
# ===============================
jumlah_koridor = int(NIM[-2])
intelijen = 0
perangkap_peledak = 0

if jumlah_koridor >= 1:
    print("\n============ MISI 3: PENYELIDIKAN ============")
    for k in range(1, jumlah_koridor+1):
        print(f"Koridor {k}:")
        for r in range(1, 4):  # setiap koridor ada 3 ruangan
            if r % 2 == 1:
                intelijen += 1
                print(f"  Ruangan {r} -> Data Intelijen 📜")
            else:
                perangkap_peledak += 1
                print(f"  Ruangan {r} -> Perangkap Peledak 💣")

    print("----------------------------------------------")
    print(f"Jumlah koridor: {jumlah_koridor}")
    print(f"Jumlah ruangan total: {jumlah_koridor * 3}")
    print(f"Data Intelijen ditemukan: {intelijen}")
    print(f"Perangkap Peledak dijinakkan: {perangkap_peledak}")
    print("==============================================")
