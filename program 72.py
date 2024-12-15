#Tulis program untuk mengurutkan kata-kata dalam sebuah kalimat berdasarkan panjangnya.

kalimat = input("Masukkan sebuah kalimat: ")

kata_list = kalimat.split()

kata_list_urut = sorted(kata_list, key=len)

print("Kata-kata setelah diurutkan berdasarkan panjangnya:")
print(" ".join(kata_list_urut))
