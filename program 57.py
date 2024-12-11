def cek_armstrong(angka):

    jumlah_digit = len(str(angka))
    
    total = sum(int(digit) ** jumlah_digit for digit in str(angka))
    
    return total == angka

angka = int(input("Masukkan sebuah angka: "))

if cek_armstrong(angka):
    print(f"{angka} adalah bilangan Armstrong.")
else:
    print(f"{angka} bukan bilangan Armstrong.")
