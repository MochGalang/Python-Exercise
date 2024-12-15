#Buat fungsi untuk mencari kata terpanjang dalam sebuah kalimat.

def cari_kata_terpanjang(kalimat):
    kata_list = kalimat.split()
    
    kata_terpanjang = max(kata_list, key=len)
    
    return kata_terpanjang

kalimat = input("Masukkan sebuah kalimat: ")

hasil = cari_kata_terpanjang(kalimat)
print(f"Kata terpanjang dalam kalimat adalah: '{hasil}' dengan panjang {len(hasil)} karakter.")
