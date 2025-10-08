while True:
    NIM = input("masukkan NIM anda: ")

    if NIM.isdigit():
        break
    else:
        print("input tidak valid, masukkan angka")

# misi 1
stamina = int(NIM[-3:])
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3
print("\n============ MISI 1: TES KONSENTRASI ============")
print(f"Chakra terkumpul: {chakra}")
print(f"sisa stamina: {stamina}")
if chakra >= 200:
    print("Status: Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Status: Naruto kehabisan stamina sebelum berhasil.")
print("=================================================")

# misi 2
tinggi_menara = int(NIM[-2:])
gulungan = 0

for i in range(3,tinggi_menara+1, 3):
    gulungan += 1

print("\n========= MISI 2: INFILTRASI ==========")
print(f"tinggi menara: {tinggi_menara} meter")
print(f"gulungan informasi yang didapatkan: {gulungan} ")
print("=======================================")

# misi 3
jumlah_koridor = int(NIM[-2])
intelijen = 0
perangkap_peledak = 0

if jumlah_koridor >= 1:
    for i in range(1, jumlah_koridor+1):
        for j in range(1, 4): 
            if j % 2 == 1:
                intelijen += 1
            else:
                perangkap_peledak += 1

    print("\n============ MISI 3: PENYELIDIKAN ============")
    print(f"Jumlah koridor: {jumlah_koridor}")
    print(f"Jumlah Ruangan: {jumlah_koridor * 3}")
    print(f"Data Intelijen ditemukan: {intelijen}")
    print(f"Perangkap Peledak dijinakkan: {perangkap_peledak}")
    print("==============================================")
