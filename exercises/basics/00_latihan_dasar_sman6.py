#!/usr/bin/env python3
"""
LATIHAN DASAR - SMAN Negeri 6 Cimahi
Program Informatika Kelas X

Konteks: Program sederhana untuk mengelola data siswa SMAN 6 Cimahi
"""

print("=" * 60)
print("PROGRAM SEDERHANA DATA SISWA SMAN NEGERI 6 CIMAHI")
print("=" * 60)

# ===== LATIHAN 1: VARIABEL & INPUT =====
print("\n1️⃣  LATIHAN: INPUT DATA SISWA SMAN 6 CIMAHI")
print("-" * 60)

nama_siswa_sman6 = input("Masukkan nama siswa: ")
nisn_sman6 = input("Masukkan NISN: ")
kelas_sman6 = input("Masukkan kelas (X-A/X-B/X-C): ")

print(f"\nData siswa SMAN 6 Cimahi yang diinput:")
print(f"  Nama: {nama_siswa_sman6}")
print(f"  NISN: {nisn_sman6}")
print(f"  Kelas: {kelas_sman6}")

# ===== LATIHAN 2: TIPE DATA =====
print("\n\n2️⃣  LATIHAN: TIPE DATA - NILAI SISWA")
print("-" * 60)

nilai_matematika = 85
nilai_bahasa = 78
nilai_informatika = 92

print(f"Nilai Matematika: {nilai_matematika} (Type: {type(nilai_matematika).__name__})")
print(f"Nilai Bahasa: {nilai_bahasa} (Type: {type(nilai_bahasa).__name__})")
print(f"Nilai Informatika: {nilai_informatika} (Type: {type(nilai_informatika).__name__})")

# ===== LATIHAN 3: OPERATOR ARITMATIKA =====
print("\n\n3️⃣  LATIHAN: MENGHITUNG RATA-RATA NILAI")
print("-" * 60)

total_nilai = nilai_matematika + nilai_bahasa + nilai_informatika
rata_rata_sman6 = total_nilai / 3

print(f"Total nilai: {total_nilai}")
print(f"Rata-rata nilai siswa SMAN 6: {rata_rata_sman6:.1f}")

# ===== LATIHAN 4: COMPARISON OPERATOR =====
print("\n\n4️⃣  LATIHAN: PENENTUAN STATUS KELULUSAN")
print("-" * 60)

nilai_kelulusan_sman6 = 70

if rata_rata_sman6 >= nilai_kelulusan_sman6:
    status_siswa = "LULUS"
else:
    status_siswa = "TIDAK LULUS"

print(f"Nilai kelulusan SMAN 6 Cimahi: {nilai_kelulusan_sman6}")
print(f"Status siswa: {status_siswa}")

# ===== LATIHAN 5: LIST =====
print("\n\n5️⃣  LATIHAN: DAFTAR SISWA SMAN 6 CIMAHI")
print("-" * 60)

daftar_siswa_sman6 = [
    "Andi Wijaya",
    "Budi Santoso",
    "Citra Dewi",
    "Dina Kusuma"
]

print("Daftar siswa SMAN 6 Cimahi Kelas X-A:")
for i, siswa in enumerate(daftar_siswa_sman6, 1):
    print(f"  {i}. {siswa}")

# ===== LATIHAN 6: DICTIONARY =====
print("\n\n6️⃣  LATIHAN: DATA GURU SMAN 6 CIMAHI")
print("-" * 60)

data_guru_sman6 = {
    "NIP001": {"nama": "Ibu Nadia", "mapel": "Informatika"},
    "NIP002": {"nama": "Pak Sugeng", "mapel": "Matematika"},
    "NIP003": {"nama": "Bu Siti", "mapel": "Bahasa Inggris"}
}

print("Data guru SMAN 6 Cimahi:")
for nip, info_guru in data_guru_sman6.items():
    print(f"  {nip}: {info_guru['nama']} - {info_guru['mapel']}")

# ===== LATIHAN 7: LOGICAL OPERATOR =====
print("\n\n7️⃣  LATIHAN: PENGECEKAN KELENGKAPAN DATA")
print("-" * 60)

data_lengkap = (nama_siswa_sman6 != "" and 
                nisn_sman6 != "" and 
                kelas_sman6 != "")

if data_lengkap:
    print("✅ Data siswa SMAN 6 Cimahi sudah lengkap!")
else:
    print("❌ Data siswa SMAN 6 Cimahi belum lengkap!")

print("\n" + "=" * 60)
print("Selesai - SMAN Negeri 6 Cimahi")
print("=" * 60)
