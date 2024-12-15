#Buat fungsi untuk menemukan kata yang paling sering muncul dalam sebuah string.

def kata_tersering(string):
    kata_list = string.split()
    freq = {}
    
    for kata in kata_list:
        if kata in freq:
            freq[kata] += 1
        else:
            freq[kata] = 1
    
    kata_tersering = max(freq, key=freq.get)
    return kata_tersering, freq[kata_tersering]

input_string = input("Masukkan sebuah kalimat: ")

tersering, frekuensi = kata_tersering(input_string)

print(f"Kata yang paling sering muncul adalah '{tersering}' dengan frekuensi {frekuensi}.")
