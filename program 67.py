#Tulis program untuk membalik urutan kata dalam sebuah kalimat.
#Contoh:
#Input: Halo dunia Python
#Output: Python dunia Halo


kalimat = input("Masukkan sebuah kalimat: ")


kata_kata = kalimat.split() 
kata_kata_terbalik = kata_kata[::-1] 
kalimat_terbalik = " ".join(kata_kata_terbalik)  

print("Kalimat asli:", kalimat)
print("Kalimat setelah dibalik:", kalimat_terbalik)
