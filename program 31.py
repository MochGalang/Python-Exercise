lampu_merah = "merah"
lampu_kuning = "kuning"
lampu_hijau ="hijau"

print('='*40)
print('\t  Lampu Lalu Lintas')
print('='*40)

lamp = (input("Masukkan Lampu Lalu Lintas: "))

if lamp == lampu_merah:
    print("Berhenti")
elif lamp == lampu_kuning:
    print('Bersiap')
elif lamp == lampu_hijau:
    print("Maju")
else:
    print('error')