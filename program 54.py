def hitung_pangkat(a, b):
    return a ** b

bilangan = float(input("Masukkan bilangan (a): "))
pangkat = int(input("Masukkan pangkat (b): "))

hasil = hitung_pangkat(bilangan, pangkat)
print(f"Hasil dari {bilangan}^{pangkat} adalah {hasil:.2f}")
