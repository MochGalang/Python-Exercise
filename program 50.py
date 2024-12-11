N = int(input("Masukkan batas atas (N): "))

print("Deret bilangan ganjil:")
for i in range(1, N + 1):
    if i % 2 != 0:
        print(i, end=" ")
