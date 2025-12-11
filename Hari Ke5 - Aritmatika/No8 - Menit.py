detik_str = input(f"masukkan detik : ")

detik_total = int(detik_str)

menit_total = detik_total // 60

detik_total = detik_total & 60

print(f"{detik_total} detik = {menit_total} menit = {detik_total} detik")