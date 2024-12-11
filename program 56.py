nilai_siswa = {
    "Frans": 85,
    "Syafiq": 90,
    "Alif": 78,
    "Faris": 88,
    "Cahyo": 92
}

nama = input("Masukkan nama siswa untuk melihat nilainya: ")

if nama in nilai_siswa:
    print(f"Nilai {nama} adalah {nilai_siswa[nama]}")
else:
    print(f"Maaf, {nama} tidak ditemukan dalam daftar.")
