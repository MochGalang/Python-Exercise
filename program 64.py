#Buat fungsi untuk mengubah huruf besar dalam string menjadi huruf kecil dan sebaliknya.

def ubah_kapital(teks):
    return teks.swapcase()


teks_asli = input("Masukkan sebuah string: ")

teks_diubah = ubah_kapital(teks_asli)

print("Teks asli:", teks_asli)
print("Teks setelah diubah:", teks_diubah)
