print('='*30)
print('\tRumus Tabung')
print('='*30)

phi = 3.14
r = float(input("Masukkan Jari-jari\t: "))
t = float(input("Masukkan Tinggi\t\t: "))

lp = 2 * phi * r * (t + r)

lp = int(lp)
print('Luas permukaan Tabung\t:',lp,'cm2')