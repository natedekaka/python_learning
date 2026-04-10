#!/usr/bin/env python3
"""
Phase 2: Loops & Conditions
============================
Belajar: if/else/elif, for loop, while loop
"""

print("=" * 50)
print("PHASE 2: LOOPS & CONDITIONS")
print("=" * 50)

# ===== 1. IF / ELSE / ELIF =====
print("\n=== 1. IF / ELSE / ELIF ===\n")

nilai = 85
print(f"Nilai Anda: {nilai}")

# Logika sederhana dengan if-else
if nilai >= 90:
    print("Grade: A (Sangat Baik)")
elif nilai >= 80:
    print("Grade: B (Baik)")
elif nilai >= 70:
    print("Grade: C (Cukup)")
else:
    print("Grade: D (Kurang)")

# Contoh 2: Kondisi AND, OR
print("\nContoh dengan AND/OR:")
umur = 25
punya_sim = True

if umur >= 17 and punya_sim:
    print("Anda boleh berkendara")
else:
    print("Anda tidak boleh berkendara")

# ===== 2. FOR LOOP =====
print("\n=== 2. FOR LOOP ===\n")

# Loop sederhana
print("Menghitung 1 sampai 5:")
for i in range(1, 6):
    print(f"Nomor: {i}")

print("\nMencetak nilai dari list:")
nilai_ujian = [85, 90, 78, 95, 88]
for nilai in nilai_ujian:
    if nilai >= 90:
        status = "Sangat Bagus"
    elif nilai >= 80:
        status = "Bagus"
    else:
        status = "Cukup"
    print(f"Nilai: {nilai} -> {status}")

# Loop dengan index
print("\nLoop dengan index:")
for idx, nilai in enumerate(nilai_ujian):
    print(f"Ujian ke-{idx + 1}: {nilai}")

# ===== 3. WHILE LOOP =====
print("\n=== 3. WHILE LOOP ===\n")

print("Menghitung mundur dari 5:")
hitung = 5
while hitung > 0:
    print(hitung)
    hitung -= 1  # Sama dengan: hitung = hitung - 1
print("LIFTOFF! 🚀\n")

# ===== 4. BREAK & CONTINUE =====
print("=== 4. BREAK & CONTINUE ===\n")

print("Cari angka 90 dalam list:")
for nilai in nilai_ujian:
    if nilai == 90:
        print(f"Ketemu! {nilai}")
        break  # Stop loop
    else:
        print(f"Cek: {nilai}")

print("\nSkip nilai >= 90:")
for nilai in nilai_ujian:
    if nilai >= 90:
        continue  # Skip iterasi ini
    print(f"Nilai: {nilai}")

# ===== 5. NESTED LOOP =====
print("\n=== 5. NESTED LOOP (Loop Bersarang) ===\n")

print("Tabel Perkalian 3x3:")
for i in range(1, 4):
    for j in range(1, 4):
        hasil = i * j
        print(f"{i} x {j} = {hasil}", end="  ")
    print()  # Baris baru

print("\n" + "=" * 50)
print("SELESAI FASE 2!")
print("=" * 50)
