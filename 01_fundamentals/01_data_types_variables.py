#!/usr/bin/env python3
"""
Python Basics - Data Types & Variables
=====================================
"""

# 1. VARIABLES & DATA TYPES
print("=== 1. VARIABLES & DATA TYPES ===\n")

# String (teks)
nama = "Ari"
print(f"Nama: {nama}, Tipe: {type(nama)}")

# Integer (angka bulat)
umur = 25
print(f"Umur: {umur}, Tipe: {type(umur)}")

# Float (angka desimal)
tinggi = 1.75
print(f"Tinggi: {tinggi}, Tipe: {type(tinggi)}")

# Boolean (True/False)
sudah_bekerja = True
print(f"Sudah bekerja: {sudah_bekerja}, Tipe: {type(sudah_bekerja)}\n")

# 2. LISTS (koleksi data)
print("=== 2. LISTS ===\n")

nilai_ujian = [85, 90, 78, 95, 88]
print(f"Nilai ujian: {nilai_ujian}")
print(f"Nilai pertama: {nilai_ujian[0]}")
print(f"3 nilai pertama: {nilai_ujian[:3]}")
print(f"Total nilai: {sum(nilai_ujian)}")
print(f"Rata-rata: {sum(nilai_ujian) / len(nilai_ujian)}\n")

# 3. DICTIONARIES (key-value pairs)
print("=== 3. DICTIONARIES ===\n")

siswa = {
    "nama": "Ari",
    "umur": 25,
    "nilai": 90,
    "kota": "Jakarta"
}
print(f"Data siswa: {siswa}")
print(f"Nama: {siswa['nama']}")
print(f"Nilai: {siswa['nilai']}\n")

# 4. OPERATIONS (operasi dasar)
print("=== 4. OPERATIONS ===\n")

a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")  # Float division
print(f"{a} // {b} = {a // b}")  # Integer division
print(f"{a} % {b} = {a % b}")   # Modulo (sisa bagi)
print(f"{a} ** {b} = {a ** b}") # Pangkat
