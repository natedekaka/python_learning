#!/usr/bin/env python3
"""
Latihan Praktik - Data Pelajaran & Info Diri
==============================================

TODO:
1. Isi list dengan nilai 5 mata pelajaran Anda
2. Hitung rata-rata, nilai tertinggi, dan terendah
3. Buat dictionary dengan info diri Anda
"""

# ===== TASK 1: Nilai 5 Mata Pelajaran =====
# TODO: Ganti dengan nilai mata pelajaran Anda
nilai_pelajaran = [85, 90, 78, 95, 88]

print("=== TASK 1: NILAI MATA PELAJARAN ===")
print(f"Nilai: {nilai_pelajaran}\n")

# TODO: Hitung rata-rata (gunakan sum() dan len())
rata_rata = sum(nilai_pelajaran) / len(nilai_pelajaran)
print(f"Rata-rata: {rata_rata}")
# TODO: Hitung nilai tertinggi (gunakan max())
nilai_max = max(nilai_pelajaran)
print(f"Nilai Tertinggi: {nilai_max}")

# TODO: Hitung nilai terendah (gunakan min())
nilai_min = min(nilai_pelajaran)
print(f"Nilai Terendah: {nilai_min}")

# ===== TASK 2: Info Diri =====
print("=== TASK 2: INFO DIRI ===")

# TODO: Buat dictionary dengan informasi diri Anda
# Isi: nama, umur, kota, pekerjaan, hobi
info_diri = {
    "nama" : "Dani",
    "umur" : 46,
    "kota" : "Cimahi",
    "pekerjaan" : "Guru",
    "hobi" : "koding"
}

# TODO: Print info dari dictionary Anda
# Hint: gunakan print(info_diri)


print(info_diri)

# ===== CHALLENGE (Opsional) =====
print("=== CHALLENGE ===")
# TODO: Print setiap info dengan format yang lebih rapi
# Contoh output yang diinginkan:
# Nama: Ari
# Umur: 25
# Kota: Jakarta
# dst...

# Hint: gunakan loop atau print satu-satu dengan f-string
print(f"Nama : {info_diri['nama']}")
print(f"Umur : {info_diri['umur']}")
print(f"Kota : {info_diri['kota']}")
print(f"Pekerjaan : {info_diri['pekerjaan']}")
print(f"Hobi : {info_diri['hobi']}")