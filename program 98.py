#Buat program untuk menerima input angka dan mencetak angka tersebut dalam format heksadesimal.

angka = int(input("Masukkan angka: "))

heksadesimal = hex(angka)
print(f"Angka {angka} dalam heksadesimal adalah {heksadesimal}")
