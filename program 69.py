def segitiga_pascal(baris):
    for i in range(baris):
        print(" " * (baris - i), end="")
        
        nilai = 1
        for j in range(i + 1):
            print(f"{nilai} ", end="")
            nilai = nilai * (i - j) // (j + 1)
        
        print()

jumlah_baris = int(input("Masukkan jumlah baris: "))
segitiga_pascal(jumlah_baris)
