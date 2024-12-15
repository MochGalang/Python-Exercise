#Tulis fungsi untuk menghitung jumlah huruf vokal dalam string yang diberikan pengguna.

def hitung_vokal(kalimat):
    vokal = 'aeiouAEIOU'
    
    jumlah_vokal = sum(1 for char in kalimat if char in vokal)
    
    return jumlah_vokal

kalimat = input("Masukkan sebuah kalimat: ")

hasil = hitung_vokal(kalimat)
print(f"Jumlah huruf vokal dalam kalimat adalah: {hasil}")
