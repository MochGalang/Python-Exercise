#Tulis program untuk mengonversi jumlah detik yang dimasukkan pengguna menjadi format HH:MM:SS.

total_detik = int(input("Masukkan jumlah detik: "))

jam = total_detik // 3600
menit = (total_detik % 3600) // 60
detik = total_detik % 60

print(f"Waktu konversi: {jam:02d}:{menit:02d}:{detik:02d}")
