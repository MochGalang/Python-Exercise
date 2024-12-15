#Buat program untuk menentukan apakah sebuah angka merupakan bilangan sempurna atau tidak. (Bilangan sempurna adalah bilangan positif yang sama dengan jumlah semua pembaginya)

def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

bilangan = int(input("Masukkan sebuah bilangan: "))

if is_perfect_number(bilangan):
    print(f"{bilangan} adalah bilangan sempurna")
else:
    print(f"{bilangan} bukan bilangan sempurna")
