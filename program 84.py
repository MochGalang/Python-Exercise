#Tulis program untuk menjumlahkan semua angka dalam sebuah string.

def jumlahkan_angka_dalam_string(teks):
    total = 0
    angka = ""
    
    for karakter in teks:
        if karakter.isdigit():
            angka += karakter
        else:
            if angka:
                total += int(angka)
                angka = ""
    
    if angka:
        total += int(angka)
    
    return total

teks = input("Masukkan sebuah string: ")

hasil = jumlahkan_angka_dalam_string(teks)
print(f"Jumlah semua angka dalam string adalah: {hasil}")
