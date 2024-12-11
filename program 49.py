usia = int(input("Masukkan usia Anda: "))

if usia < 12:
    harga = 20000
elif 12 <= usia <= 17:
    harga = 30000
elif 18 <= usia <= 59:
    harga = 50000
else:
    harga = 25000

print(f"Harga tiket untuk usia {usia} tahun adalah Rp {harga:,}.")
