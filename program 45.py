#Buat program untuk menghitung jumlah digit dalam sebuah bilangan, misalnya 12345 memiliki 4 digit.

angka = (input("Masukkan angka: "))

jumlah_digit = len(angka)

if jumlah_digit == 1:
    print("1 digit")
elif jumlah_digit == 2:
    print('2 digit')
elif jumlah_digit == 3:
    print("3 digit")
elif jumlah_digit == 4:
    print("4 digit")
else:
    print('error')