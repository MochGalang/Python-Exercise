#Buat program Python yang mencetak semua bilangan antara 1 hingga 20, tetapi lewati angka 13 menggunakan continue.

for i in range(1, 31):
    if i % 13 == 0:
        continue
    print(i)
