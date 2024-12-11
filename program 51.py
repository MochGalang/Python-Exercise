my_list = [10, 21, 32, 43, 54, 65, 76, 87, 98]

even_numbers = []
odd_numbers = []

for num in my_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Mencetak hasil
print("Genap:", even_numbers)
print("Ganjil:",odd_numbers)