Barang = input(f"masukkan barang yang ditoko : ")
jumlah_beli = int(input(f"masukkan yang mau di beli : "))
diskon = float(input(f"masukkan diskon yang anda mau : "))
ongkir = float(input(f"masukkan ongkir : "))

Total = (Barang * jumlah_beli) - diskon // 100+ ongkir

print(f"barang sudah dimasukkan : {Barang}")
print(f"jumlah yang sudah terbeli : {jumlah_beli}")
print(f"hasil semua : {Total}")