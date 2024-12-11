#Buat program yang meminta pengguna memasukkan 5 angka, kemudian mencetak angka terbesar di antara mereka.

angka = []

for i in range(5):
    num = int(input(f"Masukkan angka ke-{i + 1}: "))
    angka.append(num)

terbesar = max(angka)

print(f"Angka terbesar adalah: {terbesar}")