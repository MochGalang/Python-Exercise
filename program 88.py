#Buat program untuk mengonversi bilangan desimal ke biner.

def desimal_ke_biner(n):
    if n == 0:
        return "0"
    biner = ""
    while n > 0:
        biner = str(n % 2) + biner
        n //= 2
    return biner

desimal = int(input("Masukkan bilangan desimal: "))

print(f"Biner dari {desimal} adalah: {desimal_ke_biner(desimal)}")

