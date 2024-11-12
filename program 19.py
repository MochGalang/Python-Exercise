#Buat program yang menerima input panjang tiga sisi segitiga dan menentukan jenis segitiga berdasarkan panjang sisinya:3
#Jika ketiga sisi sama, tampilkan "Segitiga Sama Sisi".
#Jika dua sisi sama, tampilkan "Segitiga Sama Kaki".
#Jika semua sisi berbeda, tampilkan "Segitiga Sembarang".

sisi1 = float(input("Masukkan panjang sisi 1: "))
sisi2 = float(input("Masukkan panjang sisi 2: "))
sisi3 = float(input("Masukkan panjang sisi 3: "))

if sisi1 == sisi2 == sisi3:
    print("Segitiga Sama Sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")
