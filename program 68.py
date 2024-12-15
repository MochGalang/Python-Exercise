#Tulis fungsi untuk menghitung faktorial dari suatu angka.

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1) 

angka = int(input("Masukkan angka: "))

if angka < 0:
    print("Faktorial tidak didefinisikan untuk angka negatif.")
else:
    print(f"Faktorial dari {angka} adalah {faktorial(angka)}")
