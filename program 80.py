#Tulis program untuk menghitung jumlah angka genap dalam sebuah list.

def hitung_angka_genap(angka_list):
    jumlah_genap = sum(1 for angka in angka_list if angka % 2 == 0)
    return jumlah_genap

angka_input = input("Masukkan angka-angka dalam list (pisahkan dengan spasi): ")
angka_list = [int(angka) for angka in angka_input.split()]

hasil = hitung_angka_genap(angka_list)
print(f"Jumlah angka genap: {hasil}")
