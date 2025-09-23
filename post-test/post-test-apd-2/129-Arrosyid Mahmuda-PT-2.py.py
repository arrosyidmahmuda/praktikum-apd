# harga batu_bata dan semen
Harga_batu_bata = 100
Harga_semen = 100000

nama_pelanggan = input("masukkan nama pelanggan: ")

jumlah_batu_bata = int(input("masukkan jumlah batu_bata: "))
jumlah_semen = int(input("masukkan jumlah semen: "))

total_biaya_awal = (jumlah_batu_bata * Harga_batu_bata) + (jumlah_semen * Harga_semen)

#diskon
diskon = 0.0
keterangan_diskon = "Tidak ada paket"

Paket_ultra_mantap = jumlah_batu_bata == 2000 and jumlah_semen == 16
Paket_hemat = jumlah_batu_bata == 500 and jumlah_semen == 5

if Paket_ultra_mantap:
    diskon = 0.30
    keterangan_diskon = "Paket ultra mantap"
elif Paket_hemat:
    diskon = 0.15
    keterangan_diskon = "Paket hemat"

jumlah_diskon = total_biaya_awal * diskon
total_biaya_akhir = total_biaya_awal - jumlah_diskon

#output
print(f"Nama Pelanggan: {nama_pelanggan}")
print("-" * 43)
print(f"{'| Barang':<13} | {'Jumlah':<8} | {'Harga Satuan':<15} |")
print("-" * 43)
print(f"| {'Batu Bata':<11} | {jumlah_batu_bata:<8} | {(Harga_batu_bata):<15} |")
print(f"| {'Semen':<11} | {jumlah_semen:<8} | {(Harga_semen):<15} |")
print("-" * 43)
print(f"Total Biaya Awal{'':.<20}: {(total_biaya_awal)}")
print(f"Paket Yang Didapat{'':.<21}: {keterangan_diskon}")
print(f"Jumlah Diskon{'':.<27}: {(jumlah_diskon)}")
print("-" * 43)
print(f"TOTAL BIAYA AKHIR{'':.<20}: {(total_biaya_akhir)}")
print("-"*43)