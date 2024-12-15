#Buat program untuk menghitung nilai indeks massa tubuh (IMT) menggunakan rumus: IMT = berat (kg) / (tinggi (m) * tinggi (m)).

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

IMT = berat / (tinggi ** 2)
print(f"Indeks Massa Tubuh adalah {IMT}")
