print('='*30)
print('\tPengecek Umur')
print('='*30)

nama = input("Masukkan Nama Anda: ")
umur = int(input('Masukkan umur Anda: '))

if umur >= 35:
   print(f"{nama}, Anda sudah dewasa")
elif 18 <= umur <= 35:
   print(f"{nama}, Anda Dewasa Muda")
elif umur < 18:
   print(f"{nama}, Anda Belum Dewasa")
else :
   print(f"{nama}, Umur Anda tidak valid")