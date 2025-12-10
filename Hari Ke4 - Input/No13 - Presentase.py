presentase_harga = int(input(f"masukkan harga barang : "))
diskon = float(input(f"masukkan diskon dalam (%) : "))

dapat_diskon = presentase_harga  * diskon / 100

print(f"harga yang dimasukkan : {presentase_harga}")
print(f"diskon yang dimasukkan : {diskon}")
print(f"kamu mendapatkan diskon : {dapat_diskon}")