#Buat program yang mencetak angka 1 sampai 100, tetapi untuk angka kelipatan 3 cetak "Fizz",
#  kelipatan 5 cetak "Buzz", dan kelipatan 15 cetak "FizzBuzz".

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

