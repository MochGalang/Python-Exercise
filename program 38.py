teks = input("Masukkan sebuah teks: ")

vokal = "aeiouAEIOU"
jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)

print("Jumlah huruf vokal dalam teks adalah:", jumlah_vokal)
