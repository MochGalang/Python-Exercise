#Tulis program untuk menghentikan perulangan jika angka kelipatan 3 ditemukan (1-20).

for i in range(1, 21):
    if i % 3 == 0:
        break
    print(i)
