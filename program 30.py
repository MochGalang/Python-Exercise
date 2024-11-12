#Tulis program Python yang menggunakan for loop untuk menampilkan deret angka mulai dari 1 hingga angka n yang dimasukkan oleh pengguna.
#Program harus menampilkan deret angka dengan jarak antar angka 5.

n = int(input("Masukkan angka: "))

for i in range(1, n+1, 5):
        print(i)