#Buat fungsi untuk mengonversi angka Romawi ke angka Arab (contoh: XII menjadi 12).

def romawi_ke_arab(romawi):
    nilai_romawi = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(romawi):
        current_value = nilai_romawi[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

romawi = input("Masukkan angka Romawi: ").upper()
hasil = romawi_ke_arab(romawi)
print(f"Angka Arab dari {romawi} adalah: {hasil}")
