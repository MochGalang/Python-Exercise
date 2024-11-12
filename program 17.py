#Buat program untuk mengecek kelayakan donor darah. Syaratnya:
#Usia harus di atas 17 tahun.
#Berat badan harus minimal 45 kg.
#Jika memenuhi kedua syarat, tampilkan "Bisa Donor".
#Jika tidak memenuhi, tampilkan "Tidak Bisa Donor".

usia = int(input('Masukkan Umur Anda: '))
berat_badan = int(input('Masukkan Berat Badan Anda: '))

if usia >= 17 and berat_badan >= 45:
    print('Bisa Donor')
else:
    print('Tidak Bisa Donor')