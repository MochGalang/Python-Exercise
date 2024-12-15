#Tulis program yang meminta input tanggal, bulan, dan tahun, lalu menentukan apakah tanggal tersebut adalah valid atau tidak.

tanggal = int(input("Masukkan tanggal: "))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun: "))

def is_valid_date(tanggal, bulan, tahun):
    if bulan < 1 or bulan > 12:
        return False
    if bulan in [4, 6, 9, 11] and tanggal > 30:
        return False
    elif bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            if tanggal > 29:
                return False
        else:
            if tanggal > 28:
                return False
    else:
        if tanggal > 31:
            return False
    return True

if is_valid_date(tanggal, bulan, tahun):
    print("Tanggal valid")
else:
    print("Tanggal tidak valid")
