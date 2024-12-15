#Buat program untuk memeriksa apakah dua string adalah anagram (contoh: "listen" dan "silent").

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)
string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")

if is_anagram(string1, string2):
    print(f"{string1} dan {string2} adalah anagram.")
else:
    print(f"{string1} dan {string2} bukan anagram.")
