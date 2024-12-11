#Tulis program untuk menghapus file dengan nama tertentu
import os

nama_file = input("Masukkan nama file yang ingin dihapus: ")

if os.path.exists(nama_file):
    os.remove(nama_file)
    print(f"File {nama_file} telah dihapus.")
else:
    print(f"File {nama_file} tidak ditemukan.")
