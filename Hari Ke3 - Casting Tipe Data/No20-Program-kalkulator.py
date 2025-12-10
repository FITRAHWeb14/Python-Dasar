angka1 = "200" 
angka2 = "900"

mengubah1 = int(angka1)
mengubah2 = int(angka2)

perjumlaham = int(mengubah1) + int(mengubah2)
perkalian = int(mengubah1) * int(mengubah2)
pengurangan = int(mengubah1) - int(mengubah2)
pembagian = int(mengubah1) / int(mengubah2)

pembagian_float = f"{pembagian:.2f}"

#hasil
print(f"perjumlahan = {perjumlaham}")
print(f"perkalian = {perkalian}")
print(f"pengurangan = {pengurangan}")
print(f"pembagian = {pembagian_float}")