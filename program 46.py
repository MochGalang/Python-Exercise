username = "admin"
password = "nimda123"

input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username == username and input_password == password:
    print("Login berhasil!")
else:
    print("Username atau password salah.")