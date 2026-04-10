#!/usr/bin/env python3
"""
Fundamentals - Exercise 1: Variables & Data Types
==================================================

SOAL:
1. Buat variable dengan tipe: string, int, float, dan boolean
2. Tampilkan tipe dari setiap variable menggunakan type()
3. Lakukan operasi arithmetic dengan variable int dan float
4. Lakukan string concatenation dan f-string formatting
"""

# ===== SOAL 1: Deklarasi Variables =====
print("=" * 50)
print("SOAL 1: Deklarasi Variables")
print("=" * 50)

# TODO: Buat variables berikut
nama = "Ari"
umur = 20
tinggi = 1.75
aktif = True

print(f"Nama: {nama}, Tipe: {type(nama)}")
print(f"Umur: {umur}, Tipe: {type(umur)}")
print(f"Tinggi: {tinggi}, Tipe: {type(tinggi)}")
print(f"Aktif: {aktif}, Tipe: {type(aktif)}")

# ===== SOAL 2: Operasi Arithmetic =====
print("\n" + "=" * 50)
print("SOAL 2: Operasi Arithmetic")
print("=" * 50)

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} * {b} = {a * b}")
print(f"Pembagian: {a} / {b} = {a / b}")
print(f"Pembagian Bulat: {a} // {b} = {a // b}")
print(f"Sisa: {a} % {b} = {a % b}")
print(f"Pangkat: {a} ** {b} = {a ** b}")

# ===== SOAL 3: String Operations =====
print("\n" + "=" * 50)
print("SOAL 3: String Operations")
print("=" * 50)

kota = "Bandung"
negara = "Indonesia"

# Concatenation
alamat = kota + ", " + negara
print(f"Concatenation: {alamat}")

# F-string
print(f"F-string: Saya tinggal di {kota}, {negara}")

# String methods
print(f"Uppercase: {kota.upper()}")
print(f"Lowercase: {kota.lower()}")
print(f"Length: {len(kota)}")
print(f"Replace: {kota.replace('Bandung', 'Jakarta')}")

# ===== SOAL 4: Type Conversion =====
print("\n" + "=" * 50)
print("SOAL 4: Type Conversion")
print("=" * 50)

str_angka = "42"
int_angka = int(str_angka)
float_angka = float(str_angka)

print(f"String: {str_angka} (type: {type(str_angka)})")
print(f"Int: {int_angka} (type: {type(int_angka)})")
print(f"Float: {float_angka} (type: {type(float_angka)})")

# Convert to string
hasil = 100 + 50
str_hasil = str(hasil)
print(f"String conversion: {str_hasil} (type: {type(str_hasil)})")

print("\n✅ Latihan Selesai!")
