print('='*40)
print('\t\tKERUCUT')
print('='*40)

phi = 3.14
r = int(input('masukkan nilai jari-jari: '))
s = float(input('masukkan nilai sisi\t: '))
t = float(input('masukkan nilai tinggi\t: '))

ls = phi * r * s
lp = (phi * r * s) + (phi * r ** 2)
v = 1/3 * phi * r ** 2 * t

print('Luas Selimut \t\t: ',ls, 'cm')
print('Luas permukaan \t\t: ',lp)
print('Volume \t\t\t: ',round(v,2))
