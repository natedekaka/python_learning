#!/usr/bin/env python3
"""
Intermediate - Exercise 1: Loops & Conditions
==============================================

SOAL:
1. Tampilkan bilangan 1-10 menggunakan for loop
2. Hitung sum bilangan ganjil dari 1-50 menggunakan while loop
3. Tampilkan tabel perkalian 5
4. Buat segitiga bintang dengan input user
5. Gunakan nested loop untuk membuat pattern
"""

# ===== SOAL 1: For Loop =====
print("=" * 50)
print("SOAL 1: Bilangan 1-10")
print("=" * 50)

for i in range(1, 11):
    print(f"{i}", end=" ")
print("\n")

# ===== SOAL 2: While Loop & Kondisi =====
print("=" * 50)
print("SOAL 2: Sum Bilangan Ganjil 1-50")
print("=" * 50)

sum_ganjil = 0
i = 1
while i <= 50:
    if i % 2 != 0:
        sum_ganjil += i
    i += 1

print(f"Sum: {sum_ganjil}")

# ===== SOAL 3: Tabel Perkalian =====
print("\n" + "=" * 50)
print("SOAL 3: Tabel Perkalian 5")
print("=" * 50)

for i in range(1, 11):
    print(f"5 x {i:2d} = {5 * i:2d}")

# ===== SOAL 4: Segitiga Bintang =====
print("\n" + "=" * 50)
print("SOAL 4: Segitiga Bintang")
print("=" * 50)

n = int(input("Masukkan jumlah baris: "))
for i in range(1, n + 1):
    print("* " * i)

# ===== SOAL 5: Nested Loop Pattern =====
print("\n" + "=" * 50)
print("SOAL 5: Pattern Nested Loop")
print("=" * 50)

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n✅ Latihan Selesai!")
