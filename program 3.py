print('='*40)
print('\t     NILAI MAHASISWA')
print('='*40)

Nama_Siswa = (input('Masukkan Nama Siswa\t: '))
Nilai = int(input("Masukkan Nilai Siswa\t: "))

if Nilai >= 80: grade = 'A'
elif 70 <= Nilai <= 80: grade = 'B'
elif 55 <= Nilai <= 70: grade = 'C'
elif 40 <= Nilai <= 55: grade = 'D'
else: grade = 'E'

print('Nama Siswa\t:',Nama_Siswa)
print('Nilai Siswa\t:',Nilai)
print('Grade\t\t:',grade)