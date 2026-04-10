#!/usr/bin/env python3
"""
Intermediate - Exercise 3: File Operations & Exceptions
========================================================

SOAL:
1. Buat file dan tulis data ke file
2. Baca file dan tampilkan isi
3. Lakukan error handling saat membaca file
4. Append data ke file existing
5. Hitung jumlah baris di file
"""

import os

# ===== SOAL 1: Tulis ke File =====
print("=" * 50)
print("SOAL 1: Menulis ke File")
print("=" * 50)

file_path = "data.txt"

# Buat data
data = [
    "Nama: Ari\n",
    "Umur: 20\n",
    "Kota: Bandung\n",
    "Negara: Indonesia\n"
]

# Tulis ke file
try:
    with open(file_path, "w") as f:
        f.writelines(data)
    print(f"✓ File '{file_path}' berhasil dibuat")
except IOError as e:
    print(f"✗ Error saat menulis file: {e}")

# ===== SOAL 2: Baca dari File =====
print("\n" + "=" * 50)
print("SOAL 2: Membaca dari File")
print("=" * 50)

try:
    with open(file_path, "r") as f:
        content = f.read()
    print("Isi file:")
    print(content)
except FileNotFoundError:
    print(f"✗ File '{file_path}' tidak ditemukan!")
except IOError as e:
    print(f"✗ Error saat membaca file: {e}")

# ===== SOAL 3: Error Handling Lengkap =====
print("\n" + "=" * 50)
print("SOAL 3: Error Handling")
print("=" * 50)

def baca_file_aman(filepath):
    """Baca file dengan error handling lengkap"""
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filepath}' tidak ditemukan!")
        return None
    except PermissionError:
        print(f"Error: Tidak punya izin untuk membaca '{filepath}'")
        return None
    except IOError as e:
        print(f"Error IO: {e}")
        return None
    except Exception as e:
        print(f"Error tidak terduga: {e}")
        return None

lines = baca_file_aman(file_path)
if lines:
    print(f"Berhasil membaca {len(lines)} baris")
    for i, line in enumerate(lines, 1):
        print(f"  {i}: {line.strip()}")

# ===== SOAL 4: Append ke File =====
print("\n" + "=" * 50)
print("SOAL 4: Append Data ke File")
print("=" * 50)

new_data = "Email: ari@example.com\n"

try:
    with open(file_path, "a") as f:
        f.write(new_data)
    print(f"✓ Data ditambahkan ke '{file_path}'")
except IOError as e:
    print(f"✗ Error saat append: {e}")

# ===== SOAL 5: Hitung Baris =====
print("\n" + "=" * 50)
print("SOAL 5: Hitung Jumlah Baris")
print("=" * 50)

def hitung_baris(filepath):
    """Hitung jumlah baris di file"""
    try:
        with open(filepath, "r") as f:
            count = len(f.readlines())
        return count
    except FileNotFoundError:
        return -1

jumlah_baris = hitung_baris(file_path)
if jumlah_baris > 0:
    print(f"File '{file_path}' memiliki {jumlah_baris} baris")

# ===== SOAL 6: Baca File Line by Line =====
print("\n" + "=" * 50)
print("SOAL 6: Baca Line by Line")
print("=" * 50)

try:
    with open(file_path, "r") as f:
        print("Isi file baris per baris:")
        for i, line in enumerate(f, 1):
            print(f"  Baris {i}: {line.rstrip()}")
except IOError as e:
    print(f"Error: {e}")

# ===== CLEANUP =====
# Hapus file yang dibuat
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"\n✓ File '{file_path}' dihapus (cleanup)")

print("\n✅ Latihan Selesai!")
