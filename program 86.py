#Buat program untuk mencetak bilangan kelipatan 3 dari 1 hingga N (dimana N dimasukkan oleh pengguna).

def cetak_kelipatan_3(N):
    for i in range(3, N + 1, 3):
        print(i)

N = int(input("Masukkan angka N: "))

print("Bilangan kelipatan 3 dari 1 hingga", N, "adalah:")
cetak_kelipatan_3(N)
