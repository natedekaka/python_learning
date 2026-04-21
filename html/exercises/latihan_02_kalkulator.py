#!/usr/bin/env python3
"""
==========================================
LATIHAN 2: KALKULATOR SEDERHANA
==========================================
Tujuan: Memahami operator aritmatika dan input user

Konsep yang dipelajari:
- Input user (input())
- Type conversion (int(), float())
- Operator aritmatika (+, -, *, /, //, %, **)
- Print formatting

==========================================
"""

print("=" * 50)
print("🧮 KALKULATOR SEDERHANA")
print("=" * 50)

# ==============================
# BAGIAN 1: INPUT ANGKA
# ==============================

print("\n📥 Masukkan dua angka:")

# TODO 1: Minta input angka pertama
angka1 = float(input("Angka pertama: "))

# TODO 2: Minta input angka kedua
angka2 = float(input("Angka kedua: "))

# ==============================
# BAGIAN 2: OPERASI ARITMATIKA
# ==============================

print("\n" + "=" * 50)
print("📊 HASIL PERHITUNGAN")
print("=" * 50)

# TODO 3: Hitung hasil setiap operasi
# Penjumlahan
hasil_tambah = ...
print(f"📌 Penjumlahan   : {angka1} + {angka2} = {hasil_tambah}")

# Pengurangan
hasil_kurang = ...
print(f"📌 Pengurangan  : {angka1} - {angka2} = {hasil_kurang}")

# Perkalian
hasil_kali = ...
print(f"📌 Perkalian    : {angka1} * {angka2} = {hasil_kali}")

# Pembagian
hasil_bagi = ...
print(f"📌 Pembagian    : {angka1} / {angka2} = {hasil_bagi:.2f}")

# Pembagian bulat
hasil_bagi_bulat = ...
print(f"📌 Bagi Bulat   : {angka1} // {angka2} = {hasil_bagi_bulat}")

# Sisa bagi (modulo)
hasil_modulo = ...
print(f"📌 Sisa Bagi    : {angka1} % {angka2} = {hasil_modulo}")

# Pangkat
hasil_pangkat = ...
print(f"📌 Pangkat      : {angka1} ** {angka2} = {hasil_pangkat:.2f}")

# ==============================
# BAGIAN 3: KALKULATOR LUAS
# ==============================

print("\n" + "=" * 50)
print("📐 HITUNG LUAS BANGUN DATAR")
print("=" * 50)

# TODO 4: Hitung luas persegi panjang
print("\n1. Persegi Panjang")
lebar = float(input("Masukkan lebar: "))
luas_persegi_panjang = ...
print(f"Luas = {lebar} * {lebar} = {luas_persegi_panjang}")

# TODO 5: Hitung luas lingkaran
print("\n2. Lingkaran")
jari_jari = float(input("Masukkan jari-jari: "))
phi = 3.14
luas_lingkaran = ...
print(f"Luas = {phi} * {jari_jari}² = {luas_lingkaran:.2f}")

# TODO 6: Hitung luas segitiga
print("\n3. Segitiga")
alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))
luas_segitiga = ...
print(f"Luas = 0.5 * {alas} * {tinggi} = {luas_segitiga:.2f}")

print("\n✅ Latihan 2 Selesai!")
