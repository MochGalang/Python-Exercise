#Buat program yang menilai kelayakan pinjaman berdasarkan umur dan pendapatan bulanan. Syaratnya
#Umur minimal 21 tahun.
#endapatan bulanan minimal Rp3.000.000.
#ika memenuhi kedua syarat, tampilkan "Pinjaman Disetujui", jika tidak, tampilkan "Pinjaman Ditolak".

umur = int(input('Masukkan Umur Anda: '))
pendapatan = float(input('Masukkan Pendapatan Bulanan Anda:Rp '))

if umur >= 21 and pendapatan >= 3000000:
   print('Pinjaman Disetujui')
else:
   print('Pinjaman Ditolak')