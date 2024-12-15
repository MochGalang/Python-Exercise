#Tulis program yang menerima input dari pengguna berupa sebuah kata dan mengganti semua huruf vokal dengan karakter ‘*’.

kata = input("Masukkan sebuah kata: ")

vokal = "AEIOUaeiou"
kata_baru = ''.join('*' if char in vokal else char for char in kata)

print(f"Kata setelah diganti vokal: {kata_baru}")
