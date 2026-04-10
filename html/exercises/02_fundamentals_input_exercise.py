#!/usr/bin/env python3
"""
Fundamentals - Exercise 2: Input & Calculation
===============================================

SOAL:
1. Minta input nama dari user
2. Minta input nilai dari user (min 5 nilai)
3. Hitung rata-rata, nilai tertinggi, dan terendah
4. Tentukan grade berdasarkan rata-rata
5. Tampilkan hasil dengan formatting yang rapi
"""

print("=" * 50)
print("Program Hitung Nilai Siswa")
print("=" * 50)

# ===== INPUT DATA =====
nama = input("\nMasukkan nama Anda: ")

print(f"\nMasukkan 5 nilai mata pelajaran {nama}:")
nilai1 = float(input("Nilai 1: "))
nilai2 = float(input("Nilai 2: "))
nilai3 = float(input("Nilai 3: "))
nilai4 = float(input("Nilai 4: "))
nilai5 = float(input("Nilai 5: "))

# ===== PROSES DATA =====
nilai_list = [nilai1, nilai2, nilai3, nilai4, nilai5]
rata_rata = sum(nilai_list) / len(nilai_list)
nilai_max = max(nilai_list)
nilai_min = min(nilai_list)

# Tentukan grade
if rata_rata >= 90:
    grade = "A"
elif rata_rata >= 80:
    grade = "B"
elif rata_rata >= 70:
    grade = "C"
elif rata_rata >= 60:
    grade = "D"
else:
    grade = "E"

# ===== TAMPILKAN HASIL =====
print("\n" + "=" * 50)
print("HASIL ANALISIS NILAI")
print("=" * 50)
print(f"Nama: {nama}")
print(f"Nilai: {', '.join(map(str, nilai_list))}")
print(f"\nRata-rata: {rata_rata:.2f}")
print(f"Nilai Tertinggi: {nilai_max:.2f}")
print(f"Nilai Terendah: {nilai_min:.2f}")
print(f"Grade: {grade}")
print("=" * 50)

# ===== KETERANGAN =====
if grade == "A":
    keterangan = "Sangat Memuaskan!"
elif grade == "B":
    keterangan = "Memuaskan"
elif grade == "C":
    keterangan = "Cukup"
elif grade == "D":
    keterangan = "Kurang"
else:
    keterangan = "Sangat Kurang"

print(f"Keterangan: {keterangan}")
print("\n✅ Latihan Selesai!")
