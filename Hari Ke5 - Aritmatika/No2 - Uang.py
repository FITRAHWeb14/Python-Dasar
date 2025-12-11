# Input dari pengguna
uang_awal = int(input("Masukkan uang awal kamu: "))
uang_dibelanjakan = int(input("Masukkan uang yang dibelanjakan: "))
uang_didapat = int(input("Masukkan uang yang didapat (misalnya tambahan, hadiah, dll): "))

# Hitung sisa uang akhir
sisa_uang = uang_awal - uang_dibelanjakan + uang_didapat

# Tampilkan hasil
print(f"\n--- Hasil Perhitungan ---")
print(f"Uang awal         : {uang_awal}")
print(f"Uang dibelanjakan : {uang_dibelanjakan}")
print(f"Uang yang didapat : {uang_didapat}")
print(f"Sisa uang akhir   : {sisa_uang}")