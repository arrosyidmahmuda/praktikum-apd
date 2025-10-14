# # #mendefinisikan list
# # praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# # print(praktikum[4][1])

# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.append("Web")
# print(studyclub)

# list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.insert(1,"Web")
# print(studyclub)

# list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub[2] = "AI"
# print(studyclub)

# del itu hapusnya dengan elemen
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen pada indeks ke-2, yakni "Kalkulus"
# del matakuliah[2]
# print(matakuliah)

# # remove untuk variable mana yg mau kita hapus
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # menghapus elemen dengan nilai "Kalkulus"
# matakuliah.remove('Kalkulus')
# print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# # Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
# sampah = matakuliah.pop(2)
# print(matakuliah)
# print(sampah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[0:7:3])#formatnya: nama_list[start:stop:step]

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[0::3])#formatnya: nama_list[start:stop:step]

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# # Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
# print(matakuliah[::2])#formatnya: nama_list[start:stop:step]

# a = [1, 2, 3]
# b = [4, 5, 6]
# # menggabungkan kedua list dengan operator (+)
# c = a + b
# d = [1,4,5]
# e = [1,2,4]
# f = d + e
# print(c+f)

# # Membuat Nested List
# kelas = [
# ["Ridho", "Lian", "Nabil"],#list 0
# ["Daffa", "Dante", "Santoso"], #list 1
# ["Pernanda", "Riyadi", "Ahnaf"] # list 2
# ]
# print(kelas[0][1])
# # Memanggil elemen "Santoso"

# Membuat Nested List
# kelas = [
# ["Ridho", "Lian", "Nabil"],["Daffa", "Dante", "Santoso"],["Pernanda", "Riyadi", "Ahnaf"] # list 2
# ]

# print(kelas[0][2][0])
# Memanggil elemen "Santoso"

# list mahasiswa
# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#  print(i)
#  for j in i :
#   print (j)
# # i dan j merupakan variabel sementara / temporary, kita dapat menggantinya
# dengan apa saja asal sesuai dengan syarat nama variabel

# #mendefinisikan tuple
# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota)

# # tuple
# tugas = ('rangkuman', 'arduino','scrapping')
# # beri variabel setiap values
# (PTI, orsikom, basisdata) = tugas
# print(PTI)
# print(orsikom)
# print(basisdata)

# # tuple
# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# # beri variabel setiap values
# (segitiga, bulat, *kotak) = barang
# print(segitiga)
# print(bulat)
# print(kotak)

# # tuple
# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# # beri variabel setiap values
# (segitiga, bulat, *kotak) = barang
# print(segitiga)
# print(bulat)
# print(kotak)

# # tuple
# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# angka=(1,2,3)
# # simpan di dalam variabel baru
# gabung=barang+angka
# print(gabung)
# # output
# ('triangle', 'bola', 'meja', 'handphone', 'televisi', 1, 2, 3)

# barang = [["triangle",'bola'], ['meja','handphone'], ['televisi','laptop']]

# for nama_barang in barang:
#     print(nama_barang)
#     (barang1, barang2) = nama_barang
#     print(barang1)
#     print(barang2)

# buatkan list yang berisi 2 list dan 1 tuple,
# gunakan perulangan untuk mengeluarkan list satu persatu dan unpacking untuk tuple

# mahasiswa = [["satu","dua"],[]]

# kelas = [
# ["Ridho", "Lian", "Nabil"],#list 0
# ["Daffa", "Dante", "Santoso"], #list 1
mahasiswa = [["asoy","yosa"],["bib","bub"],("bas","sah")]
for nama_mahasiswa in mahasiswa:
    
