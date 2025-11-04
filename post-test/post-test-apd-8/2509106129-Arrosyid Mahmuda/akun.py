# akun.py
from data import dataAkun
from barang import clear

def daftar():
    clear()
    print("=== DAFTAR AKUN ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in dataAkun:
        print("Username sudah terdaftar!\n")
    else:
        dataAkun[username] = {"password": password, "role": 0}
        print("Registrasi berhasil!\n")
    input("Tekan Enter...")

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    if username in dataAkun and dataAkun[username]["password"] == password:
        print("Login berhasil!\n")
        return username, dataAkun[username]["role"]
    else:
        print("Username atau password salah!\n")
        input("Tekan Enter...")
        return None, None
