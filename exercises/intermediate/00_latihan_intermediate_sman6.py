#!/usr/bin/env python3
"""
LATIHAN INTERMEDIATE - SMAN Negeri 6 Cimahi
Program Informatika Kelas XI

Konteks: Sistem Manajemen Data Siswa SMAN 6 Cimahi dengan File I/O
"""

import json
import os

# ===== DATABASE SISWA SMAN 6 CIMAHI =====
DATA_SISWA_SMAN6 = {
    "1001": {
        "nama": "Andi Wijaya",
        "kelas": "XI-A",
        "nilai": [85, 90, 88],
        "status": "Aktif"
    },
    "1002": {
        "nama": "Budi Santoso",
        "kelas": "XI-A",
        "nilai": [78, 82, 80],
        "status": "Aktif"
    },
    "1003": {
        "nama": "Citra Dewi",
        "kelas": "XI-B",
        "nilai": [92, 95, 90],
        "status": "Aktif"
    },
    "1004": {
        "nama": "Dina Kusuma",
        "kelas": "XI-B",
        "nilai": [88, 85, 87],
        "status": "Aktif"
    }
}

# ===== FUNGSI-FUNGSI =====

def tampilkan_header():
    """Tampilkan header program SMAN 6 Cimahi"""
    print("\n" + "=" * 70)
    print("SISTEM MANAJEMEN DATA SISWA SMAN NEGERI 6 CIMAHI")
    print("Program Informatika - Kelas XI")
    print("=" * 70 + "\n")

def cari_siswa_sman6(nisn):
    """Cari data siswa SMAN 6 berdasarkan NISN"""
    try:
        if nisn in DATA_SISWA_SMAN6:
            return DATA_SISWA_SMAN6[nisn]
        else:
            raise ValueError(f"Siswa dengan NISN {nisn} tidak ditemukan di SMAN 6 Cimahi")
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None

def hitung_rata_rata_siswa(nisn):
    """Hitung rata-rata nilai siswa SMAN 6"""
    siswa = DATA_SISWA_SMAN6.get(nisn)
    if siswa:
        rata_rata = sum(siswa["nilai"]) / len(siswa["nilai"])
        return rata_rata
    return None

def tampilkan_data_siswa(siswa, nisn):
    """Tampilkan data siswa SMAN 6 Cimahi dengan rapi"""
    if siswa:
        rata_rata = hitung_rata_rata_siswa(nisn)
        print(f"\n📋 DATA SISWA SMAN 6 CIMAHI")
        print("-" * 70)
        print(f"NISN            : {nisn}")
        print(f"Nama            : {siswa['nama']}")
        print(f"Kelas           : {siswa['kelas']}")
        print(f"Nilai Semester  : {siswa['nilai']}")
        print(f"Rata-rata Nilai : {rata_rata:.2f}")
        print(f"Status          : {siswa['status']}")
        print("-" * 70)

def simpan_data_ke_file_sman6(nama_file="siswa_sman6.json"):
    """Simpan data siswa SMAN 6 ke file JSON"""
    try:
        with open(nama_file, 'w') as file:
            json.dump(DATA_SISWA_SMAN6, file, indent=2)
        print(f"✅ Data siswa SMAN 6 Cimahi berhasil disimpan ke {nama_file}")
        return True
    except IOError as e:
        print(f"❌ Error saat menyimpan file: {e}")
        return False

def baca_data_dari_file_sman6(nama_file="siswa_sman6.json"):
    """Baca data siswa SMAN 6 dari file JSON"""
    try:
        if os.path.exists(nama_file):
            with open(nama_file, 'r') as file:
                data = json.load(file)
            print(f"✅ Data siswa SMAN 6 Cimahi berhasil dibaca dari {nama_file}")
            return data
        else:
            print(f"❌ File {nama_file} tidak ditemukan")
            return None
    except IOError as e:
        print(f"❌ Error saat membaca file: {e}")
        return None

def tampilkan_semua_siswa_sman6():
    """Tampilkan semua data siswa SMAN 6 Cimahi"""
    print("\n📚 DAFTAR SEMUA SISWA SMAN 6 CIMAHI")
    print("-" * 70)
    print(f"{'NISN':<8} {'Nama':<20} {'Kelas':<10} {'Rata-rata':<12}")
    print("-" * 70)
    
    for nisn, siswa in DATA_SISWA_SMAN6.items():
        rata_rata = hitung_rata_rata_siswa(nisn)
        print(f"{nisn:<8} {siswa['nama']:<20} {siswa['kelas']:<10} {rata_rata:.2f}")
    print("-" * 70)

# ===== PROGRAM UTAMA =====

def main():
    tampilkan_header()
    
    # LATIHAN 1: Cari siswa tertentu
    print("1️⃣  LATIHAN: MENCARI DATA SISWA SMAN 6 CIMAHI")
    nisn_cari = input("Masukkan NISN siswa (1001-1004): ").strip()
    siswa = cari_siswa_sman6(nisn_cari)
    if siswa:
        tampilkan_data_siswa(siswa, nisn_cari)
    
    # LATIHAN 2: Tampilkan semua siswa
    print("\n2️⃣  LATIHAN: MENAMPILKAN SEMUA DATA SISWA SMAN 6 CIMAHI")
    tampilkan_semua_siswa_sman6()
    
    # LATIHAN 3: Simpan ke file
    print("\n3️⃣  LATIHAN: MENYIMPAN DATA KE FILE")
    simpan_data_ke_file_sman6()
    
    # LATIHAN 4: Baca dari file
    print("\n4️⃣  LATIHAN: MEMBACA DATA DARI FILE")
    data_dari_file = baca_data_dari_file_sman6()
    
    print("\n" + "=" * 70)
    print("Program selesai - SMAN Negeri 6 Cimahi")
    print("=" * 70)

if __name__ == "__main__":
    main()
