#Buat program yang meminta input usia dan menentukan apakah seseorang sudah bisa mendapatkan SIM (Surat Izin Mengemudi).
#Syaratnya: usia minimal 17 tahun.

umur = int(input('Masukkan Umur anda: '))

if umur >= 17:
    print('Anda sudah bisa mendapatkan SIM')
else:
    print('Anda belum bisa mendapatkan SIM')