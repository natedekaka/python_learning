#!/usr/bin/env python3
"""
Phase 3: Functions & String Operations
=======================================
Belajar: def, parameters, return, string methods
"""

print("=" * 50)
print("PHASE 3: FUNCTIONS & STRING OPERATIONS")
print("=" * 50)

# ===== 1. BASIC FUNCTIONS =====
print("\n=== 1. BASIC FUNCTIONS ===\n")

# Fungsi tanpa parameter
def sapa():
    print("Halo, selamat datang!")

sapa()

# Fungsi dengan parameter
def ucapkan_nama(nama):
    print(f"Halo, {nama}!")

ucapkan_nama("Dani")
ucapkan_nama("Ari")

# Fungsi dengan multiple parameter
def tambah(a, b):
    hasil = a + b
    return hasil  # Mengembalikan nilai

hasil = tambah(5, 3)
print(f"5 + 3 = {hasil}")

# ===== 2. DEFAULT PARAMETERS =====
print("\n=== 2. DEFAULT PARAMETERS ===\n")

def hitung_nilai(nama, nilai=0):
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"{nama}: Nilai {nilai} -> Grade {grade}")

hitung_nilai("Ari", 85)
hitung_nilai("Budi", 92)
hitung_nilai("Citra")  # Gunakan default nilai=0

# ===== 3. MULTIPLE RETURN VALUES =====
print("\n=== 3. MULTIPLE RETURN VALUES ===\n")

def statistik_nilai(nilai_list):
    total = sum(nilai_list)
    rata_rata = total / len(nilai_list)
    tertinggi = max(nilai_list)
    terendah = min(nilai_list)
    
    return rata_rata, tertinggi, terendah

nilai = [85, 90, 78, 95, 88]
rata_rata, max_val, min_val = statistik_nilai(nilai)

print(f"Nilai: {nilai}")
print(f"Rata-rata: {rata_rata}")
print(f"Tertinggi: {max_val}")
print(f"Terendah: {min_val}")

# ===== 4. STRING OPERATIONS =====
print("\n=== 4. STRING OPERATIONS ===\n")

text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Strip: '{text.strip()}'")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Find: {text.find('Program')}")
print(f"Length: {len(text)}")

# ===== 5. STRING METHODS =====
print("\n=== 5. MORE STRING METHODS ===\n")

kalimat = "Saya belajar Python"
print(f"Original: {kalimat}")
print(f"Split: {kalimat.split()}")  # Pisah berdasarkan spasi
print(f"Startswith 'Saya': {kalimat.startswith('Saya')}")
print(f"Endswith 'Python': {kalimat.endswith('Python')}")
print(f"Count 'a': {kalimat.count('a')}")
print(f"Capitalize: {kalimat.capitalize()}")
print(f"Title: {kalimat.title()}")

# ===== 6. STRING FORMATTING =====
print("\n=== 6. STRING FORMATTING ===\n")

nama = "Ari"
umur = 25
nilai = 92.5

# F-string (rekomendasi)
print(f"Nama: {nama}, Umur: {umur}, Nilai: {nilai}")

# Format method
print("Nama: {}, Umur: {}, Nilai: {}".format(nama, umur, nilai))

# % operator (old style, tapi masih digunakan)
print("Nama: %s, Umur: %d, Nilai: %.1f" % (nama, umur, nilai))

# ===== 7. LIST COMPREHENSION =====
print("\n=== 7. LIST COMPREHENSION ===\n")

# Cara biasa (with loop)
angka = [1, 2, 3, 4, 5]
kuadrat_biasa = []
for x in angka:
    kuadrat_biasa.append(x ** 2)
print(f"Kuadrat (loop): {kuadrat_biasa}")

# List comprehension (lebih singkat)
kuadrat_comp = [x ** 2 for x in angka]
print(f"Kuadrat (comprehension): {kuadrat_comp}")

# List comprehension dengan kondisi
kuadrat_genap = [x ** 2 for x in angka if x % 2 == 0]
print(f"Kuadrat angka genap: {kuadrat_genap}")

# ===== 8. DICTIONARY COMPREHENSION =====
print("\n=== 8. DICTIONARY COMPREHENSION ===\n")

nama_siswa = ["Ari", "Budi", "Citra"]
nilai_siswa = [85, 90, 78]

# Cara biasa
siswa_dict_biasa = {}
for i in range(len(nama_siswa)):
    siswa_dict_biasa[nama_siswa[i]] = nilai_siswa[i]
print(f"Dict (biasa): {siswa_dict_biasa}")

# Dictionary comprehension dengan zip()
siswa_dict_comp = {nama: nilai for nama, nilai in zip(nama_siswa, nilai_siswa)}
print(f"Dict (comprehension): {siswa_dict_comp}")

# ===== 9. *ARGS & **KWARGS =====
print("\n=== 9. *ARGS & **KWARGS ===\n")

# *args untuk banyak parameter
def jumlahkan(*angka):
    total = sum(angka)
    return total

print(f"Jumlah(1, 2, 3): {jumlahkan(1, 2, 3)}")
print(f"Jumlah(10, 20, 30, 40): {jumlahkan(10, 20, 30, 40)}")

# **kwargs untuk named parameters
def perkenalan(**info):
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")

print("Info Ari:")
perkenalan(nama="Ari", umur=25, kota="Jakarta", pekerjaan="Programmer")

# ===== 10. LAMBDA FUNCTIONS =====
print("\n=== 10. LAMBDA FUNCTIONS ===\n")

# Lambda adalah fungsi anonymous (tanpa nama)
# Syntax: lambda arguments: expression

kuadrat_lambda = lambda x: x ** 2
print(f"Kuadrat(5) dengan lambda: {kuadrat_lambda(5)}")

# Gunakan dengan map()
angka = [1, 2, 3, 4, 5]
hasil_map = list(map(lambda x: x ** 2, angka))
print(f"Map kuadrat: {hasil_map}")

# Gunakan dengan filter()
hasil_filter = list(filter(lambda x: x > 2, angka))
print(f"Filter > 2: {hasil_filter}")

# Gunakan dengan sorted()
nilai_siswa = [85, 90, 78, 95, 88]
sorted_desc = sorted(nilai_siswa, reverse=True)
print(f"Nilai sorted descending: {sorted_desc}")

print("\n" + "=" * 50)
print("SELESAI FASE 3!")
print("=" * 50)
