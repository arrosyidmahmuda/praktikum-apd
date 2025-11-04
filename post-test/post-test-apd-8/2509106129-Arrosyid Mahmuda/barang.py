# util.py
import os
from prettytable import PrettyTable
from data import jenisAlat, data_alat

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hitung_laba(modal, harga):
    return harga - modal

def hitung_total_laba():
    return sum(a["laba"] for a in data_alat.values())

def tampilkan_semua_jenis():
    tabel = PrettyTable(["No", "Nama Alat", "Modal (Rp)", "Harga (Rp)"])
    for j, data in jenisAlat.items():
        tabel.add_row([j, data["nama"], data["modal"], data["harga"]])
    print(tabel)

def tampilkan_data_alat():
    if not data_alat:
        print("Belum ada data alat.\n")
        input("Tekan Enter...")
        return
    tabel = PrettyTable(["ID", "Nama", "Jenis", "Modal", "Harga", "Laba"])
    for i, a in data_alat.items():
        tabel.add_row([i, a["nama"], a["jenis"], a["modal"], a["harga"], a["laba"]])
    print(tabel)
    print(f"Total Laba: Rp{hitung_total_laba()}\n")
    input("Tekan Enter...")
