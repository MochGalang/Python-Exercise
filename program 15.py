#Buat program yang meminta pengguna memasukkan angka dan menentukan apakah angka tersebut positif, negatif, atau nol:
#Jika angka lebih dari 0, tampilkan "Bilangan Positif".
#Jika angka kurang dari 0, tampilkan "Bilangan Negatif".
#Jika angka sama dengan 0, tampilkan "Nol".

print('='*40)
print('\t  ANGKA POSITIF NEGATIF')
print('='*40)

angka = int(input("Masukkan Angka: "))

if angka > 0:
    print("Bilangan Positif")
elif angka < 0:
    print('Bilangan Negatif')
else:
    print('Nol')