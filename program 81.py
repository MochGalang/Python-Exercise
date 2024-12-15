#Tulis fungsi untuk menghitung jumlah angka positif, negatif, dan nol dalam sebuah list.

def hitung_angka(angka_list):
    jumlah_positif = sum(1 for angka in angka_list if angka > 0)
    jumlah_negatif = sum(1 for angka in angka_list if angka < 0)
    jumlah_nol = sum(1 for angka in angka_list if angka == 0)
    return jumlah_positif, jumlah_negatif, jumlah_nol

angka_input = input("Masukkan angka-angka dalam list (pisahkan dengan spasi): ")
angka_list = [int(angka) for angka in angka_input.split()]

positif, negatif, nol = hitung_angka(angka_list)
print(f"Jumlah angka positif: {positif}")
print(f"Jumlah angka negatif: {negatif}")
print(f"Jumlah angka nol: {nol}")
