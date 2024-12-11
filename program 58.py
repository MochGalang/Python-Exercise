def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

suhu_fahrenheit = celcius_ke_fahrenheit(suhu_celcius)

print(f"{suhu_celcius:.2f}°C sama dengan {suhu_fahrenheit:.2f}°F")
