#Buat program untuk mencetak deret Fibonacci hingga angka tertentu.

def deret_fibonacci(n):
    a, b = 0, 1
    print("Deret Fibonacci:")
    
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

angka_tertentu = int(input("Masukkan batas angka untuk deret Fibonacci: "))

deret_fibonacci(angka_tertentu)
