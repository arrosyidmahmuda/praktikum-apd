# # # # # # simpan = [1, 'Dapupu' , 4.00, True]
# # # # # # for i in simpan:
# # # # # #  print(i)

# # # # # simpan = ["jaaa",'yaa', 'jaa']
# # # # # for isilist in simpan:
# # # # #     print(isilist)

# # # # for i in range (1, 1001, 1):
# # # #     print(i)

# # # # for i in range (1, 4):
# # # #     print(f'i: {i}')
# # # #     for j in range (1, 3):
# # # #         print(f'i: {i}')
# # # #         for k in range (1, 3):
# # # #             print(f'i: {i}, j: {j}, (k: {k})')
# # # #     print('')

# # #  for i in range (1, 4):
# # #     print(f'i: {i}')
# # #     for j in range (1, 3):
# # #         print(f'i: {i}')
# # #         for k in range (1, 3):
# # #             print(f'i: {i}, j: {j}, (k: {k})')
# # #     print('')

# # jawab = 'ya'
# # hitung = 0
# # while(jawab == 'ya'):
# #   hitung += 1
# #   jawab = input("Ulang lagi? ")
# # print(f"Total perulangan: {hitung}")

# hitung = 0
# while(True):
#   print(hitung)
#   hitung += 1
#   if hitung % 2 == 0:
#     continue
#   if hitung == 21:
#     break
# print(f"Total perulangan: {hitung}")

for i in range(1, 11):
  if i % 2 != 0:
   continue
  print(f"Angka genap ditemukan: {i}")
print("\nProgram selesai.")

# % = bagi  