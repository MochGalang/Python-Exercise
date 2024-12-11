kata = input("Masukkan sebuah kata: ")

kata_terbalik = kata[::-1]

if kata == kata_terbalik:
    print(f'"{kata}" adalah palindrom.')
else:
    print(f'"{kata}" bukan palindrom.')
