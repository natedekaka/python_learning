daftar_hadir = ["H", "H", "S", "H", "A", "H", "S"]

jumlah_hadir = 0
jumlah_sakit = 0
jumlah_alpa = 0

for status in daftar_hadir:
    if status == "H":
        jumlah_hadir = jumlah_hadir + 1
    elif status == "S":
        jumlah_sakit = jumlah_sakit + 1
    else :
        jumlah_alpa = jumlah_alpa + 1

print("== REKAP ABSENSI HARI INI ==")
print(f"Siswa Hadir : {jumlah_hadir}")
print(f"Siswa Sakit : {jumlah_sakit}")
print(f"Siswa Alpa  : {jumlah_alpa}")
print("==========================")