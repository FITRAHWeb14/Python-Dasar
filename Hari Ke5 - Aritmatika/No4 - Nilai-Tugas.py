Nilai_Tugas = float(input(f"Masukkan Nilai tugas(0-100): "))
Nilai_UTS = float(input(f"Masukkan Nilai UTS(0-100): "))
Nilai_Uas = float(input(f"Masukkan Nilai Uas(0-100): "))

Hasil_Nilai = (Nilai_Tugas * 0.40) + (Nilai_UTS * 0.30) + (Nilai_Uas * 0.30)

print(f"kamu mendapatkan : {Nilai_Tugas}")
print(f"kamu mendapatkan Nilai uts : {Nilai_UTS}")
print(f"kamu mendapatkan nilai : {Nilai_Uas}")
print(f"hasil dari semua nilai kamu : {Hasil_Nilai}")