#!/usr/bin/env python3
"""
Phase 4: File Operations & Exception Handling
==============================================
Belajar: membaca/menulis file, error handling, try/except
"""

import os

print("=" * 50)
print("PHASE 4: FILE OPERATIONS & EXCEPTION HANDLING")
print("=" * 50)

# ===== 1. EXCEPTION HANDLING (TRY/EXCEPT) =====
print("\n=== 1. EXCEPTION HANDLING ===\n")

# Contoh 1: ZeroDivisionError
print("Contoh 1: ZeroDivisionError")
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("ERROR: Tidak bisa membagi dengan 0!")

# Contoh 2: ValueError
print("\nContoh 2: ValueError")
try:
    angka = int("abc")
except ValueError:
    print("ERROR: Input bukan angka yang valid!")

# Contoh 3: IndexError
print("\nContoh 3: IndexError")
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError:
    print("ERROR: Index di luar jangkauan!")

# Contoh 4: KeyError (Dictionary)
print("\nContoh 4: KeyError")
try:
    siswa = {"nama": "Ari", "umur": 25}
    print(siswa["pekerjaan"])
except KeyError as e:
    print(f"ERROR: Key '{e}' tidak ditemukan!")

# Contoh 5: Multiple exceptions
print("\nContoh 5: Multiple Exceptions")
try:
    angka = int(input("Masukkan angka (atau skip dengan Enter): ") or "5")
    hasil = 100 / angka
    print(f"100 / {angka} = {hasil}")
except ValueError:
    print("ERROR: Input harus berupa angka!")
except ZeroDivisionError:
    print("ERROR: Tidak bisa dibagi 0!")

# ===== 2. TRY/EXCEPT/ELSE/FINALLY =====
print("\n=== 2. TRY/EXCEPT/ELSE/FINALLY ===\n")

def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print(f"  ERROR: Tidak bisa membagi dengan 0")
    except TypeError:
        print(f"  ERROR: Tipe data tidak sesuai")
    else:
        # Dijalankan jika tidak ada error
        print(f"  {a} / {b} = {hasil}")
    finally:
        # Selalu dijalankan, ada error atau tidak
        print(f"  Operasi selesai\n")

print("Bagi(10, 2):")
bagi(10, 2)

print("Bagi(10, 0):")
bagi(10, 0)

# ===== 3. CUSTOM EXCEPTIONS =====
print("=== 3. CUSTOM EXCEPTIONS ===\n")

class NilaiTidakValid(Exception):
    pass

def validasi_nilai(nilai):
    if nilai < 0 or nilai > 100:
        raise NilaiTidakValid(f"Nilai harus antara 0-100, dapat: {nilai}")
    return nilai

try:
    nilai = validasi_nilai(150)
except NilaiTidakValid as e:
    print(f"ERROR: {e}")

try:
    nilai = validasi_nilai(85)
    print(f"Nilai valid: {nilai}")
except NilaiTidakValid as e:
    print(f"ERROR: {e}")

# ===== 4. FILE OPERATIONS - WRITE =====
print("\n=== 4. FILE OPERATIONS - WRITE ===\n")

# Buat file data siswa
data_siswa = [
    "Nama,Umur,Kota,Nilai\n",
    "Ari,25,Jakarta,85\n",
    "Budi,26,Bandung,90\n",
    "Citra,24,Jakarta,78\n",
    "Doni,27,Surabaya,92\n"
]

# Tulis ke file
nama_file = "data_siswa.csv"
try:
    with open(nama_file, "w") as file:
        file.writelines(data_siswa)
    print(f"✓ File '{nama_file}' berhasil dibuat!")
except IOError as e:
    print(f"ERROR: {e}")

# ===== 5. FILE OPERATIONS - READ =====
print("\n=== 5. FILE OPERATIONS - READ ===\n")

# Baca file
try:
    with open(nama_file, "r") as file:
        print(f"Isi file '{nama_file}':")
        print("-" * 40)
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"ERROR: File '{nama_file}' tidak ditemukan!")

# ===== 6. READ FILE BY LINE =====
print("=== 6. READ FILE LINE BY LINE ===\n")

try:
    with open(nama_file, "r") as file:
        print(f"Membaca baris per baris dari '{nama_file}':")
        for i, line in enumerate(file, 1):
            print(f"  Baris {i}: {line.strip()}")
except FileNotFoundError:
    print(f"ERROR: File '{nama_file}' tidak ditemukan!")

# ===== 7. PROCESS FILE DATA =====
print("\n=== 7. PROCESS FILE DATA ===\n")

try:
    with open(nama_file, "r") as file:
        # Skip header
        header = file.readline()
        
        # Baca data
        siswa_list = []
        for line in file:
            data = line.strip().split(",")
            if len(data) == 4:
                siswa_list.append({
                    "nama": data[0],
                    "umur": int(data[1]),
                    "kota": data[2],
                    "nilai": int(data[3])
                })
        
        print("Data Siswa:")
        for siswa in siswa_list:
            print(f"  {siswa['nama']}: Nilai {siswa['nilai']}")
        
        # Hitung statistik
        if siswa_list:
            nilai_list = [s["nilai"] for s in siswa_list]
            rata_rata = sum(nilai_list) / len(nilai_list)
            print(f"\n  Rata-rata nilai: {rata_rata:.2f}")
            
except FileNotFoundError:
    print(f"ERROR: File '{nama_file}' tidak ditemukan!")
except ValueError as e:
    print(f"ERROR: Format data tidak sesuai - {e}")

# ===== 8. APPEND TO FILE =====
print("\n=== 8. APPEND TO FILE ===\n")

try:
    # Tambah data baru
    with open(nama_file, "a") as file:
        file.write("Eva,23,Semarang,88\n")
    print(f"✓ Data baru ditambahkan ke '{nama_file}'")
    
    # Tampilkan isi terbaru
    with open(nama_file, "r") as file:
        print(f"\nIsi file setelah append:")
        print("-" * 40)
        print(file.read())
        
except IOError as e:
    print(f"ERROR: {e}")

# ===== 9. FILE OPERATIONS WITH JSON =====
print("=== 9. FILE OPERATIONS WITH JSON ===\n")

import json

siswa_data = {
    "siswa": [
        {"nama": "Ari", "umur": 25, "nilai": 85},
        {"nama": "Budi", "umur": 26, "nilai": 90},
        {"nama": "Citra", "umur": 24, "nilai": 78}
    ]
}

# Tulis ke JSON file
json_file = "data_siswa.json"
try:
    with open(json_file, "w") as file:
        json.dump(siswa_data, file, indent=2)
    print(f"✓ JSON file '{json_file}' berhasil dibuat!")
except IOError as e:
    print(f"ERROR: {e}")

# Baca dari JSON file
try:
    with open(json_file, "r") as file:
        data = json.load(file)
    print(f"\nIsi JSON file '{json_file}':")
    for siswa in data["siswa"]:
        print(f"  {siswa['nama']}: Nilai {siswa['nilai']}")
except FileNotFoundError:
    print(f"ERROR: File '{json_file}' tidak ditemukan!")

# ===== 10. WORKING WITH FILES AND DIRECTORIES =====
print("\n=== 10. WORKING WITH FILES AND DIRECTORIES ===\n")

# Check if file exists
if os.path.exists(nama_file):
    print(f"✓ File '{nama_file}' ada")
    print(f"  Ukuran: {os.path.getsize(nama_file)} bytes")
else:
    print(f"✗ File '{nama_file}' tidak ada")

# List files in directory
print(f"\nFile .csv dan .json di direktori saat ini:")
for file in os.listdir("."):
    if file.endswith((".csv", ".json")):
        print(f"  - {file}")

# Delete files (optional)
print("\nMembersihkan file test...")
try:
    if os.path.exists(nama_file):
        os.remove(nama_file)
        print(f"  ✓ File '{nama_file}' dihapus")
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f"  ✓ File '{json_file}' dihapus")
except OSError as e:
    print(f"  ERROR: {e}")

print("\n" + "=" * 50)
print("SELESAI FASE 4!")
print("=" * 50)
