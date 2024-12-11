#Buat program untuk menambahkan teks "Hei tayo ke file yang ada.

with open("catatan.txt", "a") as file:

    file.write("Hei tayo")

print("Teks berhasil di tambah ke catatan.txt")
