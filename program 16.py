#Buat program untuk menentukan status kerja karyawan berdasarkan jam kerja per minggu. Syaratnya:
#Jika jam kerja lebih dari 40, tampilkan "Full-time".
#jika jam kerja antara 20 dan 40, tampilkan "Part-time".
#Jika jam kerja kurang dari 20, tampilkan "Freelancer".

jam = int(input('Masukkan Jam Kerja Anda: '))

if jam >= 40:
    print('Status Kerja Anda: Full-time')
elif 20 <= jam <= 40:
    print('Status Kerja Anda: Part-time')
else:
    print('Status Kerja Anda: Freelancer')
