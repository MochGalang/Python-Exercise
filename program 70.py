#Tulis program untuk membuat list yang berisi kuadrat dari bilangan 1 hingga angka yang dimasukkan pengguna.

angka = int(input("Masukkan angka: "))

kuadrat_list = [i**2 for i in range(1, angka + 1)]

print(f"List kuadrat dari 1 hingga {angka}: {kuadrat_list}")
