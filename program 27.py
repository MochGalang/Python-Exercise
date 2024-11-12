#Buat program Python yang meminta input angka dari pengguna, lalu hitung dan cetak faktorial dari angka tersebut menggunakan pengulangan while

n = int(input("Masukkan angka untuk menghitung faktorial: "))

faktorial = 1

i = 1
while i <= n:
    faktorial *= i
    i += 1

print(f"Faktorial dari {n} adalah: {faktorial}")

