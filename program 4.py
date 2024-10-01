print('='*35)
print('\t\tBulan')
print('='*35)

Angka_bulan = int(input("Masukkan Bulan berupa Angka (1-12) : "))

if Angka_bulan == 1:
    bulan ='January'
elif Angka_bulan == 2:
    bulan ='February'
elif Angka_bulan == 3:
    bulan ='March'
elif Angka_bulan == 4:
    bulan ='April'
elif Angka_bulan == 5:
    bulan ='May'
elif Angka_bulan == 6:
    bulan ='June'
elif Angka_bulan == 7:
    bulan ='July'
elif Angka_bulan == 8:
    bulan ='August'
elif Angka_bulan == 9:
    bulan ='September'
elif Angka_bulan == 10:
    bulan ='October'
elif Angka_bulan == 11:
    bulan ='November'
elif Angka_bulan == 12:
    bulan ='December'
else:
    bulan = '-_-'

print('Nama Bulan:', bulan)