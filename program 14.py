#Buat program yang menentukan apakah seorang anak mendapatkan diskon atau tidak ketika membeli mainan. 
# Jika harga mainan lebih dari 100.000, anak tersebut mendapat diskon 10%.
#  Tampilkan harga setelah diskon jika memenuhi syarat, atau tampilkan harga aslinya jika tidak.

print('='*40)
print('\t  CEK DISKON MAINAN')
print('='*40)

harga = int(input('Masukkan Harga Mainan: Rp '))

if harga > 100000:
    diskon = harga * 0.10
    harga_setelah_diskon = harga - diskon
    print("Kamu mendapatkan diskon 10%!")
    print("Harga setelah diskon: Rp", harga_setelah_diskon)
else:
    print("Tidak ada diskon")
    print("Harga yang harus dibayar: Rp", harga)