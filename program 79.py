#Buat program untuk menggantikan semua spasi dalam sebuah kalimat dengan tanda garis bawah (_).

def ganti_spasi(dalam_kalimat):
    kalimat_ganti = dalam_kalimat.replace(" ", "_")
    return kalimat_ganti

kalimat = input("Masukkan sebuah kalimat: ")

hasil = ganti_spasi(kalimat)
print(f"Kalimat setelah diganti: {hasil}")
