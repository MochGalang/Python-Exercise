#Buat program untuk membuat file baru dan menulis "Wazzap" ke dalamnya

with open("catatan.txt", "w") as file:

    file.write("Wazzap")

print("File 'catatan.txt' berhasil dibuat dan diisi.")
