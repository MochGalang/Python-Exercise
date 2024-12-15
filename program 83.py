#Tulis program untuk memeriksa apakah sebuah bilangan terdiri dari digit yang selalu naik (ascending).

def cek_digit_naik(bilangan):
    bil_str = str(bilangan)
    for i in range(len(bil_str) - 1):
        if bil_str[i] >= bil_str[i + 1]:
            return False
    return True

angka = int(input("Masukkan sebuah bilangan: "))

if cek_digit_naik(angka):
    print(f"{angka} terdiri dari digit yang selalu naik (ascending).")
else:
    print(f"{angka} tidak terdiri dari digit yang selalu naik (ascending).")
