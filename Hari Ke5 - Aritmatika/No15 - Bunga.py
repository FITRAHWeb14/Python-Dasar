Modal_awal = float(input(f"masukkan modal awal : "))
Bunga_tahun = float(input(f"masukkan bunga (%)per-tahun : "))
tahun = int(f"masukkan tahun : ")

hitung_awal = Bunga_tahun // 100
hitung_akhir = Modal_awal *(1 + hitung_awal) ** tahun

print(f"modal awal : {Modal_awal}")
print(f"bunga per-tahun : {Bunga_tahun}")
print(f"tahun bunga sekarang : {Bunga_tahun}")
print(f"hasil dari bunga per-tahun : {hitung_akhir}")