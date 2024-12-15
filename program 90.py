#Tulis fungsi untuk mengonversi tanggal dari format DD/MM/YYYY ke format MM-DD-YYYY.

def konversi_tanggal(dd_mm_yyyy):
    tanggal_parts = dd_mm_yyyy.split('/')
    mm_dd_yyyy = f"{tanggal_parts[1]}-{tanggal_parts[0]}-{tanggal_parts[2]}"
    return mm_dd_yyyy

tanggal = input("Masukkan tanggal dalam format DD/MM/YYYY: ")

print(f"Tanggal dalam format MM-DD-YYYY adalah: {konversi_tanggal(tanggal)}")
