Nama = input(f"masukkan nama : ")
barang = input(f"masukkan nama barang yang ingin dibeli : ")
Produk = int(input(f"masukkan harga produk : "))
Jumlah_beli = int(input(f"kamu beli berapa : "))
Ongkos = float(input(f"masukkan ongkos (RP): "))


hitung = Produk * Jumlah_beli
struk = hitung - Ongkos

print(f"nama pembeli : {Nama}")
print(f"kamu memasukkan barang ; {barang}")
print(f"total : {hitung}")
print(f"kamu mendapatkan total harga : {struk}")