#Buat program untuk mengecek apakah file tertentu ada di folder saat ini.

import os

nama_file = input("Masukkan nama file yang ingin dicek: ")

if os.path.isfile(nama_file):
    print(f"File {nama_file} ditemukan di folder saat ini.")
else:
    print(f"File {nama_file} tidak ditemukan di folder saat ini.")
