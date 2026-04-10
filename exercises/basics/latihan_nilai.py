daftar_nilai = [60,85,90,45,75,80]
print("===LAPORAN HASIL UJIAN===")

for nilai in daftar_nilai:
    if nilai >= 75:
        status = "LUlUS"
    else:
        status = "REMEDIAL"

    print(f"nilai siswa : {nilai} -> Status : {status}")
print("===============================")