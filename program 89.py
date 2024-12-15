#Buat fungsi untuk mengurutkan kata-kata dalam sebuah kalimat berdasarkan abjad.

def urutkan_kata_berdasarkan_abjad(kalimat):
    kata_kata = kalimat.split()
    urutkan = sorted(kata_kata)
    return " ".join(urutkan)

kalimat = input("Masukkan sebuah kalimat: ")

print("Kata-kata dalam kalimat yang diurutkan berdasarkan abjad:")
print(urutkan_kata_berdasarkan_abjad(kalimat))
