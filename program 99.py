#Tulis program untuk menentukan jumlah digit dari sebuah angka menggunakan rekursi.

def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

angka = int(input("Masukkan sebuah angka: "))
jumlah_digit = count_digits(angka)
print(f"Jumlah digit dari angka {angka} adalah {jumlah_digit}")
