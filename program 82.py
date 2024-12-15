#Tulis program untuk menggabungkan dua list dan menghapus elemen duplikat.

# Program untuk menggabungkan dua list dan menghapus elemen duplikat

def gabungkan_list(list1, list2):
    gabungan = list1 + list2
    tanpa_duplikat = list(set(gabungan))
    tanpa_duplikat.sort()
    return tanpa_duplikat

#contoh
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

hasil = gabungkan_list(list1, list2)

print("Hasil penggabungan tanpa duplikat:", hasil)
