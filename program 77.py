#Tulis program untuk menghapus elemen ganjil dari sebuah list.

def hapus_elemen_ganjil(lista):
    hasil = [x for x in lista if x % 2 == 0]
    return hasil

input_list = list(map(int, input("Masukkan elemen list (pisahkan dengan spasi): ").split()))

hasil = hapus_elemen_ganjil(input_list)

print("List setelah menghapus elemen ganjil:", hasil)
