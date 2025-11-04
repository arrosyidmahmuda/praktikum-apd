# alat.py
import inquirer
from data import data_alat, jenisAlat, id_alat
from barang import hitung_laba, tampilkan_semua_jenis, tampilkan_data_alat

def tambah_data_alat():
    global id_alat
    nama = input("Namanya: ")
    tampilkan_semua_jenis()
    pilih = inquirer.prompt([
        inquirer.List(
            "jenis",
            message="Pilih jenis alat",
            choices=[str(j) for j in jenisAlat])
    ])
    j = int(pilih["jenis"])
    modal = jenisAlat[j]["modal"]
    harga = jenisAlat[j]["harga"]
    laba = hitung_laba(modal, harga)
    id_alat += 1
    data_alat[id_alat] = {
        "nama": nama,
        "jenis": jenisAlat[j]["nama"],
        "modal": modal,
        "harga": harga,
        "laba": laba
    }
    print("\nData berhasil ditambahkan!\n")
    input("Tekan Enter...")

def ubah_jenis(alat_id, jenisBaru):
    for j in jenisAlat:
        if jenisAlat[j]["nama"] == jenisBaru:
            data_alat[alat_id]["jenis"] = jenisBaru
            data_alat[alat_id]["modal"] = jenisAlat[j]["modal"]
            data_alat[alat_id]["harga"] = jenisAlat[j]["harga"]
            data_alat[alat_id]["laba"] = hitung_laba(jenisAlat[j]["modal"], jenisAlat[j]["harga"])
            return True
    return False
