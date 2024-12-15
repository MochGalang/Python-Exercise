#Buat program untuk mengecek apakah sebuah string hanya mengandung huruf (tanpa angka atau simbol).

string = input("Masukkan string: ")

if string.isalpha():
    print("String hanya mengandung huruf")
else:
    print("String mengandung angka atau simbol")
