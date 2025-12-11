masukkan_uang = int(input(f"masukkan uang anda : "))
masukkan_harga = int(input(f"masukkan harga : "))

hasil1 = masukkan_uang // masukkan_harga
hasil2 = masukkan_uang % masukkan_harga

print(f"uang anda ada segini : {masukkan_uang}")
print(f"harga : {masukkan_harga}")
print(f"hasil : {hasil1}")
print(f"hasil 2 : {hasil2}")