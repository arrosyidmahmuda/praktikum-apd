# angka = int("10")

# print(type(angka))

# angka = [2, 8778, 312, 4134, 12, 34, 123]

# print(max(angka))
# print(min(angka))

# for i, v in enumerate(['a','b']):
#   print(i, v) # 0 a , 1 b

# panjang = len([10, 20, 30]) # 3

# list(map(str, [1,2,3])) # ['1', '2', '3']

# sorted([3, 1, 2]) # [1, 2, 3]

# tulis = list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

# print(panjang)
# print(tulis)

# x = 42
# y = 40
# def fungsi():
#    x = 10
#    y = 20
#    z = 30
#    print(globals()['y']) # mendapatkan isi dari variabel x (global)
#    print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
#    print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# import math
# from math import sqrt
# import math as m

# print(math.sqrt(16))
# print(math.factorial(4))

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#   hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu)# kocok kartu, output berupa urutan list yang berubah
# print(acak_kartu)

# from datetime import datetime
# print(datetime.now())

# import inquirer
# pertanyaan = [
# inquirer.List(
# 'size',
# message="What size do you need?",
# choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
# ),
# ]
# # mendapatkan jawaban
# answer = inquirer.prompt(pertanyaan)
# print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
# print(answer['size']) # Ambil value dari key 'size' (Large)

# def login(username, password):
# # Logika untuk memeriksa username dan password
#    print(f"Memverifikasi {username}...")
#    if username == "admin" and password == "123":
#       return True
#    return False

# from autentikasi import login
# from create import tambah_data_siswa

# print("Selamat datang di aplikasi!")

# # Menggunakan modul login
# if login("admin", "123"):
#     print("Login berhasil!")
# # Menggunakan modul create
#     tambah_data_siswa({"nama": "Budi", "nilai": 90})
# else:
#     print("Login gagal!")

import random

karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""

# memilih 12 karakter acak
for i in range(12):
    kata_sandi += random.choice(karakter)

print("Kata sandi acak:", kata_sandi)
