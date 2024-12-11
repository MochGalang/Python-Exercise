#bikin kalkulator sederhana

def kalkulator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return "Operator tidak valid."

print("Kalkulator Sederhana")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operasi = input("Masukkan operator (+, -, *, /): ")


hasil = kalkulator(angka1, angka2, operasi)


print(f"Hasil: {hasil}")
